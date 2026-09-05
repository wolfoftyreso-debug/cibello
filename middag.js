// Middagsväljaren / dinner picker. Reads dishes and labels from <script type="application/json" id="middag-data">
// when present (localized pages); falls back to the Swedish built-in list.
(function(){
  var form = document.getElementById("middagsval");
  if (!form) return;
  var data = null;
  var el = document.getElementById("middag-data");
  if (el) { try { data = JSON.parse(el.textContent); } catch (e) { data = null; } }
  var SV = {
    minutes: "min", any_protein: "valfritt protein",
    no_match: "Inget matchade. Prova att lätta på ett filter.",
    tip: "Har du det hemma? Cibello ser det i ditt matlager och föreslår rätter som passar det du faktiskt har.",
    protein_names: {"chicken":"kyckling","meat":"kött","fish":"fisk","veg":"vegetariskt"},
    dishes: [
      ["Pasta med tomatsås och bönor","veg",20,["pantry","budget","kids"]],
      ["Krämig kycklinggryta med svamp","chicken",30,["kids","leftovers"]],
      ["Omelett med rester av grönsaker","veg",15,["leftovers","budget","quick"]],
      ["Wok med nudlar och det som finns i kylen","any",20,["leftovers","quick"]],
      ["Tacos med färs eller bönor","any",20,["kids","friday"]],
      ["Linssoppa med bröd","veg",30,["pantry","budget","mealbox"]],
      ["Ugnsbakad lax med potatis och citron","fish",25,["quick"]],
      ["Kycklingcurry med kokosmjölk och ris","chicken",30,["mealbox","leftovers"]],
      ["Pannkakor med ärtor eller bacon","veg",25,["kids","budget"]],
      ["Köttbullar med potatismos","meat",30,["kids"]],
      ["Ugnsplåt med korv och rotfrukter","meat",30,["budget","kids"]],
      ["Fiskgratäng med dill och purjolök","fish",35,["kids"]],
      ["Chili sin carne","veg",30,["pantry","mealbox","budget"]],
      ["Pasta carbonara","meat",20,["quick","kids"]],
      ["Halloumi- eller kycklingsallad med bulgur","any",20,["quick","mealbox"]],
      ["Pytt i panna på rester","any",20,["leftovers","budget"]],
      ["Tomatsoppa med grillade ostmackor","veg",25,["kids","budget"]],
      ["Kycklingwraps med yoghurtsås","chicken",20,["quick","kids"]],
      ["Lasagne (dubbel sats till matlådor)","meat",60,["mealbox","kids"]],
      ["Ris med ägg och grönsaker (fried rice)","veg",15,["leftovers","quick","budget"]],
      ["Fisksoppa med saffran","fish",30,["friday"]],
      ["Kikärtsgryta med spenat och yoghurt","veg",25,["pantry","budget"]],
      ["Pastagratäng med broccoli och ost","veg",35,["kids","mealbox"]],
      ["Hamburgare med hemgjorda klyftpotatis","meat",35,["friday","kids"]],
      ["Räkpasta med citron och vitlök","fish",20,["quick","friday"]],
      ["Korvstroganoff med ris","meat",25,["kids","budget","quick"]],
      ["Tortillapizza med det som finns","any",15,["leftovers","quick","kids"]],
      ["Ugnsbakad kyckling med rotfrukter","chicken",45,["friday"]],
      ["Falafel i pitabröd","veg",20,["quick","budget"]],
      ["Laxpoké med ris och avokado","fish",20,["quick"]],
      ["Bönbiffar med potatis","veg",30,["budget","kids"]],
      ["Pasta pesto med kyckling","chicken",15,["quick","kids"]],
      ["Gulaschsoppa","meat",45,["mealbox","friday"]],
      ["Tonfiskpasta","fish",15,["pantry","quick","budget"]],
      ["Sushi- eller bowl-kväll med det som finns","any",30,["friday"]],
      ["Ugnsomelett med potatis och ost","veg",30,["leftovers","budget"]],
      ["Kycklingnudelsoppa","chicken",25,["leftovers","quick"]],
      ["Pulled pork eller pulled jackfruit i bröd","any",40,["friday"]],
      ["Grönsakslasagne","veg",50,["mealbox","friday"]],
      ["Torsk med äggsås och potatis","fish",25,["kids"]]
    ]
  };
  var T = data || SV;
  var D = T.dishes;
  var out = document.getElementById("middag-ut"), btn = document.getElementById("middag-knapp");
  var last = null;
  function pick(){
    var p = form.protein.value, t = parseInt(form.tid.value, 10), tag = form.tag.value;
    var list = D.filter(function(d){
      return (p === "any" || d[1] === p || d[1] === "any") && d[2] <= t && (tag === "all" || d[3].indexOf(tag) >= 0);
    });
    if (!list.length) { out.innerHTML = "<p>" + T.no_match + "</p>"; out.hidden = false; return; }
    var c; do { c = list[Math.floor(Math.random()*list.length)]; } while (list.length > 1 && c === last);
    last = c;
    var prot = c[1] === "any" ? T.any_protein : (T.protein_names[c[1]] || c[1]);
    out.innerHTML = '<p class="middag-namn">' + c[0] + '</p><p class="middag-meta">~' + c[2] + ' ' + T.minutes + ' · ' + prot + '</p><p class="middag-tips">' + T.tip + '</p>';
    out.hidden = false;
    out.focus();
  }
  btn.addEventListener("click", pick);
  form.addEventListener("submit", function(e){ e.preventDefault(); pick(); });
})();
