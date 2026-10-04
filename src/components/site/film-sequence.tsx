import { useCallback, useEffect, useRef, useState, type CSSProperties } from "react";
import { cn } from "@/lib/utils";

export type FilmShot = {
  src: string;
  poster: string;
};

const FADE_S = 0.7;

export function FilmSequence({
  shots,
  className,
  index: controlled,
  onBeat,
}: {
  shots: readonly FilmShot[];
  className?: string;
  /** When set, the sequence follows this index instead of playing through. */
  index?: number;
  onBeat?: (index: number, epoch: number) => void;
}) {
  const loop = shots.length > 1;
  const buffers = loop ? shots : [shots[0], shots[0]];
  const [auto, setAuto] = useState(0);
  const [reduced, setReduced] = useState(false);
  const [seen, setSeen] = useState(true);
  const root = useRef<HTMLDivElement>(null);
  const refs = useRef<Array<HTMLVideoElement | null>>([]);
  const indexRef = useRef(0);
  const epochRef = useRef(0);
  const started = useRef(-1);
  const active = controlled ?? auto;

  const go = useCallback(
    (next: number) => {
      const wrapped = ((next % buffers.length) + buffers.length) % buffers.length;
      if (wrapped === indexRef.current) return;
      indexRef.current = wrapped;
      epochRef.current += 1;
      setAuto(wrapped);
      onBeat?.(loop ? wrapped : 0, epochRef.current);
    },
    [buffers.length, loop, onBeat],
  );

  useEffect(() => {
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    const apply = () => setReduced(mq.matches);
    apply();
    mq.addEventListener("change", apply);
    return () => mq.removeEventListener("change", apply);
  }, []);

  useEffect(() => {
    const el = root.current;
    if (!el) return;
    const io = new IntersectionObserver(
      ([entry]) => setSeen(entry.isIntersecting),
      { threshold: 0.2 },
    );
    io.observe(el);
    return () => io.disconnect();
  }, []);

  useEffect(() => {
    if (controlled === undefined) return;
    const next = ((controlled % buffers.length) + buffers.length) % buffers.length;
    indexRef.current = next;
  }, [controlled, buffers.length]);

  useEffect(() => {
    if (reduced) return;
    const current = refs.current[active];
    if (current) {
      if (started.current !== active) {
        if (current.currentTime > 0.25) current.currentTime = 0;
        started.current = active;
      }
      if (seen && !document.hidden) void current.play().catch(() => {});
      else current.pause();
    }
    const fade = window.setTimeout(() => {
      refs.current.forEach((video, i) => {
        if (video && i !== indexRef.current) video.pause();
      });
    }, FADE_S * 1000);
    return () => window.clearTimeout(fade);
  }, [active, seen, reduced]);

  useEffect(() => {
    if (reduced) return;
    const onHide = () => {
      refs.current.forEach((video) => video?.pause());
      if (!document.hidden && seen) {
        const current = refs.current[indexRef.current];
        void current?.play().catch(() => {});
      }
    };
    document.addEventListener("visibilitychange", onHide);
    return () => document.removeEventListener("visibilitychange", onHide);
  }, [reduced, seen]);

  const onTime = (slot: number) => {
    if (controlled !== undefined || reduced) return;
    if (slot !== indexRef.current) return;
    const video = refs.current[slot];
    if (!video || !Number.isFinite(video.duration) || video.duration < 1) return;
    if (video.currentTime >= video.duration - FADE_S) go(slot + 1);
  };

  const poster = shots[Math.min(active, shots.length - 1)]?.poster ?? shots[0].poster;

  return (
    <div ref={root} className={cn("pointer-events-none absolute inset-0", className)} aria-hidden>
      {reduced ? (
        <img src={poster} alt="" className="size-full object-cover" />
      ) : (
        buffers.map((shot, i) => (
          <div key={`${shot.src}-${i}`} className={cn("film-shot", i === active && "is-on")}>
            <video
              ref={(node) => {
                refs.current[i] = node;
              }}
              className="size-full object-cover"
              muted
              playsInline
              autoPlay={i === 0}
              loop={controlled !== undefined}
              preload="auto"
              poster={shot.poster}
              onTimeUpdate={() => onTime(i)}
            >
              <source src={shot.src} type="video/mp4" />
            </video>
          </div>
        ))
      )}
    </div>
  );
}

export function FilmRail({
  index,
  count,
  seconds = 15,
  epoch = 0,
  timed = true,
  className,
}: {
  index: number;
  count: number;
  seconds?: number;
  epoch?: number;
  timed?: boolean;
  className?: string;
}) {
  return (
    <div className={cn("flex w-36 gap-1.5", className)} aria-hidden>
      {Array.from({ length: count }, (_, i) => (
        <span
          key={i === index ? `on-${epoch}` : `off-${i}`}
          className={cn(
            "film-beat",
            i < index && "is-done",
            i === index && "is-on",
            !timed && "is-step",
          )}
          style={{ "--shot": `${seconds}s` } as CSSProperties}
        />
      ))}
    </div>
  );
}

export function FilmCaption({ text }: { text: string }) {
  return (
    <p key={text} className="film-caption text-sm font-bold uppercase tracking-[0.2em] text-mint">
      {text}
    </p>
  );
}
