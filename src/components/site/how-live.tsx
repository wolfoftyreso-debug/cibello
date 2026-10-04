import { useEffect, useState } from "react";
import { StoreButtons } from "./store-buttons";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";

const FOUND = [
  { key: "chip_1", img: "/marketing/ing-eggs.jpg?v=hf" },
  { key: "chip_2", img: "/marketing/ing-spinach.jpg?v=hf" },
  { key: "chip_3", img: "/marketing/ing-lemon.jpg?v=hf" },
  { key: "chip_4", img: "/marketing/ing-chicken.jpg?v=hf" },
] as const;

const RECIPES = [
  { key: "ex_r1", img: "/marketing/meal-gryta.jpg?v=hf", time: "25" },
  { key: "ex_r2", img: "/marketing/meal-omelett.jpg?v=hf", time: "10" },
] as const;

const BEAT = 5200;

export function HowLive() {
  const { t } = useLocale();
  const [step, setStep] = useState(0);
  const [reduced, setReduced] = useState(false);

  const steps = [
    { title: t("step1"), body: t("step1_d") },
    { title: t("step2"), body: t("step2_d") },
    { title: t("step3"), body: t("step3_d") },
  ];

  useEffect(() => {
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    const apply = () => setReduced(mq.matches);
    apply();
    mq.addEventListener("change", apply);
    return () => mq.removeEventListener("change", apply);
  }, []);

  useEffect(() => {
    if (reduced) return;
    const id = window.setInterval(() => setStep((s) => (s + 1) % 3), BEAT);
    return () => window.clearInterval(id);
  }, [reduced, step]);

  return (
    <section
      id="how"
      className="page-wrap grid items-center gap-8 pb-16 pt-[calc(var(--header-h)+1.25rem)] lg:grid-cols-[minmax(0,0.86fr)_minmax(0,1.14fr)] lg:items-center lg:gap-x-14 lg:gap-y-8 lg:pt-[calc(var(--header-h)+2.25rem)]"
    >
      <div className="lg:col-start-1 lg:row-start-1">
        <h1 className="max-w-[12ch] font-display text-[clamp(2.7rem,6.4vw,4.8rem)] font-semibold leading-[0.96]">
          {t("plain_h")}
        </h1>
        <p className="mt-4 max-w-[34ch] text-lg text-muted">{t("plain_lead")}</p>
        <div className="mt-8 flex flex-col gap-1" role="tablist" aria-label={t("nav_how")}>
          {steps.map((item, i) => {
            const on = step === i;
            return (
              <button
                key={item.title}
                type="button"
                role="tab"
                aria-selected={on}
                onClick={() => setStep(i)}
                className={cn(
                  "rounded-2xl px-3 py-3 text-left transition-colors",
                  on ? "bg-surface" : "hover:bg-surface/70",
                )}
              >
                <span className="flex items-baseline gap-3">
                  <span className={cn("w-5 text-sm font-semibold tabular-nums", on ? "text-green" : "text-muted")}>
                    {i + 1}
                  </span>
                  <span>
                    <span className="block font-display text-2xl font-semibold leading-tight">{item.title}</span>
                    <span className="mt-0.5 block text-muted">{item.body}</span>
                  </span>
                </span>
                {on && !reduced ? (
                  <span className="mt-3 block h-px overflow-hidden bg-line">
                    <span key={step} className="how-progress block h-px bg-green" />
                  </span>
                ) : null}
              </button>
            );
          })}
        </div>
      </div>

      <div className="relative aspect-[4/3] overflow-hidden rounded-[28px] bg-surface shadow-[var(--shadow-soft)] lg:col-start-2 lg:row-span-2 lg:row-start-1">
        {step === 0 ? (
          <div key="photo" className="how-fade absolute inset-0">
            <img src="/marketing/fridge.jpg?v=hf" alt={t("step1_d")} className="size-full object-cover" />
            {reduced ? null : <div className="scan-sweep" aria-hidden />}
          </div>
        ) : null}
        {step === 1 ? (
          <ul key="list" className="how-fade absolute inset-0 flex flex-col justify-center px-5 sm:px-8">
            {FOUND.map((item, i) => (
              <li
                key={item.key}
                className="how-row flex items-center gap-3 border-b border-line py-3 last:border-b-0"
                style={{ animationDelay: `${i * 140}ms` }}
              >
                <img src={item.img} alt="" className="size-12 shrink-0 rounded-lg object-cover" />
                <span className="text-lg font-semibold">{t(item.key)}</span>
              </li>
            ))}
          </ul>
        ) : null}
        {step === 2 ? (
          <ul key="recipes" className="how-fade absolute inset-0 flex flex-col justify-center px-5 sm:px-8">
            {RECIPES.map((item, i) => (
              <li
                key={item.key}
                className="how-row flex items-center gap-3 border-b border-line py-3.5 last:border-b-0"
                style={{ animationDelay: `${i * 180}ms` }}
              >
                <img src={item.img} alt="" className="size-14 shrink-0 rounded-lg object-cover" />
                <span>
                  <span className="block font-display text-xl font-semibold">{t(item.key)}</span>
                  <span className="text-sm text-muted">
                    {item.time} {t("min")}
                  </span>
                </span>
              </li>
            ))}
          </ul>
        ) : null}
      </div>
      <StoreButtons className="lg:col-start-1 lg:row-start-2" />
    </section>
  );
}
