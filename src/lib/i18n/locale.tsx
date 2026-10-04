import { createContext, useCallback, useContext, useEffect, useMemo, useState, type ReactNode } from "react";
import messages from "./messages.json";
import { isLang, type Lang } from "./langs";

const STORAGE = "cibello-lang";

type Dict = Record<string, string>;
const DICTS = messages as Record<Lang, Dict>;

function detect(): Lang {
  if (typeof window === "undefined") return "sv";
  const saved = window.localStorage.getItem(STORAGE);
  if (saved && isLang(saved)) return saved;
  return "sv";
}

type Vars = Record<string, string | number>;
type Translate = (key: string, vars?: Vars) => string;

type Ctx = {
  lang: Lang;
  setLang: (lang: Lang) => void;
  t: Translate;
};

function interpolate(s: string, vars?: Vars) {
  if (!vars) return s;
  let out = s;
  for (const [k, v] of Object.entries(vars)) out = out.replaceAll(`{${k}}`, String(v));
  return out;
}

const LocaleContext = createContext<Ctx>({
  lang: "sv",
  setLang: () => {},
  t: (key) => key,
});

export function LocaleProvider({ children }: { children: ReactNode }) {
  const [lang, setLangState] = useState<Lang>("sv");

  useEffect(() => {
    setLangState(detect());
  }, []);

  useEffect(() => {
    document.documentElement.lang = lang;
    window.localStorage.setItem(STORAGE, lang);
  }, [lang]);

  const t = useCallback<Translate>(
    (key, vars) =>
      interpolate(DICTS[lang]?.[key] ?? DICTS.sv?.[key] ?? DICTS.en?.[key] ?? key, vars),
    [lang],
  );

  const value = useMemo(() => ({ lang, setLang: setLangState, t }), [lang, t]);

  return <LocaleContext.Provider value={value}>{children}</LocaleContext.Provider>;
}

export function useLocale() {
  return useContext(LocaleContext);
}
