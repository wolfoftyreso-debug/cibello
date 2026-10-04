import { Camera, Search } from "lucide-react";
import { MEAL_CHIPS } from "@/lib/cibello/data";
import { type Match, expiringSoon } from "@/lib/cibello/store";
import type { Recipe } from "@/lib/cibello/types";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";
import { MealTile } from "./meal-tile";

export function RecipesTab({
  matches,
  soon,
  meal,
  setMeal,
  q,
  setQ,
  onOpen,
  onScan,
}: {
  matches: Match[];
  soon: ReturnType<typeof expiringSoon>;
  meal: Recipe["meal"] | "all";
  setMeal: (m: Recipe["meal"] | "all") => void;
  q: string;
  setQ: (s: string) => void;
  onOpen: (r: Recipe) => void;
  onScan: () => void;
}) {
  const { t } = useLocale();

  return (
    <div>
      <button
        type="button"
        onClick={onScan}
        className="flex w-full flex-wrap items-center justify-between gap-4 rounded-2xl bg-green-x px-6 py-6 text-left text-surface"
      >
        <span>
          <span className="block font-display text-2xl font-semibold">{t("scan")}</span>
          <span className="mt-1 block max-w-[36ch] text-sm text-green-l">{t("plain_lead")}</span>
        </span>
        <span className="inline-flex h-12 items-center gap-2 rounded-full bg-mint px-5 font-semibold text-green-x">
          <Camera className="size-4" />
          {t("scan")}
        </span>
      </button>

      <div className="mt-8">
        <h1 className="font-display text-3xl font-semibold">{t("app_q")}</h1>
        <p className="mt-1 text-muted">{t("app_sub2")}</p>
      </div>

      {soon.length > 0 ? (
        <div className="mt-4 rounded-2xl bg-amber-l px-4 py-3 text-sm text-ink">
          <span className="font-semibold text-amber">{t("soon")}: </span>
          {soon.map((s) => s.name).join(", ")}
        </div>
      ) : null}

      <label className="mt-5 flex h-12 items-center gap-2 rounded-full border border-line bg-surface px-4">
        <Search className="size-4 text-muted" />
        <input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder={t("app_search")}
          className="h-full w-full bg-transparent outline-none"
        />
      </label>

      <div className="mt-3 flex flex-wrap gap-2">
        {MEAL_CHIPS.map((c, i) => (
          <button
            key={c.id}
            type="button"
            onClick={() => setMeal(c.id)}
            className={cn(
              "h-11 rounded-full border px-3.5 text-sm font-semibold",
              meal === c.id ? "border-green bg-green text-surface" : "border-line bg-surface text-ink hover:border-green",
            )}
          >
            {t(`app_c${i}`)}
          </button>
        ))}
      </div>

      <div className="mt-6 grid gap-3">
        {matches.map((m) => (
          <MealTile key={m.recipe.id} match={m} onOpen={() => onOpen(m.recipe)} />
        ))}
      </div>
    </div>
  );
}
