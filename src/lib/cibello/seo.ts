import { COMPANY } from "./company";

const SITE = "https://cibello.app";
const OG = `${SITE}/og.jpg`;

export function pageMeta(opts: { title: string; description: string; path: string; noindex?: boolean }) {
  const url = opts.path === "/" ? SITE : `${SITE}${opts.path}`;
  return {
    meta: [
      { title: opts.title },
      { name: "description", content: opts.description },
      { property: "og:title", content: opts.title },
      { property: "og:description", content: opts.description },
      { property: "og:url", content: url },
      { property: "og:type", content: "website" },
      { property: "og:site_name", content: COMPANY.brand },
      { property: "og:locale", content: "sv_SE" },
      { property: "og:image", content: OG },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:title", content: opts.title },
      { name: "twitter:description", content: opts.description },
      { name: "twitter:image", content: OG },
      ...(opts.noindex ? [{ name: "robots", content: "noindex, follow" }] : []),
    ],
    links: [{ rel: "canonical", href: url }],
  };
}
