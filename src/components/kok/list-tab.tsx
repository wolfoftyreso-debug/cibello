import { Check, Plus, ShoppingCart, Trash2 } from "lucide-react";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { uid } from "@/lib/cibello/data";
import { useKitchen } from "@/lib/cibello/store";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";

export function ListTab() {
  const { t } = useLocale();
  const list = useKitchen((s) => s.list);
  const [name, setName] = useState("");
  const pending = list.filter((i) => !i.done);
  const done = list.filter((i) => i.done);

  return (
    <div>
      <h1 className="font-display text-3xl font-semibold">{t("list_title")}</h1>
      <p className="mt-1 text-muted">{t("list_lead")}</p>

      <form
        className="mt-4 flex gap-2"
        onSubmit={(e) => {
          e.preventDefault();
          if (!name.trim()) return;
          useKitchen.getState().addList({
            key: uid("k"),
            name: name.trim(),
            amount: "",
          });
          setName("");
        }}
      >
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder={t("list_placeholder")}
          className="h-12 flex-1 rounded-md border border-line bg-surface px-3 outline-none focus:border-green"
        />
        <Button type="submit" className="h-12 rounded-full" aria-label={t("add")}>
          <Plus className="size-4" />
        </Button>
      </form>

      {list.length === 0 ? (
        <div className="mt-8 rounded-2xl border border-line bg-surface p-6">
          <ShoppingCart className="size-6 text-green" />
          <p className="mt-3 font-display text-2xl font-semibold">{t("list_empty_h")}</p>
          <p className="mt-2 max-w-[36ch] text-muted">{t("list_empty_p")}</p>
        </div>
      ) : (
        <ul className="mt-5 divide-y divide-line overflow-hidden rounded-xl border border-line bg-surface">
          {[...pending, ...done].map((item) => (
            <li key={item.id} className="flex items-center gap-2 px-2">
              <button
                type="button"
                onClick={() => useKitchen.getState().toggleList(item.id)}
                className="flex min-w-0 flex-1 items-center gap-3 px-2 py-3 text-left"
              >
                <span
                  className={cn(
                    "grid size-6 shrink-0 place-items-center rounded-md border",
                    item.done ? "border-green bg-green text-surface" : "border-line",
                  )}
                >
                  {item.done ? <Check className="size-3.5" /> : null}
                </span>
                <span className={cn("min-w-0", item.done && "text-muted line-through")}>
                  <span className="block font-semibold">{item.name}</span>
                  <span className="block text-sm text-muted">
                    {[item.amount, item.fromRecipe].filter(Boolean).join(" · ")}
                  </span>
                </span>
              </button>
              <button
                type="button"
                aria-label={t("remove_item", { name: item.name })}
                className="grid size-10 place-items-center text-muted hover:text-danger"
                onClick={() => useKitchen.getState().removeList(item.id)}
              >
                <Trash2 className="size-4" />
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
