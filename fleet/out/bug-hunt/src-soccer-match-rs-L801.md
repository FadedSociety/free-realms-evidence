<!-- fleet job=bug-hunt id=src-soccer-match-rs-L801 status=nothing_found turns=13 usd=0.0180 tokens(read,write,in,out)=[290577, 44254, 28, 19028] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/soccer_match.rs lines 801-1014 of 1014

No reportable defects in `prototype/osfr-tools/src/soccer_match.rs` lines 801-1014.

What I checked, with reach:

- **`advance` tail (801-885):** the ball step, ground clamp, toucher-clear, goal, out-of-play, pass-completion and loose-ball pickup branches. All index and arithmetic is on finite values. `previous` is always inside the field, since every ball-position write is a kickoff spawn, a verified player position, or an in-bounds step. The goal branch's `score[team]` index is 0 or 1. The `goal_crossing` division cannot be by zero, because `crossed` requires `previous <= line < next` (or the mirror), so `next - previous` is nonzero. The loose-ball winner uses `BTreeMap` iteration, so tie-breaks are deterministic. Mutation precedes no fallible step.
- **`snapshot`/`restore`/`validate_snapshot` (887-949):** validation runs before any write, and the stale-revision check and clock rebase keep `position_at <= server_time`. Neither is reachable from a client: `soccer_service.rs` only calls `restore` at 988-989, and the match is driven server-side via `tick`/`kickoff`/`second_half` (soccer_service.rs:829-854). The missing checks on `half`/`score`/`ball_position` are only reachable from a future save format, which the doc comment already concedes.
- **`reset_ball`, `build_outcome`, `attack_sign`, `goal_crossing` (951-1013):** the sign conventions are consistent (team 0 attacks +z, scores on crossing +z; the switch flips on half 2), and the mouth test matches its doc comment.

Upstream checks I confirmed in the window's callers (lines 1-740): `apply` refuses non-finite and out-of-range positions and kick power, requires possession and proximity for kicks, checks pass targets are registered teammates with a verified position in range, and bounds movement by `max_position_step` and the server-time budget. Kick and pass paths validate before mutating.

Observations I judged not to be defects: the ball has no friction, so a slow pass can roll in play for a long time (gameplay tuning, with `charge_floor` bounding the minimum power); and a carrier standing on the goal line cannot score by carrying the ball (design gap, not an exploit).
