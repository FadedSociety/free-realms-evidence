<!-- fleet job=note-refresh id=Harvesting-Native-Content-v2 status=done turns=14 usd=0.0169 tokens(read,write,in,out)=[345142, 54008, 30, 13480] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Native Content v2.md

**Verdict:** drifted. The writer's constants and tile registration at the tip no longer match what this note says the current writer emits (quota, seed, duration, tile count). The package hashes and the lab package contents could not be checked from these roots.

**Corrections:**

1. `old:` quotas 15 / per-reward 5, seed 111,
   `new:` quotas 25 / per-reward 5, seed 2,
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:780` (`RECONSTRUCTED_QUOTA_TILES: u32 = 25`), `:782` (per-reward 5), `:784` (`RECONSTRUCTED_SEED: u32 = 2`), applied at `:955-956` and `:1005`. The tests read the same constants (`tests/harvesting_border.rs:215-216`). Agrees with `notes/Research/Harvesting Completion.md:24` (seed 2, 25 tiles per goal).

2. `old:` `game_farming.gfx`, duration 180 s, spawn percentages and meter 0.
   `new:` `game_farming.gfx`, duration 120 s, spawn percentages and meter 0.
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:778` (`RECONSTRUCTED_DURATION_SECONDS: u32 = 120`), applied at `:1003`. Spawn percentages and meter 0 still hold (`:786-795`, `:1010`).

3. `old:` Eight tile kinds
   `new:` Four tile kinds
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:966-972` pushes one `Type8Kind` per goal (4 total, category `TILE_SELECTABLE_CATEGORY` = 400). `:999` sets `collectable: Vec::new()`. The 600 block is not registered anywhere (`TILE_COLLECTABLE_CATEGORY` at `:88` is defined but never used). `:944-945` says the old 601..604 reconstruction was dropped because it rendered unresolved labels.

4. `old:` are registered (401..404 category 400, 601..604 category 600).
   `new:` are registered (401..404, category 400); the 600 block is empty (`collectable: []`, `collectable_percent` 0).
   `why:` same as correction 3: `repo:prototype/osfr-tools/src/harvesting.rs:966-972`, `:999`, `:1007`.

5. `old:` `tiles` (4 -> 8 registered kinds)
   `new:` `tiles` (4 registered kinds from the current writer)
   `why:` `repo:prototype/osfr-tools/src/harvesting.rs:966-972`. Only if the header's "Writer = current `harvesting::write_content`" is taken at face value. The v2 file itself is outside these roots, so see Unsure.

**Checked and holding:**
- `harvesting::write_content` exists (`repo:prototype/osfr-tools/src/harvesting.rs:1044`).
- The 11x11 grid, with row 0 and column 0 inert, 90 cells at x1..10 / y1..9, and the drop row at y10 (`harvesting.rs:762-776`, `:910-921`).
- Outputs `[2885, 2887, 2890, 2877]` in that order for region 111 (`harvesting.rs:320`, `:241`, `:255`, `:276`, `:185`).
- Profile 45 (`harvesting.rs:64`), `FarmingAssets.txt` and `game_farming.gfx` (`harvesting.rs:43`, `:47`).
- Test-file counts: `harvesting_border` 3, `harvesting_runtime_border` 2, `harvesting_runtime_tiles` 3, `harvesting_tile_registration` 9, `harvesting` 17, `harvesting_job_binding` 3, `harvesting_review` 4, `harvesting_reward_catalogue` 4 (counted `#[test]` attributes under `repo:prototype/osfr-tools/tests/`).

**Unsure:**
- `type8_harvesting_gateway` is listed as 11 in the rerun, but `repo:prototype/osfr-tools/tests/type8_harvesting_gateway.rs` has 14 `#[test]` attributes (lines 438..1135) and no `#[ignore]`. This may be later test growth, not a false claim, since the note describes a frozen-revision rerun. The family total of 56 would then differ.
- The v2 package file (`content/harvesting.json`, hash `c08f264e…`), its 8 tile kinds, and the 1703-definition inventory live under `../lab/`, which is not in these roots. Not checked.
- The committed `repo:prototype/osfr-tools/data/content/harvesting.json` is stale and matches neither the writer nor this note. It has quota 15, seed 111, duration 180, and tile values 403/411/413/416 (lines 169, 218, 217, 143-163). The note's v1 figures may come from a similar earlier output.
- `notes/Reviews/Harvesting Runtime and Border Review.md:29` also says "8 tile kinds, quota 15 / per_reward 5, seed 111". That review is outside this note, but it has the same drift.
