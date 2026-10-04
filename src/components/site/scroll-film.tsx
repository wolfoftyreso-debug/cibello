import { useEffect, useRef, useState } from "react";
import { StoreButtons } from "./store-buttons";
import { useLocale } from "@/lib/i18n/locale";

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

function band(p: number, a: number, b: number, c: number, d: number) {
  if (p <= a || p >= d) return 0;
  if (p < b) return (p - a) / (b - a);
  if (p > c) return 1 - (p - c) / (d - c);
  return 1;
}

export function ScrollFilm() {
  const { t } = useLocale();
  const track = useRef<HTMLDivElement>(null);
  const [p, setP] = useState(0);
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
    let frame = 0;
    const measure = () => {
      const el = track.current;
      if (!el) return;
      const total = el.offsetHeight - window.innerHeight;
      const passed = Math.min(Math.max(-el.getBoundingClientRect().top, 0), Math.max(total, 1));
      setP(total <= 0 ? 0 : passed / total);
    };
    const onScroll = () => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(measure);
    };
    measure();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    return () => {
      mq.removeEventListener("change", apply);
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
      cancelAnimationFrame(frame);
    };
  }, []);

  const beat = p < 0.34 ? 0 : p < 0.67 ? 1 : 2;
  const fridge = band(p, -0.01, 0, 0.26, 0.42);
  const list = band(p, 0.28, 0.42, 0.56, 0.72);
  const recipes = band(p, 0.6, 0.76, 1.2, 1.3);

  return (
    <section id="how" className="bg-green-x text-surface">
      <h1 className="sr-only">{t("plain_h")}</h1>
      <div ref={track} className={reduced ? undefined : "h-[320vh]"}>
        <div className={reduced ? "flex flex-col gap-16 px-[4vw] py-28" : "sticky top-0 h-dvh"}>
          {reduced ? (
            <StaticBeats />
          ) : (
            <div className="flex h-full flex-col px-[4vw] pb-8 pt-[calc(var(--header-h)+0.5rem)] lg:flex-row lg:items-center lg:gap-14">
              <div className="lg:w-[38%]">
                <p className="text-sm font-semibold tracking-[0.22em] text-mint">
                  {beat + 1} / 3
                </p>
                <div className="relative mt-3 min-h-[4.6rem] lg:min-h-[8.5rem]">
                  {steps.map((step, i) => (
                    <p
                      key={step.title}
                      aria-hidden={i !== beat}
                      className="font-display text-[clamp(2.6rem,3.5vw,4.5rem)] font-semibold leading-[0.92] tracking-tight transition-opacity duration-500"
                      style={{ opacity: i === beat ? 1 : 0, position: i === beat ? "relative" : "absolute", inset: i === beat ? undefined : 0 }}
                    >
                      {step.title}
                    </p>
                  ))}
                </div>
                <p className="mt-4 max-w-[28ch] text-lg text-white/70">{steps[beat].body}</p>
                <div className="mt-8 flex gap-2" aria-hidden>
                  {[0, 1, 2].map((i) => (
                    <span key={i} className="h-px w-10 overflow-hidden bg-white/20">
                      <span
                        className="block h-px bg-mint"
                        style={{ width: beat > i ? "100%" : beat === i ? "60%" : "0%" }}
                      />
                    </span>
                  ))}
                </div>
              </div>

              <div className="relative mt-6 min-h-0 flex-1 overflow-hidden rounded-[28px] bg-surface lg:mt-0 lg:h-[min(78vh,820px)]">
                <img
                  src="/marketing/fridge.jpg?v=hf"
                  alt=""
                  className="absolute inset-0 size-full object-cover"
                  style={{ opacity: fridge, transform: `scale(${1.06 - fridge * 0.04})` }}
                />
                {fridge > 0.45 ? <div className="scan-sweep" aria-hidden /> : null}
                <ul
                  className="absolute inset-0 flex flex-col justify-center bg-surface px-6 sm:px-10"
                  style={{ opacity: list }}
                >
                  {FOUND.map((item, i) => {
                    const local = Math.min(1, Math.max(0, (p - 0.32) / 0.2));
                    const shown = Math.min(1, Math.max(0, local * FOUND.length - i));
                    return (
                      <li
                        key={item.key}
                        className="flex items-center gap-4 border-b border-line py-3 text-ink last:border-b-0"
                        style={{ opacity: shown, transform: `translateY(${(1 - shown) * 18}px)` }}
                      >
                        <img src={item.img} alt="" className="size-14 shrink-0 rounded-xl object-cover" />
                        <span className="font-display text-2xl font-semibold">{t(item.key)}</span>
                      </li>
                    );
                  })}
                </ul>
                <ul
                  className="absolute inset-0 flex flex-col justify-center bg-surface px-6 sm:px-10"
                  style={{ opacity: recipes }}
                >
                  {RECIPES.map((item, i) => {
                    const local = Math.min(1, Math.max(0, (p - 0.64) / 0.18));
                    const shown = Math.min(1, Math.max(0, local * RECIPES.length - i));
                    return (
                      <li
                        key={item.key}
                        className="flex items-center gap-4 border-b border-line py-4 text-ink last:border-b-0"
                        style={{ opacity: shown, transform: `translateY(${(1 - shown) * 18}px)` }}
                      >
                        <img src={item.img} alt="" className="size-16 shrink-0 rounded-xl object-cover" />
                        <span>
                          <span className="block font-display text-3xl font-semibold">{t(item.key)}</span>
                          <span className="text-muted">
                            {item.time} {t("min")}
                          </span>
                        </span>
                      </li>
                    );
                  })}
                </ul>
              </div>
            </div>
          )}
        </div>
      </div>

      <div className="page-wrap pb-24">
        <p className="max-w-[16ch] font-display text-[clamp(2.4rem,5vw,4.2rem)] font-semibold leading-[0.96]">
          {t("plain_h")}
        </p>
        <p className="mt-4 max-w-[36ch] text-lg text-white/70">{t("plain_lead")}</p>
        <StoreButtons className="mt-8" />
      </div>
    </section>
  );
}

function StaticBeats() {
  const { t } = useLocale();
  const frames = [
    { title: t("step1"), body: t("step1_d"), img: "/marketing/fridge.jpg?v=hf", alt: t("step1_d") },
    { title: t("step2"), body: t("step2_d"), img: "/marketing/ing-spinach.jpg?v=hf", alt: "" },
    { title: t("step3"), body: t("step3_d"), img: "/marketing/meal-gryta.jpg?v=hf", alt: "" },
  ];
  return (
    <>
      {frames.map((frame) => (
        <article key={frame.title} className="grid items-center gap-6 lg:grid-cols-2">
          <div>
            <h2 className="font-display text-5xl font-semibold">{frame.title}</h2>
            <p className="mt-3 text-lg text-white/70">{frame.body}</p>
          </div>
          <img src={frame.img} alt={frame.alt} className="aspect-[4/3] w-full rounded-[28px] object-cover" />
        </article>
      ))}
    </>
  );
}
