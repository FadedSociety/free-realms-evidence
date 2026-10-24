<!-- fleet job=pin-audit id=tests-soccer-entry-rs status=nothing_found turns=7 usd=0.0053 tokens(read,write,in,out)=[91816, 25083, 16, 2500] model=claude-haiku-5-5 -->
# tests/soccer_entry.rs

No findings in `prototype/osfr-tools/tests/soccer_entry.rs`. All three screened lines take their `10` from the test's own fixture, not from the shipped data.

- **Line 285, 778 (`+ 10`), 744 and 725 (`CLAIM_COINS + 10`):** the `10` is `"reward": {"coins": 10, ...}` in `soccer_content()` (lines 156 and 66). The test writes that `soccer.json` into its temp directory in `Fixture::new` (line 66) and again at line 572. The shipped `data/content/soccer.json` `reward.coins` (also 10, line 61) is never read by these assertions. The fixture sets the number, so it is not a finding.
- **`CLAIM_COINS` (line 37, value 25):** a test-local constant for the trusted claim grant (used at line 541). Its source is the test itself, and no shipped data file supplies that value, so it is not a finding.

The file already follows the rule: it builds its own content and does not pin a shipped tunable.
