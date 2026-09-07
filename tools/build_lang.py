#!/usr/bin/env python3
"""Render everything language-specific for one or more languages from tools/content/<lang>.py.

For each language it writes: the three guides (existing slugs), tools/hubtext/<lang>.html,
/<lang>/about/, /<lang>/press/, /<lang>/news/ (+feed.xml), /<lang>/privacy/, /<lang>/terms/,
/<lang>/delete-account/. Then it relinks every footer, rebuilds the landing pages and fixes
hreflang on the shared pages.

Usage: python3 tools/build_lang.py de fr …   (or: all)
"""
import re, json, pathlib, sys, importlib, html as H, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import sitedata
from sitedata import *
JS = 'document.documentElement.classList.add("js")'

def about_path(lang): return "/om/" if lang == "sv" else f"/{lang}/about/"
def press_path(lang): return "/press/" if lang == "sv" else f"/{lang}/press/"
def news_path(lang): return "/nytt/" if lang == "sv" else f"/{lang}/news/"
def privacy_path(lang): return "/integritet.html" if lang == "sv" else f"/{lang}/privacy/"
def terms_path(lang): return "/villkor.html" if lang == "sv" else f"/{lang}/terms/"
def delete_path(lang): return "/delete-account.html" if lang == "sv" else f"/{lang}/delete-account/"
sitedata.legal_paths = lambda lang: (privacy_path(lang), terms_path(lang))
sitedata.news_path = news_path

def footer(lang):
    t = T[lang]
    f = sitedata.footer(lang)
    # company column: about, press, news, privacy, terms, delete, contact
    f = re.sub(r'(<nav aria-label="' + re.escape(t["company"]) + r'"><h3>[^<]*</h3>).*?(</nav>)',
               lambda m: m.group(1) + f'<a href="{about_path(lang)}">{ABOUT[lang]}</a><a href="{press_path(lang)}">{PRESS[lang]}</a><a href="{news_path(lang)}">{NEWS[lang]}</a><a href="{privacy_path(lang)}">{t["privacy"]}</a><a href="{terms_path(lang)}">{t["terms"]}</a><a href="{delete_path(lang)}">{t["delete"]}</a><a href="mailto:hello@cibello.app">{t["contact"]}</a>' + m.group(2), f, count=1, flags=re.S)
    return f

def alt_block(pathfn, langs=None):
    langs = langs or list(LANG_NAMES)
    alts = [(l, "https://cibello.app" + pathfn(l)) for l in langs]
    alts.append(("x-default", "https://cibello.app" + pathfn("en")))
    return "\n".join(f'<link rel="alternate" hreflang="{l}" href="{u}">' for l, u in alts)

def head(lang, url, title, desc, alt_links, ld, og_type="website", extra=""):
    return f'''<!DOCTYPE html>
<html lang="{lang}"><head><meta charset="utf-8"><script>{JS}</script><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{alt_links}
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#2f7d51"><meta property="og:type" content="{og_type}"><meta property="og:locale" content="{OG_LOCALE[lang]}"><meta property="og:site_name" content="Cibello"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}">
<link rel="stylesheet" href="/tokens.css"><link rel="stylesheet" href="/seo.css">{head_extras(lang)}{extra}<script type="application/ld+json">{ld}</script></head>
'''

def webpage(url, name, desc, lang, typ="WebPage", extra=None):
    node = {"@type":typ,"@id":url+"#webpage","name":name,"url":url,"description":desc,"inLanguage":lang,"dateModified":TODAY,"isPartOf":{"@type":"WebSite","@id":"https://cibello.app/#website","name":"Cibello","url":"https://cibello.app/"},"publisher":{"@id":"https://cibello.app/#organization"},"primaryImageOfPage":{"@type":"ImageObject","url":f"https://cibello.app/img/og-{lang}.png","width":1200,"height":630}}
    if extra: node.update(extra)
    return node

def crumbs_ld(lang, h1, url):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Cibello","item":"https://cibello.app"+home_of(lang)},{"@type":"ListItem","position":2,"name":h1,"item":url}]}

