#!/usr/bin/env python3
"""Copie delle locandine interattive per i colleghi agenti.

Per ogni agente in AGENTI e ogni campagna crea <agente>/<campagna>/ con:
- index.html con nome, numero, link tel: e wa.me dell'agente;
- gli stessi file della campagna (foto, dati, anteprima, icona);
- locandina.jpg rifatta con nome e numero dell'agente (dove la locandina li ha).

Link: stefanoserafin.github.io/mak-promo/<agente>/<campagna>/
Si rilancia dopo ogni modifica a una campagna o quando se ne aggiunge una:
    python3 _build/agenti.py            # tutti gli agenti
    python3 _build/agenti.py angelo     # uno solo
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

PROMO = Path(__file__).resolve().parent.parent
LOCANDINE = PROMO.parent / "Locandine"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE_URL = "https://stefanoserafin.github.io/mak-promo/"

AGENTI = {
    "angelo": {"nome": "Angelo", "cognome": "Magnotta", "tel": "393924501782", "tel_vis": "392 450 1782"},
}

# Sorgente della locandina con nome e numero; None = l'immagine non li ha, si copia com'è.
SORGENTE_LOCANDINA = {
    "fix-pack": None,
    "halloween-ruotino": None,
    "kit-gomma-ruota": "kit-gomma-ruota-inverno/locandina-flash.html",
    "ts900-rinnovi": "ts900-rinnovi/locandina.html",
}

STEFANO = {"nome": "Stefano", "cognome": "Serafin", "tel": "393316798961", "tel_vis": "331 679 8961"}

# Frasi che hanno senso solo per Stefano (campagna → [(vecchio, nuovo)]).
FRASI = {
    "anelli-centraggio": [
        ("Il mio video breve sugli anelli di centraggio MAK.", "Video breve sugli anelli di centraggio MAK."),
        ("Stefano con gli anelli di centraggio sul tavolo", "Anelli di centraggio sul tavolo"),
    ],
    "kit-gomma-ruota": [("poi WhatsApp e Stefano */", "poi WhatsApp e l'agente */")],
    "ts900-rinnovi": [("poi WhatsApp e Stefano */", "poi WhatsApp e l'agente */")],
}


def campagne():
    return sorted(p.name for p in PROMO.iterdir()
                  if p.is_dir() and (p / "index.html").exists()
                  and not p.name.startswith(("_", ".")) and p.name not in AGENTI)


def sostituisci(testo, a, c, frasi=True):
    s = STEFANO
    for vecchio, nuovo in (FRASI.get(c, []) if frasi else []):
        assert vecchio in testo, f"{c}: frase non trovata: {vecchio}"
        testo = testo.replace(vecchio, nuovo)
    testo = testo.replace(f"{s['nome']} {s['cognome']}", f"{a['nome']} {a['cognome']}")
    testo = testo.replace(s["tel"], a["tel"]).replace(s["tel_vis"], a["tel_vis"])
    testo = testo.replace("Ciao Stefano", f"Ciao {a['nome']}")
    return testo


def pagina(chiave, a, c):
    t = sostituisci((PROMO / c / "index.html").read_text(encoding="utf-8"), a, c)
    t = t.replace(f"{BASE_URL}{c}/", f"{BASE_URL}{chiave}/{c}/")  # og:url e og:image
    rimasti = re.findall(r"Stefano|Serafin|3316798961|331 679 8961", t)
    assert not rimasti, f"{c}: restano riferimenti a Stefano: {set(rimasti)}"
    return t


def locandina(a, c, dest):
    rel = SORGENTE_LOCANDINA.get(c, f"{c}/locandina.html")
    if rel is None:
        return "copiata"
    src = LOCANDINE / rel
    tmp = src.with_name("_agente_tmp.html")
    png = src.with_name("_agente_tmp.png")
    testo = src.read_text(encoding="utf-8")
    assert STEFANO["tel_vis"] in testo, f"{c}: la locandina non ha il numero di Stefano"
    tmp.write_text(sostituisci(testo, a, c, frasi=False), encoding="utf-8")
    try:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=2", "--window-size=1080,1350",
                        "--virtual-time-budget=3000", f"--screenshot={png}", tmp.as_uri()],
                       check=True, capture_output=True)
        subprocess.run(["sips", "-Z", "1620", "-s", "format", "jpeg", "-s", "formatOptions", "85",
                        str(png), "--out", str(dest / "locandina.jpg")], check=True, capture_output=True)
    finally:
        tmp.unlink(missing_ok=True)
        png.unlink(missing_ok=True)
    return "rifatta"


def genera(chiave):
    a = AGENTI[chiave]
    radice = PROMO / chiave
    for c in campagne():
        dest = radice / c
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(PROMO / c, dest, ignore=shutil.ignore_patterns("index.template.html", ".DS_Store"))
        (dest / "index.html").write_text(pagina(chiave, a, c), encoding="utf-8")
        print(f"{chiave}/{c}: pagina ok, locandina {locandina(a, c, dest)}")
    # elenco delle campagne dell'agente
    voci = "\n".join(f'<li><a href="{c}/">{c}</a></li>' for c in campagne())
    (radice / "index.html").write_text(
        f'<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<meta name="robots" content="noindex"><title>Locandine · {a["nome"]} {a["cognome"]}</title>'
        f'<style>body{{font-family:-apple-system,sans-serif;margin:24px 16px;background:#fff;color:#14161a}}'
        f'a{{color:#da2128;font-size:18px;line-height:2}}</style>'
        f'<h1>Locandine MAK · {a["nome"]} {a["cognome"]}</h1><ul>{voci}</ul>', encoding="utf-8")


if __name__ == "__main__":
    for k in (sys.argv[1:] or AGENTI):
        genera(k)
