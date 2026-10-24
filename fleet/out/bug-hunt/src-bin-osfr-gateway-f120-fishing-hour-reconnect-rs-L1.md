<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-f120-fishing-hour-reconnect-rs-L1 status=nothing_found turns=5 usd=0.0029 tokens(read,write,in,out)=[41698, 14279, 12, 1468] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/f120_fishing_hour_reconnect.rs lines 1-595 of 595

Window: `prototype/osfr-tools/src/bin/osfr_gateway/f120_fishing_hour_reconnect.rs` lines 1-595 (whole file read).

No defects reported. The entire file is test code and is excluded by the review rules:

- `prototype/osfr-tools/src/bin/osfr-gateway.rs:4523-4525` declares the module as `#[cfg(test)] #[path = "osfr_gateway/f120_fishing_hour_reconnect.rs"] mod f120_fishing_hour_reconnect;`. The file is compiled only under `cargo test`.
- The only item with production-looking visibility, `drain_replies` (line 147, `pub(super)`), is consumed only by other test modules: `t199_world_notice.rs:7`, `tests.rs` (many call sites), and `test_support.rs:310`. No non-test caller exists.
- Its `unwrap()` calls on `sender.poll`, `codec.decode`, and `acknowledge` (lines 150, 156, 179) and the slice indexing on `packet.payload` (lines 162, 166) are test-harness assertions on the test's own traffic, not reachable from a client packet on a live server.

The helpers (`request`, `register`, `cast`, `reel`, `lifecycle`, `menu`, `send`, `try_catch`, `coins`, `fisherman_xp`, `ledger`) and the `#[test]` at line 216 are all test-only. The test's `assert!`/`unwrap` usage is expected there and is not a finding.
