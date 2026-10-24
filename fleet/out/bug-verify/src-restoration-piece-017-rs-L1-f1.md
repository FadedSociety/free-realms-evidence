<!-- fleet job=bug-verify id=src-restoration-piece-017-rs-L1-f1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[28388, 17509, 10, 2303] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/restoration/piece_017.rs:186

**Verdict:** refuted (test-only code, so it cannot reach the live server)

**Severity if confirmed:** n/a

**Evidence:**

1. **Module tree (decisive).** `src/restoration/piece_017.rs` is not declared anywhere in the library or binaries. `src/lib.rs` has `pub mod` lines for other modules, but no `restoration` module and no `piece_017`. The only include of the file is `prototype/osfr-tools/tests/piece_017.rs:6-7`: `#[path = "../src/restoration/piece_017.rs"] mod piece_017;`. The file's own header (`piece_017.rs:3`, `tests/piece_017.rs:3-4`) and the work-item notes say it is "included by path until the lead registers it in `lib.rs`".

2. **No production caller.** A repo-wide search of `prototype/osfr-tools/src` for `audit_recovery`, `audit_conservation` finds only their definitions in `piece_017.rs:111` and `:204-206`. The `initialize_world` hits (`gameplay.rs:1680`, `gateway.rs:1484`) are the real disconnect/world-load path, and they do not call this audit. Nothing in the gateway or gameplay dispatch reaches `audit_recovery`.

3. **Reachability.** Because the audit has no packet or save-load caller, the claimed "remote player" path (input → `audit_recovery` → `audit_conservation`) does not exist in the shipped server. The claimed reuse of `next_instance_id` would have to come from the real allocator, and the finding does not show that. The claim only describes a checker's acceptance of a hypothetical post-state.

4. **Failure arithmetic not checked further.** I did not need to verify lines 155/183/186 in detail, since the defect is not reachable. For the record, the lines the claim cites match the file (`piece_017.rs:155`, `:183`, `:186`), and the doc comment at `:108-110` says what the claim quotes.

**Corrected fix:** not applicable. If the lead later registers the module and wires `audit_recovery` into a live path, the reviewer's suggested bound (`replacement < counter(after)`, i.e., the replacement must sit below the advanced counter) would be worth re-evaluating then. Right now it guards only a test contract.
