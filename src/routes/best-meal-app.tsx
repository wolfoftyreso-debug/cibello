import { createFileRoute } from "@tanstack/react-router";
import { Check, Minus } from "lucide-react";
import { SiteLayout } from "@/components/site/layout";
import { StoreButtons } from "@/components/site/store-buttons";
import { useLocale } from "@/lib/i18n/locale";
import { pageMeta } from "@/lib/cibello/seo";

export const Route = createFileRoute("/best-meal-app")({
  component: ComparePage,
  head: () =>
    pageMeta({
      title: "Bästa matappen? Jämförelse | Cibello",
      description: "Cibello jämfört med receptappar och veckolådor. Skanna kylen och laga det du redan har, utan matkasse.",
      path: "/best-meal-app",
    }),
});

const ROWS: { label: string; values: Array<boolean | string> }[] = [
  { label: "Utgår från vad du har hemma", values: [true, true, false, true] },
  { label: "Foto av kyl / skafferi", values: [true, false, false, false] },
  { label: "Veckomeny", values: [true, false, false, true] },
  { label: "Delad inköpslista", values: [true, false, true, true] },
  { label: "Bäst-före-påminnelser", values: [true, false, false, false] },
  { label: "Data i EU", values: [true, "varierar", "varierar", "varierar"] },
  { label: "Svenska som förstaspråk", values: [true, false, true, false] },
];

function Cell({ v }: { v: boolean | string }) {
  if (v === true) return <Check className="mx-auto size-4 text-green" />;
  if (v === false) return <Minus className="mx-auto size-4 text-line" />;
  return <span className="text-xs text-muted">{v}</span>;
}

function ComparePage() {
  const { t } = useLocale();
  return (
    <SiteLayout>
      <div className="mx-auto w-[min(960px,92vw)] py-12">
        <p className="text-[0.8rem] font-bold uppercase tracking-[0.12em] text-green">Jämförelse</p>
        <h1 className="mt-2 font-display text-[clamp(1.9rem,4vw,2.8rem)] font-semibold">
          {t("cmp_page_h")}
        </h1>
        <p className="mt-4 max-w-[62ch] text-lg text-muted">
          SuperCook utgår från ingredienser du skriver in. Matlistan är stark på delad inköpslista. Mealime planerar
          veckan. Cibello gör de tre sakerna — men börjar med en bild av ditt kök.
        </p>

        <div className="mt-8 overflow-x-auto rounded-[16px] border border-line bg-surface">
          <table className="w-full min-w-[640px] text-left text-sm">
            <thead>
              <tr className="border-b border-line bg-bg2">
                {["", "Cibello", "SuperCook", "Matlistan", "Mealime"].map((h) => (
                  <th key={h} className="px-4 py-3 font-semibold">
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {ROWS.map((row) => (
                <tr key={row.label} className="border-b border-line last:border-0">
                  <th className="px-4 py-3 font-medium">{row.label}</th>
                  {row.values.map((v, i) => (
                    <td key={i} className="px-4 py-3 text-center">
                      <Cell v={v} />
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="mt-4 text-sm text-muted">
          Jämförelsen är en översikt av typiska funktioner, inte en recension. Appar förändras.
        </p>
        <StoreButtons className="mt-6" />
      </div>
    </SiteLayout>
  );
}
