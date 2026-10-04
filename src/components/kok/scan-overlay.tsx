import { Camera, X } from "lucide-react";
import { Portal } from "./portal";
import { useEffect, useMemo, useState } from "react";
import { SCAN_BATCH } from "@/lib/cibello/data";
import { pantryImage } from "@/lib/cibello/marketing";
import { useKitchen } from "@/lib/cibello/store";
import type { PantryItem } from "@/lib/cibello/types";
import { useLocale } from "@/lib/i18n/locale";

export function ScanOverlay({
  onClose,
  onDone,
}: {
  onClose: () => void;
  onDone: (items: PantryItem[]) => void;
}) {
  const { t } = useLocale();
  const pantry = useKitchen((s) => s.pantry);
  const pending = useMemo(
    () => SCAN_BATCH.filter((item) => !pantry.some((p) => p.key === item.key)).slice(0, 3),
    [pantry],
  );
  const [ready, setReady] = useState(false);

  useEffect(() => {
    const show = window.setTimeout(() => setReady(true), 1600);
    const finish = window.setTimeout(() => {
      const added = useKitchen.getState().scanFridge();
      onDone(added);
    }, 2800);
    return () => {
      window.clearTimeout(show);
      window.clearTimeout(finish);
    };
  }, [onDone]);

  return (
    <Portal>
    <div className="fixed inset-0 z-overlay flex flex-col bg-green-x text-surface">
      <div className="flex items-center justify-between px-5 py-4">
        <p className="flex items-center gap-2 text-sm font-bold uppercase tracking-[0.14em] text-mint">
          <Camera className="size-4" />
          {t("scan")}
        </p>
        <button
          type="button"
          className="grid size-11 place-items-center rounded-full hover:bg-surface/10"
          onClick={onClose}
          aria-label={t("close")}
        >
          <X className="size-5" />
        </button>
      </div>

      <div className="mx-auto flex w-full max-w-md flex-1 flex-col justify-center px-5 pb-10">
        <div className="relative aspect-photo overflow-hidden rounded-2xl bg-green-d">
          <div className="pointer-events-none absolute inset-4 rounded-xl border border-mint/70" />
          <div className="scan-sweep" />
        </div>
        <p className="mt-5 text-center text-lg text-green-l">{ready ? t("scan_found_label") : t("scan_looking")}</p>
        <p className="mt-1 text-center text-sm text-green-l/80">{t("scan_hint")}</p>
        <div className="mt-6 flex flex-wrap justify-center gap-2">
          {(pending.length ? pending : SCAN_BATCH.slice(0, 3)).map((item) => (
            <span
              key={item.key}
              className="scan-chip inline-flex items-center gap-2 rounded-full bg-surface/15 px-3 py-1.5 text-sm font-semibold"
            >
              <img src={pantryImage(item.key)} alt="" className="size-6 rounded-full object-cover" />
              {item.name}
            </span>
          ))}
        </div>
      </div>
    </div>
    </Portal>
  );
}
