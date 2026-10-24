<!-- fleet job=note-refresh id=Housing-Service-Integration status=done turns=20 usd=0.0306 tokens(read,write,in,out)=[683289, 71411, 42, 29669] model=claude-haiku-5-5 -->
# notes/Research/Housing Service Integration.md

**Verdict:** badly stale. The service, its tests and the gateway wiring exist, but the note still describes the pre-integration state: "lead hook" steps that are already done, and two decode claims (127/5, 127/20 and the reply table) that the code has since changed.

**Corrections:**

1. Codec item 2 (127/5), the whole item from "block is opaque" to "decoded."
   - `old:` "block is opaque and nothing identifies the fixture, so `handle` answers `SaveFixture` with\n    `ServiceError::UnresolvedRequest { opcode: 5, missing: [...] }`. Movement is reachable only\n    through the typed `move_fixture` command until 5/51 are decoded."
   - `new:` "block is opaque, but the fixture guid is its first eight bytes, so `decode_request` returns `Request::Move` for opcode 5 and `handle` routes it to `move_fixture`. Only the opaque tail stays unread. `SaveFixture` / `UnresolvedRequest { opcode: 5 }` is no longer reachable from the wire."
   - `why:` repo:prototype/osfr-tools/src/housing_service.rs:457-483 (OP_SAVE branch reads guid, transform; returns `Request::Move`); :1277-1283 (`handle` routes Move to `move_fixture`); :1294-1297 (SaveFixture arm now unreachable for opcode 5); repo:prototype/osfr-tools/tests/housing_service.rs:502-508 and :855-860 pin `save_frame(9)` decoding to `Request::Move`.

2. Table row "Request / decode_request", cell about 1/5/20.
   - `old:` 1/5/20 as typed non-actions
   - `new:` 1 binds a selection (`fixture_asset`, offers the owned item); 5 decodes as a typed move (`Request::Move`); 20 is a preview answered with an unrecovered 42
   - `why:` repo:prototype/osfr-tools/src/housing_service.rs:1871-1882 (fixture_asset calls `offer`); :457-483 (5 -> Move); :1291-1293 (20 -> unrecovered 42)

3. Table row "HousingReply", cell about Unrecovered.
   - `old:` `Unrecovered { opcode }` for 28/39/42/51
   - `new:` `Unrecovered { opcode }` for 42 only (the 127/20 preview); 28, 39, 42 (127/1 fixture asset) and 51 (`PositionUpdate`) are encoded
   - `why:` repo:prototype/osfr-tools/src/housing_service.rs:81-90 (REPLY_* consts incl. REPLY_POSITION = 51); :718-730 (variants incl. PositionUpdate); :754-762 (encode arms); :1292 (only unrecovered use); :1343 (PositionUpdate reply from move)

4. Codec item 3, first sentence.
   - `old:` 3. **`127/51`, `127/42`, `127/28`, `127/39`.** Reply bodies are unrecovered, so the replies are
   - `new:` 3. **`127/20` preview (42).** Its reply body is unrecovered, so the reply is
   - `why:` repo:prototype/osfr-tools/src/housing_service.rs:1291-1293, 754-762, 1343; the following line ("`encode_inner()` on those returns `io::ErrorKind::Unsupported`") still holds for 42 via 127/20.

5. Exact lead hooks, item 1 header (gateway).
   - `old:` 1. **Gateway dispatch (`src/gateway.rs` -> `Gameplay::handle_in_world`/`handle`).** Add a branch
   - `new:` 1. **Gateway dispatch (wired at `src/gameplay.rs:2239` -> `Gameplay::handle_housing`, `src/gameplay/housing.rs:81`; original plan:).** Add a branch
   - `why:` repo:prototype/osfr-tools/src/gameplay.rs:2239 (`self.handle_housing(inner, character)` before the mounts fall-through); repo:prototype/osfr-tools/src/gameplay/housing.rs:81-110. `src/gateway.rs` contains no housing dispatch.

6. Exact lead hooks, item 1, silent-drop rule (part A).
   - `old:` `MalformedRequest` and `UnresolvedRequest` should stay silent drops, matching the
   - `new:` `MalformedRequest` and `UnresolvedRequest` get the chat line from `denial_message()` (no 127/53 unless `answers_with_denial()`, as wired), which replaces the
   - `why:` repo:prototype/osfr-tools/src/gameplay/housing.rs:97-108 (every `Err` pushes `chat::system(&error.denial_message())`; 127/53 only when `decode_request(inner)...answers_with_denial()`); repo:prototype/osfr-tools/src/housing_service.rs:378-390 (answers_with_denial covers 1, 2, 3, 4, 6 only).

7. Exact lead hooks, item 1, silent-drop rule (part B).
   - `old:` current swallowed behaviour but visible in the log.
   - `new:` earlier silent drop, now a chat line for the player.
   - `why:` as in correction 6.

8. Exact lead hooks, item 2 (restore call).
   - `old:` `HousingService::from_state(FixtureConfig::capture_defaults(), state, &self.inventory.state())`.
   - `new:` `HousingService::from_state_with_content(FixtureConfig::capture_defaults(), content, state, &inventory)`, with `content` loaded from `houses.json` (state field already present at `src/gameplay.rs:139`).
   - `why:` repo:prototype/osfr-tools/src/gameplay/housing.rs:31-51 (load: `HousingContent::load(houses.json)`, `from_state_with_content`); repo:prototype/osfr-tools/src/gameplay.rs:139, 262, 1147, 1377.

9. Header, "No native acceptance" paragraph.
   - `old:` The gateway hook below is the lead's integration step.
   - `new:` The gateway hook below is already wired (`src/gameplay.rs:2239`, `src/gameplay/housing.rs:81`); live acceptance is still the lead's step.
   - `why:` repo:prototype/osfr-tools/src/gameplay.rs:2239; repo:prototype/osfr-tools/src/gameplay/housing.rs:81. Also repo:prototype/osfr-tools/src/lib.rs:32 (`pub mod housing_service;` is registered, so hook 4's registration step is done; the `tests/housing_service.rs` file has no `#[path]` include).

**Unsure:**

- **Test counts.** The note says `--test housing_service`: 19 passed. Autopilot reports say 33 passed (`notes/Autopilot/L031.md:84`, `notes/Autopilot/L045.md:133`). I could not settle the current count without running the tests; the test file has at least 15 named test fns plus helpers (`tests/housing_service.rs:512`–`1758`). Treat the 19 as the old run's number.
- **Evidence paths under `lab/`.** `lab/references/...`, `lab/decompiled/...` and `lab/reports/housing-service-repair-20261009/` do not exist in the repo tip (`lab` is not a directory at the repo root). They may live outside the tip, so I did not correct them.
- **`#[path]` for piece_025.** `src/housing_service.rs:58` still uses `#[path = "restoration/piece_025.rs"]`, and `lib.rs` has no `restoration` module, so the "not registered yet" statement still holds.
- **Fixture defaults.** The seven `capture_defaults()` triples match the note (`src/housing_service.rs:857-865`). I did not check the 127/40 pcap source.