def aside(lang, self_path=None):
    t = T[lang]
    links = "".join(f'<a href="{p}">{l}</a>' for p, l in GUIDES[lang] if p != self_path) + f'<a href="{home_of(lang)}">{t["home"]}</a>'
    langs = "".join(f'<a href="{home_of(c)}" lang="{c}" hreflang="{c}">{n}</a>' for c, n in LANG_NAMES.items() if c != lang)
    return f'<aside class="aside"><h2>{t["more"]}</h2>{links}<h2>{t["other_langs"]}</h2>{langs}</aside>'

def write(path, html):
    out = ROOT / path.strip("/") / "index.html"; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8"); print("wrote", path)

def render_article(lang, path, c, faq_title, alt_links=None, typ="WebPage", og_type="article", with_faq=True, with_app=True):
    url = f"https://cibello.app{path}"; t = T[lang]
    graph = [ORG, webpage(url, c["h1"], c["desc"], lang, typ), crumbs_ld(lang, c["h1"], url)]
    faq = c.get("faq") or []
    if faq: graph.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in faq]})
    if with_app: graph.append(app_node(lang))
    ld = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False, separators=(",",":"))
    body = "".join(f"<section><h2>{h2}</h2>{b}</section>" for h2, b in c["sections"])
    faq_html = (f'<section class="faq"><h2>{faq_title}</h2>' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq) + "</section>") if faq else ""
    eyebrow = f'<div class="eyebrow">{c["eyebrow"]}</div>' if c.get("eyebrow") else ""
    html = head(lang, url, c["title"], c["desc"], alt_links or alt_block(lambda l: path), ld, og_type)
    html += f'''<body><a class="skip" href="#main">{SKIP[lang]}</a>{header(lang)}
<main id="main"><div class="hero"><div class="wrap">{crumbs(lang, c["h1"])}{eyebrow}<h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p></div></div>
<div class="wrap content"><article class="article">{body}{faq_html}{cta_block(lang)}<p class="updated"><small>{t["updated"]} {TODAY}</small></p></article>{aside(lang, path)}</div></main>
{footer(lang)}</body></html>
'''
    html = html.replace('href="https://play.google.com/store/apps/details?id=com.cibello.app"', 'href="https://play.google.com/store/apps/details?id=com.cibello.app&amp;referrer=utm_source%3Dcibello.app%26utm_medium%3Dweb%26utm_campaign%3D' + path.strip("/").replace("/", "-") + '"')
    write(path, html)

def render_legal(lang, path, c, ui, kind):
    """Legal pages use legal.css like the Swedish originals."""
    url = f"https://cibello.app{path}"
    pathfn = {"privacy": privacy_path, "terms": terms_path, "delete": delete_path}[kind]
    sv_path = pathfn("sv")
    ld = json.dumps({"@context":"https://schema.org","@graph":[ORG, webpage(url, c["h1"], c["desc"], lang, extra={"about":{"@id":"https://cibello.app/#organization"}})]}, ensure_ascii=False, separators=(",",":"))
    nav = f'<a href="{home_of(lang)}">{T[lang]["home"]}</a><a href="{privacy_path(lang)}">{ui["privacy_nav"]}</a><a href="{terms_path(lang)}">{ui["terms_nav"]}</a><a href="{delete_path(lang)}">{ui["delete_nav"]}</a><a href="{sv_path}" lang="sv" hreflang="sv">Svenska</a>'
    notice = f'<p class="notice"><strong>{ui["translation_label"]}</strong> {ui["translation_note"].replace("{sv}", sv_path)}</p>' if kind != "delete" else ""
    extra_notice = f'<p class="notice">{c["notice"]}</p>' if c.get("notice") else ""
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
  <head>
    <meta charset="utf-8" />
