<!-- fleet job=bug-verify id=src-restoration-piece-056-rs-L1-f1 status=done turns=8 usd=0.0063 tokens(read,write,in,out)=[104386, 24591, 18, 4264] model=claude-haiku-5-5 -->
# medium: `prototype/osfr-tools/src/restoration/piece_056.rs:563-568`

**Verdict:** refuted

**Severity if confirmed:** n/a

**Evidence:**

1. **Module tree.** `piece_056.rs` is pulled into the library only as a private module: `prototype/osfr-tools/src/abilities.rs:14-16` is `#[allow(dead_code)] #[path = "restoration/piece_056.rs"] mod effect_packets;`, and `lib.rs:3` declares `pub mod abilities;`. So the file is compiled into the crate, but the `#[allow(dead_code)]` marks that not everything in it is used.

2. **No production caller of the claimed path.** A repo-wide search for `StatusLedger`, `decode_profile_rows`, `encode_profile_rows` and `read_payload` finds only:
   - definitions inside `piece_056.rs` (`:417` struct, `:428` impl, `:780` `decode_profile_rows`, `:770` `encode_profile_rows`);
   - `tests/piece_056.rs:42-45, 122, 186-375`, which includes the file directly with `#[path = "../src/restoration/piece_056.rs"]` (line 32) and calls `StatusLedger::restore(&rows, 0, 600)` (`:309`, `:319`) and `encode_profile_rows` (`:122`).
   
   Neither `StatusLedger::restore` nor `decode_profile_rows` has any caller in `src/` (the gateway, gameplay, or save-load code). `abilities.rs` uses only the packet helpers from this module: `encode_remove_effect_tag` (`abilities.rs:745`), `EffectTagPayload` (`:929`) and `encode_add_effect_tag` (`:954`). The `effect_packets(` helper at `piece_056.rs:607` is used internally.

3. **No wire input reaches `restore`.** Nothing in the gateway or gameplay dispatch calls `decode_profile_rows` (step 2 above). The claimed chain `decode_profile_rows` → `restore` is therefore not reachable from a remote player or a save load. The claim also says "the loader calls these", but no loader exists in the tree.

4. **The arithmetic is real but unreachable.** `piece_056.rs:563-564` (`stored - downtime_seconds.max(0)`) is unchecked, and `restore` lacks the `MAX_EFFECT_SECONDS` check that `apply` has at `:463`. These are accurate descriptions of the code. They do not matter because the function is only exercised by test code.

**Corrected fix:** not needed for the defect as stated. If the team wants hardening anyway (it is not a live bug), apply the same bounds in `restore` (`stored <= 0 || stored > MAX_EFFECT_SECONDS` → skip, and `saturating_sub`) before any future loader calls it. Treat it as a latent issue in test-only/dead code, not a medium-severity defect.
