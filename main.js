document.getElementById('yr').textContent = new Date().getFullYear();
(function(){
  // Every language has its own static page (/, /en/, /de/ …). Nothing is translated in the
  // browser and nobody is redirected automatically: the switcher navigates, and a visitor
  // whose browser language differs from the page gets a one-line offer they can dismiss.
  var SUPPORTED = ["sv","en","de","fr","es","it","nl","pl","da","nb","fi","pt"];
  var BAR = {
    "sv": {"bar": "Den här sidan finns också på svenska.", "bar_btn": "Visa på svenska"},
    "en": {"bar": "This page is also available in English.", "bar_btn": "Switch to English"},
    "de": {"bar": "Diese Seite gibt es auch auf Deutsch.", "bar_btn": "Auf Deutsch anzeigen"},
    "fr": {"bar": "Cette page existe aussi en français.", "bar_btn": "Afficher en français"},
    "es": {"bar": "Esta página también está disponible en español.", "bar_btn": "Ver en español"},
    "it": {"bar": "Questa pagina è disponibile anche in italiano.", "bar_btn": "Mostra in italiano"},
    "nl": {"bar": "Deze pagina is ook beschikbaar in het Nederlands.", "bar_btn": "Toon in het Nederlands"},
    "pl": {"bar": "Ta strona jest dostępna również po polsku.", "bar_btn": "Pokaż po polsku"},
    "da": {"bar": "Denne side findes også på dansk.", "bar_btn": "Vis på dansk"},
    "nb": {"bar": "Denne siden finnes også på norsk.", "bar_btn": "Vis på norsk"},
    "fi": {"bar": "Tämä sivu on saatavilla myös suomeksi.", "bar_btn": "Näytä suomeksi"},
    "pt": {"bar": "Esta página também está disponível em português.", "bar_btn": "Mostrar em português"}
  };
  var pageLang = (document.documentElement.lang || "sv").split("-")[0];
  function pathFor(l){ return l === "sv" ? "/" : "/" + l + "/"; }
  function detect(){
    var langs = navigator.languages || [navigator.language || "en"];
    for (var i = 0; i < langs.length; i++) {
      var code = (langs[i] || "").toLowerCase().split("-")[0];
      if (code === "no") code = "nb";
      if (SUPPORTED.indexOf(code) >= 0) return code;
    }
    return "en";
  }
  function store(k, v){ try { localStorage.setItem(k, v); } catch(e){} }
  function read(k){ try { return localStorage.getItem(k); } catch(e){ return null; } }

  var sel = document.getElementById("langsel");
  if (sel) {
    sel.value = pageLang;
    sel.addEventListener("change", function(e){ store("cibello-lang", e.target.value); location.href = pathFor(e.target.value); });
  }

  var bar = document.getElementById("langbar");
  var detected = detect();
  var chosen = read("cibello-lang");
  var wanted = (chosen && SUPPORTED.indexOf(chosen) >= 0) ? chosen : detected;
  if (bar && wanted !== pageLang && BAR[wanted] && read("cibello-lang-dismissed") !== wanted) {
    document.getElementById("langbar-text").textContent = BAR[wanted].bar;
    var btn = document.getElementById("langbar-btn");
    btn.textContent = BAR[wanted].bar_btn;
    btn.addEventListener("click", function(){ store("cibello-lang", wanted); location.href = pathFor(wanted); });
    document.getElementById("langbar-close").addEventListener("click", function(){ bar.hidden = true; store("cibello-lang-dismissed", wanted); });
    bar.hidden = false;
  }

  var mb = document.querySelector(".menu-btn"), mn = document.getElementById("mobilenav");
  if (mb && mn) {
    mb.addEventListener("click", function(){ var open = mb.getAttribute("aria-expanded") === "true"; mb.setAttribute("aria-expanded", String(!open)); mn.hidden = open; });
    mn.querySelectorAll("a").forEach(function(a){ a.addEventListener("click", function(){ mb.setAttribute("aria-expanded", "false"); mn.hidden = true; }); });
  }

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, {threshold: .12});
    document.querySelectorAll(".reveal").forEach(function(el){ io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function(el){ el.classList.add("in"); });
  }
})();
