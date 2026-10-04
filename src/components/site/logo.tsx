import { Link } from "@tanstack/react-router";
import { cn } from "@/lib/utils";

export function Mark({ className }: { className?: string }) {
  return (
    <span
      className={cn(
        "grid size-8 shrink-0 place-items-center rounded-[9px] bg-green text-white shadow-[inset_0_1px_0_rgb(255_255_255_/_0.28)]",
        className,
      )}
      aria-hidden
    >
      <svg width="18" height="18" viewBox="0 0 32 32">
        <path
          d="M16 6c4.4 0 8 3.4 8 8 0 5.6-8 12-8 12S8 19.6 8 14c0-4.6 3.6-8 8-8z"
          fill="currentColor"
        />
        <circle cx="16" cy="14" r="2.6" fill="#2f7d51" />
      </svg>
    </span>
  );
}

export function Logo({ className, to = "/" }: { className?: string; to?: string }) {
  return (
    <Link
      to={to}
      className={cn("flex items-center gap-2.5 font-display text-[1.28rem] font-semibold tracking-tight text-ink", className)}
    >
      <Mark />
      Cibello
    </Link>
  );
}
