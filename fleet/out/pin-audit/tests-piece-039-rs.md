<!-- fleet job=pin-audit id=tests-piece-039-rs status=nothing_found turns=3 usd=0.0022 tokens(read,write,in,out)=[11378, 10322, 8, 1559] model=claude-haiku-5-5 -->
# tests/piece_039.rs

No findings in `prototype/osfr-tools/tests/piece_039.rs` for the screened lines (156-161, 169-171, 178).

- The expected values come from the recovered farm xp ladder. The test's own `FARM_XP_REQUIRED` const (test lines 44-47) mirrors `FARM_RANKS_58` in `prototype/osfr-tools/src/restoration/piece_039.rs:101-122`, which is hard-coded to the original client `FactoryRanks.txt` (header comments, test lines 4-8).
- No `data/content/*.json` file carries farm rank or xp values. A search of `prototype/osfr-tools/data` for `xp_required`, `FactoryRanks`, and `rank_max` returned nothing, so retuning a data value cannot break these assertions.
- Lines 156-161 and 169-178 are derived from that recovered ladder (for example 540 and 990 for ranks 3 and 4, giving 160 and 450 at 700 xp; 180 for rank 2). 700 is the test's own input. The ladder is recovered historical content and is not a live-tunable data value, so these are not findings under the stated rule.
