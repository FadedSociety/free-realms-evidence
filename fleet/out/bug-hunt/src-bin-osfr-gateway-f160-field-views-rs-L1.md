<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-f160-field-views-rs-L1 status=nothing_found turns=5 usd=0.0026 tokens(read,write,in,out)=[30767, 11694, 12, 1756] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/f160_field_views.rs lines 1-355 of 355

Window reviewed: `prototype/osfr-tools/src/bin/osfr_gateway/f160_field_views.rs` lines 1-355 (the whole file).

No reportable defects. The entire file is test-only code and falls under the "not defects" rule:

- `prototype/osfr-tools/src/bin/osfr-gateway.rs:4537-4539` declares the module as `#[cfg(test)] #[path = "osfr_gateway/f160_field_views.rs"] mod f160_field_views;`. Everything in the window is compiled only for `cargo test`, so none of it runs in the shipped server and none of it is reachable from a client packet or a save.
- The helpers `Server::test_set_ready` (line 9) and `Server::test_lose_world` (line 32) are `pub fn` in an `impl Server` block, but they sit inside that same cfg(test) module. They are used only from `tests/shared_field_interest.rs:382` and `:411`.
- The `#[test]` functions (lines 57-114 and 186-355) and their fixtures (`sender`, `f213_login`, `f213_npc_position`, `f213_sender`, `f213_application_body`, `f213_bodies`) are test code. The unchecked indexing and `unwrap`s in them, such as `end[6..14]` at line 299 and `body[4..12]` at line 284, read test-built buffers and are not client input.

I did not find a production-path logic error here, so there is nothing to attribute to a shipped code path. The production code that the tests drive (`Server::tick_shared_fields`, `Server::sync_field_views`, and `ReliableSender`) is outside this window and was not reviewed.
