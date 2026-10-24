<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-test-support-rs-L1 status=nothing_found turns=6 usd=0.0031 tokens(read,write,in,out)=[44674, 13314, 14, 2020] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/test_support.rs lines 1-356 of 356

No defects found in `prototype/osfr-tools/src/bin/osfr_gateway/test_support.rs` lines 1-356.

Why nothing qualifies:

- **The whole file is test-only.** `tests.rs:926-929` declares it as `#[cfg(test)] #[path = "test_support.rs"] pub(super) mod test_support;`, and the file's own header says production never includes it. The task excludes `#[cfg(test)]` code from the defect categories.
- **Nothing in the window reads client input.** The helpers build fixtures from constants and test-chosen values (`Scratch::new`, `vendor_content`, `item_catalogue`, `options`, `enter`, `save_character`, `Scene::*`, `break_next_save`, `repair_save`, `bin_test_target`). The only client-shaped bytes are the hand-built login body in `enter` (lines 199-214), and its lengths come from the test's own literals.
- **The panic-on-failure helpers are intentional.** `unwrap`/`expect` in `Scratch::new`, `session`, `enter` and `Scene::tick`, and the `panic!` in `Scene::exchange`, are how these tests fail fast on fixture setup. They are not reachable from a player's packets.
- **Nothing here checks server state that a client could influence.** `break_next_save` and `repair_save` only swap the session's `state_path` for a test scenario.

I checked two candidates and dropped them. `bin_test_target` uses the compile-time `option_env!("CARGO_BIN_NAME")`, which I judged correct for distinguishing the binary's own test target from embedded copies. `Scratch::new` removes and recreates its directory, which is fine for a unique, per-process path.
