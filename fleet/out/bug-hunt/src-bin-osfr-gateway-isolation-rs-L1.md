<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-isolation-rs-L1 status=nothing_found turns=4 usd=0.0017 tokens(read,write,in,out)=[16818, 8210, 10, 1101] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/isolation.rs lines 1-213 of 213

No defects in `prototype/osfr-tools/src/bin/osfr_gateway/isolation.rs` lines 1-213.

The whole file is test-only code. `osfr-gateway.rs:4531-4533` declares it as `#[cfg(test)] #[path = "osfr_gateway/isolation.rs"] mod isolation;`, and every item in the window is a `#[test]` function, a `#[cfg(test)]`-gated helper (`movie_gateway`), or the `thread_local!` `PANIC_IN_TICK` hook. The only production-side reference is `osfr-gateway.rs:2442-2445`, which is itself `#[cfg(test)]`. The rules exclude code in `#[cfg(test)]`, so nothing here is reportable.

I did not look for defects in the production code the tests exercise (`Server::step`, `commit_outcome`, the session cleanup path). Those lie outside this window.
