import { mealImage } from "@/lib/cibello/marketing";
import type { Match } from "@/lib/cibello/store";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";

export function MealTile({
  match,
  onOpen,
  flash,
  cta,
}: {
  match: Match;
  onOpen: () => void;
  flash?: boolean;
  cta?: string;
}) {
  const { t } = useLocale();
  const r = match.recipe;
  return (
    <button
      type="button"
      onClick={onOpen}
      className={cn(
        "flex flex-wrap items-center justify-between gap-3 rounded-xl border border-line bg-surface px-4 py-4 text-left",
        flash && "is-flash",
      )}
    >
      <span className="flex min-w-0 items-center gap-3">
        <img src={mealImage(r.id)} alt="" className="size-12 shrink-0 rounded-lg object-cover" />
        <span>
          <span className="block font-display text-lg font-semibold leading-snug">{r.title}</span>
          <span className="mt-1 block text-sm text-muted">
            {r.time} {t("min")} · {match.percent} {t("at_home")}
          </span>
        </span>
      </span>
      <span className="inline-flex h-11 w-full shrink-0 items-center justify-center rounded-full bg-dark px-4 text-sm font-semibold text-surface sm:h-10 sm:w-auto">
        {cta ?? t("cook_this")}
      </span>
    </button>
  );
}