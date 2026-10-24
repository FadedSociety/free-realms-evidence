<!-- fleet job=note-refresh id=Harvesting-Completion status=done turns=12 usd=0.0158 tokens(read,write,in,out)=[316248, 54824, 26, 11483] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Completion.md

**Verdict:** minor drift. The code claims hold at the tip: the lifecycle adapter, the constants, the 4 seeded lifecycle tests and the packet/grant wiring all match. Two statements need fixing: one citation points at the wrong place, and one generalisation about `chef.json` is too broad.

**Corrections:**

1. old: `This is recorded in `notes/Current Progress.md:23`.`
   new: `The Harvesting run record is not located at that line. The only `realmexit` entry in `notes/Current Progress.md` (line 169) concerns a Mining run (`client-baseline-20261009T143211Z`), so the Harvesting realmexit record needs a source or should be dropped.`
   why: repo:notes/Current Progress.md:23 is about other players' AddPc visibility. The only `realmexit` entry is repo:notes/Current Progress.md:169, which is a Mining run.

2. old: `current `chef.json` records have empty objective arrays`
   new: `most current `chef.json` records have empty objective arrays (two carry visit and talk objectives), and none tracks minigame 111 or item collection`
   why: repo:prototype/osfr-tools/data/content/quests/chef.json:161 (`visit_position`) and :580 (`talk_to_npc`) are non-empty. A search for `finish_minigame`, `collect_item` or minigame kinds in that file found nothing. The conclusion that quest advancement is still lead work stands.

**Checked and holding:**
- `src/harvesting_lifecycle.rs` exists, and `harvesting.rs:33-34` exposes it as `pub mod lifecycle`.
- Produce order is stickfruit, stainberry, tumtumnip, spiralmint (`harvesting.rs:320`). Goal values are 411/413/416/403 via `produce_value` (`harvesting.rs:100-116`). Tile frames are `value - 400`, giving 11/13/16/3 (`harvesting.rs:966-972`).
- `RECONSTRUCTED_DURATION_SECONDS` is 120, quota 25, per-reward 5, seed 2, wildcard 5%, collectable/blocker/powerup 0% (`harvesting.rs:778-795`). Board is 11x11 with a 1-cell border and 9 playable rows, giving 10x9 (`harvesting.rs:765-774`).
- `CHEF_PROFILE_ID` is 45 (`harvesting.rs:64`). The Chef XP award is 25 (`harvesting_lifecycle.rs:17`, `:443`). Zero coins (`:434`). `HARVESTING_ICON_ID` is 908 (`harvesting.rs:60`).
- Win emits `CollectItem` per grant and `FinishMinigame { minigame_id: game_id }` (`harvesting_lifecycle.rs:455-469`). The grant key `minigame-run:<instance>` is set in `minigame.rs:581` and asserted in `tests/harvesting_lifecycle.rs:436`.
- The 22-chain / 84-second claim matches the test: `actions == 22`, `wall_ms == (actions-1)*4000 = 84000` (`tests/harvesting_lifecycle.rs:416`, `:441-445`; `INPUT_INTERVAL_MS` 4000 at `:37`).
- `tests/harvesting_lifecycle.rs` has 4 `#[test]` functions (lines 407, 504, 537, 576), matching "seeded lifecycle 4/4".
- All 11 test targets in the cargo command exist under `prototype/osfr-tools/tests/`.
- The packet sequence (`39/6` Quit; `39/18`, `39/47`, `39/19`; automatic `39/7`; Close `26/42`) matches `notes/Build Guides/Gameplay/Minigame Framework.md` (repo:…Minigame Framework.md, the lifecycle table and results sections). `notes/Research/Minigame Lifecycle.md` and `Harvesting Restoration.md` exist.

**Unsure:**
- "all 67 tests across 11 binaries passed" and the lifecycle/minigame/gateway counts (4/4, 7/7, 11/11) are run results. I did not run them, so I could not check them.
- The client-side hashes and `Resources/` line citations (MiniGameData.txt:112, CodeStringMappings.txt lines) live in the client root. I did not open them.
- The claim that `apply_grant` is called directly is slightly indirect. `harvesting_lifecycle.rs` calls `runs.finish`, which applies the grant through the shared `minigame.rs:581`. The note's wording is accurate enough, so I did not correct it.
