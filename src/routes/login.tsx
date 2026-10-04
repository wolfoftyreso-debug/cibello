import { createFileRoute, Link, Navigate } from "@tanstack/react-router";
import { useState } from "react";
import { GROK_PROVIDERS, authClient, authEnabled, signIn } from "@/lib/auth/client";
import { useCurrentUserState } from "@/lib/auth/use-current-user";
import { SiteLayout } from "@/components/site/layout";
import { Button } from "@/components/ui/button";
import { Logo } from "@/components/site/logo";
import { useLocale } from "@/lib/i18n/locale";
import { pageMeta } from "@/lib/cibello/seo";
import { cn } from "@/lib/utils";

export const Route = createFileRoute("/login")({
  component: LoginPage,
  head: () =>
    pageMeta({
      title: "Logga in | Cibello",
      description: "Logga in i Cibello för att spara kök, veckomeny och inköpslista.",
      path: "/login",
      noindex: true,
    }),
});

function LoginPage() {
  const { t } = useLocale();
  const { user, isPending } = useCurrentUserState();
  const [mode, setMode] = useState<"in" | "up">("in");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  if (isPending) {
    return (
      <SiteLayout>
        <div className="flex min-h-[70vh] items-center justify-center text-muted">{t("opening")}</div>
      </SiteLayout>
    );
  }
  if (user) return <Navigate to="/" />;

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!authEnabled) return;
    setBusy(true);
    setError(null);
    try {
      if (mode === "up") {
        const { error: err } = await authClient.signUp.email({
          email: email.trim(),
          password,
          name: name.trim() || email.split("@")[0] || "Cibello",
          callbackURL: "/",
        });
        if (err) throw new Error(err.message ?? t("login_error"));
      } else {
        const { error: err } = await authClient.signIn.email({
          email: email.trim(),
          password,
          callbackURL: "/",
        });
        if (err) throw new Error(err.message ?? t("login_error"));
      }
      window.location.href = "/";
    } catch (err) {
      setError(err instanceof Error ? err.message : t("login_error"));
      setBusy(false);
    }
  }

  return (
    <SiteLayout>
      <div className="page-wrap grid min-h-[calc(100dvh-5rem)] items-center gap-10 py-10 lg:grid-cols-2 lg:gap-16">
        <div className="mx-auto w-full max-w-md">
          <p className="text-sm font-bold uppercase tracking-[0.14em] text-green-d">{t("login_kicker")}</p>
          <h1 className="mt-3 font-display text-4xl font-semibold">
            {mode === "in" ? t("login_h") : t("login_signup_h")}
          </h1>
          <p className="mt-3 text-muted">{t("login_lead")}</p>

          <form className="mt-8 space-y-3" onSubmit={onSubmit}>
            {mode === "up" ? (
              <label className="block">
                <span className="mb-1.5 block text-sm font-semibold">{t("login_name")}</span>
                <input
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  autoComplete="name"
                  className="h-12 w-full rounded-md border border-line bg-surface px-4 outline-none focus:border-green"
                />
              </label>
            ) : null}
            <label className="block">
              <span className="mb-1.5 block text-sm font-semibold">{t("login_email")}</span>
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                autoComplete="email"
                className="h-12 w-full rounded-md border border-line bg-surface px-4 outline-none focus:border-green"
              />
            </label>
            <label className="block">
              <span className="mb-1.5 block text-sm font-semibold">{t("login_password")}</span>
              <input
                type="password"
                required
                minLength={8}
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                autoComplete={mode === "up" ? "new-password" : "current-password"}
                className="h-12 w-full rounded-md border border-line bg-surface px-4 outline-none focus:border-green"
              />
            </label>
            {error ? <p className="text-sm text-danger">{error}</p> : null}
            <Button type="submit" disabled={busy || !authEnabled} className="h-12 w-full rounded-full">
              {busy ? t("login_busy") : mode === "in" ? t("login_submit") : t("login_create")}
            </Button>
          </form>

          <div className="my-6 flex items-center gap-3 text-sm text-muted">
            <span className="h-px flex-1 bg-line" />
            {t("login_or")}
            <span className="h-px flex-1 bg-line" />
          </div>

          {authEnabled ? (
            <div className="space-y-2">
              {GROK_PROVIDERS.map((p) => (
                <button
                  key={p.providerId}
                  type="button"
                  onClick={() => signIn(p.providerId, { callbackURL: "/" })}
                  className={cn(
                    "flex h-12 w-full items-center justify-center gap-3 rounded-full border border-line bg-surface font-semibold hover:border-green",
                  )}
                >
                  {p.providerId === "grok-google" ? <GoogleMark /> : <XMark />}
                  {p.providerId === "grok-google" ? t("login_google") : t("login_x")}
                </button>
              ))}
            </div>
          ) : (
            <p className="text-sm text-muted">{t("login_disabled")}</p>
          )}

          <p className="mt-6 text-sm text-muted">
            {mode === "in" ? t("login_no_account") : t("login_have_account")}{" "}
            <button
              type="button"
              className="font-semibold text-green-d underline-offset-4 hover:underline"
              onClick={() => {
                setMode(mode === "in" ? "up" : "in");
                setError(null);
              }}
            >
              {mode === "in" ? t("login_signup") : t("login_signin")}
            </button>
          </p>
        </div>

        <div className="hidden rounded-2xl bg-bg2 p-8 lg:flex lg:flex-col lg:justify-end">
          <Logo />
          <p className="mt-3 font-display text-2xl font-semibold leading-snug">{t("login_aside_h")}</p>
          <p className="mt-2 text-sm text-muted">{t("login_aside_p")}</p>
          <Link to="/" className="mt-4 inline-flex text-sm font-semibold text-green-d">
            {t("login_guest")}
          </Link>
        </div>
      </div>
    </SiteLayout>
  );
}

function GoogleMark() {
  return (
    <svg width="18" height="18" viewBox="0 0 48 48" aria-hidden>
      <path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.3 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.1 8 3l5.7-5.7C34.2 6.1 29.4 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.2-.1-2.3-.4-3.5z" />
      <path fill="#FF3D00" d="M6.3 14.7l6.6 4.8C14.7 16 19 12 24 12c3.1 0 5.8 1.1 8 3l5.7-5.7C34.2 6.1 29.4 4 24 4 16.3 4 9.6 8.3 6.3 14.7z" />
      <path fill="#4CAF50" d="M24 44c5.2 0 10-2 13.6-5.2l-6.3-5.3C29.2 35.1 26.7 36 24 36c-5.3 0-9.7-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z" />
      <path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-1.1 3.2-3.5 5.7-6.7 7.1l6.3 5.3C38.2 37.3 44 31.5 44 24c0-1.2-.1-2.3-.4-3.5z" />
    </svg>
  );
}

function XMark() {
  return (
    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden>
      <path d="M18.2 2H21l-6.6 7.5L22 22h-6.8l-5.3-7-6 7H2.1l7-8L2 2h7l4.8 6.4L18.2 2zm-1.2 18h1.9L7.1 3.9H5.1L17 20z" />
    </svg>
  );
}