<script>{JS}</script>
    <meta name="viewport" content="width=device-width, initial-scale=1" /><meta name="color-scheme" content="light">
    <meta name="description" content="{c["desc"]}" />
    <title>{c["title"]}</title>
    <link rel="stylesheet" href="/tokens.css"><link rel="stylesheet" href="/legal.css" />
{head_extras(lang).replace("><", ">" + chr(10) + "<")}
<link rel="canonical" href="{url}" />
{alt_block(pathfn)}
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1" />
<meta name="theme-color" content="#2f7d51" />
<meta property="og:type" content="website" /><meta property="og:site_name" content="Cibello" /><meta property="og:locale" content="{OG_LOCALE[lang]}" />
<meta property="og:title" content="{c["title"]}" /><meta property="og:description" content="{c["desc"]}" /><meta property="og:url" content="{url}" />
<meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="{c["title"]}" /><meta name="twitter:description" content="{c["desc"]}" />
<script type="application/ld+json">{ld}</script>
</head>
  <body><a class="skip" href="#main">{SKIP[lang]}</a>
    <header>
      <div>
        <h1>{c["h1"]}</h1>
        <p class="meta">{ui["legal_meta"]}</p>
        <nav>{nav}</nav>
      </div>
    </header>
    <main id="main">
      {notice}{extra_notice}
{c["body"]}
    </main>
    <footer>
      © 2026 LandveX AB · <a href="mailto:privacy@cibello.app">privacy@cibello.app</a> · <a href="mailto:support@cibello.app">support@cibello.app</a>
    </footer>
  </body>
</html>
'''
    write(path, html)

def render_news(lang, c):
    path = news_path(lang); url = f"https://cibello.app{path}"; t = T[lang]
    items = "".join(f'<article class="newsitem"><time datetime="{d}">{d}</time><h2><a href="{link}">{H.escape(tt)}</a></h2><p>{H.escape(body)}</p></article>' for d, tt, link, body in c["entries"])
    ld = json.dumps({"@context":"https://schema.org","@graph":[ORG, webpage(url, c["h1"], c["desc"], lang, "CollectionPage"), crumbs_ld(lang, c["h1"], url)]}, ensure_ascii=False, separators=(",",":"))
    extra = f'<link rel="alternate" type="application/rss+xml" title="Cibello – {NEWS[lang]}" href="{path}feed.xml">'
    html = head(lang, url, c["title"], c["desc"], alt_block(news_path), ld, extra=extra)
    html += f'''<body><a class="skip" href="#main">{SKIP[lang]}</a>{header(lang)}
