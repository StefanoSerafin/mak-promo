#!/usr/bin/env python3
"""Genera le pagine delle campagne dai modelli, con dentro i dati del configuratore NPK.

halloween-ruotino: ruotini da Mak/noproblemkit/dati/ruotini.csv.
kit-gomma-ruota: marche e modelli da Mak/noproblemkit/dati/veicoli.csv.
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

# kit-gomma-ruota: elenco marca -> modelli per la richiesta kit
VEICOLI_CSV = RADICE.parent / "noproblemkit" / "dati" / "veicoli.csv"
KIT = RADICE / "kit-gomma-ruota"
veicoli = {}
with open(VEICOLI_CSV, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f, delimiter=";"):
        marca, modello = r["marca"].strip(), r["modello"].strip()
        if marca and modello:
            veicoli.setdefault(marca, set()).add(modello)
veicoli = {m: sorted(v) for m, v in sorted(veicoli.items())}
blob = json.dumps(veicoli, ensure_ascii=False, separators=(",", ":"))
modello_html = (KIT / "index.template.html").read_text(encoding="utf-8")
(KIT / "index.html").write_text(modello_html.replace("/*__VEICOLI__*/{}", blob), encoding="utf-8")
print(f"kit-gomma-ruota: {len(veicoli)} marche, {sum(len(v) for v in veicoli.values())} modelli")
