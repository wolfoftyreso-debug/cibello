export const RECIPE_IMAGES: Record<string, string> = {
  kycklinggryta: "/marketing/meal-gryta.jpg",
  "pasta-bonor": "/marketing/meal-pasta.jpg",
  omelett: "/marketing/meal-omelett.jpg",
  wok: "/marketing/meal-wok.jpg",
  "lax-ugn": "/marketing/meal-lax.jpg",
  curry: "/marketing/meal-gryta.jpg",
  kikartsgryta: "/marketing/meal-bowl.jpg",
  korvstroganoff: "/marketing/meal-gryta.jpg",
  tonfiskpasta: "/marketing/meal-pasta.jpg",
  pastagratang: "/marketing/meal-pasta.jpg",
  pytt: "/marketing/meal-omelett.jpg",
  tomatsoppa: "/marketing/meal-panini.jpg",
  wraps: "/marketing/meal-bowl.jpg",
  chili: "/marketing/meal-bowl.jpg",
  pannkakor: "/marketing/meal-havre.jpg",
  fiskgratang: "/marketing/meal-lax.jpg",
  linssoppa: "/marketing/meal-sallad.jpg",
  ugnsomelett: "/marketing/meal-omelett.jpg",
};

const PANTRY_IMAGES: Record<string, string> = {
  kyckling: "/marketing/ing-chicken.jpg",
  fars: "/marketing/ing-mince.jpg",
  gradde: "/marketing/ing-cream.jpg",
  svamp: "/marketing/ing-mushrooms.jpg",
  lok: "/marketing/ing-onion.jpg",
  vitlok: "/marketing/ing-garlic.jpg",
  pasta: "/marketing/ing-pasta.jpg",
  nudlar: "/marketing/ing-pasta.jpg",
  tomat: "/marketing/ing-tomato.jpg",
  paprika: "/marketing/ing-pepper.jpg",
  bonor: "/marketing/ing-beans.jpg",
  kikartor: "/marketing/ing-beans.jpg",
  tonfisk: "/marketing/ing-salmon.jpg",
  agg: "/marketing/ing-eggs.jpg",
  ost: "/marketing/ing-cheese.jpg",
  halloumi: "/marketing/ing-cheese.jpg",
  mjolk: "/marketing/ing-milk.jpg",
  yoghurt: "/marketing/ing-cream.jpg",
  smor: "/marketing/ing-cream.jpg",
  kokos: "/marketing/ing-cream.jpg",
  potatis: "/marketing/ing-potato.jpg",
  morot: "/marketing/ing-carrot.jpg",
  broccoli: "/marketing/ing-broccoli.jpg",
  ris: "/marketing/ing-rice.jpg",
  citron: "/marketing/ing-lemon.jpg",
  brod: "/marketing/ing-bread.jpg",
  olja: "/marketing/ing-oil.jpg",
  soja: "/marketing/ing-oil.jpg",
  spenat: "/marketing/ing-spinach.jpg",
  lax: "/marketing/ing-salmon.jpg",
  gurka: "/marketing/ing-cucumber.jpg",
  avokado: "/marketing/ing-avocado.jpg",
};

export function pantryImage(key: string): string {
  return PANTRY_IMAGES[key] ?? "/marketing/ingredients.jpg";
}

export function mealImage(titleOrId: string): string {
  if (RECIPE_IMAGES[titleOrId]) return RECIPE_IMAGES[titleOrId];
  const t = titleOrId.toLowerCase();
  if (t.includes("lax") || t.includes("fisk")) return "/marketing/meal-lax.jpg";
  if (t.includes("wok") || t.includes("nudel")) return "/marketing/meal-wok.jpg";
  if (t.includes("pasta") || t.includes("gratäng")) return "/marketing/meal-pasta.jpg";
  if (t.includes("omelett") || t.includes("pytt")) return "/marketing/meal-omelett.jpg";
  if (t.includes("gryta") || t.includes("curry") || t.includes("stroganoff")) return "/marketing/meal-gryta.jpg";
  if (t.includes("macka") || t.includes("wrap") || t.includes("taco")) return "/marketing/meal-panini.jpg";
  if (t.includes("pannkak") || t.includes("havre")) return "/marketing/meal-havre.jpg";
  if (t.includes("sallad") || t.includes("lins")) return "/marketing/meal-sallad.jpg";
  return "/marketing/meal-bowl.jpg";
}

export type MenuMeal = {
  title: string;
  with: string;
  time: number;
  tag: string;
  chips: string[];
  image: string;
  atHome: number;
  badge?: string;
};

export const WEEK_MENU: MenuMeal[] = [
  {
    title: "Krämig kycklingpasta",
    with: "med parmesan och basilika",
    time: 25,
    tag: "Högt protein",
    chips: ["Kyckling", "Enkelt"],
    image: "/marketing/meal-pasta.jpg",
    atHome: 82,
    badge: "Toppval",
  },
  {
    title: "Grillad laxbowl",
    with: "med örter, tomat och microgreens",
    time: 25,
    tag: "Fisk",
    chips: ["Snabb", "Näringsrik"],
    image: "/marketing/meal-lax.jpg",
    atHome: 74,
  },
  {
    title: "Kikärtsbowl med avokado",
    with: "rostade grönsaker och tahini",
    time: 25,
    tag: "Veg",
    chips: ["Skafferi", "Budget"],
    image: "/marketing/meal-bowl.jpg",
    atHome: 90,
    badge: "Skafferi",
  },
  {
    title: "Tomat, mozzarella & pesto",
    with: "grillad macka och ruccola",
    time: 15,
    tag: "Lunch",
    chips: ["Lunch", "Snabb"],
    image: "/marketing/meal-panini.jpg",
    atHome: 68,
  },
  {
    title: "Krämig kycklinggryta",
    with: "serveras med jasminris",
    time: 30,
    tag: "Vardag",
    chips: ["Barnvänlig", "Matlåda"],
    image: "/marketing/meal-gryta.jpg",
    atHome: 88,
  },
  {
    title: "Overnight oats",
    with: "bär, honung och mandel",
    time: 10,
    tag: "Frukost",
    chips: ["Gör kvällen innan", "Frukost"],
    image: "/marketing/meal-havre.jpg",
    atHome: 70,
  },
  {
    title: "Wok med nudlar",
    with: "kyckling och det som finns i kylen",
    time: 20,
    tag: "Rester",
    chips: ["Snabb", "Vardag"],
    image: "/marketing/meal-wok.jpg",
    atHome: 76,
  },
  {
    title: "Couscoussallad med spenat",
    with: "rostade grönsaker och citron",
    time: 20,
    tag: "Lätt",
    chips: ["Veg", "Meal prep"],
    image: "/marketing/meal-sallad.jpg",
    atHome: 81,
  },
];
