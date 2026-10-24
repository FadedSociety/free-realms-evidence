<!-- fleet job=pin-audit id=tests-sc-earnings-rs status=nothing_found turns=8 usd=0.0026 tokens(read,write,in,out)=[46430, 12083, 18, 1185] model=claude-haiku-5-5 -->
# tests/sc_earnings.rs

`prototype/osfr-tools/tests/sc_earnings.rs` does not exist in the repo: `read` returns "not a file", and the tests directory listing (`list`, which was truncated at 107 more entries) and a content search for `sc_earnings`, `next.wallet`, `again.wallet`, `restored.balance`, and `balance, 4/10/20)` found no such file or assertions. The four screened lines (331, 347, 365, 411) therefore cannot be checked against the file and are not findings as written.

Closest real match: `prototype/osfr-tools/tests/station_cash.rs:479` asserts `restored.balance == config.max_balance`, which reads from config rather than pinning a number, so it is not a finding.

If the file lives under another name or on another branch, send the path and I will audit it.
