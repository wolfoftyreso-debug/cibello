import { Camera, Plus, Trash2 } from "lucide-react";
import { useState } from "react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { daysUntil } from "@/lib/cibello/data";
import { pantryImage } from "@/lib/cibello/marketing";
import { expiringSoon, useKitchen } from "@/lib/cibello/store";
import type { Location } from "@/lib/cibello/types";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";

const GROUPS: Location[] = ["kyl", "skafferi", "frys"];

export function PantryTab({
  soon,
  flashIds,
  onScan,
}: {
  soon: ReturnType<typeof expiringSoon>;
  flashIds: string[];
  onScan: () => void;
}) {
  const { t } = useLocale();
  const pantry = useKitchen((s) => s.pantry);
  const [name, setName] = useState("");
  const [loc, setLoc] = useState<Location>("kyl");
  const flash = new Set(flashIds);

  const expiryLabel = (iso: string) => {
    const d = daysUntil(iso);
    if (d < 0) return t("exp_gone");
    if (d === 0) return t("exp_today");
    if (d === 1) return t("exp_tomorrow");
    return t("exp_days", { n: d });
  };

  return (
    <div>
      <div className="flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="font-display text-3xl font-semibold">{t("shot_pantry_t")}</h1>
          <p className="mt-1 text-muted">{t("pantry_lead")}</p>
        </div>
        <Button className="rounded-full" onClick={onScan}>
          <Camera className="size-4" />
          {t("scan")}
        </Button>
      </div>

      {soon.length > 0 ? (
        <p className="mt-4 rounded-xl bg-amber-l px-4 py-3 text-sm">{t("soon_n", { n: soon.length })}</p>
      ) : null}

      <form
        className="mt-4 flex flex-col gap-2 sm:flex-row"
        onSubmit={(e) => {
          e.preventDefault();
          if (!name.trim()) return;
          const key = name.trim().toLowerCase().replace(/\s+/g, "-");
          useKitchen.getState().addPantry({
            key,
            name: name.trim(),
            location: loc,
            qty: "1",
            expires: new Date(Date.now() + 7 * 86400000).toISOString().slice(0, 10),
          });
          setName("");
          toast(t("added_pantry"));
        }}
      >
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder={t("add_item")}
          className="h-12 flex-1 rounded-md border border-line bg-surface px-3 outline-none focus:border-green"
        />
        <select
          value={loc}
          onChange={(e) => setLoc(e.target.value as Location)}
          className="h-12 rounded-md border border-line bg-surface px-3"
        >
          {GROUPS.map((g) => (
            <option key={g} value={g}>
              {t(`loc_${g}`)}
            </option>
          ))}
        </select>
        <Button type="submit" className="h-12 rounded-full">
          <Plus className="size-4" />
          {t("add")}
        </Button>
      </form>

      {pantry.length === 0 ? (
        <button type="button" onClick={onScan} className="mt-8 w-full rounded-2xl border border-line bg-surface p-6 text-left">
          <p className="font-display text-2xl font-semibold">{t("pantry_empty_h")}</p>
          <p className="mt-2 text-muted">{t("pantry_empty_p")}</p>
          <span className="mt-4 inline-flex h-12 items-center gap-2 rounded-full bg-green-x px-5 font-semibold text-surface">
            <Camera className="size-4" />
            {t("scan")}
          </span>
        </button>
      ) : (
        <div className="mt-8 space-y-8">
          {GROUPS.map((g) => {
            const items = pantry.filter((p) => p.location === g);
            if (!items.length) return null;
            return (
              <section key={g}>
                <h2 className="mb-3 font-display text-lg font-semibold">{t(`loc_${g}`)}</h2>
                <ul className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">
                  {items.map((item) => {
                    const d = daysUntil(item.expires);
                    return (
                      <li
                        key={item.id}
                        className={cn("rounded-2xl bg-surface p-4", flash.has(item.id) && "is-flash")}
                      >
                        <div className="flex items-start gap-3">
                          <img src={pantryImage(item.key)} alt="" className="size-12 shrink-0 rounded-lg object-cover" />
                          <div className="min-w-0 flex-1">
                            <div className="flex items-start justify-between gap-2">
                              <p className="font-semibold">{item.name}</p>
                              <button
                                type="button"
                                aria-label={t("remove_item", { name: item.name })}
                                className="grid size-9 shrink-0 place-items-center rounded-full text-muted hover:bg-danger-l hover:text-danger"
                                onClick={() => useKitchen.getState().removePantry(item.id)}
                              >
                                <Trash2 className="size-4" />
                              </button>
                            </div>
                            <p className="mt-1 text-sm text-muted">{item.qty}</p>
                            <p
                              className={cn(
                                "mt-2 text-xs font-semibold",
                                d <= 1 ? "text-danger" : d <= 3 ? "text-amber" : "text-green-d",
                              )}
                            >
                              {expiryLabel(item.expires)}
                            </p>
                          </div>
                        </div>
                      </li>
                    );
                  })}
                </ul>
              </section>
            );
          })}
        </div>
      )}
    </div>
  );
}
