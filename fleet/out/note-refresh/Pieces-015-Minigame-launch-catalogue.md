<!-- fleet job=note-refresh id=Pieces-015-Minigame-launch-catalogue status=done turns=11 usd=0.0138 tokens(read,write,in,out)=[240387, 40190, 24, 12834] model=claude-haiku-5-5 -->
# notes/Research/Pieces/015 Minigame launch catalogue.md

**Verdict:** minor drift. The file layout, counts, test totals and the Forging 139 / Smelting 77 / Cooking 46 bindings hold at the tip. Two claims are stale: the piece_018 leftover was fixed, and the soccer row-42 binding cites a module that has no such constant.

**Corrections:**

1. `old:` `` `src/restoration/piece_018.rs:156` still says "TYPE 9 mimic anvil movie" ``
   `new:` `` `src/restoration/piece_018.rs:156` no longer says "TYPE 9 mimic anvil movie"; it now reads "TYPE 8 MatchThree (Forging row 139)", so no leftover remains open ``
   `why:` `repo:prototype/osfr-tools/src/restoration/piece_018.rs:156` reads `family: "TYPE 8 MatchThree (Forging row 139)"`. The forging route at lines 152-172 is `NativeAccepted` with `original_games: &[139]`. The lead-in "Known leftover outside this piece:" (line 219) should be dropped with it.

2. `old:` `| \`src/soccer.rs\` | 42 | code/test-candidate |`
   `new:` `| \`src/soccer_entry.rs\` (doc comment only, line 49: "equal to the shipped MiniGameData row (42/43/44)"; \`soccer.rs\` defines only \`SOCCER_TYPE_ID = 12\`) | 42 | code/test-candidate |`
   `why:` `repo:prototype/osfr-tools/src/soccer.rs:14-15` defines only `SOCCER_TYPE_ID: i32 = 12`, and no `MINIGAME_ID`/`GAME` constant with value 42 exists in `src/`. The only id-42 mention is `repo:prototype/osfr-tools/src/soccer_entry.rs:49`, a doc comment. `repo:scripts/pieces/piece_015.py:507` also says "soccer.rs MINIGAME_ID 42", which the tree does not support. Because of this, the "20 rows" bound by module constants (line 116) becomes 19, and the "21 soccer rows" unbound count on line 133 would become 22.

**Unsure:**

- **kart_racing.rs types 10/19/20 (line 127):** `repo:prototype/osfr-tools/src/kart_racing.rs:57-63` defines `KART_RACE_GAME_TYPE = 1`, `DEMO_DERBY_GAME_TYPE = 2`, and locale name ids 3052/3053 ("Kart Race Lobby" / "Demo Derby Lobby"). It never mentions 10, 19 or 20, so "code/test-candidate for types 10/19/20" is not supported by a citation. The same file's 3052/3053 are locale name ids, not lobby ids, as line 71 says. I could not settle whether the note's row-type mapping for kart is intended, so I left it unchanged.
- **Verified and unchanged:** `scripts/pieces/piece_015.py`, `tests/pieces/test_piece_015.py` (20 `def test_`), and `prototype/osfr-tools/tests/piece_015.rs` (6 `#[test]`). `piece_015.rs` is not registered in `src/lib.rs`, and nothing outside the piece reads it. The Mining 18/91, Harvesting 58/109-120/217, Cooking 46, Smelting 77 and Forging 139 bindings match `const` or `RECOVERED_REGION_GAME_IDS`/`UNNAMED_VARIANT_GAME_IDS` at `repo:prototype/osfr-tools/src/{mining.rs:49-50, harvesting.rs:52-57, cooking.rs:17, smelting.rs:16, forging.rs:17}`. The `client` table shows types 1 (IS_FLASH 0), 8, 9 and 14 (IS_FLASH 1) as the note says.
- **Not checked:** the 783/22/20/610 counts, the per-row receipt rows, and the 360/417/6 engine split. These need the lab bundle, which is outside the repo root.
