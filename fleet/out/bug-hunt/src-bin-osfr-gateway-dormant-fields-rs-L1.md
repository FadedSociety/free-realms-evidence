<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-dormant-fields-rs-L1 status=nothing_found turns=5 usd=0.0014 tokens(read,write,in,out)=[15255, 5249, 12, 1150] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/dormant_fields.rs lines 1-40 of 40

No defects in `prototype/osfr-tools/src/bin/osfr_gateway/dormant_fields.rs` lines 1-40.

The whole file is a single `#[test]` function. It is compiled only under test: `prototype/osfr-tools/src/bin/osfr-gateway.rs:4541-4543` declares `#[cfg(test)] #[path = "osfr_gateway/dormant_fields.rs"] mod dormant_fields;`. Per the review rules, test code is not a defect, so there is nothing to report. The `unwrap`s and the `u64::MAX - due(u64::MAX)` helper are test-only, and nothing in the window is reachable from a client packet or a save.
