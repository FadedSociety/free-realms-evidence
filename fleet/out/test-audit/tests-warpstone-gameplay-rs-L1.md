<!-- fleet job=test-audit id=tests-warpstone-gameplay-rs-L1 status=nothing_found turns=10 usd=0.0110 tokens(read,write,in,out)=[156567, 34192, 22, 10265] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/warpstone_gameplay.rs lines 1-176 of 176

No findings in `repo:prototype/osfr-tools/tests/warpstone_gameplay.rs` lines 1-176. Every assertion in the window can fail on a plausible regression, and nothing is silently skipped.

What I checked against the code under test:
- **Fixture (`content()`, `game()`, lines 24-47):** `Gameplay::load` returns an error on a missing directory and the helper unwraps it, so a missing fixture panics rather than passing. No early return and no `#[ignore]`.
- **Attunement and 57 refresh (`attune_sanctuary`, 82-87):** `WarpRegistry::visit` (piece_077.rs:1102-1131) returns `changed: true` and the refreshed list only when a fresh stone is in range, so the `changed` and `[vec![5]]` checks are real.
- **Empty list and no save before a visit (93-94):** `warpstones` is serialized only when non-empty (gameplay.rs:1370), so `is_none()` is meaningful.
- **Relog (97-110):** `Gameplay::load` restores `warpstones` (gameplay.rs:608-609), and the test then travels from the reloaded state, so the round-trip is exercised.
- **Forged ids and malformed body (113-133):** unknown, non-warpstone and locked ids all map to the "have not attuned" notice (piece_077.rs:963-965), and the relocation is checked for each. The malformed `[90,0,1,0]` path returns `Err` via `handle_warp` (gameplay.rs:3576-3580). The cooldown is set only on success (piece_077.rs:1182-1183), so the 5000 ms forged requests cannot block the 6000 ms success. The success path checks the relocation position and `!changed`.
- **Zone and battle refusals (136-154):** `check_context` returns `WrongZone` for zone 411 (piece_077.rs:1286-1289), which yields the "open world" text. `warp_blocker` (gameplay.rs:3253-3266) blocks on an active encounter or the warp gate, and both map to "Finish what you are doing". If `realm battle 411` failed to start, the travel assertion at line 152 would fail, so the test cannot pass silently.
- **Friend refusal (157-166):** `friend` is hardcoded to `None` (gameplay.rs:3571), so the 58 request returns `TargetUnavailable`, which shares the "cannot teleport" notice. The assertion matches the test name's claim.
- **Destination list (168-176):** `[56, 0]` goes through the same `definitions` path as the attuned list.

Weaker points I considered and did not report, because they fail loudly or are not in the five categories:
- Line 98 pins the serialized `"warpstones":{"attuned":[5]}` shape. This is the persisted save format, and the round-trip at line 101 covers the same ground. It is not incidental churn, so I left it out.
- The battle test does not assert that the battle actually started. A refused start would fail the later travel assertion, so it is self-checking.
- The position assertions at lines 109 and 131 expect the exact stored `SANCTUARY` y-value. `arrival` can raise y to terrain plus lift (piece_077.rs:1339-1341). This is a fixed-data expectation, not one derived from the code, so it is not a cannot-fail case.
