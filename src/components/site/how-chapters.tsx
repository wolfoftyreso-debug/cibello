import { useEffect, useRef, useState } from "react";
import { FILM, FILM_SECONDS } from "@/lib/cibello/film";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";
import { FilmRail, FilmSequence } from "./film-sequence";

export function HowChapters() {
  const { t } = useLocale();
  const [scrollBeat, setScrollBeat] = useState(0);
  const [playBeat, setPlayBeat] = useState(0);
  const [epoch, setEpoch] = useState(0);
  const [desktop, setDesktop] = useState(false);
  const refs = useRef<Array<HTMLElement | null>>([]);

  const steps = [
    { n: "01", title: t("s1_h"), text: t("s1_p") },
    { n: "02", title: t("s2_h"), text: t("s2_p") },
    { n: "03", title: t("s3_h"), text: t("s3_p") },
  ];
  const shown = desktop ? scrollBeat : playBeat;

  useEffect(() => {
    const mq = window.matchMedia("(min-width: 1024px)");
    const apply = () => setDesktop(mq.matches);
    apply();
    mq.addEventListener("change", apply);
    return () => mq.removeEventListener("change", apply);
  }, []);

  useEffect(() => {
    if (!desktop) return;
    const nodes = refs.current.filter(Boolean) as HTMLElement[];
    const io = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
        if (!visible) return;
        const i = nodes.indexOf(visible.target as HTMLElement);
        if (i >= 0) setScrollBeat(i);
      },
      { threshold: [0.45, 0.65], rootMargin: "-18% 0px -28% 0px" },
    );
    nodes.forEach((node) => io.observe(node));
    return () => io.disconnect();
  }, [desktop]);

  return (
    <div className="page-wrap mt-12 grid gap-8 lg:grid-cols-2 lg:gap-16">
      <div className="lg:sticky lg:top-28 lg:self-start">
        <div className="relative aspect-wide overflow-hidden rounded-2xl bg-green-x lg:aspect-photo">
          <FilmSequence
            shots={FILM}
            index={desktop ? scrollBeat : undefined}
            onBeat={(i, nextEpoch) => {
              setPlayBeat(i);
              setEpoch(nextEpoch);
            }}
          />
        </div>
        <FilmRail className="mt-4" index={shown} count={steps.length} seconds={FILM_SECONDS} epoch={epoch} timed={!desktop} />
      </div>
      <div>
        {steps.map((step, i) => (
          <article
            key={step.n}
            ref={(node) => {
              refs.current[i] = node;
            }}
            className="flex flex-col justify-center border-t border-line py-8 first:border-t-0 lg:min-h-beat lg:border-t-0 lg:py-0"
          >
            <p
              className={cn(
                "font-display text-sm font-semibold tracking-[0.2em] transition-colors duration-300",
                i === shown ? "text-green" : "text-muted",
              )}
            >
              {step.n}
            </p>
            <h3 className="mt-3 font-display text-3xl font-semibold leading-snug">{step.title}</h3>
            <p className="mt-3 max-w-[36ch] text-lg text-muted">{step.text}</p>
          </article>
        ))}
      </div>
    </div>
  );
}
