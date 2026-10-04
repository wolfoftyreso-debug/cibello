import { createFileRoute } from "@tanstack/react-router";
import { Flow } from "@/components/site/flow";
import { SiteLayout } from "@/components/site/layout";
import { organizationJsonLd } from "@/lib/cibello/company";
import { pageMeta } from "@/lib/cibello/seo";
import { useLocale } from "@/lib/i18n/locale";
import messages from "@/lib/i18n/messages.json";

const HOME_TITLE = "Cibello – recept från det du har hemma";
const HOME_DESCRIPTION =
  "Fota kylen. Cibello känner igen varorna, föreslår middag och tar bort frågan vad ska vi äta. 14 dagar utan kort. Data i EU.";

export const Route = createFileRoute("/")({
  component: Home,
  head: () => {
    const seo = pageMeta({ title: HOME_TITLE, description: HOME_DESCRIPTION, path: "/" });
    return {
      meta: [...seo.meta, { name: "p:domain_verify", content: "255b1ca1d9a9fd708796d25e3fa18336" }],
      links: seo.links,
    };
  },
});

function Home() {
  const { t } = useLocale();
  const sv = messages.sv;
  const orgLd = {
    "@context": "https://schema.org",
    "@graph": [
      organizationJsonLd(),
      {
        "@type": "WebSite",
        "@id": "https://cibello.app/#website",
        url: "https://cibello.app/",
        name: "Cibello",
        inLanguage: "sv",
        publisher: { "@id": "https://cibello.app/#organization" },
      },
      {
        "@type": "SoftwareApplication",
        name: "Cibello",
        applicationCategory: "LifestyleApplication",
        operatingSystem: "iOS, Android",
        url: "https://cibello.app/",
        inLanguage: ["sv", "en", "de", "fr", "es", "it", "nl", "pl", "da", "nb", "fi", "pt"],
        offers: { "@type": "Offer", price: "0", priceCurrency: "SEK" },
        publisher: { "@id": "https://cibello.app/#organization" },
      },
      {
        "@type": "FAQPage",
        mainEntity: (
          [
            [sv.faq_q1, sv.faq_a1],
            [sv.faq_q2, sv.faq_a2],
            [sv.faq_q3, sv.faq_a3],
            [sv.faq_q4, sv.faq_a4],
            [sv.faq_q5, sv.faq_a5],
            [sv.faq_q6, sv.faq_a6],
          ] as const
        ).map(([name, text]) => ({
          "@type": "Question",
          name,
          acceptedAnswer: { "@type": "Answer", text },
        })),
      },
    ],
  };
  const faq = [1, 2, 3, 4, 5, 6].map((n) => ({
    q: t(`faq_q${n}`),
    a: t(`faq_a${n}`),
  }));

  return (
    <SiteLayout>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(orgLd) }} />
      <Flow />

      <section id="faq" className="section-y border-t border-line bg-surface">
        <div className="page-wrap">
          <h2 className="text-section">{t("faq_h")}</h2>
        </div>
        <div className="page-wrap mt-8 max-w-3xl">
          {faq.map((item) => (
            <details key={item.q} className="group border-t border-line">
              <summary className="cursor-pointer list-none py-5 font-display text-xl font-semibold marker:content-none [&::-webkit-details-marker]:hidden">
                {item.q}
              </summary>
              <p className="pb-5 text-muted">{item.a}</p>
            </details>
          ))}
          <div className="border-t border-line" />
        </div>
      </section>
    </SiteLayout>
  );
}
