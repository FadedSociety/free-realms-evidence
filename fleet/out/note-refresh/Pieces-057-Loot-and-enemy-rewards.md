<!-- fleet job=note-refresh id=Pieces-057-Loot-and-enemy-rewards status=done turns=12 usd=0.0171 tokens(read,write,in,out)=[376726, 64034, 26, 10632] model=claude-haiku-5-5 -->
# notes/Research/Pieces/057 Loot and enemy rewards.md

**Verdict:** current, with one minor drift. The module, tests, oracle and wiki/locale/item joins all match the tip. Only one qualifier is false.

**Corrections:**

- `old:` (sha256 `0b0296ac…`): the only weighted
  `new:` (sha256 `0b0296ac…`): the only weighted *reward* table. `Sanctuary/src/Resources/CollectionNodeTypes.json` also carries `Weight` rows (100 each) for collection-node drops, so it is a weighted table but not a reward table.
  `why:` refs `Sanctuary/src/Resources/CollectionNodeTypes.json:12-17` and `:30-31` (`"Weight": 100`); `Sanctuary/src/Resources/Rewards.json:3-28` is the only reward table.

**Checked and holding:**

- Paths exist: `prototype/osfr-tools/src/restoration/piece_057.rs` (461 lines), `prototype/osfr-tools/tests/piece_057.rs` (11 `#[test]`s), `scripts/pieces/piece_057.py`, `tests/pieces/test_piece_057.py` (19 `def test_`s).
- Not registered: no `piece_057` or `restoration` mod in `prototype/osfr-tools/src/lib.rs`. The module is `#[path]`-included in the test only.
- `weighted_from_documented()` always returns `Err(LootGap::NoProbabilityData)` (`piece_057.rs:249-251`).
- `LootLedger` policy (`piece_057.rs:433-452`): killer-only, registered defeat, once per kill, caller-supplied roll. It grants nothing itself.
- Prop plan: boss gives `Chest`, normal enemy gives `SmallBag` plus `Coins` (`piece_057.rs:78-84`).
- Documented-list counts: 35 entries, 5 Coins, 30 items, 5 joined (3 distinct), 25 unjoined, 6 with no locale row. Per-page revisions 48775, 45373, 45371, 50196 and 45434 match the wiki filenames. The "Drops from Chest" heading and "from the treasure chest" text are at `freerealms-wiki/wikitext/8112-50196-*.wiki:11-12`.
- Model rows 720/807/808/841 are in `Sanctuary/src/Resources/Models.txt:721,808,809,842`. Locale 2, 3 and 4923 match. Item ids 18172, 38822 and 38827 are present in the client item definitions.
- Sub-opcode 29 (`FUN_0089fbb0(0x1d)`) is recorded in the Native Map notes. `Rewards.json` is `dev-test-reward` with item 205 and 50 coins, both weight 1. The table also has tint rows 227 and 231, which the note leaves out. That omission is not false.

**Unsure:**

- The oracle's "107 checks" and the Python/Rust test passes cannot be re-run from the tip. The `lab/reports/piece-057-*` directories are outside the repo, so I could not confirm them.
- The "defeat branch that already emits 35/3" hook is not settled. `prototype/osfr-tools/src/encounter.rs:3081` builds a `header(35, 3)`, but I did not trace it to the defeat path.
