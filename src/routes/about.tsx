import { createFileRoute } from "@tanstack/react-router";
import { SiteLayout } from "@/components/site/layout";
import { StoreButtons } from "@/components/site/store-buttons";
import { COMPANY, COMPANY_ADDRESS } from "@/lib/cibello/company";
import { useLocale } from "@/lib/i18n/locale";
import { pageMeta } from "@/lib/cibello/seo";

export const Route = createFileRoute("/about")({
  component: OmPage,
  head: () =>
    pageMeta({
      title: "Om Cibello – appen från LandveX AB",
      description: "Cibello är en matapp från LandveX AB i Tyresö. Fota kylen, laga det du har och minska matsvinnet.",
      path: "/about",
    }),
});

function OmPage() {
  const { t } = useLocale();
  return (
    <SiteLayout>
      <article className="mx-auto w-[min(720px,92vw)] py-12">
        <p className="text-[0.8rem] font-bold uppercase tracking-[0.12em] text-green">Företaget</p>
        <h1 className="mt-2 font-display text-[clamp(1.9rem,4vw,2.8rem)] font-semibold">{t("about_title")}</h1>
        <p className="mt-4 text-lg text-muted">
          Cibello är en svensk matapp från {COMPANY.legalName}. Den byggdes för att svara på en fråga som ställs i nästan
          varje hushåll varje dag: vad ska vi äta?
        </p>
        <section className="mt-10 space-y-4">
          <h2 className="font-display text-2xl font-semibold">Varför Cibello finns</h2>
          <p>
            De flesta receptappar utgår från recept. Vi ville göra tvärtom och utgå från köket: vad som faktiskt
            finns i kylen, frysen och skafferiet, vad som snart går ut och vad hushållet brukar gilla. Därför är
            kärnan i Cibello ett matlager, ”din Food Twin”.
          </p>
        </section>
        <section className="mt-8 space-y-4">
          <h2 className="font-display text-2xl font-semibold">Så ser vi på AI</h2>
          <p>
            AI gör Cibello möjligt, men den har fel ibland. Skanningen kan tolka en vara fel, missa något längst
            in eller gissa fel datum. Därför granskar du alltid resultatet innan det sparas, och förslagen är
            just förslag. Recept- och allergenfilter är vägledning, aldrig en garanti.
          </p>
        </section>
        <section className="mt-8 space-y-4">
          <h2 className="font-display text-2xl font-semibold">Dina data</h2>
          <p>
            Allt lagras inom EU. Du kan se dina uppgifter i appen och radera ditt konto när du vill, utan att
            kontakta support. Vi säljer inte personuppgifter.
          </p>
        </section>
        <section className="mt-8 space-y-4">
          <h2 className="font-display text-2xl font-semibold">Företaget</h2>
          <p>
            Cibello utvecklas och ägs av {COMPANY.legalName}, org.nr {COMPANY.orgNr}, med adress {COMPANY_ADDRESS}.
            Momsnummer {COMPANY.vatId}. Appen finns för iOS och Android på tolv språk och är byggd i Sverige. Den är
            tills vidare avsedd för personer som är minst 18 år, eftersom villkoren för den AI-tjänst som används kräver
            vuxna användare. Provperioden är 14 dagar utan kort.
          </p>
        </section>
        <section className="mt-8 space-y-4">
          <h2 className="font-display text-2xl font-semibold">Kontakt</h2>
          <p>
            Allmänna frågor och samarbeten:{" "}
            <a className="font-semibold text-green-d" href={`mailto:${COMPANY.email}`}>
              {COMPANY.email}
            </a>
            . Support:{" "}
            <a className="font-semibold text-green-d" href={`mailto:${COMPANY.supportEmail}`}>
              {COMPANY.supportEmail}
            </a>
            . Integritet och dataskydd:{" "}
            <a className="font-semibold text-green-d" href={`mailto:${COMPANY.privacyEmail}`}>
              {COMPANY.privacyEmail}
            </a>
            . Press är välkommen till samma adress; vi svarar normalt inom ett par arbetsdagar.
          </p>
          <p>
            Telefon till Cibello och {COMPANY.legalName}:{" "}
            <a className="font-semibold text-green-d" href={`tel:${COMPANY.phoneE164}`}>
              {COMPANY.phoneDisplay}
            </a>{" "}
            (Sverige).
          </p>
        </section>
        <div className="mt-10 rounded-[20px] bg-green-l p-6">
          <h2 className="font-display text-xl font-semibold">Prova Cibello</h2>
          <p className="mt-2 text-muted">Fota kylen, få middagstips från det du har hemma och dela inköpslistan.</p>
          <StoreButtons className="mt-4" />
        </div>
      </article>
    </SiteLayout>
  );
}
