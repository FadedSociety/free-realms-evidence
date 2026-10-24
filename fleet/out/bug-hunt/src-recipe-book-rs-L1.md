<!-- fleet job=bug-hunt id=src-recipe-book-rs-L1 status=nothing_found turns=11 usd=0.0083 tokens(read,write,in,out)=[152065, 26503, 24, 7009] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/recipe_book.rs lines 1-405 of 405

No defects found in `prototype/osfr-tools/src/recipe_book.rs` lines 1-405 that I could tie to a client-reachable path.

I read the whole file and traced the candidates that looked suspicious:

- **`has_ingredients` (314-323) double-counts duplicate definition ids.** It checks each required entry against the full owned total, so a repeated id would pass twice. Not reachable: `recipes.rs:465-478` (`validate_recipe`) rejects any recipe that repeats an ingredient `definition_id`, and `RecipeCatalog::load` runs that check on every record. The same pattern in `cooking.rs:855` is covered by the same gate.
- **`near_any` (270-282) squares the radius, so a negative radius would act as positive.** Not reachable: world rules are checked to `0.1..=100.0` in `load_world_station_rules` (lines 96-103), and opening actors are checked the same way at `opening.rs:344-345`. NaN and infinite positions make the check false, as the doc says.
- **`decode` (39-50) indexing.** Length is checked before `inner[4..8]`, and `inner[..2]`/`inner[2..4]` are guarded by the `len() < 4` test first. No panic path.
- **`start` (329-404) atomicity and trust.** The recipe id is parsed with `try_from` and looked up server-side. Learned set, job, station position (`character.position`, server state per `gameplay.rs:4403-4410`), rank and available items all come from server state. Each `begin_recipe` refusal happens before any mutation (`cooking.rs:284-299`, and the `checked_add` at 300-303 precedes the writes). Nothing fallible runs after a service mutation inside this function.
- **`open_window` (295-312).** Reads only server-supplied station and profile data; no client-controlled value reaches an index or allocation.
- **`load_world_station_rules` (81-106).** Size is capped at 64 KiB, and the uniqueness and range checks are applied before the stations are returned.

Out of window, noted only: `gameplay.rs:4432-4433` sets `forging_tick_ms` before `apply_craft(...)?` runs, and `apply_craft` can return an error after `begin_recipe` has already changed service state. I did not check whether that leaves a half-started craft, since it is outside this window.
