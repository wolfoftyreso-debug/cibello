import { Check } from "lucide-react";
import { recipeById, recipeNutrition } from "@/lib/cibello/data";
import { mealImage } from "@/lib/cibello/marketing";
import { useKitchen } from "@/lib/cibello/store";
import type { CookEntry } from "@/lib/cibello/types";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";

function dayKey(iso: string) {
  return iso.slice(0, 10);
}

function groupLog(log: CookEntry[]) {
  const groups: { key: string; items: CookEntry[] }[] = [];
  for (const entry of log) {
    const key = dayKey(entry.cookedAt);
    const last = groups[groups.length - 1];
    if (last && last.key === key) last.items.push(entry);
    else groups.push({ key, items: [entry] });
  }
  return groups;
}

function dateLabel(iso: string, t: (k: string) => string, lang: string) {
  const day = iso.slice(0, 10);
  const today = new Date();
  const ymd = (d: Date) => d.toISOString().slice(0, 10);
  if (day === ymd(today)) return t("history_today");
  const yest = new Date(today);
  yest.setDate(today.getDate() - 1);
  if (day === ymd(yest)) return t("history_yesterday");
  return new Date(iso).toLocaleDateString(lang, {
    weekday: "long",
    day: "numeric",
    month: "short",
  });
}

export function HistoryTab({ onOpen }: { onOpen: (id: string) => void }) {
  const { t, lang } = useLocale();
  const cookLog = useKitchen((s) => s.cookLog);
  const groups = groupLog(cookLog);

  if (!cookLog.length) {
    return (
      <div className="rounded-2xl bg-surface p-6">
        <h1 className="font-display text-3xl font-semibold">{t("history_empty_h")}</h1>
        <p className="mt-2 max-w-[42ch] text-muted">{t("history_empty_p")}</p>
      </div>
    );
  }

  return (
    <div>
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-3xl font-semibold">{t("history_h")}</h1>
          <p className="mt-1 text-muted">{t("history_lead")}</p>
        </div>
        <p className="text-sm font-semibold text-muted">{t("dishes_n", { n: cookLog.length })}</p>
      </div>

      <div className="mt-6 space-y-8">
        {groups.map((group) => (
          <section key={group.key}>
            <h2 className="text-sm font-bold uppercase tracking-[0.14em] text-muted">
              {dateLabel(group.items[0].cookedAt, t, lang)}
            </h2>
            <div className="mt-3 grid gap-4 sm:grid-cols-2">
              {group.items.map((entry) => {
                const recipe = recipeById(entry.recipeId);
                const nut = recipeNutrition(entry.recipeId);
                const time = recipe?.time ?? 25;
                return (
                  <button
                    key={entry.id}
                    type="button"
                    onClick={() => onOpen(entry.recipeId)}
                    className="flex items-center gap-3 rounded-2xl bg-surface p-3 text-left hover:bg-green-l/40"
                  >
                    <img src={mealImage(entry.recipeId)} alt="" className="size-12 shrink-0 rounded-lg object-cover" />
                    <span className="flex min-w-0 flex-1 flex-col justify-center">
                      <span className="line-clamp-2 font-display text-lg font-semibold leading-snug">
                        {entry.title}
                      </span>
                      <span className="mt-2 flex flex-wrap items-center gap-x-3 gap-y-1 text-sm text-muted">
                        <span className="tabular-nums">{nut.kcal} kcal</span>
                        <span className="tabular-nums">
                          {nut.protein} {t("protein_unit")}
                        </span>
                        <span className="tabular-nums">
                          {time} {t("min")}
                        </span>
                      </span>
                    </span>
                    <span
                      className={cn(
                        "mt-2 mr-1 grid size-8 shrink-0 place-items-center rounded-full bg-green-l text-green-d",
                      )}
                      aria-hidden
                    >
                      <Check className="size-4" />
                    </span>
                  </button>
                );
              })}
            </div>
          </section>
        ))}
      </div>
    </div>
  );
}
