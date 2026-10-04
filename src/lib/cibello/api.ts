import { createServerFn } from "@tanstack/react-start";
import { authMiddleware } from "@/lib/auth/middleware";
import { getSql } from "@/lib/db";
import type { CookEntry, DayKey, ListItem, Location, PantryItem, WeekPlan } from "./types";

const DAYS: DayKey[] = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
const LOCS: Location[] = ["kyl", "skafferi", "frys"];

export type KitchenSnapshot = {
  pantry: PantryItem[];
  list: ListItem[];
  week: WeekPlan;
  cookLog: CookEntry[];
};

type PantryRow = {
  id: string;
  item_key: string;
  name: string;
  location: string;
  qty: string;
  expires: string;
};

type ListRow = {
  id: string;
  item_key: string;
  name: string;
  amount: string;
  done: boolean;
  from_recipe: string | null;
};

type WeekRow = { day: string; recipe_id: string | null };

type CookRow = { id: string; recipe_id: string; title: string; cooked_at: string };

function emptyWeek(): WeekPlan {
  return { mon: null, tue: null, wed: null, thu: null, fri: null, sat: null, sun: null };
}

function asPantry(rows: PantryRow[]): PantryItem[] {
  return rows
    .filter((r) => LOCS.includes(r.location as Location))
    .map((r) => ({
      id: r.id,
      key: r.item_key,
      name: r.name,
      location: r.location as Location,
      qty: r.qty,
      expires: r.expires,
    }));
}

function asList(rows: ListRow[]): ListItem[] {
  return rows.map((r) => ({
    id: r.id,
    key: r.item_key,
    name: r.name,
    amount: r.amount,
    done: Boolean(r.done),
    fromRecipe: r.from_recipe ?? undefined,
  }));
}

function asWeek(rows: WeekRow[]): WeekPlan {
  const week = emptyWeek();
  for (const row of rows) {
    if (DAYS.includes(row.day as DayKey)) week[row.day as DayKey] = row.recipe_id;
  }
  return week;
}

function asCook(rows: CookRow[]): CookEntry[] {
  return rows.map((r) => ({
    id: r.id,
    recipeId: r.recipe_id,
    title: r.title,
    cookedAt: r.cooked_at,
  }));
}

export const loadKitchen = createServerFn({ method: "GET" })
  .middleware([authMiddleware])
  .handler(async ({ context }): Promise<KitchenSnapshot> => {
    const sql = await getSql();
    const uid = context.userId;
    const pantry = await sql<PantryRow>`
      select id, item_key, name, location, qty, expires
      from pantry_items where user_id = ${uid}
    `;
    const list = await sql<ListRow>`
      select id, item_key, name, amount, done, from_recipe
      from list_items where user_id = ${uid}
    `;
    const week = await sql<WeekRow>`
      select day, recipe_id from week_days where user_id = ${uid}
    `;
    const cookLog = await sql<CookRow>`
      select id, recipe_id, title, cooked_at::text as cooked_at
      from cook_log where user_id = ${uid}
      order by cooked_at desc
    `;
    return {
      pantry: asPantry(pantry),
      list: asList(list),
      week: asWeek(week),
      cookLog: asCook(cookLog),
    };
  });

type SaveInput = {
  pantry: PantryItem[];
  list: ListItem[];
  week: WeekPlan;
};

function parseSave(raw: SaveInput): SaveInput {
  return {
    pantry: Array.isArray(raw.pantry) ? raw.pantry.slice(0, 200) : [],
    list: Array.isArray(raw.list) ? raw.list.slice(0, 200) : [],
    week: { ...emptyWeek(), ...(raw.week ?? {}) },
  };
}

export const saveKitchen = createServerFn({ method: "POST" })
  .middleware([authMiddleware])
  .validator((raw: SaveInput) => parseSave(raw))
  .handler(async ({ context, data }) => {
    const sql = await getSql();
    const uid = context.userId;
    await sql`delete from pantry_items where user_id = ${uid}`;
    for (const item of data.pantry) {
      const loc = LOCS.includes(item.location) ? item.location : "kyl";
      await sql`
        insert into pantry_items (id, user_id, item_key, name, location, qty, expires)
        values (${item.id}, ${uid}, ${item.key}, ${item.name}, ${loc}, ${item.qty}, ${item.expires})
      `;
    }
    await sql`delete from list_items where user_id = ${uid}`;
    for (const item of data.list) {
      await sql`
        insert into list_items (id, user_id, item_key, name, amount, done, from_recipe)
        values (${item.id}, ${uid}, ${item.key}, ${item.name}, ${item.amount}, ${item.done}, ${item.fromRecipe ?? null})
      `;
    }
    await sql`delete from week_days where user_id = ${uid}`;
    for (const day of DAYS) {
      await sql`
        insert into week_days (user_id, day, recipe_id)
        values (${uid}, ${day}, ${data.week[day]})
      `;
    }
    return { ok: true as const };
  });

type CookInput = {
  id: string;
  recipeId: string;
  title: string;
  cookedAt: string;
};

export const addCookLog = createServerFn({ method: "POST" })
  .middleware([authMiddleware])
  .validator((raw: CookInput): CookInput => ({
    id: String(raw.id ?? "").slice(0, 64),
    recipeId: String(raw.recipeId ?? "").slice(0, 64),
    title: String(raw.title ?? "").slice(0, 160),
    cookedAt: String(raw.cookedAt ?? new Date().toISOString()).slice(0, 40),
  }))
  .handler(async ({ context, data }) => {
    if (!data.id || !data.recipeId || !data.title) return { ok: false as const };
    const sql = await getSql();
    await sql`
      insert into cook_log (id, user_id, recipe_id, title, cooked_at)
      values (${data.id}, ${context.userId}, ${data.recipeId}, ${data.title}, ${data.cookedAt})
      on conflict (id) do nothing
    `;
    return { ok: true as const };
  });
