import type { ReactNode } from "react";
import { StoreButtons } from "./store-buttons";
import { useLocale } from "@/lib/i18n/locale";

const FOUND = [
  { key: "chip_1", img: "/marketing/ing-eggs.jpg?v=2" },
  { key: "chip_2", img: "/marketing/ing-spinach.jpg?v=2" },
  { key: "chip_3", img: "/marketing/ing-lemon.jpg?v=2" },
  { key: "chip_4", img: "/marketing/ing-chicken.jpg?v=2" },
] as const;

export function Premiere() {
  const { t } = useLocale();
  return (
    <div className="bg-[#f3efe7]">
      <section className="lg:grid lg:min-h-dvh lg:grid-cols-[minmax(0,0.82fr)_minmax(0,1.18fr)]">
        <div className="flex flex-col justify-end px-[4vw] pb-8 pt-[calc(var(--header-h)+2.5rem)] lg:pb-16 lg:pt-[var(--header-h)]">
          <p className="text-[0.72rem] font-semibold uppercase tracking-[0.28em] text-green">
            01
            <span className="px-3 text-green/40">/</span>
            {t("step1")}
          </p>
          <h1 className="mt-4 max-w-[9ch] font-display text-[clamp(3.4rem,5.6vw,6.4rem)] font-semibold leading-[0.88] tracking-[-0.045em]">
            {t("plain_h")}
          </h1>
          <p className="mt-6 max-w-[32ch] text-xl leading-relaxed text-muted">{t("plain_lead")}</p>
        </div>
        <img
          src="/marketing/p-hand.jpg?v=2"
          alt={t("step1_d")}
          className="aspect-[16/9] w-full object-cover lg:aspect-auto lg:h-dvh"
        />
      </section>

      <Chapter n="02" title={t("step2")} body={t("step2_d")}>
        <p className="page-wrap mb-5 text-lg text-ink">
          {FOUND.map((item) => t(item.key)).join("  ·  ")}
        </p>
        <img src="/marketing/p-ings.jpg?v=3" alt="" className="aspect-[16/9] w-full object-cover" />
      </Chapter>

      <Chapter n="03" title={t("step3")} body={t("step3_d")}>
        <div className="grid lg:grid-cols-2">
          <figure>
            <figcaption className="mb-4 px-[4vw] font-display text-2xl font-semibold">
              {t("ex_r1")}
            </figcaption>
            <img src="/marketing/p-plate.jpg?v=2" alt="" className="aspect-[3/4] w-full object-cover lg:aspect-[4/5]" />
          </figure>
          <figure className="mt-12 lg:mt-24">
            <figcaption className="mb-4 px-[4vw] font-display text-2xl font-semibold">
              {t("ex_r2")}
            </figcaption>
            <img src="/marketing/meal-omelett.jpg?v=2" alt="" className="aspect-[3/4] w-full object-cover lg:aspect-[4/5]" />
          </figure>
        </div>
      </Chapter>

      <Chapter n="04" title={t("step4")} body={t("step4_d")}>
        <img src="/marketing/p-cook.jpg?v=2" alt="" className="aspect-[16/9] w-full object-cover" />
      </Chapter>

      <Chapter n="05" title={t("step5")} body={t("step5_d")}>
        <img src="/marketing/p-steam.jpg?v=2" alt="" className="aspect-[3/2] w-full object-cover" />
      </Chapter>

      <section className="page-wrap py-28 lg:py-36">
        <p className="max-w-[14ch] font-display text-[clamp(2.8rem,5vw,4.8rem)] font-semibold leading-[0.94]">
          {t("plain_h")}
        </p>
        <p className="mt-5 max-w-[36ch] text-lg text-muted">{t("plain_lead")}</p>
        <StoreButtons className="mt-10" />
      </section>
    </div>
  );
}

function Chapter({
  n,
  title,
  body,
  children,
}: {
  n: string;
  title: string;
  body: string;
  children: ReactNode;
}) {
  return (
    <section className="pb-20 pt-20 lg:pb-28 lg:pt-28">
      <div className="page-wrap mb-5">
        <p className="text-[0.72rem] font-semibold uppercase tracking-[0.28em] text-green">
          {n}
          <span className="px-3 text-green/40">/</span>
          {title}
        </p>
        <h2 className="mt-3 max-w-[18ch] font-display text-[clamp(2rem,3.5vw,3.1rem)] font-semibold leading-tight">
          {body}
        </h2>
      </div>
      {children}
    </section>
  );
}
