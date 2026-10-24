<!-- fleet job=note-refresh id=Pieces-063-Dungeon-party-rewards status=done turns=13 usd=0.0133 tokens(read,write,in,out)=[298487, 40974, 28, 10318] model=claude-haiku-5-5 -->
# notes/Research/Pieces/063 Dungeon party rewards.md

**Verdict:** minor drift. The status, file paths, test counts and the "not registered in `lib.rs`" claim all hold at the tip. Two sentences overstate what the code or captures show.

**Verified as current:**
- `src/restoration/piece_063.rs` and `tests/piece_063.rs` exist. The test file includes the module by `#[path]` (tests/piece_063.rs:41-43).
- `lib.rs` has no `restoration` module, so the module is still unregistered (src/lib.rs:3-22).
- The Rust test file has 7 `#[test]` functions (tests/piece_063.rs:96, 130, 165, 189, 223, 262, 290).
- `tests/pieces/test_piece_063.py` has 8 test methods, and `scripts/pieces/piece_063.py` exists.
- `DungeonRewardLedger` with `open`, `finish`, `claim` and `pending` exists (piece_063.rs:225-335). `finish` refuses a second completion of the same instance id via the `finished` set (piece_063.rs:252-253, 287-289, 299).
- The header is 13 bytes (`1 + 3 * 4`, piece_063.rs:54, 140-151).
- Sub-opcodes 22, 45, 46 and 68 are right in both the constructors and the Rust enum. Client `FUN_009b9d10` calls `FUN_008a4420(0x16,…)`, `FUN_009b9e20` calls `(0x2d,…)`, `FUN_009aa0c0` calls `(0x2e,…)` and `FUN_009b9eb0` calls `(0x44,…)`. The family constant is `0x27` (client `FUN_008a4420`, `param_1[1] = 0x27`).
- `EncounterPhase::Won` (encounter.rs:155), `EncounterOutcome::rewards` (encounter.rs:643-647) and `ActivityGroupRegistry::instance_members` (piece_020.rs:411, 773) exist.
- The item 057, 060, 020 and 089 owners in the Explicit gaps section exist as work items.

**Corrections:**

1. `old:` Reward traffic therefore carries the same group/instance and game identity as the encounter it belongs to.
   `new:` The three captures are sub-7 and sub-23 frames (not reward sub-opcodes) and all carry group −1 and game −1, so no captured reward frame shows the encounter's group or game identity; whether 45/46 carry it is unverified.
   `why:` repo:prototype/osfr-tools/tests/piece_063.rs:58-71 (capture vectors are `2700 07` and `2700 17`), :99-103 (expected group/game are −1); no 45/46 frame is present.

2. `old:` Duplicate 39/18 win packets and replayed instance ids are refused by the ledger, not by the packet writer.
   (This sentence spans lines 104-105 of the note; it is item 3 of "Integration for the lead".)
   `new:` The ledger never sees packets. It refuses a replayed or repeated `finish` call for the same instance id, so the caller must turn a 39/18 win into a single `finish` call.
   `why:` repo:prototype/osfr-tools/src/restoration/piece_063.rs:278-301 (`finish` takes `instance_id` and `actor` only); a grep for 39/18 handling in piece_063.rs finds none.

**Unsure:**

- The `lab/reports/piece-063-20261009T0456Z/` run logs, `provenance.json` and the evidence hash `9b39557f…` are outside the repo and were not checked.
- The client file hashes (`pseudocode.c`, `DoAction.as`) and the pinned community-table hashes were not recomputed.
- The claim that the client dispatcher decodes 45 and 68 (not just constructs them) was not traced; only the constructors were checked.
- The PR-76 `MiniGameLootWheelPackets.cs` reference and the `RewardBundleBase` layout were not checked.
- Integration step 3 says to fan the ledger output "into the existing `EncounterOutcome::rewards` path". That field is `Vec<EncounterReward>` (encounter.rs:636-647), which has a `job_xp` field. The ledger's `RewardBundle` has only `coins` and `items`, so the mapping needs a `job_xp` default. This is a note-level gap, not a false status claim.
