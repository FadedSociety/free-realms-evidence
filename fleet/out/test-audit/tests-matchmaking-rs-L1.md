<!-- fleet job=test-audit id=tests-matchmaking-rs-L1 status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[31089, 18026, 10, 3729] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/matchmaking.rs lines 1-571 of 571

Window reviewed: `prototype/osfr-tools/tests/matchmaking.rs` lines 1-571. Two findings were confirmed against `src/matchmaking.rs`. Most of the window checks real output, including the exact byte layouts, the `Duplicate`/`SessionBusy` results, and the match-state counts.

- **[medium] prototype/osfr-tools/tests/matchmaking.rs:455 configured_team_capacity_assigns_whole_groups_without_oversizing_a_team - the name claims team placement (whole groups, no team oversized), but the only check is the flat roster of the launch packet.**
  - Why it cannot catch a regression: `decode_activity_launched` (src/matchmaking.rs:1395) returns `(i32, i32, Vec<u64>)`, so team ids never reach the test. The team id is computed per member in the selection loop (src/matchmaking.rs:597-613, 638-640) and is dropped before the packet is built. A change that puts a group on the wrong team, or places a solo into the already-full team, would still produce the same four GUIDs in the same order, and the test would pass.
  - Fix: assert team membership through an observable surface, for example a team-aware accessor on the match or a team field in the launch packet. Then check that group 9 (sessions 3 and 4) shares one team of size 2 and that each team's member count is exactly 2. If no accessor exists, rename the test to what it checks (`launch_roster_contains_all_four_queued_players`) so the name stops overclaiming.

- **[low] prototype/osfr-tools/tests/matchmaking.rs:246 adapter_answers_list_stats_running_list_and_leave_lobby - the leave check asserts only that the reply list is empty and the refusal is `None`.**
  - Why it cannot catch a regression: any handler that silently accepts or drops packet 101/9 and returns an empty `Ok` passes. The test never checks that the lobby was actually left or that a different response was not sent. The inline comment about the u32 lobby type is also not asserted.
  - Fix: assert a concrete observable on the leave path, such as a specific reply or refusal variant for a non-zero lobby type, or an explicit check that the call does not produce a mutation. Also add a second case where the body's lobby type is zero, and assert the distinct outcome.

No other findings in this window. The ignored kart test at line 327 has a reason. The ready-timeout, disconnect, and leave tests check the queue state and the reservation state after each step.
