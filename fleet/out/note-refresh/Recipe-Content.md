<!-- fleet job=note-refresh id=Recipe-Content status=done turns=20 usd=0.0243 tokens(read,write,in,out)=[673198, 64531, 42, 18963] model=claude-haiku-5-5 -->
# notes/Research/Recipe Content.md

**Verdict:** Badly stale. The row counts, the Seared Stainberry status, the Tin Bar output, the gateway's learned-recipe handling and the `begin(profile)` path all contradict the tip. The native wire claims (op codes 1/2/3/5, row field order, `00c8cfc0`/`00c8bd10`/`00c8d170` names) still match the code.

**Corrections:**

1. `old:` W51b expands `data/content/recipes.json` to **31 content rows**: 25 Chef dishes, five Miner bars, and the Spunky Scrapper Hammer local Blacksmith sample.
   `new:` W51b expands `data/content/recipes.json` to **32 content rows**: 26 Chef dishes, five Miner bars, and the Spunky Scrapper Hammer local Blacksmith sample.
   `why:` `repo:prototype/osfr-tools/tests/recipes.rs:112` asserts 32 loaded rows, and `:262` asserts 26 Chef; `repo:notes/Autopilot/T033.md:56` says "32 loaded rows".

2. `old:` The remaining candidate catalogue has **83 rows**: 19 Chef and 64 Blacksmith.
   `new:` The remaining candidate catalogue has **82 rows**: 18 Chef and 64 Blacksmith.
   `why:` `repo:prototype/osfr-tools/tests/recipes.rs:132` asserts 82 unresolved rows; `data/content/recipes_unresolved.json` has 18 `chef.*` keys and 64 `blacksmith.*` keys; `repo:notes/Autopilot/T033.md:57`, `:328` ("18 Chef and 64 Blacksmith candidates remain").

3. `old:` Nineteen candidates remain incomplete, including Seared Stainberry, which has no ingredient row.
   `new:` Eighteen candidates remain incomplete. Seared Stainberry was promoted to a loaded row (recipe 51, pattern item 861, components 2880x3, 2884x3, 2887x3, 2906x7, output 21825x1).
   `why:` `repo:prototype/osfr-tools/data/content/recipes.json:2343` (`chef.seared_stainberry`) is in the loaded file, and `repo:notes/Autopilot/T033.md:26-30` describes the promotion; the key is absent from `recipes_unresolved.json`.

4. `old:` | Chef | 25 |
   `new:` | Chef | 26 |
   `why:` `repo:prototype/osfr-tools/tests/recipes.rs:262` (`by_job(CraftingJob::Chef).count(), 26`); `repo:notes/Autopilot/T033.md:260`.

5. `old:` Seared Stainberry and 18 other unresolved Chef candidates lack complete ingredients.
   `new:` 18 unresolved Chef candidates lack complete ingredients.
   `why:` `repo:notes/Autopilot/T033.md:26` (Seared Stainberry promoted) and `:328`; `repo:prototype/osfr-tools/data/content/recipes_unresolved.json` (18 chef keys).

6. `old:` The other four Miner rows are one bar per wiki recipe; Copper uses the client tutorial's five-bar quantity.
   `new:` Copper and Tin use the five-bar quantity (Copper from tutorial locale 1772250646; Tin from locales 451207523/740309274/2947743611). Gold, Iron and Silver remain one bar per wiki recipe.
   `why:` `repo:prototype/osfr-tools/data/content/recipes.json:3994-3997` (`miner.tin_bar` output 21786 count 5); `repo:notes/Autopilot/T033.md:36-38`, `:107-108`.

7. `old:` The current gateway does not yet track learned recipes or map every content key to a recovered native recipe id, so those rows cannot all be emitted as verified client recipe rows yet.
   `new:` The gateway tracks learned recipes (`learned_recipes`, seeded at `[11, 70, 4, 2002]`), sends operation 5 after zone ready, and sends operation 1 when a pattern item is consumed. Operations 2 and 3 are encoded but have no gameplay caller. Not every content key maps to a recovered native recipe id (`recipe_id: null` rows), so those rows cannot all be emitted as verified client recipe rows yet.
   `why:` `repo:prototype/osfr-tools/src/gameplay.rs:244`, `:867`, `:1479-1505` (`learn_consumed_patterns` calls `learn_recipe`), `:1799` and `:5275` (`recipe_replace_all_packet`); `encode_component_update` and `encode_recipe_remove` have no callers outside `src/recipes.rs:646`/`:655`; `recipes.json:7` has `recipe_id: null`.

8. `old:` Their legacy `begin(profile)` entry remains for the current gateway path
   `new:` Their legacy `begin(profile)` entry remains only for developer teleport and tests
   `why:` `repo:prototype/osfr-tools/src/gameplay/crafting.rs:185-203` calls `begin_recipe(profile, &key, rank, learned, &available)` for all three jobs; `begin(45)` appears only in `src/gameplay/developer_teleport.rs:44` and `src/gameplay/ordinary_quit_routing.rs:44,81`.

9. `old:` The current gateway still uses the compatibility `begin(profile)` path, which assumes the default learned recipe and does not receive player-specific rank/inventory.
   `new:` The gateway's crafting start already calls `begin_recipe` with the player's rank, learned state and inventory (`src/gameplay/crafting.rs:185-203`); the compatibility path is no longer on the gateway route.
   `why:` `repo:prototype/osfr-tools/src/gameplay/crafting.rs:185-203`; the `begin(profile)` grep above.

10. `old:` Its successor must call `begin_recipe` with those facts and must send the recipe-list/add messages above.
    `new:` The gateway already sends the recipe-list (operation 5) and add (operation 1) messages. The remaining gap is operation 2 component refreshes on inventory change, which is not wired.
    `why:` `repo:prototype/osfr-tools/src/gameplay.rs:1799`, `:1500`; `encode_component_update` (`src/recipes.rs:646`) has no gameplay caller.

11. `old:** 5 passed**. Checks both catalogues, all item references, total candidate coverage and per-job counts,` (the sentence is "`cargo test --manifest-path Cargo.toml --test recipes`: **5 passed**. Checks both catalogues, …")
    `new:` the same sentence with **8 passed** in place of **5 passed**.
    `why:` `repo:notes/Autopilot/T033.md:144` ("`cargo test --test recipes`: **8 passed, 0 failed**"). I did not run the suite, so this rests on T033's report.

**Unsure:**
- Per-job row counts in `recipes.json` rest on the test assertions (`tests/recipes.rs:262`) and T033, not a full count. My key search was capped at 20 hits per query.
- The wire claims for `00c8d170`, `009471a0`, `00a12740`, `00c8beb0`, `0090a720` and `008db930` exist in the client DB, but I did not re-verify their byte-level behaviour.
- The recipes_wire test count (note says 4 passed; T033 reports 5) was not settled.
</result>
