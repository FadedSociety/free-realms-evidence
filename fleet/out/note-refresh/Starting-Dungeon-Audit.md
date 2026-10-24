<!-- fleet job=note-refresh id=Starting-Dungeon-Audit status=done turns=34 usd=0.0411 tokens(read,write,in,out)=[1723123, 89698, 70, 25203] model=claude-haiku-5-5 -->
# notes/Research/Starting Dungeon Audit.md

**Verdict:** minor drift. The code-level claims hold (packet families, encounter header layout, movement opcode 125, the opening-cave content, the prepare script, the zone exit and completion rules, and the loading order). The stale parts are two status sentences that still call native acceptance pending, although the Build Ledger and Current Progress record it as passed.

**Corrections:**

1. `old:` Native zoning and a complete native encounter remain acceptance gates.
   `new:` Native zoning and a complete native encounter were accepted in the lead run `client-baseline-20261009T114509Z`; the Build Ledger lists the opening cave as Playable (runs 081219, 114509).
   `why:` repo:notes/Design/Build Ledger.md:70 ("Opening cave 411 | **Playable** | Runs 081219, 114509"); repo:notes/Current Progress.md:98 (lead native run `client-baseline-20261009T114509Z` passed cave replay).

2. `old:` Required next checks are native cave loading and ground position, enemy visibility and attacks, retaliation/knockout/retry, native objective/result/return behavior, once-only inventory rewards, and restart restoration.
   `new:` Native runs 081219 and 114509 covered cave loading, guide entry, a first-attempt loss with retry, result Close with world return, fresh re-entry, and once-only rewards.
   `why:` repo:notes/Current Progress.md:98 (guide entry, first-attempt loss, ordinary result Close/world return, fresh instance entry with boss500); repo:notes/Current Progress.md:124 (opening cave and its boss, once-only rewards, return to the world); repo:notes/Design/Build Ledger.md:70.

**Checked and current:**
- Encounter packet families and layouts: `src/encounter.rs` header/encounter_header (2907–2915), `minigame` sub as u8 (2926), `objective` sub as u8 (2973), `player_hp` 38/1 with two i32 fields (2995), `enemy_hp` 35/5 (3001), `movement` standalone 125 (3061), `rules` 62 (2985), and 41/107, 41/2, 41/132–133, 39/17, 39/18, 39/19, 45/1–3, 32/7, 32/9 in the same file. The 45, 12, 24, 15, 11 and 36 byte sizes match the layouts (I did not check the 98, 50 or 423 byte sizes).
- Loading order (line 62): `src/gateway.rs:1767–1768` and `1785–1786` reset ready/loaded on zoning; `1455–1474` send Ready startup on 13; `1477–1497` call `initialize_world` on 10.
- Opening cave content: `scripts/prepare-opening-encounters.py:55` (five wolves), `:73–75` (three Gloamlings, the boss at 304/28/299, 50 coins plus item 1195), `:90` (writes `lab/references/rust-opening/encounters.json`, template hash), `:92` (`native_zoning_validated: False`). `data/content/enemies.json:2226–2320` has the wolf, Gloam creature and Mac spawn groups, staged by 910007/910008/910011. Zone 411 is local (`dungeons/opening_cave.json`, `encounters.json` provenance).
- Exit behaviour (line 30): `src/encounter.rs:2579–2607` restores the return location and sets `completed` only when the phase is Won.

**Unsure:**
- Line 22: "Six synthetic tests additionally cover…". `tests/encounter.rs` has 16 non-ignored `#[test]` functions (lines 86–694), not six. The count may refer to a subset I did not map, so I left it as is.
- Line 22: "The Rust private-content test matched…". The test is `actual_opening_content_and_community_packet_oracle` (`tests/encounter.rs:716`), marked `#[ignore]` and opt-in via `OSFR_OPENING_CONTENT`. It asserts byte equality with the oracle files and does not assert the byte lengths. The claim is not false, but the note should say it is opt-in.
- Line 28: "Reducing the Overlord representation to zero health signals Darkthorne's seal." The code has no seal logic; the boss is a plain `boss` actor (`encounter.rs:211`), and an encounter is cleared when all enemies reach zero health (`encounter.rs:1047`). This is an interpretation and I did not change it.
- Line 28: "the caller must suppress the earlier training combat and duplicate outdoor enemy spawns". I found no code that gates training combat on the opening, so this is a caller obligation I could not verify either way.
- Lab-only claims (ForgeLight floor samples, the 44-byte stride, CDN asset hashes, `lab/` report paths) are not in the repo and were not checked.