<main id="main"><div class="hero"><div class="wrap">{crumbs(lang, c["h1"])}<h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p><p><a class="rsslink" href="{path}feed.xml">{c["rss_label"]}</a></p></div></div>
<div class="wrap content"><div class="article news">{items}<p class="updated"><small>{t["updated"]} {TODAY}</small></p></div>{aside(lang)}</div></main>
{footer(lang)}</body></html>
'''
    write(path, html)
    rss_items = "".join(f'<item><title>{H.escape(tt)}</title><link>https://cibello.app{link}</link><guid isPermaLink="false">cibello-{lang}-{d}-{i}</guid><pubDate>{d}T08:00:00+02:00</pubDate><description>{H.escape(body)}</description></item>' for i, (d, tt, link, body) in enumerate(c["entries"]))
    (ROOT / path.strip("/") / "feed.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Cibello – {NEWS[lang]}</title><link>{url}</link><description>{H.escape(c["desc"])}</description><language>{lang}</language><atom:link href="{url}feed.xml" rel="self" type="application/rss+xml"/>{rss_items}</channel></rss>\n', encoding="utf-8")

def build(lang):
    C = importlib.import_module(f"content.{lang}")
    ui = C.UI
    # guides: keep the existing hreflang block of each file
    for path, c in C.GUIDES.items():
        f = ROOT / path.strip("/") / "index.html"
        alt = None
        if f.exists():
            alts = re.findall(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">', f.read_text(encoding="utf-8"))
            alt = "\n".join(alts) if alts else None
        render_article(lang, path, c, ui["faq_title"], alt_links=alt)
    (ROOT / "tools" / "hubtext" / f"{lang}.html").write_text(C.HUBTEXT.strip(), encoding="utf-8")
    render_article(lang, about_path(lang), C.ABOUT, ui["faq_title"], alt_links=alt_block(about_path), typ="AboutPage", og_type="website", with_faq=False)
    render_article(lang, press_path(lang), C.PRESS, ui["faq_title"], alt_links=alt_block(press_path), og_type="website", with_faq=False)
    render_news(lang, C.NEWS)
    render_legal(lang, privacy_path(lang), C.PRIVACY, ui, "privacy")
    render_legal(lang, terms_path(lang), C.TERMS, ui, "terms")
    render_legal(lang, delete_path(lang), C.DELETE, ui, "delete")

def relink_all():
    """Footers on every seo.css page, hreflang on shared sv/en pages, Swedish legal links."""
    n = 0
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith("tools/") or rel == "404.html": continue
        h = p.read_text(encoding="utf-8")
        lang = re.search(r'<html lang="(\w+)"', h).group(1)
        if "seo.css" in h and '<footer class="foot">' in h:
            h2 = re.sub(r'<footer class="foot">.*?</footer>', footer(lang), h, count=1, flags=re.S)
            if lang != "sv":
                h2 = h2.replace('href="/en/privacy/"', f'href="{privacy_path(lang)}"').replace('href="/en/terms/"', f'href="{terms_path(lang)}"').replace('href="/delete-account.html"', f'href="{delete_path(lang)}"')
            if h2 != h: p.write_text(h2, encoding="utf-8"); n += 1
    print("footers relinked:", n)
    # shared pages: full hreflang sets
    for pathfn, pages in [(about_path, ["om/index.html", "en/about/index.html"]), (press_path, ["press/index.html", "en/press/index.html"]), (news_path, ["nytt/index.html", "en/news/index.html"]),
                          (privacy_path, ["integritet.html", "en/privacy/index.html"]), (terms_path, ["villkor.html", "en/terms/index.html"]), (delete_path, ["delete-account.html"])]:
        for rel in pages:
            f = ROOT / rel
            if not f.exists(): continue
            h = f.read_text(encoding="utf-8")
            block = alt_block(pathfn)
            if rel.endswith(".html") and "/" not in rel:  # legacy sv pages use " />"
                block = block.replace(">", " />")
            h2 = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]+"\s*/?>\s*)+', block + "\n", h, count=1)
            if h2 == h and 'hreflang=' not in h:
                h2 = h.replace("</head>", block + "\n</head>", 1)
            f.write_text(h2, encoding="utf-8")
    # build_home uses the same path functions
    bh = ROOT / "tools" / "build_home.py"; b = bh.read_text(encoding="utf-8")
    b2 = b.replace('ap = "/om/" if lang == "sv" else "/en/about/"; pp = "/press/" if lang == "sv" else "/en/press/"', 'from build_lang import about_path, press_path, news_path, privacy_path, terms_path, delete_path\n    ap = about_path(lang); pp = press_path(lang)')
    b2 = b2.replace('<a href="{legal_paths(lang)[0]}">{t["privacy"]}</a><a href="{legal_paths(lang)[1]}">{t["terms"]}</a><a href="/delete-account.html">{t["delete"]}</a>', '<a href="{privacy_path(lang)}">{t["privacy"]}</a><a href="{terms_path(lang)}">{t["terms"]}</a><a href="{delete_path(lang)}">{t["delete"]}</a>')
    if b2 != b: bh.write_text(b2, encoding="utf-8")

if __name__ == "__main__":
    args = sys.argv[1:] or ["all"]
    langs = [l for l in LANG_NAMES if l not in ("sv", "en") and (ROOT / "tools" / "content" / f"{l}.py").exists()] if args == ["all"] else args
    for l in langs: build(l)
    relink_all()
    subprocess.run([sys.executable, str(ROOT / "tools" / "build_home.py")], check=True)
