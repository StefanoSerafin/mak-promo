/* conta.js — conteggio anonimo delle locandine interattive (mak-promo).
 * Manda al Worker mak-promo-conta: apertura, tocchi su WhatsApp / Chiama / B2B / mail, ricerche.
 * Niente cookie, niente localStorage, niente dati del cliente: dal messaggio WhatsApp partono
 * solo le righe d'ordine («•», «Totale») e quelle tecniche dell'assistenza (strumento, vettura, richiesta).
 * Le pagine agganciano le ricerche con:  window.conta && window.conta("ricerca", "205/55 R16")
 * La pagina elenco di un collega include lo script con  data-elenco  (campagna «_elenco»).
 * Se qualcosa va storto non succede niente: la pagina funziona lo stesso.
 */
(function () {
  var ENDPOINT = "https://mak-promo-conta.serafin-stefano72.workers.dev/e";
  var me = document.currentScript;
  var elenco = !!(me && me.hasAttribute("data-elenco"));

  // /mak-promo/<campagna>/  oppure  /mak-promo/<agente>/<campagna>/  oppure  /mak-promo/<agente>/ (elenco)
  var parti = location.pathname.replace(/^\/mak-promo\/?/, "").split("/").filter(function (p) { return p && p.indexOf(".") < 0; });
  var agente = "stefano", campagna = "";
  if (elenco) { agente = parti[0] || "stefano"; campagna = "_elenco"; }
  else if (parti.length >= 2) { agente = parti[0]; campagna = parti[1]; }
  else { campagna = parti[0] || ""; }
  if (!/^[a-z0-9_-]{2,40}$/.test(campagna)) return;

  function invia(t, d) {
    try {
      var corpo = JSON.stringify({ c: campagna, a: agente, t: t, d: d == null ? undefined : String(d).slice(0, 500) });
      if (navigator.sendBeacon && navigator.sendBeacon(ENDPOINT, corpo)) return;
      fetch(ENDPOINT, { method: "POST", body: corpo, keepalive: true, mode: "no-cors" }).catch(function () {});
    } catch (e) {}
  }

  var TENGO = /^(•|Totale|Strumento:|Vettura:|Mi serve aiuto per:)/;
  function righeOrdine(href) {
    try {
      var testo = new URL(href).searchParams.get("text") || "";
      var r = testo.split("\n").map(function (x) { return x.trim(); }).filter(function (x) { return TENGO.test(x); });
      return r.length ? r.join("\n") : null;
    } catch (e) { return null; }
  }

  var ultima = "";
  window.conta = function (t, d) {
    if (t === "ricerca") {
      d = String(d || "").trim().slice(0, 200);
      if (!d || d === ultima) return;
      ultima = d;
    }
    invia(t, d);
  };

  invia("apertura");

  document.addEventListener("click", function (e) {
    try {
      var a = e.target && e.target.closest ? e.target.closest("a[href]") : null;
      if (!a) return;
      var h = a.href || "";
      if (h.indexOf("wa.me/") >= 0 || h.indexOf("api.whatsapp.com") >= 0) invia("whatsapp", righeOrdine(h));
      else if (h.indexOf("tel:") === 0) invia("chiama");
      else if (h.indexOf("b2bshop.makwheels.it") >= 0) invia("b2b");
      else if (h.indexOf("mailto:") === 0) invia("mail");
    } catch (err) {}
  }, true);
})();
