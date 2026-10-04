import type { CookEntry, DayKey, PantryItem, Protein, Recipe } from "./types";

export const DAYS: { key: DayKey; label: string; short: string }[] = [
  { key: "mon", label: "Måndag", short: "Mån" },
  { key: "tue", label: "Tisdag", short: "Tis" },
  { key: "wed", label: "Onsdag", short: "Ons" },
  { key: "thu", label: "Torsdag", short: "Tor" },
  { key: "fri", label: "Fredag", short: "Fre" },
  { key: "sat", label: "Lördag", short: "Lör" },
  { key: "sun", label: "Söndag", short: "Sön" },
];

export const PROTEIN_LABEL: Record<Protein, string> = {
  chicken: "kyckling",
  meat: "kött",
  fish: "fisk",
  veg: "vegetariskt",
  any: "valfritt protein",
};

export const LOCATION_LABEL = {
  kyl: "Kyl",
  skafferi: "Skafferi",
  frys: "Frys",
} as const;

export const MEAL_CHIPS: { id: "all" | Recipe["meal"]; label: string }[] = [
  { id: "all", label: "Rekommenderat" },
  { id: "frukost", label: "Frukost" },
  { id: "lunch", label: "Lunch" },
  { id: "middag", label: "Middag" },
  { id: "mellanmal", label: "Mellanmål" },
  { id: "efterratt", label: "Efterrätt" },
  { id: "baka", label: "Baka" },
];

export function daysFromNow(n: number): string {
  const d = new Date();
  d.setDate(d.getDate() + n);
  return d.toISOString().slice(0, 10);
}

export function daysUntil(iso: string): number {
  const a = new Date();
  a.setHours(0, 0, 0, 0);
  const b = new Date(iso + "T00:00:00");
  return Math.round((b.getTime() - a.getTime()) / 86400000);
}

export function uid(prefix = "id"): string {
  return `${prefix}-${Math.random().toString(36).slice(2, 9)}`;
}

export function seedPantry(): PantryItem[] {
  const items: Array<Omit<PantryItem, "id">> = [
    { key: "kyckling", name: "Kycklingfilé", location: "kyl", qty: "600 g", expires: daysFromNow(2) },
    { key: "gradde", name: "Vispgrädde", location: "kyl", qty: "4 dl", expires: daysFromNow(3) },
    { key: "svamp", name: "Champinjoner", location: "kyl", qty: "250 g", expires: daysFromNow(1) },
    { key: "lok", name: "Gul lök", location: "skafferi", qty: "4 st", expires: daysFromNow(18) },
    { key: "vitlok", name: "Vitlök", location: "skafferi", qty: "1 knippe", expires: daysFromNow(21) },
    { key: "pasta", name: "Pasta", location: "skafferi", qty: "500 g", expires: daysFromNow(180) },
    { key: "tomat", name: "Krossade tomater", location: "skafferi", qty: "2 burkar", expires: daysFromNow(240) },
    { key: "bonor", name: "Svarta bönor", location: "skafferi", qty: "1 burk", expires: daysFromNow(200) },
    { key: "agg", name: "Ägg", location: "kyl", qty: "10 st", expires: daysFromNow(12) },
    { key: "ost", name: "Prästost", location: "kyl", qty: "250 g", expires: daysFromNow(9) },
    { key: "mjolk", name: "Mjölk", location: "kyl", qty: "1 l", expires: daysFromNow(4) },
    { key: "smor", name: "Smör", location: "kyl", qty: "250 g", expires: daysFromNow(30) },
    { key: "potatis", name: "Potatis", location: "skafferi", qty: "1.5 kg", expires: daysFromNow(14) },
    { key: "morot", name: "Morötter", location: "kyl", qty: "6 st", expires: daysFromNow(8) },
    { key: "broccoli", name: "Broccoli", location: "kyl", qty: "1 st", expires: daysFromNow(2) },
    { key: "ris", name: "Jasminris", location: "skafferi", qty: "1 kg", expires: daysFromNow(200) },
    { key: "citron", name: "Citron", location: "kyl", qty: "3 st", expires: daysFromNow(10) },
    { key: "yoghurt", name: "Naturell yoghurt", location: "kyl", qty: "500 g", expires: daysFromNow(5) },
    { key: "brod", name: "Surdegsbröd", location: "skafferi", qty: "1 limpa", expires: daysFromNow(3) },
    { key: "olja", name: "Olivolja", location: "skafferi", qty: "1 flaska", expires: daysFromNow(300) },
    { key: "kokos", name: "Kokosmjölk", location: "skafferi", qty: "1 burk", expires: daysFromNow(220) },
    { key: "spenat", name: "Babyspenat", location: "kyl", qty: "75 g", expires: daysFromNow(2) },
    { key: "kikartor", name: "Kikärtor", location: "skafferi", qty: "1 burk", expires: daysFromNow(180) },
    { key: "lax", name: "Laxfilé", location: "frys", qty: "400 g", expires: daysFromNow(60) },
    { key: "fars", name: "Köttfärs", location: "frys", qty: "500 g", expires: daysFromNow(45) },
    { key: "nudlar", name: "Äggnudlar", location: "skafferi", qty: "300 g", expires: daysFromNow(150) },
    { key: "soja", name: "Soja", location: "skafferi", qty: "1 flaska", expires: daysFromNow(400) },
  ];
  return items.map((item) => ({ ...item, id: uid("p") }));
}

