create table if not exists pantry_items (
  id text primary key,
  user_id text not null,
  item_key text not null,
  name text not null,
  location text not null,
  qty text not null,
  expires text not null
);
create index if not exists pantry_items_user_id_idx on pantry_items (user_id);

create table if not exists list_items (
  id text primary key,
  user_id text not null,
  item_key text not null,
  name text not null,
  amount text not null default '',
  done boolean not null default false,
  from_recipe text
);
create index if not exists list_items_user_id_idx on list_items (user_id);

create table if not exists week_days (
  user_id text not null,
  day text not null,
  recipe_id text,
  primary key (user_id, day)
);

create table if not exists cook_log (
  id text primary key,
  user_id text not null,
  recipe_id text not null,
  title text not null,
  cooked_at timestamptz not null default now()
);
create index if not exists cook_log_user_id_idx on cook_log (user_id, cooked_at desc);
