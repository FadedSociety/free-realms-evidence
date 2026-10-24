<!-- fleet job=bug-verify id=src-restoration-piece-030-rs-L1-f1 status=done turns=4 usd=0.0033 tokens(read,write,in,out)=[24397, 14614, 10, 2373] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/restoration/piece_030.rs:711-778`

**Verdict:** refuted

**Severity if confirmed:** n/a (the code is test-only, so no server impact)

**Evidence:**

1. **Module tree (decisive).** `src/restoration/piece_030.rs` is not registered in the crate. A search of `prototype/osfr-tools` for `piece_030|native_evidence_complete|evaluate_transcript` returns only:
   - `prototype/osfr-tools/src/restoration/piece_030.rs:442` (`native_evidence_complete`), `:482`, `:511` (`evaluate_transcript`), `:1460`
   - `prototype/osfr-tools/tests/piece_030.rs:3`, `:26-28` (`#[path = "../src/restoration/piece_030.rs"] mod piece_030;`), and the test call sites at `:96`, `:216`, `:261`, `:502`, `:514`, `:534`, `:592`

   No `mod piece_030` or `pub mod piece_030` appears in `src/lib.rs`, `src/bin/*`, or any `mod.rs`. The only `mod restoration` hits are in `src/restoration/*` comments that say the lead has not registered the modules yet. The restoration modules that are live are pulled in with `#[path]` from specific owners, such as `abilities.rs:15`, `inventory.rs:40` and `item_bar.rs:42`, and piece_030 is not one of them. So `evaluate_transcript`, `evaluate_place` and `native_evidence_complete` run only inside the `tests/piece_030.rs` test crate. No gateway or gameplay packet handler and no save load can reach them. Step 1 of the check refutes the claim.

2. **Reach (moot, but for the record).** The claim's chain is `evaluate_transcript` → `evaluate_gate` → `evaluate_place`. In the tree, the only entry is the test crate. The claimed check at `piece_030.rs:714` (`rows.iter().find(... PlaceFixture ...)`) and the loop at `:748-758` read as described. The defect is logically real inside the verifier, which only examines the first placement. That is a limitation of a test-only evidence checker, not a defect in the shipped server.

3. **Not a server defect.** Nothing in `src/` calls the piece_030 gate, so a remote player cannot trigger a crash, save corruption, or item/coin gain through this code.

**Corrected fix:** none needed for the server. If the team wants the verifier to be stricter, the `find` at `:712-715` could become a loop over all `PlaceFixture` rows, as the claim suggests. That is a test-tooling improvement, not a medium-severity defect.
</result>
