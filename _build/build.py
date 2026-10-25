#!/usr/bin/env python3
"""Genera halloween-ruotino/index.html dal modello, con dentro i ruotini NPK.

Fonte: Mak/noproblemkit/dati/ruotini.csv (configuratore del sito NPK).
Uso: python3 _build/build.py
"""
import csv, json, re
from pathlib import Path

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent
CSV = RADICE.parent / "noproblemkit" / "dati" / "ruotini.csv"
CARTELLA = RADICE / "halloween-ruotino"

dati = {}
righe = 0
with open(CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter=";"):
        marca, modello = r["marca"].strip(), r["modello"].strip()
        m = re.search(r"(\d{2})\s*$", r["pneumatico"].strip())
        if not (marca and modello and r["codice"] and m):
            continue
        voce = [r["anno"].strip(), r["codice"].strip(), r["pneumatico"].strip(),
                "L" if r["ruota"] == "ALLOY" else "A"]
        lista = dati.setdefault(marca, {}).setdefault(modello, [])
        if voce not in lista:
            lista.append(voce)
            righe += 1

modello_html = (CARTELLA / "index.template.html").read_text(encoding="utf-8")
blob = json.dumps(dati, ensure_ascii=False, separators=(",", ":"))
(CARTELLA / "index.html").write_text(modello_html.replace("/*__RUOTINI__*/{}", blob), encoding="utf-8")
print(f"{len(dati)} marche, {sum(len(v) for v in dati.values())} modelli, {righe} abbinamenti")
