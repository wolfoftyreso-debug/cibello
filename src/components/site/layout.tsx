import type { ReactNode } from "react";
import { useRouterState } from "@tanstack/react-router";
import { Toaster } from "sonner";
import { SiteFooter } from "./footer";
import { SiteHeader } from "./header";
import { useLocale } from "@/lib/i18n/locale";

export function SiteLayout({ children }: { children: ReactNode }) {
  const { t } = useLocale();
  const pathname = useRouterState({ select: (s) => s.location.pathname });
  return (
    <div className="min-h-dvh bg-bg text-ink">
      <Toaster position="top-center" richColors />
      <a
        href="#main"
        className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:rounded-md focus:bg-surface focus:px-3 focus:py-2"
      >
        {t("skip")}
      </a>
      <SiteHeader />
      <main id="main" className={pathname === "/" ? undefined : "pt-[var(--header-h)]"}>
        {children}
      </main>
      <SiteFooter />
    </div>
  );
}
