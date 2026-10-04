import { LANGS } from "@/lib/i18n/langs";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";

export function LangSelect({ className, tone = "light" }: { className?: string; tone?: "light" | "dark" }) {
  const { lang, setLang, t } = useLocale();
  return (
    <label className={cn("inline-flex items-center", className)}>
      <span className="sr-only">{t("lang_label")}</span>
      <select
        value={lang}
        aria-label={t("lang_label")}
        onChange={(e) => setLang(e.target.value as typeof lang)}
        className={cn(
          "h-10 cursor-pointer rounded-full border bg-transparent px-3 text-sm font-semibold outline-none focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2",
          tone === "light"
            ? "border-line text-ink focus-visible:outline-green"
            : "border-white/20 text-white focus-visible:outline-mint",
        )}
      >
        {LANGS.map((item) => (
          <option key={item.id} value={item.id} className="text-ink">
            {item.name}
          </option>
        ))}
      </select>
    </label>
  );
}
