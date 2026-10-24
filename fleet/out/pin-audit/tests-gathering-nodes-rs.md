<!-- fleet job=pin-audit id=tests-gathering-nodes-rs status=nothing_found turns=6 usd=0.0035 tokens(read,write,in,out)=[42419, 14993, 14, 2375] model=claude-haiku-5-5 -->
# tests/gathering_nodes.rs

No findings in `prototype/osfr-tools/tests/gathering_nodes.rs` for the two screened lines.

- **Line 624 `(R) Miner XP per win` (25):** the 25 comes from the code constant `RECONSTRUCTED_MINER_XP_PER_WIN` (`prototype/osfr-tools/src/mining_lifecycle.rs:22`), not from a file under `data/content`. A grep of `data/` finds no 25-per-win mining XP row. The rule covers only data-file values, so this is not a finding. It is still a hard-coded copy of a value the test already imports, so `xp(&gateway, MINING)` could be compared to `RECONSTRUCTED_MINER_XP_PER_WIN` directly if the team wants it to follow the constant.
- **Line 780 `ore ... vec![2; game.goals]`:** the 2 is the test's own count of two wins, each paying one ore per goal. The per-win payout of 1 is set by the test's `win()` helper (lines 437-454) and the `OUTPUTS`/`VALUES` fixtures (lines 38-39), not by a data file. Not a finding.
