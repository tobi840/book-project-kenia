#!/usr/bin/env python3
"""Linkcheck fuer ein Kapitel des Kenia-Vorlesebuchs.

Prueft jeden Link im Block "Weiterlesen und Sehen": erreichbar, Statuscode,
Weiterleitungsziel, Seitentitel. Ob der Titel zum Kontextsatz passt und ob die
URL im Research-Doc steht, beurteilt die QS, nicht dieses Skript.

Deep Research erfindet gelegentlich URLs. Das ist der haeufigste Fehlertyp,
deshalb laeuft der Check als Skript und nicht im Kopf.

    python3 scripts/check_links.py chapters/001-wuergefeige.html
    python3 scripts/check_links.py chapters/001-wuergefeige.html --research research/001-wuergefeige.txt
    python3 scripts/check_links.py chapters/001-wuergefeige.html --offline

Zwei Pruefungen:

1. Herkunft (offline, mit --research): steht die URL woertlich im Research-Doc?
   Das faengt vom Schreiber erfundene oder umgebaute Adressen. Haeufigster
   Fehlertyp, und der einzige, den wir selbst verursachen.
2. Erreichbarkeit (braucht Netz): HTTP-Status, Weiterleitung, Seitentitel.
   Sperrt die Egress-Policy den Host, meldet das Skript "nicht pruefbar" und
   nicht "kaputt". Ein blockierter Host ist keine tote Quelle.

Exit-Code 0 = keine erfundene URL und kein toter Link, sonst 1.
"""

import argparse
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser

TIMEOUT = 25
UA = "Mozilla/5.0 (compatible; KeniaBuch-Linkcheck/1.0)"
CA = "/root/.ccr/ca-bundle.crt"

EGRESS = re.compile(r"(403 Forbidden|407 |Tunnel connection failed|EGRESS_BLOCKED|"
                    r"blocked by the network egress proxy)", re.I)

FEHLERSEITE = re.compile(
    r"(404|not found|seite nicht gefunden|page not found|error|zugriff verweigert|"
    r"access denied|forbidden)", re.I)


