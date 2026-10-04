import { Link, useRouterState } from "@tanstack/react-router";
import { UserButton } from "@/lib/auth/gates";
import { useCurrentUserState } from "@/lib/auth/use-current-user";
import { useLocale } from "@/lib/i18n/locale";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";

export function AuthSlot({ inverted }: { inverted?: boolean }) {
  const { t } = useLocale();
  const { user, isPending } = useCurrentUserState();
  const pathname = useRouterState({ select: (s) => s.location.pathname });

  if (isPending) {
    return <div className="size-11 shrink-0 animate-pulse rounded-full bg-line/80" aria-hidden />;
  }

  if (!user) {
    if (pathname === "/login") return null;
    return (
      <Button
        asChild
        variant="outline"
        className={cn(
          "rounded-full",
          inverted && "border-surface/40 bg-transparent text-surface hover:border-mint hover:text-mint",
        )}
      >
        <Link to="/login">{t("nav_login")}</Link>
      </Button>
    );
  }

  return (
    <div
      className={cn(
        "flex items-center gap-2",
        inverted && "rounded-full bg-surface/95 px-2 py-1 text-ink",
      )}
    >
      <Link
        to="/account"
        className="hidden text-sm font-semibold hover:text-green-d sm:inline"
      >
        {t("nav_account")}
      </Link>
      <UserButton />
    </div>
  );
}
