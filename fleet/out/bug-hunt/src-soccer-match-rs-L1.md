<!-- fleet job=bug-hunt id=src-soccer-match-rs-L1 status=nothing_found turns=9 usd=0.0208 tokens(read,write,in,out)=[209755, 42510, 20, 26837] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/soccer_match.rs lines 1-800 of 1014

No defect I can tie to a line in `soccer_match.rs` 1-800 with a client- or save-reachable trigger. I read the whole window and the callers that matter (`soccer.rs` decode, `soccer_service.rs` 200-300 and 919-978, `soccer_entry.rs` 420-436), and read 800-1014 only to follow the `advance` and `goal_crossing` flow.

Checked and dismissed:

- **Panics on client input.** `self.players[&player]` (line 697) is guarded by `players.get` in `apply` (line 614) and nothing removes the player in between. `vectors[0..2]` (lines 333-335) index a fixed `[[f32; 4]; 3]` (soccer.rs:198). `normalize` (58-64) rejects non-finite and near-zero lengths, and the `distance` and `goal_crossing` divisions (line 1002) are only reached when the segment strictly crosses the line, so the denominator is non-zero.
- **Atomicity.** Every `apply` refusal happens before any write. The Shot branch's `normalize(...)?` (708) and the Pass branch's `toward` (737-741) both run before `ball_velocity` is assigned. `advance` has no fallible step after `remaining`/`server_time` are mutated.
- **Trusting the client.** Sender must equal payload player (598). Power is bounded to `(0, max_kick_power]` (690). Possession and kicker range are checked (694-705). Pass target must be a registered teammate with a verified position (722-731). Position step is bounded by both the spawn distance and the server-time budget (638-657). `now` is clamped to `server_time` (607-611), and `position_at` cannot move backwards because a negative budget refuses the intent.
- **Logic against docs or tests.** `classify_state` matches its doc comment. The dt=0 "any nonzero step is refused" claim holds. `register` enforces team and slot bounds and uniqueness. `unregister` checks the roster before mutating, matching its doc.

Observation not reported (too weak to show harm): after a pass is caught, `last_touch` still names the kicker and `toucher_clear` stays false (lines 744-749, 854-863). If the receiver then leaves and the kicker is still within `control_radius` of the ball, pickup stays blocked until the kicker moves. This is a gameplay stall that resolves itself, not a security or save-corruption issue.
