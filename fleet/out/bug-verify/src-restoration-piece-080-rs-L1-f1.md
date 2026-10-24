<!-- fleet job=bug-verify id=src-restoration-piece-080-rs-L1-f1 status=done turns=4 usd=0.0040 tokens(read,write,in,out)=[26689, 20640, 10, 2234] model=claude-haiku-5-5 -->
# medium: prototype/osfr-tools/src/restoration/piece_080.rs:400

**Verdict:** refuted (step 1: the code is not in the real server; it is test-only).

**Severity if confirmed:** n/a

**Evidence:**
- No module tree includes `piece_080`. A repo-wide search of `prototype/osfr-tools/src` for `restoration|piece_0` shows no `mod restoration` in `src/lib.rs` or any `mod.rs`. The only `piece_080` include is `prototype/osfr-tools/tests/piece_080.rs:22-24`: `#[path = "../src/restoration/piece_080.rs"] mod piece_080;`.
- `CollisionSection`, `from_gcnk` and `parse` are referenced only inside `src/restoration/piece_080.rs` itself and in `tests/piece_080.rs` (lines 130-201). No file under `src/` (including the binaries `osfr-gateway.rs` and `osfr-login.rs`, and the other `#[path]` includes such as `piece_081`, `piece_093` and `piece_098`) calls `from_gcnk`, `CollisionSection`, or `piece_080`.
- The arithmetic is as described: `piece_080.rs:400` is `root_node_index + subtree_size > node_count as u32`, unchecked, and line 403 repeats the addition. So the wrap is real in release builds and a panic in debug. But the only caller is an integration test that feeds synthetic or preserved-chunk bytes. No remote packet or save-load path reaches it, so the severity is not a server risk.
- The work item (`notes/WorkItems/080.md`) and the readiness review list the module as unregistered, with the test using `#[path]` "until the lead registers it", which agrees with this reading.

**Corrected fix:** not needed for the server. The overflow is still worth fixing as hygiene, using the widened check the reviewer proposed (`(root_node_index as u64) + (subtree_size as u64) > node_count as u64`), and it would become a real issue only if `piece_080` is registered in `lib.rs` and wired to the GCNK loader. That wiring would then need to be re-reviewed.
