<!-- fleet job=bug-verify id=src-restoration-piece-069-rs-L1-f2 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[14228, 12477, 8, 1716] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/restoration/piece_069.rs:487-490

**Verdict:** refuted

**Severity if confirmed:** n/a (the code is not in the shipped server; the defect is test-only today)

**Evidence:**

1. **Module tree (step 1, decisive).** `prototype/osfr-tools/src/lib.rs` declares only `pub mod` entries for the crate modules, and nothing for `restoration` or `piece_069`. A search of the whole `prototype/osfr-tools` tree for `piece_069` returns only:
   - `tests/piece_069.rs:27-29`: `#[path = "../src/restoration/piece_069.rs"] mod piece_069;`
   - `tests/economy_review.rs:16-18`: the same `#[path]` include.
   - `src/restoration/piece_069.rs:71`: a comment saying the owned test target includes the file by path.

   `src/bin/osfr-gateway.rs` and `src/bin/osfr-login.rs` never reference it. The file is compiled only into the integration-test binaries. The repo notes agree: `notes/Reviews/Economy Independent Review.md:83` lists "Lead-owned `lib.rs` registration for `piece_069`/`piece_081`" as a pending step, and line 53 says the `candidate_*` tests include the modules "by `#[path]`".

2. **Input reach (step 2).** Because there is no module path from `lib.rs`, no gateway or gameplay handler can call `TurnInLedger::consider`, `commit` or `recover`. The append-failure retry scenario cannot occur in the running server.

3. **Line facts (step 3).** The cited lines are accurate as far as they go: `append` writes at 487, syncs at 489, and pushes to `records` at 490. `consider` calls `append` at 377. `commit` calls it at 417 and `recover` at 452. The retry analysis is plausible if the module were wired in. It is still moot until registration, and the reviewer's fix (truncate on failure, or push after fsync and check file state) would be a correct hardening to apply when the module is registered.

**Note:** Once piece_069 is registered in `lib.rs` and wired to a handler, this finding should be re-raised. Until then it is a latent issue in an unregistered module, not a live server defect.
