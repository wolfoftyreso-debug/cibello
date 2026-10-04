import { Link } from "@tanstack/react-router";
import { Logo } from "./logo";
import { StoreButtons } from "./store-buttons";
import { LangSelect } from "./lang-select";
import { COMPANY, COMPANY_LINE } from "@/lib/cibello/company";
import { LANGS } from "@/lib/i18n/langs";
import { useLocale } from "@/lib/i18n/locale";

const SOCIAL = [
  {
    href: "https://www.facebook.com/profile.php?id=61593336222919",
    label: "Facebook",
    icon: (
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" className="text-white" aria-hidden>
        <path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5 3.66 9.15 8.44 9.94v-7.03H7.9v-2.9h2.54V9.85c0-2.51 1.49-3.9 3.78-3.9 1.09 0 2.24.2 2.24.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 2.9h-2.34V22c4.78-.79 8.44-4.94 8.44-9.94z" />
      </svg>
    ),
  },
  {
    href: "https://www.instagram.com/cibelloapp/",
    label: "Instagram",
    icon: (
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="text-white" aria-hidden>
        <rect x="3" y="3" width="18" height="18" rx="5" />
        <circle cx="12" cy="12" r="4" />
        <circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none" />
      </svg>
    ),
  },
  {
    href: "https://www.tiktok.com/@cibello_recipes",
    label: "TikTok",
    icon: (
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" className="text-white" aria-hidden>
        <path d="M21 8.5a6.3 6.3 0 0 1-3.7-1.2v6.9A5.6 5.6 0 1 1 11.7 8.6c.3 0 .6 0 .9.1v2.9a2.7 2.7 0 1 0 1.9 2.6V2h2.8A3.9 3.9 0 0 0 21 5.6V8.5z" />
      </svg>
    ),
  },
  {
    href: "https://www.pinterest.com/cibelloapp/",
    label: "Pinterest",
    icon: (
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" className="text-white" aria-hidden>
        <path d="M12.04 2C6.52 2 2.1 6.38 2.1 11.86c0 4.14 2.54 7.68 6.1 8.95-.08-.76-.16-1.92.03-2.75.17-.75 1.11-4.72 1.11-4.72s-.28-.57-.28-1.4c0-1.32.76-2.3 1.72-2.3.81 0 1.2.61 1.2 1.34 0 .81-.52 2.03-.79 3.16-.22.94.47 1.71 1.4 1.71 1.68 0 2.81-2.16 2.81-4.73 0-1.95-1.31-3.41-3.7-3.41-2.7 0-4.37 2-4.37 4.24 0 .77.23 1.32.59 1.74.16.2.18.27.13.49-.04.16-.14.53-.18.68-.06.22-.24.3-.44.22-1.14-.47-1.67-1.75-1.67-3.18 0-2.37 2-5.22 5.98-5.22 3.18 0 5.28 2.3 5.28 4.77 0 3.26-1.81 5.7-4.5 5.7-.9 0-1.75-.49-2.04-1.05l-.56 2.12c-.2.78-.75 1.75-1.11 2.34A10 10 0 0 0 12.04 22C17.56 22 22 17.52 22 12S17.56 2 12.04 2z" />
      </svg>
    ),
  },
  {
    href: "https://www.youtube.com/@cibelloappofficial",
    label: "YouTube",
    icon: (
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" className="text-white" aria-hidden>
        <path d="M23.5 6.19a3.02 3.02 0 0 0-2.12-2.14C19.54 3.55 12 3.55 12 3.55s-7.54 0-9.38.5A3.02 3.02 0 0 0 .5 6.19 31.6 31.6 0 0 0 0 12a31.6 31.6 0 0 0 .5 5.81 3.02 3.02 0 0 0 2.12 2.14c1.84.5 9.38.5 9.38.5s7.54 0 9.38-.5a3.02 3.02 0 0 0 2.12-2.14A31.6 31.6 0 0 0 24 12a31.6 31.6 0 0 0-.5-5.81zM9.75 15.57V8.43L15.84 12l-6.09 3.57z" />
      </svg>
    ),
  },
] as const;

export function SiteFooter() {
  const { t, lang, setLang } = useLocale();
  return (
    <footer className="bg-dark text-dark-ink">
      <div className="page-wrap grid gap-10 py-14 md:grid-cols-[1.2fr_0.8fr]">
        <div>
          <Logo className="text-white" />
          <p className="mt-3 max-w-[34ch] text-[0.95rem]">
            {t("foot_tag")}
          </p>
          <div className="mt-5 flex flex-wrap gap-3">
            {SOCIAL.map((item) => (
              <a
                key={item.label}
                href={item.href}
                aria-label={item.label}
                target="_blank"
                rel="noopener noreferrer"
                className="grid size-10 place-items-center rounded-full bg-white/8 hover:bg-white/14 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-amber"
              >
                {item.icon}
              </a>
            ))}
          </div>
        </div>
        <div>
          <p className="mb-3 font-semibold text-white">{t("foot_get")}</p>
          <StoreButtons />
        </div>
      </div>
      <div className="page-wrap grid gap-8 border-t border-white/10 py-10 sm:grid-cols-2">
        <nav aria-label={t("foot_site")} className="flex flex-col gap-2 text-[0.95rem]">
          <h3 className="mb-1 font-semibold text-white">{t("foot_site")}</h3>
          <Link to="/best-meal-app" className="hover:text-white">{t("foot_compare")}</Link>
          <Link to="/about" className="hover:text-white">{t("foot_about")}</Link>
        </nav>
        <nav aria-label={t("foot_company")} className="flex flex-col gap-2 text-[0.95rem]">
          <h3 className="mb-1 font-semibold text-white">{t("foot_company")}</h3>
          <Link to="/privacy" className="hover:text-white">{t("foot_privacy")}</Link>
          <Link to="/terms" className="hover:text-white">{t("foot_terms")}</Link>
          <a href={`mailto:${COMPANY.email}`} className="hover:text-white">{t("foot_contact")}</a>
          <a href={`tel:${COMPANY.phoneE164}`} className="hover:text-white">
            {COMPANY.phoneDisplay}
          </a>
          <a href={COMPANY.parentUrl} rel="noopener" className="hover:text-white">
            {COMPANY.legalName}
          </a>
        </nav>
      </div>
      <div className="page-wrap space-y-4 pb-10 text-sm text-dark-ink/80">
        <div>
          <p className="mb-2 font-semibold text-white">{t("foot_langs")}</p>
          <ul className="flex flex-wrap gap-x-4 gap-y-2">
            {LANGS.map((item) => (
              <li key={item.id}>
                <button
                  type="button"
                  onClick={() => setLang(item.id)}
                  className={item.id === lang ? "font-semibold text-white" : "hover:text-white"}
                >
                  {item.name}
                </button>
              </li>
            ))}
          </ul>
          <LangSelect tone="dark" className="mt-3 sm:hidden" />
        </div>
        <p>{t("foot_disclaimer")}</p>
        <p>© {new Date().getFullYear()} {COMPANY_LINE}</p>
      </div>
    </footer>
  );
}
