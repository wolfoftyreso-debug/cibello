import { Link, useRouterState } from "@tanstack/react-router";
import { Menu, X } from "lucide-react";
import { useEffect, useRef, useState } from "react";
import { Button } from "@/components/ui/button";
import { Logo } from "./logo";
import { LangSelect } from "./lang-select";
import { cn } from "@/lib/utils";
import { useLocale } from "@/lib/i18n/locale";

export function SiteHeader() {
  const [open, setOpen] = useState(false);
  const pathname = useRouterState({ select: (s) => s.location.pathname });
  const { t } = useLocale();
  const [overFilm, setOverFilm] = useState(pathname === "/");
  const inverted = pathname === "/" && overFilm && !open;

  const NAV = [
    { to: "/", hash: "how", label: t("nav_how") },
    { to: "/about", label: t("nav_about") },
  ] as const;

  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [open]);

  const bar = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const onScroll = () => {
      const y = window.scrollY;
      const max = document.documentElement.scrollHeight - window.innerHeight;
      if (bar.current) bar.current.style.setProperty("--progress", String(max > 0 ? y / max : 0));
      const marker = document.querySelector("[data-header='invert']");
      const next = marker ? y < marker.getBoundingClientRect().bottom + y - 80 : false;
      setOverFilm((prev) => (prev === next ? prev : next));
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
    };
  }, [pathname]);

  return (
    <header
      className={cn(
        "fixed inset-x-0 top-0 z-50 border-b pt-[env(safe-area-inset-top)] transition-colors duration-300",
        inverted ? "border-transparent bg-gradient-to-b from-green-x/70 to-transparent" : "border-line bg-surface/90 backdrop-blur-md",
      )}
    >
      <nav className="page-wrap flex items-center justify-between gap-4 py-3.5" aria-label={t("nav_main")}>
        <Logo className={inverted ? "text-surface" : undefined} />
        <div
          className={cn(
            "hidden items-center gap-7 text-[0.95rem] font-semibold lg:flex",
            inverted ? "text-white/75" : "text-muted",
          )}
        >
          {NAV.map((item) => (
            <Link
              key={item.label}
              to={item.to}
              hash={"hash" in item ? item.hash : undefined}
              className={cn(
                inverted ? "hover:text-mint" : "hover:text-green",
                pathname === item.to && item.to !== "/" && !inverted && "text-green-d",
              )}
            >
              {item.label}
            </Link>
          ))}
        </div>
        <div className="flex items-center gap-2">
          <LangSelect className="hidden sm:inline-flex" tone={inverted ? "dark" : "light"} />
          <Button
            asChild
            variant="outline"
            className={cn(
              "hidden rounded-full md:inline-flex",
              inverted && "border-white/35 bg-transparent text-white hover:bg-white/10",
            )}
          >
            <a href="https://apps.apple.com/app/id6807100747" rel="noopener">
              {t("nav_cta")}
            </a>
          </Button>
          <button
            type="button"
            className={cn(
              "grid size-11 place-items-center rounded-md lg:hidden",
              inverted && "text-surface",
            )}
            aria-label={open ? t("menu_close") : t("menu_open")}
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
          >
            {open ? <X className="size-5" /> : <Menu className="size-5" />}
          </button>
        </div>
      </nav>
      {open ? (
        <div className="border-t border-line bg-surface px-[4vw] py-4 lg:hidden">
          <div className="flex flex-col gap-1">
            {NAV.map((item) => (
              <Link
                key={item.label}
                to={item.to}
                hash={"hash" in item ? item.hash : undefined}
                className="rounded-md px-3 py-3 font-semibold hover:bg-green-l"
                onClick={() => setOpen(false)}
              >
                {item.label}
              </Link>
            ))}
            <LangSelect className="mt-2" />
            <Button asChild className="mt-2 w-full rounded-full">
              <a href="https://apps.apple.com/app/id6807100747" rel="noopener" onClick={() => setOpen(false)}>
                {t("nav_cta")}
              </a>
            </Button>
          </div>
        </div>
      ) : null}
      <div
        ref={bar}
        className="progress-line pointer-events-none absolute inset-x-0 bottom-0 h-px bg-green"
      />
    </header>
  );
}
