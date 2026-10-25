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
- `index.html` scritto a mano (nessun dato incorporato, niente build).
- `kit.webp`: foto del kit Davinci scontornata (ruota che gira scorrendo la pagina).
- Richiesta kit guidata (vettura, misura, invernale/4 stagioni, TPMS, quantità) → messaggio WhatsApp già scritto.
- Conto alla rovescia al 31/12; a promo finita diventa «Chiedimi le offerte attive».
- Anteprima: `_build/anteprima-kit-gomma-ruota.html` → `anteprima.jpg` (Chrome senza finestra, 1200×630).
