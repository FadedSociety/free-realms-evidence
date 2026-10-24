<!-- fleet job=note-refresh id=Harvesting-Native-Launch-Preflight status=done turns=12 usd=0.0161 tokens(read,write,in,out)=[323488, 45681, 26, 14300] model=claude-haiku-5-5 -->
# notes/Research/Harvesting Native Launch Preflight.md

**Verdict:** minor drift. The job-binding repair in the note's last section is real and matches the code. The "Recovered versus reconstructed" table and the proposal still describe the pre-repair tree, and several `path:line` citations have moved.

**Corrections:**

1. `old:` `` `harvesting.rs` sets `profile_id: game_id` (`:921`) with a placeholder comment — not a usable gate ``
   `new:` `` `harvesting.rs` binds `profile_id: CHEF_PROFILE_ID` (45, `:1026`); `validate_content` refuses any other profile (`:1070`). Fixed by the job-binding repair below. ``
   `why:` repo:prototype/osfr-tools/src/harvesting.rs:64 (`pub const CHEF_PROFILE_ID: i32 = 45`), :1026, :1070-1075; the placeholder no longer exists.

2. `old:` `` `seed = game_id`, `58_000_001` — local choices ``
   `new:` `` `seed = RECONSTRUCTED_SEED` (2, `:1005`), `58_000_001` (`:49`) — local choices ``
   `why:` repo:prototype/osfr-tools/src/harvesting.rs:784 (`RECONSTRUCTED_SEED: u32 = 2`), :1005, :49 (`FIRST_INSTANCE_ID = 58_000_001`).

3. `old:` `three **empty** 69-byte reward-bundle records (`mining.rs:753-772`)`
   `new:` `three **empty** 69-byte reward-bundle records (`mining.rs:933`, a 207-byte zero block in `info_packet`)`
   `why:` repo:prototype/osfr-tools/src/mining.rs:926-933 (`// Three empty 69-byte RewardBundleBase records.`). Lines 753-772 are now the collect-chain call site.

4. `old:` `embeds it in the `39/16` info packet (`mining.rs:756`)`
   `new:` `compares it at `mining.rs:477` and embeds it in the `39/16` info packet (`mining.rs:929`, in `info_packet` from `mining.rs:926`)`
   `why:` repo:prototype/osfr-tools/src/mining.rs:477 (`if profile != self.content.profile_id || self.active()`), :926-929. Line 756 is now inside the collect path.

5. `old:` `(`MAX_GOALS = 8`, `mining.rs:85`)`
   `new:` `(`MAX_GOALS = 8`, `mining.rs:99`; enforced at `mining.rs:1159`)`
   `why:` repo:prototype/osfr-tools/src/mining.rs:99 (`const MAX_GOALS: usize = 8;`), :1159 (`if spec.goals.len() > MAX_GOALS`). Line 85 is now `fn default_preload_file`.

6. `old:` `(`gameplay.rs:1216-1223` grants 2884/2875 per newly counted Chef interaction)`
   `new:` `(`gameplay.rs:4758-4769`, `local_gather_drop`, grants 2884 at `:4765` and 2875 at `:4766` per newly counted Chef interaction under cooking and profile 45)`
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4756-4769. Lines 1216-1226 are now `ground_height`, `active_profile` and `guild_eligible`.

7. `old:` `3. Gateway dispatch (lead-owned): add harvesting only behind the existing dev gate, `begin(45)` with content `harvesting.json` for game 111, instance namespace `58_000_001`; wrong active profile must be refused before any packet is sent.`
   `new:` `3. Gateway dispatch (lead-owned): already wired as an opt-in candidate. `gameplay.rs:977-1023` loads `harvesting.json` for game 111 with instance `58_000_001`, refuses non-Chef content (`:990`), and counts it in the single-active-engine check (`:1034`). Completion outside the Chef job is refused (`:452-457`). Still open: confirm that a wrong active profile is refused before any `39/16` or `26/12` is sent.`
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:142-144, :977-1034; :452-457 (`harvesting completion is outside the accepted Chef job`). The "add harvesting" step is therefore partly done. The sentence is also stale in another way: the section's own "harvesting stays an unregistered separate candidate" wording is consistent with the code, but the proposal is not.

8. `old:` `the quest gather path (`gameplay.rs:1216-1223`)`
   `new:` `the quest gather path (`gameplay.rs:4758-4769`)`
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:4758-4769. The "received no edit" claim still holds as far as I can see, but I did not check the hash.

**Checked and current:**
- `CHEF_PROFILE_ID` exists and `content(111)` binds it. `validate_content` refuses other profiles.
- `tests/harvesting_job_binding.rs` exists. `RECOVERED_REGION_GAME_IDS` has six entries, matching "all six supported regional specs".
- The harvesting id list (58, 109, 110–120, 217) matches `harvesting.rs:52-57`.
- `FarmingAssets.txt` / `game_farming.gfx` are at `harvesting.rs:43, :47`.
- `piece_018` still marks harvesting `Entry::ModuleDriver` (`restoration/piece_018.rs:201`).
- The produce-to-item mapping (gummyfruit 2875, rainleaf 2884) is at `harvesting.rs:170, :234`.

**Unsure:**
- `ConfigServer.GAME_ID = 60` (Unresolved table): I found no `GAME_ID = 60` under `prototype/osfr-tools`. Possibly the config lives elsewhere; I did not verify.
- The `src/*.rs` hashes (`4e5196ba…`, `e6e421d8…`, `077ef906…`, `272711da…`, `20ae4610…`) and the `../lab/reports/` evidence paths: I could not check them from the repo tools.
- "Seven-minute" / 26/12 launcher "no pinned community writer" and the wiki spawn-set claims: outside the code, not checked.
- Board geometry (10x9, quota 15, 5 tiles per bundle) was not checked beyond the `padded_engine_shape` doc comment.
