<!-- fleet job=bug-hunt id=src-kart-service-rs-L801 status=nothing_found turns=23 usd=0.0255 tokens(read,write,in,out)=[782168, 59771, 48, 20383] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/kart_service.rs lines 801-1600 of 2709

No reportable defects in `kart_service.rs` lines 801-1600. Nothing here reads a client packet directly. The window is save-shape fields, content validation, curtain/band geometry, and the begin/prepare/start_countdown transitions. Client positions reach `contains` (outside the window, ~2668) and the geometry is NaN-safe there.

Checked and dismissed:
- **Clone `expect` (1411):** `RaceSession::restore(session.snapshot())` should always succeed. Every live transition in `kart_racing.rs` (`begin`, `start`, `on_checkpoint`, `abandon`) produces a state that `restore` (639-698) accepts. `TrackLayout::new` and `validate()` are the same check.
- **`begin` on Finished with an unclaimed reward (1521-1573):** the finish is discarded. The gateway path (`kart_gateway.rs:569-572`) builds a fresh service per entry anyway. The entry-side `33/9` that calls `prepare` is accepted only in `EntryPhase::Waiting` (`kart_entry.rs:657-662`), so a finished race cannot be re-prepared from the client. Not a remote exploit.
- **`validate_content` `minimum` (1302):** `gates.len() as u32 * laps.max(1)` could overflow, but `laps` and the schedule come from server content, not from clients.
- **`band_axes` doc (1182-1184):** the `(None, Some(next))` arm computes `next - current`, while the doc says `next -> current`. `BandVolume::contains` (2680-2682) takes `abs()` of both `along` and `across`, so axis sign has no behavioural effect.
- **`point_triangle_distance2` divisions (1016, 1029, 1036, 1045):** the denominators can only be zero for degenerate triangles, and `curtain_normal` rejects those (area floor, 1088) before any geometry is used.
- **`curtain_normal` (1071-1128) and `curtain_volume` (1132-1172):** the validation is consistent with its doc. Both triangles are checked for verticality, the fourth vertex for planarity, and convexity is checked against the normal. Leaf and group counts are bounded.
- **`save_decision_eq` (863-922):** the exhaustive destructure covers every field. Only `observations` and `weapon_pose` are excluded, and the doc says so.
- **`start_countdown` (1583-1610) and `begin` (1521-1573):** all fallible calls (`RaceSession::open`/`begin`) run before any state is mutated. `schedule.get`/`position` have safe fallbacks.
