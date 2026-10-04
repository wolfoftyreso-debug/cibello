import { createFileRoute, Link } from "@tanstack/react-router";
import { SiteLayout } from "@/components/site/layout";
import { COMPANY, COMPANY_ADDRESS } from "@/lib/cibello/company";
import { useLocale } from "@/lib/i18n/locale";
import { pageMeta } from "@/lib/cibello/seo";

export const Route = createFileRoute("/privacy")({
  component: Page,
  head: () =>
    pageMeta({
      title: "Integritetspolicy | Cibello",
      description: "Så behandlar LandveX AB personuppgifter i Cibello. Data lagras inom EU. Du kan se och radera ditt konto.",
      path: "/privacy",
    }),
});

function Page() {
  const { t } = useLocale();
  return (
    <SiteLayout>
      <article className="mx-auto w-[min(720px,92vw)] py-12">
        <h1 className="font-display text-4xl font-semibold">Integritetspolicy</h1>
        <p className="mt-4 text-muted">
          Personuppgiftsansvarig är {COMPANY.legalName}, org.nr {COMPANY.orgNr}, {COMPANY_ADDRESS}. Kontakt:{" "}
          <a className="font-semibold text-green-d" href={`mailto:${COMPANY.privacyEmail}`}>
            {COMPANY.privacyEmail}
          </a>
          . Telefon:{" "}
          <a className="font-semibold text-green-d" href={`tel:${COMPANY.phoneE164}`}>
            {COMPANY.phoneDisplay}
          </a>
          .
        </p>
        <div className="mt-8 space-y-6">
          <section>
            <h2 className="font-display text-xl font-semibold">Vad vi samlar in</h2>
            <p className="mt-2 text-muted">
              Konto (e-post), matlager, receptval, inköpslistor och — om du fotar — bilder av kyl, skafferi eller kvitto.
              Bilderna analyseras för att känna igen varor. Du granskar resultatet innan det sparas.
            </p>
          </section>
          <section>
            <h2 className="font-display text-xl font-semibold">Var data lagras</h2>
            <p className="mt-2 text-muted">
              Inom EU. Vi säljer inte personuppgifter. Du kan se dina uppgifter i appen och radera kontot när du vill.
            </p>
          </section>
          <section>
            <h2 className="font-display text-xl font-semibold">AI-träning</h2>
            <p className="mt-2 text-muted">
              Cibello AI tränas bara på dina egna rättelser och, om du väljer det separat, sanerade bilder. Båda valen är
              av från början.
            </p>
          </section>
          <section>
            <h2 className="font-display text-xl font-semibold">Den här webbplatsen</h2>
            <p className="mt-2 text-muted">
              Matlager, veckomeny och inköpslista i köksdelen lagras lokalt i din webbläsare. Inget av det skickas till en server.
            </p>
          </section>
        </div>
        <p className="mt-8 text-sm text-muted">
          Svensk version gäller vid avvikelse mot översättningar. Se även{" "}
          <Link to="/terms" className="font-semibold text-green-d">{t("foot_terms")}</Link>.
        </p>
      </article>
    </SiteLayout>
  );
}
