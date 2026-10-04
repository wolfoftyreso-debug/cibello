import type { ReactNode } from "react";
import { cn } from "@/lib/utils";
import { useLocale } from "@/lib/i18n/locale";

const APP_STORE = "https://apps.apple.com/app/id6807100747";
const PLAY =
  "https://play.google.com/store/apps/details?id=com.cibello.app&referrer=utm_source%3Dcibello.app%26utm_medium%3Dweb%26utm_campaign%3Dhome";

function StoreLink({
  href,
  small,
  bold,
  icon,
  className,
}: {
  href: string;
  small: string;
  bold: string;
  icon: ReactNode;
  className?: string;
}) {
  return (
    <a
      href={href}
      rel="noopener"
      className={cn(
        "inline-flex w-full items-center justify-center gap-2.5 rounded-[11px] border border-white/10 bg-dark px-4 py-2.5 text-white shadow-[0_8px_18px_-12px_rgb(0_0_0_/_0.55)] transition-transform duration-150 hover:brightness-110 active:translate-y-px sm:w-auto",
        className,
      )}
    >
      {icon}
      <span className="leading-tight">
        <small className="block text-[0.66rem] uppercase tracking-wide text-white/75">{small}</small>
        <b className="text-[1.02rem] font-semibold">{bold}</b>
      </span>
    </a>
  );
}

export function StoreButtons({ className }: { className?: string }) {
  const { t } = useLocale();
  return (
    <div className={cn("flex flex-col gap-3 sm:flex-row sm:flex-wrap sm:items-center", className)}>
      <StoreLink
        href={APP_STORE}
        small={t("dl_apple")}
        bold="App Store"
        icon={
          <svg viewBox="0 0 24 24" fill="currentColor" className="size-6 shrink-0" aria-hidden>
            <path d="M16.4 12.7c0-2 1.6-3 1.7-3.1-.9-1.4-2.4-1.6-2.9-1.6-1.2-.1-2.4.7-3 .7-.6 0-1.6-.7-2.6-.7-1.3 0-2.6.8-3.3 2-1.4 2.4-.4 6 1 8 .7 1 1.4 2 2.4 2 1 0 1.3-.6 2.5-.6 1.2 0 1.5.6 2.5.6 1 0 1.7-.9 2.3-1.9.7-1.1 1-2.2 1-2.3-.1 0-2-.8-2.1-3.1zM14.6 6.3c.5-.7.9-1.6.8-2.5-.8 0-1.7.5-2.3 1.2-.5.6-.9 1.5-.8 2.4.9.1 1.8-.4 2.3-1.1z" />
          </svg>
        }
      />
      <StoreLink
        href={PLAY}
        small={t("dl_google")}
        bold="Google Play"
        icon={
          <svg viewBox="0 0 24 24" className="size-6 shrink-0" aria-hidden>
            <path d="M4 3.5v17c0 .5.5.8.9.5l9.3-8.5-9.3-8.5c-.4-.3-.9 0-.9.5z" fill="#34d399" />
            <path d="M14.2 12.5l2.7-2.5 3.6 2c.6.4.6 1.2 0 1.6l-3.6 2-2.7-2.5z" fill="#fbbf24" />
            <path d="M4.9 20.5l9.3-8-2.7-2.5-6.6 6c-.4.3-.4.9 0 .5z" fill="#f87171" />
            <path d="M4.9 3.5l9.3 8-2.7 2.5-6.6-6c-.4-.3-.4-.9 0-.5z" fill="#60a5fa" />
          </svg>
        }
      />
    </div>
  );
}
