import { useEffect, useRef, useState } from "react";
import { StoreButtons } from "./store-buttons";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";

const CLIPS = [
  { src: "/marketing/flow-photo.mp4?v=4", poster: "/marketing/flow-photo.jpg", step: "step1", body: "step1_d" },
  { src: "/marketing/flow-ings.mp4", poster: "/marketing/flow-ings.jpg", step: "step2", body: "step2_d" },
  { src: "/marketing/flow-plate.mp4", poster: "/marketing/flow-plate.jpg", step: "step3", body: "step3_d" },
  { src: "/marketing/flow-cook.mp4", poster: "/marketing/flow-cook.jpg", step: "step4", body: "step4_d" },
  { src: "/marketing/flow-steam.mp4", poster: "/marketing/flow-steam.jpg", step: "step5", body: "step5_d" },
] as const;

function arm(node: HTMLVideoElement | null) {
  if (!node) return;
  node.muted = true;
  node.defaultMuted = true;
  node.playsInline = true;
  node.setAttribute("muted", "");
  node.setAttribute("playsinline", "");
  node.setAttribute("webkit-playsinline", "true");
  const pending = node.play();
  if (pending) pending.catch(() => {});
}

export function Flow() {
  const { t } = useLocale();
  const [index, setIndex] = useState(0);
  const bar = useRef<HTMLSpanElement>(null);
  const video = useRef<HTMLVideoElement>(null);
  const clip = CLIPS[index];

  useEffect(() => {
    const next = CLIPS[(index + 1) % CLIPS.length].src;
    const warm = document.createElement("video");
    warm.preload = "auto";
    warm.muted = true;
    warm.src = next;
    return () => {
      warm.src = "";
    };
  }, [index]);

  return (
    <section id="how" data-header="invert" className="relative h-dvh bg-black">
      <h1 className="sr-only">{t("plain_h")}</h1>
      {CLIPS.map((item, i) => (
        <img
          key={item.poster}
          src={item.poster}
          alt=""
          className={cn(
            "absolute inset-0 size-full object-cover transition-opacity duration-500",
            i === index ? "opacity-100" : "opacity-0",
          )}
        />
      ))}
      <video
        key={clip.src}
        ref={(node) => {
          video.current = node;
          arm(node);
        }}
        src={clip.src}
        poster={clip.poster}
        muted
        playsInline
        preload="auto"
        disablePictureInPicture
        onPlaying={(event) => {
          event.currentTarget.style.opacity = "1";
        }}
        onTimeUpdate={(event) => {
          const node = event.currentTarget;
          if (bar.current && node.duration) bar.current.style.transform = `scaleX(${node.currentTime / node.duration})`;
        }}
        onEnded={() => setIndex((current) => (current + 1) % CLIPS.length)}
        className="absolute inset-0 size-full object-cover opacity-0 transition-opacity duration-500"
      />
      <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/80 via-black/15 to-black/25" />

      <div className="absolute inset-x-0 bottom-0 z-10 px-5 pb-[max(1.25rem,env(safe-area-inset-bottom))] sm:px-10 lg:px-14">
        <div key={clip.step} className="how-fade">
          <p className="text-[0.72rem] font-semibold tracking-[0.28em] text-white/70">
            0{index + 1}
            <span className="px-3 text-white/35">/</span>
            05
          </p>
          <p className="mt-2 max-w-[12ch] font-display text-[clamp(2.7rem,6vw,4.6rem)] font-semibold leading-[0.92] tracking-tight text-white">
            {t(clip.step)}
          </p>
          <p className="mt-3 max-w-[36ch] text-base text-white/80 sm:text-lg">{t(clip.body)}</p>
        </div>

        <div className="mt-5 flex max-w-md gap-1.5">
          {CLIPS.map((item, i) => (
            <button
              key={item.src}
              type="button"
              onClick={() => setIndex(i)}
              className="h-8 flex-1"
              aria-label={t(item.step)}
              aria-current={i === index}
            >
              <span className="block h-px bg-white/30">
                <span
                  ref={i === index ? bar : undefined}
                  className="block h-px origin-left bg-white"
                  style={{ transform: i < index ? "scaleX(1)" : "scaleX(0)" }}
                />
              </span>
            </button>
          ))}
        </div>

        <StoreButtons className="pointer-events-auto mt-4" />
      </div>
      <button
        type="button"
        className="absolute inset-0 z-0"
        aria-label={t(clip.step)}
        onClick={() => arm(video.current)}
      />
    </section>
  );
}
