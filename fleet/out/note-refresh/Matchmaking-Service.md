<!-- fleet job=note-refresh id=Matchmaking-Service status=done turns=12 usd=0.0141 tokens(read,write,in,out)=[261371, 41958, 26, 12443] model=claude-haiku-5-5 -->
# notes/Research/Matchmaking Service.md

**Verdict:** stale on wiring and routing. The W52 policy text (queue state machine, ready check, launch, close_match) still matches `src/matchmaking.rs`, but later Autopilot work (T007) changed the library wiring, the gateway routing and the typed codec set, and the note says otherwise.

**Corrections:**

1. `old:` the library wiring is one line in `src/lib.rs` after review:
   `new:` the library wiring is the one line in `src/lib.rs` (line 52), which is now in place:
   `why:` repo:prototype/osfr-tools/src/lib.rs:52 (`pub mod matchmaking;`)

2. `old:` `src/lib.rs` remains unchanged.
   `new:` `src/lib.rs` now declares `pub mod matchmaking;` (line 52).
   `why:` repo:prototype/osfr-tools/src/lib.rs:52; the same line also appears in notes/Autopilot/T007.md (lines 15-17).

3. `old:` This module does not copy queue catalogue data, select an activity from an undocumented queue id, own sockets, or alter a save.
   `new:` The queue state machine does not copy queue catalogue data, own sockets, or alter a save. The separate read-only `Listings` adapter publishes one solo queue per field-battle activity (`Kind::Battle`, queue id = activity id) from the activity catalogue, with zero statistics.
   `why:` repo:prototype/osfr-tools/src/matchmaking.rs:1157-1195 (`Listings::from_activities`, `Kind::Battle` filter at line 1170); repo:prototype/osfr-tools/src/gameplay/matchmaking_route.rs:18

4. `old:` The integration builder owns this work; no shared module was changed for W52.
   `new:` The integration builder owns the queue-to-match half of this work. T007 later added a non-mutating adapter: `gameplay.rs` dispatches to `gameplay/matchmaking_route.rs`, and `gateway.rs` labels 141/1, 141/3, 141/13 and 41/129 (and 101/9) as `matchmaking`. `Matchmaking::join` and the `Matchmaking<C, R>` state machine are still not called from production code, only from `src/matchmaking.rs` and its tests.
   `why:` repo:prototype/osfr-tools/src/gateway.rs:490-491; repo:prototype/osfr-tools/src/gameplay.rs:52 and :2245; repo:prototype/osfr-tools/src/gameplay/matchmaking_route.rs:12-33; search for `Matchmaking::new` / `Matchmaking<` finds only matchmaking.rs:200-212 and tests/matchmaking.rs:72-73; notes/Autopilot/T007.md:15-19

5. `old:` 2. Decode tunneled family 141 packets with `Packet141`; route 141/1, /3, /6, /10 and /13 through the exact request codecs or opaque captured bodies.
   `new:` 2. Decode tunneled family 141 packets with `Packet141`; route 141/1, /3 and /13 through `gameplay/matchmaking_route.rs` (a 141/3 join is always refused with a chat line). 141/6 and 141/10 remain unrouted.
   `why:` repo:prototype/osfr-tools/src/gateway.rs:490-491 and :2111-2114; repo:prototype/osfr-tools/src/matchmaking.rs:1289-1313 (141/1, 141/13, 141/3 arms; no 6 or 10 arm)

6. `old:` Typed 141 codecs cover 141/1, /2, /6, /14 and /15.
   `new:` Typed 141 codecs cover 141/1, /2, /6, /13, /14 and /15. The 141/3 queue id is read at body `+0x0c` for the join refusal, but no typed join codec exists.
   `why:` repo:prototype/osfr-tools/src/matchmaking.rs:905-932 (`QueueStatsRequest`, sub-op 13), :29-30 (`JOIN_QUEUE_ID_IN_BODY = 0x0c`), :1303-1311

7. `old:` 141/12 queue selection, 141/13 stats request, and 141/18 system-removal meanings.
   `new:` 141/12 queue selection and 141/18 system-removal meanings. (141/13 is now a typed 8-byte request, with its 8-byte key echoed opaquely; the 141/3 queue-id offset is recovered.)
   `why:` repo:prototype/osfr-tools/src/matchmaking.rs:905-908 and :1215-1218; notes/Autopilot/T007.md:57-70

Unsure:
- **Test count.** The "Checks run" entry (11 passed, 0 failed, 1 ignored) is a W52 log, so it is not false as history. At the tip, `tests/matchmaking.rs` has 17 `#[test]` items, one `#[ignore]`d, so 16 run and 1 ignored. T007 reports the same (`cargo test --test matchmaking`: 16 passed, 0 failed, 1 ignored). Consider adding the current figure next to the W52 one.
- **Raw frame sizes and SHA256 values** (19-byte 141/1 frame, 413-byte 141/2 frame) and the `lab/reports` paths were not checked; they are outside the repo.
- **Policy paragraph** (formation, ready timeout, requeue, countdown, launch, leave/disconnect) matches `matchmaking.rs` lines 356-748 as far as I read: `take_formation` 579-646, `set_ready` 356-416, `timeout_ready_check`/`cancel_ready_and_requeue` 516-577, `start_match` 685-748, `remove_session` 466-514, `close_match` 455-464.
- **Native-fact claims** (encounter ids, `00a9d9c0`, `00aa0460`, etc.) rely on the decompiled client and were not re-verified.