export const SCAN_BATCH: Array<Omit<PantryItem, "id">> = [
  { key: "paprika", name: "Paprika", location: "kyl", qty: "2 st", expires: daysFromNow(6) },
  { key: "gurka", name: "Gurka", location: "kyl", qty: "1 st", expires: daysFromNow(5) },
  { key: "tonfisk", name: "Tonfisk i vatten", location: "skafferi", qty: "2 burkar", expires: daysFromNow(360) },
  { key: "halloumi", name: "Halloumi", location: "kyl", qty: "200 g", expires: daysFromNow(7) },
  { key: "avokado", name: "Avokado", location: "kyl", qty: "2 st", expires: daysFromNow(3) },
];

export const RECIPES: Recipe[] = [
  {
    id: "kycklinggryta",
    title: "Krämig kycklinggryta med svamp",
    time: 30,
    protein: "chicken",
    tags: ["kids", "leftovers"],
    meal: "middag",
    rating: 4.8,
    ratings: 132,
    ingredients: [
      { key: "kyckling", name: "Kycklingfilé", amount: "500 g" },
      { key: "svamp", name: "Champinjoner", amount: "250 g" },
      { key: "gradde", name: "Vispgrädde", amount: "3 dl" },
      { key: "lok", name: "Gul lök", amount: "1 st" },
      { key: "ris", name: "Ris", amount: "3 dl" },
    ],
    steps: [
      "Bryt svampen och skiva löken. Bryn kycklingen i smör tills den fått färg.",
      "Tillsätt svamp och lök. Häll på grädde, sjud 12 minuter.",
      "Koka ris parallellt. Smaka av med salt, peppar och en skvätt citron.",
    ],
  },
  {
    id: "pasta-bonor",
    title: "Pasta med tomatsås och bönor",
    time: 20,
    protein: "veg",
    tags: ["pantry", "budget", "kids"],
    meal: "middag",
    rating: 4.5,
    ratings: 88,
    ingredients: [
      { key: "pasta", name: "Pasta", amount: "400 g" },
      { key: "tomat", name: "Krossade tomater", amount: "1 burk" },
      { key: "bonor", name: "Svarta bönor", amount: "1 burk" },
      { key: "vitlok", name: "Vitlök", amount: "2 klyftor" },
      { key: "olja", name: "Olivolja", amount: "2 msk" },
    ],
    steps: [
      "Koka pastan enligt förpackningen.",
      "Fräs vitlök i olja, häll på tomater och bönor. Sjud 10 minuter.",
      "Blanda med pastan. Riv ost över om du har.",
    ],
  },
  {
    id: "omelett",
    title: "Omelett med rester av grönsaker",
    time: 15,
    protein: "veg",
    tags: ["leftovers", "budget", "quick"],
    meal: "lunch",
    rating: 4.6,
    ratings: 64,
    ingredients: [
      { key: "agg", name: "Ägg", amount: "4 st" },
      { key: "mjolk", name: "Mjölk", amount: "0.5 dl" },
      { key: "ost", name: "Ost", amount: "en näve" },
      { key: "broccoli", name: "Broccoli eller spenat", amount: "en näve" },
      { key: "smor", name: "Smör", amount: "1 msk" },
    ],
    steps: [
      "Vispa ägg med mjölk, salt och peppar.",
      "Fräs grönsaker snabbt i smör. Häll över äggen.",
      "Strö ost, vik ihop när den stelnat.",
    ],
  },
  {
    id: "wok",
    title: "Wok med nudlar och det som finns i kylen",
    time: 20,
    protein: "any",
    tags: ["leftovers", "quick"],
    meal: "middag",
    rating: 4.4,
    ratings: 71,
    ingredients: [
      { key: "nudlar", name: "Nudlar", amount: "200 g" },
      { key: "soja", name: "Soja", amount: "2 msk" },
      { key: "lok", name: "Lök", amount: "1 st" },
      { key: "morot", name: "Morot", amount: "2 st" },
      { key: "kyckling", name: "Kyckling eller tofu", amount: "300 g" },
    ],
    steps: [
      "Koka nudlarna kort, skölj kallt.",
      "Woka protein och grönsaker hett. Tillsätt soja.",
      "Vänd ner nudlarna. Kläm citron över.",
    ],
  },
  {
    id: "lax-ugn",
    title: "Ugnsbakad lax med potatis och citron",
    time: 25,
    protein: "fish",
    tags: ["quick"],
    meal: "middag",
    rating: 4.7,
    ratings: 101,
    ingredients: [
      { key: "lax", name: "Laxfilé", amount: "400 g" },
      { key: "potatis", name: "Potatis", amount: "800 g" },
      { key: "citron", name: "Citron", amount: "1 st" },
      { key: "olja", name: "Olivolja", amount: "2 msk" },
    ],
    steps: [
      "Koka potatisen nästan mjuk. Lägg i ugnsform med lax.",
      "Pressa citron, ringla olja, salta. 200° i 12–15 min.",
    ],
  },
  {
    id: "curry",
    title: "Kycklingcurry med kokosmjölk och ris",
    time: 30,
    protein: "chicken",
    tags: ["mealbox", "leftovers"],
    meal: "middag",
    rating: 4.8,
    ratings: 156,
    ingredients: [
      { key: "kyckling", name: "Kycklingfilé", amount: "500 g" },
      { key: "kokos", name: "Kokosmjölk", amount: "1 burk" },
      { key: "lok", name: "Lök", amount: "1 st" },
      { key: "ris", name: "Ris", amount: "3 dl" },
      { key: "spenat", name: "Spenat", amount: "en näve" },
    ],
    steps: [
      "Bryn kyckling och lök. Häll på kokosmjölk och en nypa curry.",
      "Sjud 15 minuter. Vänd i spenat sista minuten. Servera med ris.",
    ],
  },
  {
    id: "kikartsgryta",
    title: "Kikärtsgryta med spenat och yoghurt",
    time: 25,
    protein: "veg",
    tags: ["pantry", "budget"],
    meal: "middag",
    rating: 4.5,
    ratings: 77,
    ingredients: [
      { key: "kikartor", name: "Kikärtor", amount: "1 burk" },
      { key: "tomat", name: "Krossade tomater", amount: "1 burk" },
      { key: "spenat", name: "Spenat", amount: "en påse" },
      { key: "yoghurt", name: "Yoghurt", amount: "2 dl" },
      { key: "lok", name: "Lök", amount: "1 st" },
    ],
    steps: [
      "Fräs lök, tillsätt kikärtor och tomater. Sjud 12 minuter.",
      "Vänd i spenat. Servera med en klick yoghurt.",
    ],
  },
  {
    id: "korvstroganoff",
    title: "Korvstroganoff med ris",
    time: 25,
    protein: "meat",
    tags: ["kids", "budget", "quick"],
    meal: "middag",
    rating: 4.6,
    ratings: 210,
    ingredients: [
      { key: "fars", name: "Falukorv eller färs", amount: "400 g" },
      { key: "gradde", name: "Grädde", amount: "2 dl" },
      { key: "tomat", name: "Tomatpuré eller krossade", amount: "2 msk" },
      { key: "lok", name: "Lök", amount: "1 st" },
      { key: "ris", name: "Ris", amount: "3 dl" },
    ],
    steps: [
      "Fräs lök och korv/färs. Tillsätt tomat och grädde.",
      "Sjud 10 minuter. Servera med ris.",
    ],
  },
  {
    id: "tonfiskpasta",
    title: "Tonfiskpasta",
    time: 15,
    protein: "fish",
    tags: ["pantry", "quick", "budget"],
    meal: "lunch",
    rating: 4.3,
    ratings: 54,
    ingredients: [
      { key: "pasta", name: "Pasta", amount: "350 g" },
      { key: "tonfisk", name: "Tonfisk", amount: "1 burk" },
      { key: "citron", name: "Citron", amount: "0.5 st" },
      { key: "olja", name: "Olivolja", amount: "2 msk" },
    ],
    steps: [
      "Koka pasta. Blanda med tonfisk, olja och citron.",
      "Om tonfisken saknas i lagret: lägg den på inköpslistan och gör rätten imorgon.",
    ],
  },
  {
    id: "pastagratang",
    title: "Pastagratäng med broccoli och ost",
    time: 35,
    protein: "veg",
    tags: ["kids", "mealbox"],
    meal: "middag",
    rating: 4.7,
    ratings: 93,
    ingredients: [
      { key: "pasta", name: "Pasta", amount: "400 g" },
      { key: "broccoli", name: "Broccoli", amount: "1 st" },
      { key: "ost", name: "Ost", amount: "150 g" },
      { key: "mjolk", name: "Mjölk", amount: "3 dl" },
      { key: "smor", name: "Smör", amount: "2 msk" },
    ],
    steps: [
      "Koka pasta och broccoli. Gör en enkel sås på smör och mjölk.",
      "Varva i form, riv ost över. 200° i 15 minuter.",
    ],
  },
  {
    id: "pytt",
    title: "Pytt i panna på rester",
    time: 20,
    protein: "any",
    tags: ["leftovers", "budget"],
    meal: "lunch",
    rating: 4.4,
    ratings: 48,
    ingredients: [
      { key: "potatis", name: "Potatis", amount: "4 st" },
      { key: "lok", name: "Lök", amount: "1 st" },
      { key: "agg", name: "Ägg", amount: "2 st" },
      { key: "smor", name: "Smör", amount: "1 msk" },
    ],
    steps: [
      "Tärna potatis och bryn knaprigt. Tillsätt lök och eventuella rester.",
      "Stek ägg och lägg ovanpå.",
    ],
  },
  {
    id: "tomatsoppa",
    title: "Tomatsoppa med grillade ostmackor",
    time: 25,
    protein: "veg",
    tags: ["kids", "budget"],
    meal: "lunch",
    rating: 4.6,
    ratings: 119,
    ingredients: [
      { key: "tomat", name: "Krossade tomater", amount: "1 burk" },
      { key: "lok", name: "Lök", amount: "1 st" },
      { key: "brod", name: "Bröd", amount: "4 skivor" },
      { key: "ost", name: "Ost", amount: "100 g" },
      { key: "gradde", name: "Grädde", amount: "1 dl" },
    ],
    steps: [
      "Fräs lök, häll på tomater och sjud. Mixa slät, tillsätt grädde.",
      "Grilla ostmackor i panna. Doppa.",
    ],
  },
  {
    id: "wraps",
    title: "Kycklingwraps med yoghurtsås",
    time: 20,
    protein: "chicken",
    tags: ["quick", "kids"],
    meal: "lunch",
    rating: 4.5,
    ratings: 82,
    ingredients: [
      { key: "kyckling", name: "Kyckling", amount: "300 g" },
      { key: "yoghurt", name: "Yoghurt", amount: "2 dl" },
      { key: "citron", name: "Citron", amount: "0.5 st" },
      { key: "spenat", name: "Spenat", amount: "en näve" },
    ],
    steps: [
      "Stek kycklingstrimlor. Blanda yoghurt, citron och salt.",
      "Rulla i tortilla eller ät som bowl med spenat.",
    ],
  },
  {
    id: "chili",
    title: "Chili sin carne",
    time: 30,
    protein: "veg",
    tags: ["pantry", "mealbox", "budget"],
    meal: "middag",
    rating: 4.6,
    ratings: 90,
    ingredients: [
      { key: "bonor", name: "Bönor", amount: "1 burk" },
      { key: "tomat", name: "Krossade tomater", amount: "1 burk" },
      { key: "lok", name: "Lök", amount: "1 st" },
      { key: "ris", name: "Ris", amount: "3 dl" },
    ],
    steps: [
      "Fräs lök, tillsätt tomater och bönor. Krydda med chili och spiskummin.",
      "Sjud 20 minuter. Servera med ris.",
    ],
  },
  {
    id: "pannkakor",
    title: "Pannkakor",
    time: 25,
    protein: "veg",
    tags: ["kids", "budget"],
    meal: "mellanmal",
    rating: 4.9,
    ratings: 240,
    ingredients: [
      { key: "agg", name: "Ägg", amount: "3 st" },
      { key: "mjolk", name: "Mjölk", amount: "6 dl" },
      { key: "smor", name: "Smör", amount: "50 g" },
    ],
    steps: [
      "Vispa 2.5 dl mjöl (om du har), ägg och mjölk till en slät smet. Vila 10 min.",
      "Stek tunna pannkakor i smör. Sylt, bär eller ost och skinka.",
    ],
  },
  {
    id: "fiskgratang",
    title: "Fiskgratäng med dill och purjolök",
    time: 35,
    protein: "fish",
    tags: ["kids"],
    meal: "middag",
    rating: 4.4,
    ratings: 61,
    ingredients: [
      { key: "lax", name: "Fiskfilé", amount: "400 g" },
      { key: "potatis", name: "Potatis", amount: "700 g" },
      { key: "gradde", name: "Grädde", amount: "3 dl" },
      { key: "ost", name: "Ost", amount: "80 g" },
    ],
    steps: [
      "Skiva potatis tunt. Varva med fisk i form.",
      "Häll på grädde, riv ost. 200° i 25 minuter.",
    ],
  },
  {
    id: "linssoppa",
    title: "Linssoppa med bröd",
    time: 30,
    protein: "veg",
    tags: ["pantry", "budget", "mealbox"],
    meal: "lunch",
    rating: 4.5,
    ratings: 73,
    ingredients: [
      { key: "morot", name: "Morötter", amount: "3 st" },
      { key: "lok", name: "Lök", amount: "1 st" },
      { key: "tomat", name: "Krossade tomater", amount: "1 burk" },
      { key: "brod", name: "Bröd", amount: "att doppa" },
    ],
    steps: [
      "Fräs lök och morot. Tillsätt tomater och vatten. Sjud 20 minuter.",
      "Mixa halvsmooth. Servera med bröd.",
    ],
  },
  {
    id: "ugnsomelett",
    title: "Ugnsomelett med potatis och ost",
    time: 30,
    protein: "veg",
    tags: ["leftovers", "budget"],
    meal: "frukost",
    rating: 4.3,
    ratings: 41,
    ingredients: [
      { key: "agg", name: "Ägg", amount: "6 st" },
      { key: "potatis", name: "Kokt potatis", amount: "4 st" },
      { key: "ost", name: "Ost", amount: "100 g" },
      { key: "mjolk", name: "Mjölk", amount: "1 dl" },
    ],
    steps: [
      "Skiva potatis i smord form. Vispa ägg och mjölk, häll över.",
      "Ost på toppen. 180° i 20 minuter.",
    ],
  },
];

