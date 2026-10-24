<!-- fleet job=pin-audit id=tests-piece-084-rs status=nothing_found turns=3 usd=0.0021 tokens(read,write,in,out)=[9921, 10457, 8, 1300] model=claude-haiku-5-5 -->
# tests/piece_084.rs

No findings in `prototype/osfr-tools/tests/piece_084.rs`.

The screened lines all derive from one value, the resell value of 27. The `ledger()` fixture (lines 46-53) sets it itself with `ledger.grant(79_388, 0, 5, 27, false)`. The file's own comment says it was copied from a community catalogue row (cost 400, resell 27), but the test does not read that row or any data file. Nothing in the test loads a value from `data/content/*.json`, so retuning a data file would not change these expectations. Each affected line is therefore a fixture-set number, which the rule excludes:

- 138, 150, 196, 226, 239: 81 = 3 × 27 and 27 are the fixture's resell value times quantity.
- 253: `buyback_cost(27, 5) == 135` is the same fixture value times 5.
- 260, 265: the balance of 15 follows from the 1,000 starting coins, the 135 sale, and the 1,120 sink, all set in the test.
- 357, 358: the resell value 27 is passed in by the fixture and the re-grant.

The other numbers (`i32::MAX` products, 1,000/1,081/1,135 balances, guids, ids, opcodes, and the 165 packet id) are arithmetic, fixture, protocol, or id values, not tunables.

One caveat: the 27 is a copy of a catalogue value, not a read from data. If the team wants the fixture tied to real data, read the resell value from the item definition row instead of hard-coding it. That is a cleanup, not a tunable-value pin.
