#!/usr/bin/env python3
"""Static SEO/link checker for the Cibello site. Exit code 1 on any error.

Checks every *.html: internal links resolve, canonical matches the file path,
hreflang targets exist and are reciprocal, JSON-LD parses, title/description
present and within length, exactly one <h1>, lang attribute set, og:image set.
Also verifies that sitemap.xml lists every indexable page and nothing else.

Usage: python3 tools/check.py
"""
import re, json, pathlib, sys, html as htmlmod

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://cibello.app"
errors, warnings = [], []

def url_to_path(url):
    url = url.split("#")[0].split("?")[0]
    if url.startswith(BASE):
        url = url[len(BASE):]
    if not url.startswith("/"):
        return None
    p = ROOT / url.lstrip("/")
    if url.endswith("/"):
        p = p / "index.html"
    return p

pages = [p for p in ROOT.rglob("*.html") if not p.relative_to(ROOT).as_posix().startswith(("tools/", "node_modules/"))]
canon_of = {}
hreflang_of = {}
for p in pages:
    rel = "/" + p.relative_to(ROOT).as_posix()
    html = p.read_text(encoding="utf-8")
    where = rel
    if not re.search(r'<html[^>]*\blang="[a-z]{2}"', html):
        errors.append(f"{where}: missing <html lang>")
    titles = re.findall(r"<title>(.*?)</title>", html, re.S)
    if len(titles) != 1:
        errors.append(f"{where}: {len(titles)} <title> tags")
    else:
        t = htmlmod.unescape(titles[0]).strip()
        if len(t) > 70:
            warnings.append(f"{where}: title {len(t)} chars: {t}")
    d = re.search(r'<meta name="description" content="([^"]*)"', html)
    if not d:
        errors.append(f"{where}: missing meta description")
    elif len(d.group(1)) > 165:
        warnings.append(f"{where}: description {len(d.group(1))} chars")
    h1 = re.findall(r"<h1[\s>]", html)
    if len(h1) != 1:
        errors.append(f"{where}: {len(h1)} <h1>")
    if 'property="og:image"' not in html and "noindex" not in html:
        errors.append(f"{where}: missing og:image")
    c = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    if c:
        canon_of[rel] = c.group(1)
        cp = url_to_path(c.group(1))
        if cp is None or cp.resolve() != p.resolve():
            errors.append(f"{where}: canonical {c.group(1)} does not point to this file")
    elif "noindex" not in html:
        errors.append(f"{where}: missing canonical")
    alts = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', html)
    hreflang_of[rel] = alts
    for h, u in alts:
        tp = url_to_path(u)
        if tp is None or not tp.exists():
            errors.append(f"{where}: hreflang {h} -> {u} missing")
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            json.loads(m.group(1))
        except Exception as e:
            errors.append(f"{where}: invalid JSON-LD: {e}")
    for m in re.finditer(r'(?:href|src)="([^"]+)"', html):
        u = m.group(1)
        if u.startswith(("http", "mailto:", "data:", "#", "tel:")):
            continue
        tp = url_to_path(u)
        if tp is None:
            tp = (p.parent / u.split("#")[0]).resolve()
        if not tp.exists():
            errors.append(f"{where}: broken link {u}")

# hreflang reciprocity
for rel, alts in hreflang_of.items():
    if not alts:
        continue
    self_url = canon_of.get(rel)
    for h, u in alts:
        tp = url_to_path(u)
        if tp is None:
            errors.append(f"{rel}: hreflang {h} has a malformed href {u}"); continue
        trel = "/" + tp.relative_to(ROOT).as_posix()
        back = [x for _, x in hreflang_of.get(trel, [])]
        if self_url and back and self_url not in back:
            errors.append(f"{rel}: hreflang to {u} is not reciprocal")

# sitemap coverage
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
listed = set(re.findall(r"<loc>([^<]+)</loc>", sm))
expected = set()
for p in pages:
    html = p.read_text(encoding="utf-8")
    rel = p.relative_to(ROOT).as_posix()
    if rel == "404.html" or "noindex" in html:
        continue
    url = BASE + "/" + (rel[:-len("index.html")] if rel.endswith("index.html") else rel)
    expected.add(url)
for u in sorted(expected - listed):
    errors.append(f"sitemap: missing {u}")
for u in sorted(listed - expected):
    errors.append(f"sitemap: stale {u}")
for u in listed:
    tp = url_to_path(u)
    if tp is None or not tp.exists():
        errors.append(f"sitemap: {u} does not exist")

for w in warnings:
    print("WARN", w)
for e in errors:
    print("ERROR", e)
print(f"{len(pages)} pages, {len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
