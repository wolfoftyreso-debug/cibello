import { ShoppingCart, X } from "lucide-react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { DAYS } from "@/lib/cibello/data";
import { mealImage } from "@/lib/cibello/marketing";
import { useKitchen, type Match } from "@/lib/cibello/store";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";
import { Portal } from "./portal";

export function RecipeSheet({ match, onClose }: { match: Match; onClose: () => void }) {
  const { t } = useLocale();
  const week = useKitchen((s) => s.week);
  const { recipe } = match;

  return (
    <Portal>
    <div
      className="fixed inset-0 z-overlay flex items-end justify-center bg-ink/40 p-0 sm:items-center sm:p-6"
      onClick={onClose}
    >
      <div
        className="max-h-sheet w-full max-w-lg overflow-y-auto rounded-t-2xl bg-surface p-5 shadow-xl sm:rounded-2xl sm:p-6"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-labelledby="recipe-title"
      >
        <div className="flex items-start gap-3">
          <img src={mealImage(recipe.id)} alt="" className="size-16 shrink-0 rounded-lg object-cover" />
          <div className="min-w-0 flex-1">
            <p className="text-sm text-muted">
              {recipe.time} {t("min")} · {match.percent} {t("at_home")}
            </p>
            <div className="mt-1 flex items-start justify-between gap-3">
              <h2 id="recipe-title" className="font-display text-2xl font-semibold leading-tight">
                {recipe.title}
              </h2>
              <button
                type="button"
                className="grid size-10 shrink-0 place-items-center rounded-md hover:bg-bg2"
                onClick={onClose}
                aria-label={t("close")}
              >
                <X className="size-5" />
              </button>
            </div>
          </div>
        </div>
        <p className="mt-2 text-sm text-muted">
          {t(match.why.key, {
            percent: match.why.percent,
            name: match.why.name ?? "",
            missing: match.why.missing ?? "",
          })}
        </p>
        <ul className="mt-4 space-y-2">
          {recipe.ingredients.map((ing) => {
            const have = !match.missing.some((m) => m.key === ing.key);
            return (
              <li key={ing.key} className="flex items-center justify-between gap-3 text-sm">
                <span className={have ? undefined : "text-muted"}>{ing.name}</span>
                <span className={cn("font-semibold", have ? "text-green-d" : "text-amber")}>
                  {have ? t("have") : t("need")} · {ing.amount}
                </span>
              </li>
            );
          })}
        </ul>
        <ol className="mt-5 list-decimal space-y-2 pl-5 text-muted">
          {recipe.steps.map((s) => (
            <li key={s}>{s}</li>
          ))}
        </ol>
        <div className="mt-5 flex flex-col gap-2">
          <Button
            onClick={() => {
              const n = useKitchen.getState().addMissingToList(recipe);
              toast(n === 0 ? t("have_all") : n === 1 ? t("added_one") : t("added_n", { n }));
            }}
          >
            <ShoppingCart className="size-4" />
            {t("add_missing")}
          </Button>
          <div className="grid grid-cols-7 gap-1">
            {DAYS.map((d) => (
              <button
                key={d.key}
                type="button"
                onClick={() => {
                  useKitchen.getState().assignDay(d.key, recipe.id);
                  toast(t("added_day", { day: t(`day_${d.key}`).toLowerCase() }));
                }}
                className={cn(
                  "h-11 rounded-md text-xs font-semibold",
                  week[d.key] === recipe.id ? "bg-green text-surface" : "bg-bg2 text-muted hover:bg-green-l",
                )}
              >
                {t(`day_${d.key}_s`)}
              </button>
            ))}
          </div>
        </div>
        <p className="mt-4 text-xs text-muted">{t("allergen_note")}</p>
      </div>
    </div>
    </Portal>
  );
}
