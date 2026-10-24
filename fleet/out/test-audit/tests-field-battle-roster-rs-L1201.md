<!-- fleet job=test-audit id=tests-field-battle-roster-rs-L1201 status=nothing_found turns=9 usd=0.0080 tokens(read,write,in,out)=[107117, 25010, 20, 7620] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/field_battle_roster.rs lines 1201-1509 of 1509

Reviewed `prototype/osfr-tools/tests/field_battle_roster.rs` lines 1201-1509 (tests `an_ungrantable_prize_quantity_is_refused_through_gameplay`, `cancel_mid_battle_returns_to_the_marker_without_paying`, `closing_the_start_screen_releases_the_pending_go`, `another_begin_consumes_the_open_start_screen`, `go_from_outside_the_marker_radius_is_inert`, `go_while_knocked_out_refuses_instead_of_ending_the_session`) against the code under test. No findings meet the five criteria.

What I checked:
- **No `#[ignore]`, no early `return`, no fixture-dependent skip** in the window.
- **Cannot-fail:** none. The expected values are literals or come from independent observations (the row's prize ids, the marker position, the screen bytes captured earlier). The refusal assertions compare against the stored `before` snapshot and the chat text `"one of its rewards cannot be granted"`, which matches `UNAVAILABLE_BATTLE_PRIZE` in `src/gameplay/field_battle.rs:11`.
- **Sensitivity of the Go-replay assertions:** if the Close (26/42) or leave (41/109) packet stopped releasing the pending battle, the subsequent Go would start the arena, so `began_zoning` would be true and the test would fail. The same holds for dropping the 8 m radius (`BATTLE_SCREEN_RADIUS`, `src/encounter/field.rs:28`): the walk helper (`field_battle_roster.rs:448`) asserts the player reaches the 50 m target, so the Go is genuinely out of reach.
- **Knocked-out path:** `receive_field_damage` sets `player_health` to 0 (asserted), and `begin` returns "cannot begin an encounter while knocked out" (`src/encounter.rs:1367`), which `refuse_battle` turns into a chat refusal that reopens the same screen. The test checks the chat text, the reopened screen bytes, and an unchanged snapshot, both on the first and repeated Go.
- **Ungrantable prize:** the first two assertions pin the boundary (`accepts_reward` true at `max_stack`, false at `max_stack + 1`), so the later refusal is attributable to quantity. The gameplay refusal path (`battle_prizes_available`, `src/gameplay/field_battle.rs:27`) matches the test name.
- **Cancel test:** `economy` (coins, per-prize counts, experience) is compared before and after the cancel, and the replayed cancel is checked for no change.

Minor observations that are not reportable under the criteria: the two Close/leave steps assert only `!began_zoning` for the dismissing packet itself, so they rely on the subsequent Go replay to prove the release. That is still a sensitive check, so I did not report it.
