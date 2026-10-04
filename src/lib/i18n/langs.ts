export const LANGS = [
  { id: "sv", name: "Svenska" },
  { id: "en", name: "English" },
  { id: "de", name: "Deutsch" },
  { id: "fr", name: "Français" },
  { id: "es", name: "Español" },
  { id: "it", name: "Italiano" },
  { id: "nl", name: "Nederlands" },
  { id: "pl", name: "Polski" },
  { id: "da", name: "Dansk" },
  { id: "nb", name: "Norsk" },
  { id: "fi", name: "Suomi" },
  { id: "pt", name: "Português" },
] as const;

export type Lang = (typeof LANGS)[number]["id"];

export const LANG_IDS = LANGS.map((l) => l.id);

export function isLang(v: string): v is Lang {
  return (LANG_IDS as string[]).includes(v);
}
