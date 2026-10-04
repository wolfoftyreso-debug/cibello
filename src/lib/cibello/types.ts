export type Location = "kyl" | "skafferi" | "frys";
export type Protein = "chicken" | "meat" | "fish" | "veg" | "any";
export type Meal = "frukost" | "lunch" | "middag" | "mellanmal" | "efterratt" | "baka";
export type DayKey = "mon" | "tue" | "wed" | "thu" | "fri" | "sat" | "sun";

export type Ingredient = {
  key: string;
  name: string;
  amount: string;
};

export type Recipe = {
  id: string;
  title: string;
  time: number;
  protein: Protein;
  tags: string[];
  meal: Meal;
  rating: number;
  ratings: number;
  ingredients: Ingredient[];
  steps: string[];
};

export type PantryItem = {
  id: string;
  key: string;
  name: string;
  location: Location;
  qty: string;
  expires: string;
};

export type ListItem = {
  id: string;
  key: string;
  name: string;
  amount: string;
  done: boolean;
  fromRecipe?: string;
};

export type WeekPlan = Record<DayKey, string | null>;

export type CookEntry = {
  id: string;
  recipeId: string;
  title: string;
  cookedAt: string;
};
