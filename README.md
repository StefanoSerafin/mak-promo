# mak-promo — locandine interattive

Versione web delle locandine promo: una cartella per campagna, pubblicata su GitHub Pages
(`stefanoserafin.github.io/mak-promo/<campagna>/`). Il link si manda su WhatsApp al posto
dell'immagine: l'anteprima mostra la locandina (`anteprima.jpg`, 1200×630, tag `og:image`),
il tocco apre la pagina con bottoni e ricerca.

## halloween-ruotino (25 ott – 1 nov 2026)

- `locandina.jpg`: la locandina originale (estratta dal PDF sulla Scrivania).
- `index.template.html`: la pagina da modificare a mano; `index.html` si genera.
- Ricerca vettura → ruotino dai dati del configuratore NPK (`../noproblemkit/dati/ruotini.csv`).
- In promo = ruotino in acciaio fino a 17" (regola in `PROMO` dentro la pagina).
- Bottone WhatsApp con l'ordine già scritto, conto alla rovescia, chiamata, B2B.

Rigenera: `python3 _build/build.py`

## kit-gomma-ruota (stagione invernale, montaggio gratuito fino al 31/12/2026)

- `locandina.jpg`: la locandina con il flash, da `../Locandine/kit-gomma-ruota-inverno/locandina-flash.html`.
- `index.template.html` da modificare a mano; `index.html` lo genera `_build/build.py` con dentro marche e modelli del configuratore NPK (`../noproblemkit/dati/veicoli.csv`).
- `kit.webp`: foto del kit Davinci scontornata (ruota che gira scorrendo la pagina).
- Richiesta kit guidata: foto del libretto oppure marca → modello → anno, misura, preferenze ruota (silver, nero, diamantato, prezzo promo; anche più di una), invernale/4 stagioni, TPMS, quantità → messaggio WhatsApp già scritto.
- Con il libretto il bottone verde apre il menu Condividi (foto + testo, poi WhatsApp e Stefano); dove non si possono condividere file apre la chat e chiede di allegarlo. La foto non passa da nessun server.
- Barra fissa in alto «Vuoi un preventivo? Compila la richiesta» che porta al form e sparisce quando lo si raggiunge.
- Conto alla rovescia al 31/12 in fondo alla pagina; a promo finita diventa «Chiedimi le offerte attive».
- Anteprima: `_build/anteprima-kit-gomma-ruota.html` → `anteprima.jpg` (Chrome senza finestra, 1200×630).

## prossima-fermata-futuro (storia sull'IA, senza scadenza)

- Storia in 8 scene: il treno «Intelligenza Artificiale», chi sale e chi resta sulla banchina; le stazioni cambiano nome (Futuro → Presente → Passato).
- Disegni SVG generati da `../Locandine/prossima-fermata-futuro/scene.py`; `build.py` nella stessa cartella scrive la locandina (clienti e colleghi) e `index.html` da `index.template.html` (le scene vanno al posto di `<!--__SCENE__-->`).
- Visore a storie: tocco a destra/sinistra, swipe, frecce; tabellone a palette nella scena 5, braccio animato nelle scene 6-7. Niente conto alla rovescia.
- Anteprima: `../Locandine/prossima-fermata-futuro/anteprima.html` → `anteprima.jpg`.

## fix-pack (Fix Pack 2026, 154,00 €, senza scadenza)

- `locandina.jpg`: la locandina ricevuta (853×1280, da Downloads il 2026-10-26).
- `index.html` scritto a mano (nessun dato incorporato): i 7 kit della locandina sono in `KIT` dentro la pagina, codici verificati sul database ordini.
- Schede dei kit da toccare per aggiungerli; ordine a righe (menu codice + quantità + togli), «+ Aggiungi riga», «+ Fix Pack completo», nome officina facoltativo → messaggio WhatsApp con codici e quantità.
- Niente conto alla rovescia (la locandina non ha scadenza). Barra in alto che porta all'ordine.
- Anteprima: `_build/anteprima-fix-pack.html` → `anteprima.jpg`; icona da `_build/icona-fix-pack.html`.

## refill-multisens (Refill 20 MATE MULTIsens MP6, 15,90 € cad. + IVA, senza scadenza)

- `locandina.jpg`: da `../Locandine/refill-multisens/locandina.html` (PNG/PDF clienti e colleghi nella stessa cartella).
- `index.html` scritto a mano: tre righe fisse (930000MP6R Rubber, 93000MP6BM Metal Black, 930000MP6M Silver) con il campo pezzi, barra verso i 20 minimi (anche misti), totale indicativo a 20,40 € sotto il minimo e a 15,90 € da 20 in su, risparmio, messaggio WhatsApp con codici e pezzi.
- Foto: sensori ritagliati dallo screenshot B2B, MA41 da `Video Avatar/Immagini/MATE/MATE MA41.png`, scontornati con `../Locandine/refill-multisens/scontorna.py`.
- Anteprima: `_build/anteprima-refill-multisens.html`; icona: `_build/icona-refill-multisens.html`.
