<!-- fleet job=bug-verify id=src-restoration-piece-043-rs-L1-f2 status=done turns=4 usd=0.0037 tokens(read,write,in,out)=[29164, 18291, 10, 2162] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/restoration/piece_043.rs:458,460-468,401-411`

**Verdict:** refuted

**Severity if confirmed:** n/a

**Evidence:**

1. **Not in the real server (refutes at step 1).** `prototype/osfr-tools/src/restoration/piece_043.rs` is not declared anywhere in the library or binaries. A search for `mod (piece_|restoration)` under `prototype/osfr-tools/src` finds no `mod piece_043` in `lib.rs`, in any `mod.rs`, or in `src/bin/*`. The only module declaration of piece_043 in the repo is the test include at `prototype/osfr-tools/tests/piece_043.rs:33-35`:
   ```
   // The module is not registered in `src/lib.rs` (lead-owned). ...
   #[path = "../src/restoration/piece_043.rs"]
   #[allow(dead_code)]
   mod piece_043;
   ```
   So `ProgressionLedger`, `from_snapshot` and `snapshot` are compiled only into the `piece_043` integration test. That makes the defect test-only, which the skeptic checklist treats as a refutation.

2. **No production caller (confirms the reviewer's own "latent" note).** Searching for `ProgressionLedger|ProgressionSnapshot|from_snapshot` across `src/` finds only the piece_043 definitions (`piece_043.rs:378, 403, 413, 426, 460`) and the test file. The `from_snapshot` hits in `piece_010.rs` and `inventory.rs` are unrelated `TcgMatch::from_snapshot` and `allocate_from_snapshot` functions. No gateway or gameplay handler and no save-load path reaches the ledger, so input cannot reach it (step 2 also fails).

3. **The code and line references are accurate, but they do not change the outcome.** `credited` is a `BTreeSet` at `piece_043.rs:410`. `from_snapshot` sets `credited: BTreeSet::new()` at line 456. `snapshot()` at lines 460-468 omits it. The replay check at lines 528-530 (`if !self.credited.insert(...) { DuplicateOutcome }`) is in-memory only, as the reviewer says. The defect as described is real in the sense that the snapshot drops replay state. But the module is not shipped in the server, so it is not a live defect.

**Corrected fix:** not needed for a refutation. When the module is registered in `lib.rs` and given a caller, persist the credited `(source, instance_id)` pairs in `ProgressionSnapshot` (or document that the owning module enforces replay across sessions). Until then, this is a design note, not a bug in the running server.