class LinkSammler(HTMLParser):
    """Sammelt die <li>-Eintraege aus <section class="weiterlesen">."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_wl = 0
        self.depth = 0
        self.eintraege = []
        self._href = None
        self._text = []
        self._in_li = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and "weiterlesen" in (a.get("class") or "").split():
            self.in_wl = True
            self.depth = 0
        if self.in_wl:
            if tag == "section":
                self.depth += 1
            if tag == "li":
                self._in_li = True
                self._href = None
                self._text = []
            if tag == "a" and self._in_li and self._href is None:
                self._href = a.get("href")

    def handle_endtag(self, tag):
        if not self.in_wl:
            return
        if tag == "li" and self._in_li:
            self.eintraege.append({
                "url": self._href,
                "zeile": " ".join("".join(self._text).split()),
            })
            self._in_li = False
        if tag == "section":
            self.depth -= 1
            if self.depth <= 0:
                self.in_wl = False

    def handle_data(self, data):
        if self._in_li:
            self._text.append(data)


def titel_von(html):
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    if not m:
        return ""
    t = re.sub(r"<[^>]+>", " ", m.group(1))
    t = (t.replace("&amp;", "&").replace("&nbsp;", " ")
          .replace("&#39;", "'").replace("&quot;", '"'))
    return " ".join(t.split())[:160]


def opener():
    ctx = ssl.create_default_context(cafile=CA if os.path.exists(CA) else None)
    return urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=ctx),
        urllib.request.ProxyHandler(urllib.request.getproxies()),
    )


def pruefe_url(op, url):
    e = {"url": url, "status": None, "ziel": None, "titel": "",
         "erreichbarkeit": "kaputt", "hinweis": ""}
    if not url or not url.startswith("http"):
        e["hinweis"] = "Keine vollstaendige URL"
        return e
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/pdf,*/*",
        "Accept-Language": "de,en;q=0.8",
    })
    try:
        with op.open(req, timeout=TIMEOUT) as r:
            e["status"] = r.status
            e["ziel"] = r.geturl()
            typ = (r.headers.get("Content-Type") or "").lower()
            if "html" in typ:
                e["titel"] = titel_von(r.read(200000).decode("utf-8", "replace"))
            else:
                e["titel"] = "(" + (typ.split(";")[0] or "unbekannt") + ")"
    except urllib.error.HTTPError as ex:
        e["status"] = ex.code
        e["ziel"] = url
        if ex.code in (403, 407) and EGRESS.search(str(ex.reason) + str(ex.headers)):
            e["erreichbarkeit"] = "nicht-pruefbar"
            e["hinweis"] = "Egress-Policy sperrt den Host, Erreichbarkeit hier nicht pruefbar"
        else:
            e["hinweis"] = "HTTP " + str(ex.code) + " " + str(ex.reason)
        return e
    except Exception as ex:
        text = type(ex).__name__ + ": " + str(ex)[:200]
        if EGRESS.search(text):
            e["erreichbarkeit"] = "nicht-pruefbar"
            e["hinweis"] = "Egress-Policy sperrt den Host, Erreichbarkeit hier nicht pruefbar"
        else:
            e["hinweis"] = text
        return e

    e["erreichbarkeit"] = "ok" if e["status"] == 200 else "kaputt"
    if e["ziel"] and e["ziel"].rstrip("/") != url.rstrip("/"):
        e["hinweis"] = ("Weiterleitung auf " + e["ziel"] + ". " + e["hinweis"]).strip()
    if e["titel"] and FEHLERSEITE.search(e["titel"]):
        e["erreichbarkeit"] = "kaputt"
        e["hinweis"] = ('Titel sieht nach Fehlerseite aus: "' + e["titel"] + '". ' + e["hinweis"]).strip()
    return e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("datei")
    ap.add_argument("--research", help="Research-Doc als Textdatei, prueft die Herkunft jeder URL")
    ap.add_argument("--offline", action="store_true", help="Nur Herkunft pruefen, kein Netz")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    s = LinkSammler()
    s.feed(open(a.datei, encoding="utf-8").read())

    quelle = ""
    if a.research and os.path.exists(a.research):
        quelle = open(a.research, encoding="utf-8").read()

    op = None if a.offline else opener()
    ergebnisse = []
    for eintrag in s.eintraege:
        url = (eintrag["url"] or "").strip()
        if op is not None:
            r = pruefe_url(op, url)
        else:
            r = {"url": url, "status": None, "ziel": None, "titel": "",
                 "erreichbarkeit": "nicht-geprueft", "hinweis": "Offline-Lauf"}
        if not quelle:
            r["herkunft"] = "nicht-geprueft"
        elif not url:
            r["herkunft"] = "keine-url"
        elif url.rstrip("/") in quelle or url in quelle:
            r["herkunft"] = "im-research"
        else:
            r["herkunft"] = "NICHT-IM-RESEARCH"
        r["zeile"] = eintrag["zeile"]
        ergebnisse.append(r)

    erfunden = [r for r in ergebnisse if r["herkunft"] == "NICHT-IM-RESEARCH"]
    tot = [r for r in ergebnisse if r["erreichbarkeit"] == "kaputt"]
    geblockt = [r for r in ergebnisse if r["erreichbarkeit"] == "nicht-pruefbar"]

    aus = {
        "datei": a.datei,
        "research": a.research or None,
        "links": len(ergebnisse),
        "erfundene_urls": len(erfunden),
        "tote_links": len(tot),
        "nicht_pruefbar": len(geblockt),
        "ergebnisse": ergebnisse,
    }

    if a.json:
        print(json.dumps(aus, ensure_ascii=False, indent=2))
    else:
        print("Linkcheck: " + a.datei)
        print(str(len(ergebnisse)) + " Links, " + str(len(erfunden)) + " nicht im Research-Doc, "
              + str(len(tot)) + " tot, " + str(len(geblockt)) + " nicht pruefbar (Egress)")
        print("")
        for r in ergebnisse:
            marke = "FEHLER" if (r["herkunft"] == "NICHT-IM-RESEARCH" or r["erreichbarkeit"] == "kaputt") else "ok"
            print("  [" + marke + "] " + str(r["url"]))
            print("        Herkunft:      " + r["herkunft"])
            print("        Erreichbarkeit: " + r["erreichbarkeit"]
                  + ("" if r["status"] is None else " (HTTP " + str(r["status"]) + ")"))
            if r["titel"]:
                print("        Titel:         " + r["titel"])
            if r["hinweis"]:
                print("        Hinweis:       " + r["hinweis"])
            if r["zeile"]:
                print("        Zeile:         " + r["zeile"][:150])

    sys.exit(1 if (erfunden or tot) else 0)


if __name__ == "__main__":
    main()
