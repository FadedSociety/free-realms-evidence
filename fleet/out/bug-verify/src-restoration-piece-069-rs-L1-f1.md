<!-- fleet job=bug-verify id=src-restoration-piece-069-rs-L1-f1 status=done turns=4 usd=0.0043 tokens(read,write,in,out)=[33846, 21371, 10, 2487] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/restoration/piece_069.rs:479

**Verdict:** refuted (the defect is real as code, but it is test-only and unreachable from the shipped server).

**Severity if confirmed:** n/a. The claimed `medium` does not apply to the running server.

**Evidence:**
1. **Module tree (step 1 fails).** `prototype/osfr-tools/src/lib.rs` declares `pub mod` entries (lines 3-22 and onward) but no `restoration` module and no `piece_069`. A search of `src/` for `piece_069` finds only a comment at `src/restoration/piece_069.rs:71`. `TurnInLedger` appears in no file under `src/` except `piece_069.rs` itself. The only includes are `#[path = "../src/restoration/piece_069.rs"] mod piece_069;` in `tests/piece_069.rs:27-29` and `tests/economy_review.rs:16-18`. That test file says the module "is not registered in `src/lib.rs` (lead-owned)" (`tests/piece_069.rs:23-25`).
2. **Input reach (step 2 fails).** Since nothing in `src/` calls `consider`, `commit` or `recover`, no packet handler or save load can reach `append` at `piece_069.rs:473-492`. The gateway and gameplay code paths never touch the ledger.
3. **Accuracy of the code claim (step 3).** The line numbers and the check are as described: `piece_069.rs:272-273` (the `open` size check), `:474` (the record cap) and `:479` (`line.len() + self.records.len() > MAX_LEDGER_BYTES`). The file total is indeed not tracked, so the bug exists inside the test-compiled module. It does not matter for the shipped server, which never compiles this code.

**Corrected fix:** not needed for the server. If the module is later registered by the lead, the byte-tracking fix from the claim (a `bytes` field set from `bytes.len()` in `open`, incremented in `append`, checked against `self.bytes + line.len() + 1`) would be the right change. It should be filed as a latent issue for the integration step, not as a live defect.
