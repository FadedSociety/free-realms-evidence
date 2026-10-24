<!-- fleet job=note-refresh id=Pieces-051-Enemy-catalogue status=nothing_found turns=26 usd=0.0302 tokens(read,write,in,out)=[1122564, 75947, 54, 19046] model=claude-haiku-5-5 -->
# notes/Research/Pieces/051 Enemy catalogue.md

**Verdict:** current. Every checkable claim about our code and status that I could reach still holds at the tip. No corrections.

**Checked and holding:**
- Artifact paths exist: `prototype/osfr-tools/src/restoration/piece_051.rs`, `prototype/osfr-tools/tests/piece_051.rs`, `scripts/pieces/piece_051.py`, `tests/pieces/test_piece_051.py` (line 1 of the note's Artifacts list).
- Test counts: `tests/piece_051.rs` has 8 `#[test]` functions (lines 79-272); `tests/pieces/test_piece_051.py` has 12 `def test_` methods (lines 59-264).
- Module status: `tests/piece_051.rs:31-33` still uses `#[path = "../src/restoration/piece_051.rs"] mod piece_051;`. `src/lib.rs` has no `piece_051` or `restoration` registration, so "until the lead registers the module" is still accurate.
- Original model table: `Resources/Models.txt` has 3743 data rows plus one `#` header (3744 lines), 17 columns (`MODELS_TXT_COLUMNS`, `piece_051.rs:38-56`).
- Combat marker: 27 rows. `Combat NPC` = 17, `Halloween Combat NPC` = 8 (ids 3293-3298, 3319, 3321), `Combat NPC: Forest Giant` = 1 (id 70), `Combat NPC: Forest Giant Boss` = 1 (id 75). `Combat training prop` (2037) and `Halloween Combat Powerup` (3299, 3300) are rejected by `is_enemy_model` (`piece_051.rs:241-246`).
- Race names: RaceDefinitions 27, 102, 105, 20 and others resolve to Animated Plant, Robgoblin Warrior, Vine Golem and Forest Troll Village, matching the note's list.
- Named enemy locale ids resolve: 5100200 Hooligan Wolf, 5100344 Mac, 5101961 Gloam Creature, 441457 Gloamling, 5101505 Gloam Overlord.
- Seven applied enemies: `APPLIED_ENEMIES` has 7 rows (`piece_051.rs:376-447`). The local ids 920001, 920002, 920100-920102 and 920110 match `scripts/prepare-opening-content.py:101-102` and `scripts/prepare-opening-encounters.py:55-74`.
- Local wolves: `scripts/prepare-opening-encounters.py:54-60` asserts five wolves on definition 3156 and steps them by (+4, 0, +3). Wolf position `(-2100.965, -45.98195, 456.7631)` and guid `100000003156` are asserted in `tests/pieces/test_piece_051.py:46,185,270`.
- Models 3933 and 3897 have no community NPC row (no `"ModelId": 3933|3897` in any pinned `Npcs.json`). Community ids 3157 and 3158 exist, so the note's "3156-3160" claim is consistent.
- Divergent placements: the 12 listed ids (2163-2166, 2254, 2552, 2649, 2853, 2886, 3422, 4611, 33081) match the count the note gives.
- Faction arithmetic: 70 + 59 + 4 = 133, and 443 - 133 = 310, which matches `notes/Reviews/MMO Dispatch Ledger.json:111`.
- Internal link targets exist (`notes/WorkItems/051.md`, `052 Enemy patrol and idle.md`, `054 Melee attacks.md`, `MMO Worker Contract.md`).

**Unsure (could not check from this tip):**
- `lab/reports/piece-051-20261009T053532Z/` (443 rows, findings.json, RED/GREEN logs): there is no `lab/` directory under the repo root, so the evidence bundle and the 443 / 180 / 111 / 12 / 6 counts cannot be re-derived here. The checker in `scripts/pieces/piece_051.py:395-600` implements the logic that produces them.
- Pinned community file hashes (`Models.txt` sha256 `0bad5a15...`, Sanctuary `Npcs.json` `b51d2d92...`, Legacy `f8f22448...`, locale `f1f22a30...`) and the 3426 / 4253 / 3419 / 834 definition counts: not recomputed.
- The wiki figures (92 `Category:Enemies` pages, 39 name matches, 19 `Category:Groups` pages): these come from a wiki database I could not reach.
- The note writes the Sanctuary path as `references/Sanctuary/src/...`. The refs root holds it as `Sanctuary/src/...`, and sibling notes use `lab/references/...`. This is a path-prefix difference only, not a false claim.
- The "trailing space" drift items (model 4446; locale ids 3043, 3227, 4280, 4286) were not checked.
