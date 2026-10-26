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
