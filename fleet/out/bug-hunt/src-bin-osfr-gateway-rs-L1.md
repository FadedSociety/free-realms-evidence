<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-rs-L1 status=nothing_found turns=11 usd=0.0109 tokens(read,write,in,out)=[232932, 36057, 24, 8110] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr-gateway.rs lines 1-800 of 4671

Reviewed `prototype/osfr-tools/src/bin/osfr-gateway.rs` lines 1-800 in full (plus the surrounding callers and helpers they touch: `trace::protocol_summary`, `hex_prefix_len`, `mounts::RideView::follow`, `rider_event`, the staged-world caller at ~1820-1880, and `active_sessions` use). No defect I could tie to a line and show reachable from client input or a save.

Checked and dropped:
- `studio_decode` (47-72): the `%` guard `i + 2 < bytes.len()` is exactly right for a two-byte escape; invalid UTF-8 falls back to `"zz"` and pushes `%`, so no panic. `from_str_radix` accepts a leading `+` (e.g. `%+1`), which is lenient but harmless, and the path is Studio/dev-tools only.
- `trace_transport` (110-192), `trace_gateway_rejected`, `trace_application_out`: all slices are guarded by `get(..2)` / `len() >= 2`. `protocol_summary` (trace.rs:75-102) checks `len >= 7` before reading `message[3..7]`, and `size <= len-7` before `message[7..7+size]`, so no out-of-range index.
- `Options::parse` (307-406): bounds checks are present for guild TTL; the handoff-key length check (`< 16`) is only a lenient bound; all values are operator CLI input, not client input.
- `join_player` (602-671): the registry, `joined`, `active_sessions`, and chat mutations happen before `social_profile(...)?` and `social.login(...)?`. That is a mutation-before-error pattern, but the only caller (~1850) runs it on `staged_world`, a clone that is dropped on error, so nothing lands half-applied.
- `leave_player` (673-701): ordering is correct (`joined` is still set during `ride_fanout`, and `joined`/`chat_sessions` are removed after fanout).
- `ride_fanout`, `with_rides`, `ride_follow` (706-766), `with_pets` (770-794): every index is through `get(..)`/`?`; `RideView::follow` (mounts.rs:683-693) checks `get(2..10)` before `copy_from_slice`. The inputs are server-built delivery frames anyway.
- `rider_event` (2754-2765): all reads are `get`-guarded.
- `social_profile` (584-600): the early mutation of `identities`/`social_paths` before a load error is harmless; the caller discards the staged world on error.

No findings to report.
