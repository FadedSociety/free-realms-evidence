<!-- fleet job=test-audit id=tests-type8-gateway-rs-L1 status=done turns=6 usd=0.0082 tokens(read,write,in,out)=[97651, 30661, 14, 6722] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/type8_gateway.rs lines 1-918 of 918

Window: `prototype/osfr-tools/tests/type8_gateway.rs` lines 1-918 (read in full). Most assertions in this window are meaningful: refusal tests compare full gateway snapshots, the loss and repeat-win tests check grant counts, and the orphan-output and wrong-game cases are rejected by real checks (`mining.rs:1168-1178`, `mining.rs:318`). Two findings:

- **[medium] prototype/osfr-tools/tests/type8_gateway.rs:608 active_mining_blocks_unrelated_actions_like_crafting - the name says crafting is blocked, but no crafting frame is ever sent.** The blocked frames are class select (`26/13`), interact (`26/8`), interact-select (`26/10`), equip (`36/10`), inventory (`42/3`), plus a teleport chat. None of them is a crafting request.
  - **Why it cannot catch a regression:** a change that lets crafting start during a live Mining run would leave every assertion in this test passing, because crafting is never exercised.
  - **Fix:** add the real crafting frame (or the crafting chat command) to the blocked list and assert `chat_text` contains "Close the mining game" and the snapshot is unchanged. Alternatively, rename the test to match the actions it covers.

- **[low] prototype/osfr-tools/tests/type8_gateway.rs:808 mining_content_loads_fail_closed_without_a_bound_file - the bad-binding cases only assert `Gameplay::load(...).is_err()`, so any error passes.** The comments say the wrong job must be refused by the job binding, but a malformed fixture or an unrelated failure would also satisfy the assertion. The job check's message is "mining content does not bind the Miner job" (`gameplay.rs:847`).
  - **Why it cannot catch a regression:** if the job check were removed or reordered, a different error from the same file would still make `is_err()` true. The test would then pass without the binding being enforced.
  - **Fix:** match the error text for each case, e.g. `err.to_string().contains("does not bind the Miner job")` for the wrong-job case and the matching invalid-message for the wrong-game and orphan cases.

Nothing in the window is `#[ignore]`d or returns early on a missing fixture. The `OSFR_TYPE8_CONTENT` base directory is an env var with a default path, not a silent skip. The dump step at lines 913-915 is opt-in by env var, so it does not skip assertions.
