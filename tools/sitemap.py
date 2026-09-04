#!/usr/bin/env python3
"""Regenerate sitemap.xml from the HTML files in the repo.

Every indexable page contributes one <url>; hreflang alternates are read from
the page's own <link rel="alternate" hreflang> tags so the sitemap can never
drift from the markup. lastmod comes from the last git commit touching the file.

Usage: python3 tools/sitemap.py
"""
import re, subprocess, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://cibello.app"
SKIP = {"404.html"}

def lastmod(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        if out:
            return out
    except Exception:
        pass
    return datetime.date.today().isoformat()

def url_of(path):
    rel = path.relative_to(ROOT).as_posix()
    if rel.endswith("index.html"):
        rel = rel[:-len("index.html")]
    return BASE + "/" + rel

def priority(url):
    depth = url[len(BASE):].strip("/").count("/")
    if url == BASE + "/":
        return "1.0"
    if url.endswith(".html"):
        return "0.3"
    return "0.9" if depth == 0 else "0.8"

entries = []
for p in sorted(ROOT.rglob("*.html")):
    rel = p.relative_to(ROOT).as_posix()
    if rel in SKIP or rel.startswith(("tools/", "node_modules/", ".git/")):
        continue
    html = p.read_text(encoding="utf-8")
    if 'name="robots" content="noindex' in html:
        continue
    url = url_of(p)
    alts = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', html)
    entries.append((url, lastmod(p), alts))

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for url, mod, alts in entries:
    xl = "".join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{u}"/>' for h, u in alts)
    lines.append(f"  <url><loc>{url}</loc><lastmod>{mod}</lastmod>{xl}<priority>{priority(url)}</priority></url>")
lines.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"sitemap.xml: {len(entries)} urls")
