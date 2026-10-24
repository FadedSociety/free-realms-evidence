<!-- fleet job=note-refresh id=Kart-Race-Service status=done turns=24 usd=0.0324 tokens(read,write,in,out)=[1077422, 80969, 50, 22950] model=claude-haiku-5-5 -->
# notes/Research/Kart Race Service.md

**Verdict:** minor drift. The core service API, validation, bounds and refusal behaviour match the tip. The note is stale on pickup status, on the lead wiring and on the test count.

**Corrections:**

1. old: `CountdownSpoof`, `InvalidPhase`, `GateDisabled`, `NoOpenRace`.
   new: `CountdownSpoof`, `InvalidPhase`, `GateDisabled`, `NoOpenRace`, `ObservationBudget`, `ItemQueueFull`.
   why: repo:prototype/osfr-tools/src/kart_service.rs:422 (`ObservationBudget`) and :437 (`ItemQueueFull`) are refusal variants that the list omits.

2. old: only client positions), `33/6` and pickups are observations with no effect, other racers are not
   new: only client positions), `33/6` feeds only the opt-in weapon pose (`weapon_effects`), a pickup claim stages a live box and pushes its item type into the mirror queue (see the next line of the note), other racers are not
   why: repo:prototype/osfr-tools/src/kart_service.rs:1953 (`self.queued_items.push(staged.item_type())` in the `33/17` arm) and :2018 (`weapon_pose = Some(WeaponObservation …)` in the `33/6` arm). The module doc at :69-82 describes pickups as implemented through `kart_pickups`, with respawn.

3. old: * Pickups, gates-hit effects, derby and the return scene remain the lead's/other slices' work; the
   new: * Pickup claims and grants are implemented (`kart_pickups.rs`, the `33/15`-`33/18` path in `kart_service.rs`). The client owns each item's effect; gates-hit effects, derby and the return scene remain the lead's/other slices' work; the
   why: repo:prototype/osfr-tools/src/kart_pickups.rs:362 (`PickupSet::new`), repo:prototype/osfr-tools/src/kart_service.rs:1888-1953 (`PICKUP_HIT_SUBTYPE` arm) and :1649 (`spawn_pickups`).

4. old: ## Lead route and seams
   new: ## Lead route and seams

   Wired at tip, so the steps below are a record of the route, not a to-do list: `pub mod kart_service;` is at `src/lib.rs:48`; `kart_gateway.rs` holds the `KartService` (`:159`), restores or creates it (`:342`, `:347`), calls `set_gate(Enabled)` (`:353`, `:571`), `begin` (`:684`), `handle_inner` (`:697`) and `take_finished_session` (`:742`), and `gameplay.rs` uses `KartGateway` (`:201`, `:1066`).
   why: repo:prototype/osfr-tools/src/lib.rs:48; repo:prototype/osfr-tools/src/kart_gateway.rs:159, 342-353, 571, 684-697, 742; repo:prototype/osfr-tools/src/gameplay.rs:201, 1066.

5. old: # 19 passed; 0 failed; 1 ignored
   new: # 76 passed; 0 failed; 1 ignored (latest Autopilot run, F188; the 19 was the 2026-10-09 count)
   why: repo:notes/Autopilot/F188.md:131 (`cargo test --test kart_service`: 76 passed, 0 failed, 1 ignored). repo:notes/Research/Suite Status 2026-10-13.md:98 shows 73. The test file has 4095 lines, and the private gate `private_capture_route_is_accepted` at repo:prototype/osfr-tools/tests/kart_service.rs:3935-3937 is `#[ignore]`d, so "1 ignored" holds.

**Checked and holding:** `pub fn` signatures for `new`, `set_gate`, `session`, `finish_flag`, `take_finished_session`, `begin`, `start_race`, `tick`, `handle_inner`, `snapshot` and `restore` (kart_service.rs:1436-2113). `MIN_GATE_RADIUS_M = 3.0`, enforced at :1245. `default_max_observations` = 120_000 (:321-322). `ServiceError::CorruptSnapshot` bounds and clock checks in `restore` (:2182-2235). The 85-byte, 24-byte and 12-byte payload constants (:174-178). The private capture test asserts 31 hits and one lap (tests/kart_service.rs:3995, 4082-4086). The tests/kart_service.rs row in the artifacts table is correct.

**Unsure:**
- The `lab/reports/kart-service-20261009/` artifacts cannot be checked here: `/lab/` is gitignored and lives in the sibling `../lab` (repo:.gitignore:28).
- The `31 gates` content count and the capture timings are in the sibling lab, so they are unverified.
- The claim that a dedicated test drives one overlapping point through two consecutive gates: the search tool returned incomplete results for tests/kart_service.rs past about line 1400, so I could not confirm it.
- The `19/13/13/9 passed, 2 ignored` line for the other kart test files was not checked.
- The exact live test count: I did not re-run cargo. The count above comes from Autopilot F188.
