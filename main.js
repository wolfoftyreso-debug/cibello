document.getElementById('yr').textContent = new Date().getFullYear();
  var BAR = {"en": {"bar": "This page is also available in English.", "bar_btn": "Switch to English"}, "de": {"bar": "Diese Seite gibt es auch auf Deutsch.", "bar_btn": "Auf Deutsch anzeigen"}, "fr": {"bar": "Cette page existe aussi en français.", "bar_btn": "Afficher en français"}, "es": {"bar": "Esta página también está disponible en español.", "bar_btn": "Ver en español"}, "it": {"bar": "Questa pagina è disponibile anche in italiano.", "bar_btn": "Mostra in italiano"}, "nl": {"bar": "Deze pagina is ook beschikbaar in het Nederlands.", "bar_btn": "Toon in het Nederlands"}, "pl": {"bar": "Ta strona jest dostępna również po polsku.", "bar_btn": "Pokaż po polsku"}, "da": {"bar": "Denne side findes også på dansk.", "bar_btn": "Vis på dansk"}, "nb": {"bar": "Denne siden finnes også på norsk.", "bar_btn": "Vis på norsk"}, "fi": {"bar": "Tämä sivu on saatavilla myös suomeksi.", "bar_btn": "Näytä suomeksi"}, "pt": {"bar": "Esta página também está disponível em português.", "bar_btn": "Mostrar em português"}};
  var I18N = null;
  function withDict(cb){
    if (I18N) return cb(I18N);
    if (window.CIBELLO_I18N) { I18N = window.CIBELLO_I18N; return cb(I18N); }
    var s = document.createElement("script"); s.src = "/i18n.js"; s.async = true;
    s.onload = function(){ I18N = window.CIBELLO_I18N || {}; cb(I18N); };
    document.head.appendChild(s);
  }
  var SUPPORTED = ["sv","en","de","fr","es","it","nl","pl","da","nb","fi","pt"];
  function detect(){
    var langs = navigator.languages || [navigator.language || "en"];
    for (var i=0;i<langs.length;i++){
      var code = (langs[i]||"").toLowerCase().split("-")[0];
      if (code==="no") code="nb";
      if (SUPPORTED.indexOf(code)>=0) return code;
    }
    return "en"; // fallback för icke-stödda språk
  }
  // Snapshot the original Swedish markup so we can always restore it (sv-dict är tom).
  var ORIG = new Map();
  document.querySelectorAll("[data-i18n]").forEach(function(el){
    ORIG.set(el, el.tagName==="META" ? el.getAttribute("content") : el.textContent);
  });
  function apply(lang){
    if (lang !== "sv" && !I18N) { return withDict(function(){ apply(lang); }); }
    var dict = (I18N && I18N[lang]) || {};
    document.documentElement.lang = lang;
    document.querySelectorAll("[data-i18n]").forEach(function(el){
      var k = el.getAttribute("data-i18n");
      // översatt sträng om den finns, annars original svensk markup (gäller sv + ev. saknad nyckel)
      var v = (dict[k]!==undefined) ? dict[k] : ORIG.get(el);
      if (v==null) return;
      if (el.tagName==="META"){ el.setAttribute("content", v); } else { el.textContent = v; }
    });
    document.querySelectorAll("[data-href-en]").forEach(function(a){ a.setAttribute("href", lang === "sv" ? a.getAttribute("data-href-sv") || a.getAttribute("href") : a.getAttribute("data-href-en")); if(!a.getAttribute("data-href-sv")) a.setAttribute("data-href-sv", "/basta-matapp/"); });
    document.getElementById("langsel").value = lang;
  }
  // SEO: the page is served in Swedish and never auto-translated on load (crawlers render
  // with an English locale). A visitor who has chosen a language before gets it back;
  // everyone else with a supported browser language gets a one-line offer instead.
  function store(lang){ try { localStorage.setItem("cibello-lang", lang); } catch(e){} }
  var saved = null; try { saved = localStorage.getItem("cibello-lang"); } catch(e){}
  var detected = detect();
  if (saved && SUPPORTED.indexOf(saved) >= 0) {
    apply(saved);
  } else if (detected !== "sv" && BAR[detected]) {
    var bar = document.getElementById("langbar");
    document.getElementById("langbar-text").textContent = BAR[detected].bar;
    var btn = document.getElementById("langbar-btn");
    btn.textContent = BAR[detected].bar_btn;
    btn.addEventListener("click", function(){ apply(detected); store(detected); bar.hidden = true; });
    document.getElementById("langbar-close").addEventListener("click", function(){ bar.hidden = true; store("sv"); });
    bar.hidden = false;
  }
  document.getElementById("langsel").addEventListener("change", function(e){ apply(e.target.value); store(e.target.value); });

  var mb = document.querySelector(".menu-btn"), mn = document.getElementById("mobilenav");
  if (mb && mn) {
    mb.addEventListener("click", function(){ var open = mb.getAttribute("aria-expanded") === "true"; mb.setAttribute("aria-expanded", String(!open)); mn.hidden = open; });
    mn.querySelectorAll("a").forEach(function(a){ a.addEventListener("click", function(){ mb.setAttribute("aria-expanded","false"); mn.hidden = true; }); });
  }

  var io = new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target);}});},{threshold:.12});
  document.querySelectorAll(".reveal").forEach(function(el){io.observe(el);});
