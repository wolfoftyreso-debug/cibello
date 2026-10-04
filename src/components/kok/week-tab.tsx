import { X } from "lucide-react";
import { useMemo, useState } from "react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { DAYS, recipeById } from "@/lib/cibello/data";
import { mealImage } from "@/lib/cibello/marketing";
import { matchRecipe, rankedRecipes, useKitchen } from "@/lib/cibello/store";
import type { DayKey } from "@/lib/cibello/types";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";
import { MealTile } from "./meal-tile";
import { Portal } from "./portal";

export function WeekTab({
  onOpen,
  flashDays,
  onFilled,
}: {
  onOpen: (id: string) => void;
  flashDays: string[];
  onFilled: () => void;
}) {
  const { t } = useLocale();
  const pantry = useKitchen((s) => s.pantry);
  const week = useKitchen((s) => s.week);
  const top = rankedRecipes(pantry, "middag").slice(0, 7);
  const [pick, setPick] = useState<DayKey | null>(null);
  const flash = new Set(flashDays);
  const picks = useMemo(() => rankedRecipes(pantry, "middag").slice(0, 6), [pantry]);

  return (
    <div>
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-3xl font-semibold">{t("week_title")}</h1>
          <p className="mt-1 text-muted">{t("week_lead")}</p>
        </div>
        <Button
          className="rounded-full"
          onClick={() => {
            useKitchen.getState().fillWeekFromMatches(top.map((m) => m.recipe.id));
            toast(t("week_filled"));
            onFilled();
          }}
        >
          {t("week_fill")}
        </Button>
      </div>

      <div className="mt-6 grid gap-3">
        {DAYS.map((d) => {
          const id = week[d.key];
          const recipe = id ? recipeById(id) : undefined;
          const match = recipe ? matchRecipe(recipe, pantry) : null;
          return (
            <div
              key={d.key}
              className={cn("rounded-2xl bg-surface px-4 py-3", flash.has(d.key) && "is-flash")}
            >
              <div className="flex min-w-0 flex-1 flex-col justify-center px-4 py-3">
                <div className="flex items-start justify-between gap-3">
                  <p className="text-xs font-bold uppercase tracking-[0.14em] text-green">{t(`day_${d.key}`)}</p>
                  {id ? (
                    <button
                      type="button"
                      className="text-sm font-semibold text-muted hover:text-green-d"
                      onClick={() => setPick(d.key)}
                    >
                      {t("week_clear")}
                    </button>
                  ) : null}
                </div>
                {match ? (
                  <button type="button" className="mt-2 flex w-full items-center gap-3 text-left" onClick={() => onOpen(match.recipe.id)}>
                    <img src={mealImage(match.recipe.id)} alt="" className="size-12 shrink-0 rounded-lg object-cover" />
                    <span>
                      <span className="block font-display text-lg font-semibold leading-snug">{match.recipe.title}</span>
                      <span className="mt-1 block text-sm text-muted">
                        {match.recipe.time} {t("min")} · {match.percent} {t("at_home")}
                      </span>
                    </span>
                  </button>
                ) : (
                  <button
                    type="button"
                    className="mt-1 text-left font-semibold text-green-d"
                    onClick={() => setPick(d.key)}
                  >
                    {t("week_add_meal")}
                  </button>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {pick ? (
        <Portal>
        <div
          className="fixed inset-0 z-overlay flex items-end justify-center bg-ink/40 sm:items-center sm:p-6"
          onClick={() => setPick(null)}
        >
          <div
            className="max-h-sheet w-full max-w-lg overflow-y-auto rounded-t-2xl bg-surface p-5 sm:rounded-2xl sm:p-6"
            onClick={(e) => e.stopPropagation()}
            role="dialog"
            aria-labelledby="pick-title"
          >
            <div className="flex items-center justify-between gap-3">
              <h2 id="pick-title" className="font-display text-2xl font-semibold">
                {t("week_pick")} · {t(`day_${pick}`)}
              </h2>
              <button
                type="button"
                className="grid size-10 place-items-center rounded-md hover:bg-bg2"
                onClick={() => setPick(null)}
                aria-label={t("close")}
              >
                <X className="size-5" />
              </button>
            </div>
            <div className="mt-5 grid gap-5 sm:grid-cols-2">
              {picks.map((m) => (
                <MealTile
                  key={m.recipe.id}
                  match={m}
                  cta={t("week_add_meal")}
                  onOpen={() => {
                    useKitchen.getState().assignDay(pick, m.recipe.id);
                    toast(t("added_day", { day: t(`day_${pick}`).toLowerCase() }));
                    setPick(null);
                  }}
                />
              ))}
            </div>
          </div>
        </div>
        </Portal>
      ) : null}
    </div>
  );
}
