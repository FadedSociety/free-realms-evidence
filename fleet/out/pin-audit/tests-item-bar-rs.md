<!-- fleet job=pin-audit id=tests-item-bar-rs status=nothing_found turns=5 usd=0.0029 tokens(read,write,in,out)=[31749, 14122, 12, 1721] model=claude-haiku-5-5 -->
# tests/item_bar.rs

No findings in `prototype/osfr-tools/tests/item_bar.rs` for the four screened lines (394, 435, 454, 536).

Where the 35 comes from:
- `Fixture::bar()` (tests/item_bar.rs:143-145) calls `ItemBar::load(&self.path, Default::default(), None)`. It does not write a `consumables.json`, so it gets `Effects::default()`.
- `Effects::default()` in `src/item_bar.rs:77-89` hard-codes `heal_percent: 35` (and `cooldown_ms: 10_000`) for definitions 2173 and 11002.
- No shipped file under `data/content/` contains a consumables table or a `heal_percent` field. A search for `heal_percent` under `data` returned nothing.

So the expected 35 does not equal any value from a shipped data file. By the audit rule, these are not findings.

Side note, not a test finding: the live heal value is a code constant, not a data value. The data-file override (`consumables.json`) is the tunable path, and the shipped default is only in code. If Bryce's rule is meant to cover this too, the fix belongs in the source: ship a `data/content/consumables.json` and have the default load from it. The tests would then read the row (for example through `Effects::load(&fixture.path)` and `.get(SMALL)`, as the test at tests/item_bar.rs:641-647 already does) instead of pinning 35.
