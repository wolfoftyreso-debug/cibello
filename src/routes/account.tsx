import { createFileRoute } from "@tanstack/react-router";
import { SiteLayout } from "@/components/site/layout";
import { StoreButtons } from "@/components/site/store-buttons";
import { useLocale } from "@/lib/i18n/locale";
import { pageMeta } from "@/lib/cibello/seo";

export const Route = createFileRoute("/account")({
  component: KontoPage,
  head: () =>
    pageMeta({
      title: "Konto | Cibello",
      description: "Ditt Cibello-konto.",
      path: "/account",
      noindex: true,
    }),
});

function KontoPage() {
  const { t } = useLocale();
  return (
    <SiteLayout>
      <article className="mx-auto w-[min(720px,92vw)] py-16">
        <p className="text-sm font-bold uppercase tracking-[0.14em] text-green">{t("nav_account")}</p>
        <h1 className="mt-3 font-display text-4xl font-semibold">{t("nav_account")}</h1>
        <p className="mt-4 max-w-[42ch] text-lg text-muted">{t("app_nudge")}</p>
        <StoreButtons className="mt-8" />
      </article>
    </SiteLayout>
  );
}
