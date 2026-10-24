<!-- fleet job=test-verify id=tests-piece-018-rs-L1-f1 status=done turns=8 usd=0.0077 tokens(read,write,in,out)=[87531, 25940, 18, 7221] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_018.rs:401

**Verdict:** `confirmed`

**Evidence:**

- `tests/piece_018.rs:118-123`: `reply_text` maps both variants to their text: `Command::Reply(text) => text, Command::Route { reply, .. } => reply`. Every module-driver and derby check goes through it, so the variant is erased.
- Lines 404-413 (`mining`, `harvesting`, `fishing`, `kart_racing`, `soccer`) and 414-418 (`derby`) call `reply_text(command)` at 409 and 414. Nothing asserts `Command::Reply`.
- The walk-through with the claimed change (a `Command::Route { reply, actor, guid }` returned for a `ModuleDriver` route, with the same reply text): `handle(...).unwrap()` passes; `route(slug).entry` is still `ModuleDriver` (static table, line 406); `reply_text` returns the text; `api`, `driver` and `module_path` are all present in that text; `derby`'s `missing` text is present. Every assertion passes.
- The other tests that touch these routes don't close the gap:
  - `every_reply_carries_the_route_native_gate` (421-451) also uses `reply_text`.
  - `unknown_and_foreign_commands_are_left_alone` (327-340) uses `reply_text`.
  - `acceptance_status_is_limited_to_the_three_reviewed_movies` (294-314) checks the static `Entry`, not the returned `Command`.
  - The only `Command::Route` patterns (lines 351, 477, 507) assert that crafting routes *are* `Route`. None assert that module or derby routes are *not*.
  - The `#[ignore]` tests (457-520) cover only cooking, smelting and forging.
- No other test can catch it. `piece_018` is not registered in `src` (`grep` finds no `piece_018` module wiring; the header says the lead integrates it later). The module is compiled only via `#[path]` in this test file, so no app-level dispatch test exercises `Command::Route` for these routes.

The claim's fix is sound. Since `reply_text` consumes `command`, the assertion has to run before it, for example `assert!(matches!(command, Command::Reply(_)), "{slug} must not relocate");` placed before line 409. The same applies to line 414 for derby.

**Minimal fix:** Assert the variant before `reply_text` consumes the command, at lines 405-409 and 414: `assert!(matches!(command, Command::Reply(_)), "{slug} must not relocate");` (and the equivalent for `derby`). Optionally, add a canary that `handle` returns `Command::Reply` for every `ModuleDriver`/`Unrecovered` route in `routes()`.
