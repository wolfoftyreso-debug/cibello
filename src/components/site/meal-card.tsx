import { Link } from "@tanstack/react-router";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";

export function MealCard({
  title,
  time,
  image,
  atHome,
  badge,
  layout = "grid",
}: {
  title: string;
  with?: string;
  time: number;
  tag?: string;
  chips?: string[];
  image: string;
  atHome: number;
  badge?: string;
  layout?: "grid" | "film";
}) {
  const { t } = useLocale();
  const film = layout === "film";
  return (
    <article className="group flex h-full flex-col">
      <div className={cn("relative overflow-hidden rounded-2xl bg-bg2", film ? "aspect-portrait" : "aspect-photo")}>
        <img
          src={image}
          alt={title}
          className="size-full object-cover transition-transform duration-700 ease-out-soft group-hover:scale-105"
        />
        <span className="absolute left-3 top-3 rounded-full bg-surface/95 px-2.5 py-1 text-xs font-semibold tabular-nums text-ink">
          {time} {t("min")}
        </span>
        {badge ? (
          <span className="absolute right-3 top-3 rounded-full bg-surface px-2.5 py-1 text-xs font-semibold text-green-d">
            {badge}
          </span>
        ) : null}
        <span className="absolute bottom-3 left-3 rounded-full bg-green px-2.5 py-1 text-xs font-semibold text-surface">
          {atHome} {t("at_home")}
        </span>
      </div>
      <h3 className="mt-3 line-clamp-2 min-h-12 font-display text-xl font-semibold leading-snug">{title}</h3>
      <div className="mt-3">
        <Link
          to="/kitchen"
          className="inline-flex h-10 items-center rounded-full bg-dark px-4 text-sm font-semibold text-surface transition-colors duration-150 hover:bg-ink"
        >
          {t("cook_this")}
        </Link>
      </div>
    </article>
  );
}
