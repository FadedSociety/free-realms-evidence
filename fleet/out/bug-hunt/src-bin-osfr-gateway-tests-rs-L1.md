<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-tests-rs-L1 status=nothing_found turns=7 usd=0.0044 tokens(read,write,in,out)=[83230, 20448, 16, 2038] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/tests.rs lines 1-800 of 1772

No findings in `prototype/osfr-tools/src/bin/osfr_gateway/tests.rs` lines 1-800.

Why the window is out of scope: the whole file is test-only code. `prototype/osfr-tools/src/bin/osfr-gateway.rs:4519-4521` declares it as `#[cfg(test)] #[path = "osfr_gateway/tests.rs"] mod tests;`, so nothing in it ships in the release binary. The brief excludes `#[cfg(test)]` code from defect review.

I read the full window (1-300, 300-560, 560-800). It is fixtures, `Options` setup, hand-built wire packets, and assertions. The panicking `unwrap`s and indexing there are test assertions, not defects on client input. Client-controlled values are not reached in production through this file.

I did not review production code the tests exercise (e.g. `trace::parse_hex`, `dispatch_message`, `BundleBudget`). Those belong to other windows.