export type DinnerDish = [string, Protein, number, string[]];

export const DINNER_DISHES: DinnerDish[] = [
  ["Pasta med tomatsås och bönor", "veg", 20, ["pantry", "budget", "kids"]],
  ["Krämig kycklinggryta med svamp", "chicken", 30, ["kids", "leftovers"]],
  ["Omelett med rester av grönsaker", "veg", 15, ["leftovers", "budget", "quick"]],
  ["Wok med nudlar och det som finns i kylen", "any", 20, ["leftovers", "quick"]],
  ["Tacos med färs eller bönor", "any", 20, ["kids", "friday"]],
  ["Linssoppa med bröd", "veg", 30, ["pantry", "budget", "mealbox"]],
  ["Ugnsbakad lax med potatis och citron", "fish", 25, ["quick"]],
  ["Kycklingcurry med kokosmjölk och ris", "chicken", 30, ["mealbox", "leftovers"]],
  ["Pannkakor", "veg", 25, ["kids", "budget"]],
  ["Köttbullar med potatismos", "meat", 30, ["kids"]],
  ["Chili sin carne", "veg", 30, ["pantry", "mealbox", "budget"]],
  ["Pastagratäng med broccoli och ost", "veg", 35, ["kids", "mealbox"]],
  ["Pytt i panna på rester", "any", 20, ["leftovers", "budget"]],
  ["Tomatsoppa med grillade ostmackor", "veg", 25, ["kids", "budget"]],
  ["Kycklingwraps med yoghurtsås", "chicken", 20, ["quick", "kids"]],
  ["Korvstroganoff med ris", "meat", 25, ["kids", "budget", "quick"]],
  ["Tonfiskpasta", "fish", 15, ["pantry", "quick", "budget"]],
  ["Kikärtsgryta med spenat och yoghurt", "veg", 25, ["pantry", "budget"]],
  ["Fiskgratäng med dill och purjolök", "fish", 35, ["kids"]],
  ["Ugnsomelett med potatis och ost", "veg", 30, ["leftovers", "budget"]],
];

export function recipeById(id: string): Recipe | undefined {
  return RECIPES.find((r) => r.id === id);
}

export function recipeNutrition(id: string): { kcal: number; protein: number } {
  const recipe = recipeById(id);
  const minutes = recipe?.time ?? 25;
  const protein =
    recipe?.protein === "veg" ? 16 : recipe?.protein === "fish" ? 34 : recipe?.protein === "chicken" ? 36 : 28;
  return { kcal: Math.round(180 + minutes * 12), protein };
}

export function seedCookLog(): CookEntry[] {
  return [];
}
