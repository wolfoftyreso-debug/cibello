// Middagsväljaren på /vad-ska-jag-ata-till-middag/ – slumpar en rätt utifrån valda filter.
(function(){
  var D = [
    // [namn, protein, tid(min), taggar]
    ["Pasta med tomatsås och bönor","vego",20,["skafferi","billig","barn"]],
    ["Krämig kycklinggryta med svamp","kyckling",30,["barn","rester"]],
    ["Omelett med rester av grönsaker","vego",15,["rester","billig","snabb"]],
    ["Wok med nudlar och det som finns i kylen","valfritt",20,["rester","snabb"]],
    ["Tacos med färs eller bönor","valfritt",20,["barn","fredag"]],
    ["Linssoppa med bröd","vego",30,["skafferi","billig","matlåda"]],
    ["Ugnsbakad lax med potatis och citron","fisk",25,["snabb"]],
    ["Kycklingcurry med kokosmjölk och ris","kyckling",30,["matlåda","rester"]],
    ["Pannkakor med ärtor eller bacon","vego",25,["barn","billig"]],
    ["Köttbullar med potatismos","kött",30,["barn"]],
    ["Ugnsplåt med korv och rotfrukter","kött",30,["billig","barn"]],
    ["Fiskgratäng med dill och purjolök","fisk",35,["barn"]],
    ["Chili sin carne","vego",30,["skafferi","matlåda","billig"]],
    ["Pasta carbonara","kött",20,["snabb","barn"]],
    ["Halloumi- eller kycklingsallad med bulgur","valfritt",20,["snabb","matlåda"]],
    ["Pytt i panna på rester","valfritt",20,["rester","billig"]],
    ["Tomatsoppa med grillade ostmackor","vego",25,["barn","billig"]],
    ["Kycklingwraps med yoghurtsås","kyckling",20,["snabb","barn"]],
    ["Lasagne (dubbel sats till matlådor)","kött",60,["matlåda","barn"]],
    ["Ris med ägg och grönsaker (fried rice)","vego",15,["rester","snabb","billig"]],
    ["Fisksoppa med saffran","fisk",30,["fredag"]],
    ["Kikärtsgryta med spenat och yoghurt","vego",25,["skafferi","billig"]],
    ["Pastagratäng med broccoli och ost","vego",35,["barn","matlåda"]],
    ["Hamburgare med hemgjorda klyftpotatis","kött",35,["fredag","barn"]],
    ["Räkpasta med citron och vitlök","fisk",20,["snabb","fredag"]],
    ["Korvstroganoff med ris","kött",25,["barn","billig","snabb"]],
    ["Tortillapizza med det som finns","valfritt",15,["rester","snabb","barn"]],
    ["Ugnsbakad kyckling med rotfrukter","kyckling",45,["helg"]],
    ["Falafel i pitabröd","vego",20,["snabb","billig"]],
    ["Laxpoké med ris och avokado","fisk",20,["snabb"]],
    ["Bönbiffar med potatis","vego",30,["billig","barn"]],
    ["Pasta pesto med kyckling","kyckling",15,["snabb","barn"]],
    ["Gulaschsoppa","kött",45,["matlåda","helg"]],
    ["Tonfiskpasta","fisk",15,["skafferi","snabb","billig"]],
    ["Sushi- eller bowl-kväll med det som finns","valfritt",30,["fredag"]],
    ["Ugnsomelett med potatis och ost","vego",30,["rester","billig"]],
    ["Kycklingnudelsoppa","kyckling",25,["rester","snabb"]],
    ["Pulled pork eller pulled jackfruit i bröd","valfritt",40,["helg","fredag"]],
    ["Grönsakslasagne","vego",50,["matlåda","helg"]],
    ["Torsk med äggsås och potatis","fisk",25,["barn"]],
  ];
  var form = document.getElementById("middagsval");
  if (!form) return;
  var out = document.getElementById("middag-ut"), btn = document.getElementById("middag-knapp");
  var last = null;
  function pick(){
    var p = form.protein.value, t = parseInt(form.tid.value, 10), tag = form.tag.value;
    var list = D.filter(function(d){
      return (p === "valfritt" || d[1] === p || d[1] === "valfritt") && d[2] <= t && (tag === "alla" || d[3].indexOf(tag) >= 0);
    });
    if (!list.length) { out.innerHTML = "<p>Inget matchade. Prova att lätta på ett filter.</p>"; return; }
    var c; do { c = list[Math.floor(Math.random()*list.length)]; } while (list.length > 1 && c === last);
    last = c;
    out.innerHTML = '<p class="middag-namn">' + c[0] + '</p><p class="middag-meta">Ca ' + c[2] + ' min · ' + (c[1] === "valfritt" ? "valfritt protein" : c[1]) + '</p><p class="middag-tips">Har du det hemma? Cibello ser det i ditt matlager och föreslår rätter som passar det du faktiskt har.</p>';
    out.hidden = false;
    out.focus();
  }
  btn.addEventListener("click", pick);
  form.addEventListener("submit", function(e){ e.preventDefault(); pick(); });
})();
