<!-- fleet job=bug-hunt id=src-derby-rs-L1601 status=nothing_found turns=19 usd=0.0202 tokens(read,write,in,out)=[506545, 50486, 40, 17668] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/derby.rs lines 1601-1960 of 1960

No reportable defects in `prototype/osfr-tools/src/derby.rs` lines 1601-1960.

Candidates I examined and dropped, with the reason:

- **`handle_close` (derby.rs:1766-1783) `closed.len() == human_count()` and `disconnect` (derby.rs:1735-1760) not clearing `closed`.** This looks like a stuck `CloseEnabled` phase for multi-human matches. It cannot be reached in production. `derby_gateway.rs:436` always passes the owner as `sender`, so `closed` holds at most one key. `add_human` (derby.rs:946) has no caller outside tests, so `human_count()` is 1 in every live match. On a successful close, `derby_session.rs:162` calls `exit()`, which sets `service = None` (derby_gateway.rs:501), so `Closed` is never observed.
- **`DerbyService::disconnect` (derby.rs:1735-1760).** It removes acks but never re-checks whether the remaining acks now satisfy the countdown or phase threshold, which could stall a countdown. No production caller exists: `.disconnect(` has no match under the derby sources, and `disconnect` appears nowhere in the derby gateway or session code. Unreachable.
- **Mutation before `?` in `tick` respawn (derby.rs:1680-1686), `finish_match` (1602-1630) and `disconnect`.** `encode_inner` only fails for `CreateVehicle` with oversized blobs (derby.rs:420-429), and none of the messages broadcast in this window take that path. The gateway also runs `tick` and `cancel` on a cloned service and commits only on success (derby_gateway.rs:389-403, 407-420; derby_session.rs:73-94), so no partial state is kept.
- **Panics in `state_message` (derby.rs:1564-1565) and the `unwrap()`s at 1681, 1715 and 1361.** The keys come from iterating `drivers`, or are checked just before the call, so they cannot be absent.
- **Integer overflow in the `finish_match` comparator (derby.rs:1612-1613).** `damage_dealt` and `damage_received` are `u32` (derby.rs:271-272), so the `as i64` subtraction cannot overflow.
- **Timer arithmetic in `tick` (derby.rs:1698-1728, 1634-1665).** Uses `saturating_sub`/`saturating_add` throughout. The `timed_out` comparison uses `>=` on the elapsed time, which is correct.
- **`pose_position` (derby.rs:1849-1862).** `transform_bits` is `[u32; 16]` (derby.rs:250), so indexes 12-14 are in range.
- **`Reader` (derby.rs:1864-1930).** `bytes()` uses `checked_add` and `get()`, so it cannot slice out of range. `remaining()` cannot underflow because `offset <= len` is maintained.
- **`read_i32` (derby.rs:1958-1960).** Every caller in the file is preceded by a length check: the `len() == 15` check at derby.rs:1025 and the `matches!`/`len() == 15` guard at derby.rs:1062.
- **NPC pose refresh in `tick` (derby.rs:1687-1697).** Deliberate and documented in the comment as placeholder behaviour, not a defect.
