import { createFileRoute, Link } from "@tanstack/react-router";
import { SiteLayout } from "@/components/site/layout";
import { COMPANY, COMPANY_ADDRESS } from "@/lib/cibello/company";
import { useLocale } from "@/lib/i18n/locale";
import { pageMeta } from "@/lib/cibello/seo";

export const Route = createFileRoute("/terms")({
  component: Page,
  head: () =>
    pageMeta({
      title: "Villkor | Cibello",
      description: "Villkor för Cibello, matappen från LandveX AB. Tjänsten är avsedd för personer som är minst 18 år.",
      path: "/terms",
    }),
});

function Page() {
  const { t } = useLocale();
  return (
    <SiteLayout>
      <article className="mx-auto w-[min(720px,92vw)] py-12">
        <h1 className="font-display text-4xl font-semibold">Villkor</h1>
        <p className="mt-4 text-muted">
          Tjänsten tillhandahålls av {COMPANY.legalName}, org.nr {COMPANY.orgNr}, {COMPANY_ADDRESS}.
          Appen är tills vidare avsedd för personer som är minst 18 år, eftersom villkoren för den AI-tjänst som
          används kräver vuxna användare.
        </p>
        <div className="mt-8 space-y-6">
          <section>
            <h2 className="font-display text-xl font-semibold">Provperiod</h2>
            <p className="mt-2 text-muted">
              14 dagar utan kort. Hushållsfunktioner ingår under provperioden och därefter med en betalplan. Priser
              visas i App Store och Google Play.
            </p>
          </section>
          <section>
            <h2 className="font-display text-xl font-semibold">Inget medicinskt råd</h2>
            <p className="mt-2 text-muted">
              Recept, allergenfilter och näringsvärden är vägledning, inte medicinsk rådgivning eller garanti. Du
              ansvarar för att kontrollera ingredienser och förpackningar, särskilt vid allergi.
            </p>
          </section>
          <section>
            <h2 className="font-display text-xl font-semibold">AI kan ha fel</h2>
            <p className="mt-2 text-muted">
              Skanning kan känna igen fel vara eller missa något. Du ska granska resultatet innan det används.
            </p>
          </section>
        </div>
        <p className="mt-8 text-sm text-muted">
          <Link to="/privacy" className="font-semibold text-green-d">{t("foot_privacy")}</Link>. Kontakt:{" "}
          <a href={`mailto:${COMPANY.email}`} className="font-semibold text-green-d">
            {COMPANY.email}
          </a>
          . Telefon:{" "}
          <a href={`tel:${COMPANY.phoneE164}`} className="font-semibold text-green-d">
            {COMPANY.phoneDisplay}
          </a>
          .
        </p>
      </article>
    </SiteLayout>
  );
}
