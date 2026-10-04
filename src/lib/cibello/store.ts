import { create } from "zustand";
import { persist } from "zustand/middleware";
import type { CookEntry, DayKey, ListItem, PantryItem, Recipe, WeekPlan } from "./types";
import { RECIPES, SCAN_BATCH, daysUntil, seedPantry, uid } from "./data";

const emptyWeek = (): WeekPlan => ({
  mon: null,
  tue: null,
  wed: null,
  thu: null,
  fri: null,
  sat: null,
  sun: null,
});

export type Why = {
  key: "why_now" | "why_soon" | "why_all" | "why_almost" | "why_base";
  percent: number;
  name?: string;
  missing?: string;
};

export type Match = {
  recipe: Recipe;
  have: number;
  total: number;
  percent: number;
  missing: Recipe["ingredients"];
  why: Why;
};

type KitchenState = {
  pantry: PantryItem[];
  list: ListItem[];
  week: WeekPlan;
  cookLog: CookEntry[];
  addPantry: (item: Omit<PantryItem, "id">) => PantryItem;
  removePantry: (id: string) => void;
  scanFridge: () => PantryItem[];
  toggleList: (id: string) => void;
  removeList: (id: string) => void;
  addList: (item: Omit<ListItem, "id" | "done">) => void;
  addMissingToList: (recipe: Recipe) => number;
  assignDay: (day: DayKey, recipeId: string | null) => void;
  fillWeekFromMatches: (ids: string[]) => void;
  addCook: (recipe: Recipe, at?: string) => CookEntry;
  hydrate: (snap: { pantry: PantryItem[]; list: ListItem[]; week: WeekPlan; cookLog: CookEntry[] }) => void;
  reset: () => void;
};

export const useKitchen = create<KitchenState>()(
  persist(
    (set, get) => ({
      pantry: seedPantry(),
      list: [],
      week: emptyWeek(),
      cookLog: [],
      addPantry: (item) => {
        const existing = get().pantry.find((p) => p.key === item.key);
        if (existing) {
          set((s) => ({
            pantry: s.pantry.map((p) =>
              p.id === existing.id ? { ...p, qty: item.qty, expires: item.expires } : p,
            ),
          }));
          return existing;
        }
        const full: PantryItem = { ...item, id: uid("p") };
        set((s) => ({ pantry: [...s.pantry, full] }));
        return full;
      },
      removePantry: (id) => set((s) => ({ pantry: s.pantry.filter((p) => p.id !== id) })),
      scanFridge: () => {
        const existing = new Set(get().pantry.map((p) => p.key));
        const added: PantryItem[] = [];
        for (const item of SCAN_BATCH) {
          if (!existing.has(item.key)) added.push({ ...item, id: uid("p") });
        }
        if (added.length) set((s) => ({ pantry: [...s.pantry, ...added] }));
        return added;
      },
      toggleList: (id) =>
        set((s) => ({
          list: s.list.map((i) => (i.id === id ? { ...i, done: !i.done } : i)),
        })),
      removeList: (id) => set((s) => ({ list: s.list.filter((i) => i.id !== id) })),
      addList: (item) =>
        set((s) => {
          if (s.list.some((i) => i.key === item.key && !i.done)) return s;
          return { list: [...s.list, { ...item, id: uid("l"), done: false }] };
        }),
      addMissingToList: (recipe) => {
        const keys = new Set(get().pantry.map((p) => p.key));
        let n = 0;
        for (const ing of recipe.ingredients) {
          if (!keys.has(ing.key)) {
            get().addList({
              key: ing.key,
              name: ing.name,
              amount: ing.amount,
              fromRecipe: recipe.title,
            });
            n += 1;
          }
        }
        return n;
      },
      assignDay: (day, recipeId) => set((s) => ({ week: { ...s.week, [day]: recipeId } })),
      fillWeekFromMatches: (ids) => {
        const days: DayKey[] = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
        const week = emptyWeek();
        days.forEach((d, i) => {
          week[d] = ids[i % ids.length] ?? null;
        });
        set({ week });
      },
      addCook: (recipe, at) => {
        const entry: CookEntry = {
          id: uid("c"),
          recipeId: recipe.id,
          title: recipe.title,
          cookedAt: at ?? new Date().toISOString(),
        };
        set((s) => ({ cookLog: [entry, ...s.cookLog] }));
        return entry;
      },
      hydrate: (snap) => set(snap),
      reset: () => set({ pantry: seedPantry(), list: [], week: emptyWeek(), cookLog: [] }),
    }),
    { name: "cibello-kok", skipHydration: true },
  ),
);

export function matchRecipe(recipe: Recipe, pantry: PantryItem[]): Match {
  const keys = new Set(pantry.map((p) => p.key));
  const haveList = recipe.ingredients.filter((i) => keys.has(i.key));
  const missing = recipe.ingredients.filter((i) => !keys.has(i.key));
  const total = recipe.ingredients.length;
  const have = haveList.length;
  const percent = total === 0 ? 0 : Math.round((have / total) * 100);

  const soon = pantry
    .filter((p) => daysUntil(p.expires) <= 3 && recipe.ingredients.some((i) => i.key === p.key))
    .sort((a, b) => daysUntil(a.expires) - daysUntil(b.expires));

  let why: Why = { key: "why_base", percent };
  if (soon[0]) {
    why = {
      key: daysUntil(soon[0].expires) <= 1 ? "why_now" : "why_soon",
      name: soon[0].name.toLowerCase(),
      percent,
    };
  } else if (percent === 100) {
    why = { key: "why_all", percent };
  } else if (percent >= 80) {
    why = {
      key: "why_almost",
      missing: missing.map((m) => m.name.toLowerCase()).join(", "),
      percent,
    };
  }

  return { recipe, have, total, percent, missing, why };
}

export function rankedRecipes(pantry: PantryItem[], meal?: Recipe["meal"] | "all"): Match[] {
  return RECIPES.filter((r) => !meal || meal === "all" || r.meal === meal)
    .map((r) => matchRecipe(r, pantry))
    .sort((a, b) => b.percent - a.percent || b.recipe.rating - a.recipe.rating);
}

export function expiringSoon(pantry: PantryItem[], within = 3): PantryItem[] {
  return [...pantry]
    .filter((p) => daysUntil(p.expires) <= within)
    .sort((a, b) => daysUntil(a.expires) - daysUntil(b.expires));
}
