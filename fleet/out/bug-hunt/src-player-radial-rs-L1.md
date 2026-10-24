<!-- fleet job=bug-hunt id=src-player-radial-rs-L1 status=nothing_found turns=10 usd=0.0092 tokens(read,write,in,out)=[162043, 29165, 22, 7798] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/player_radial.rs lines 1-425 of 425

I read all of `prototype/osfr-tools/src/player_radial.rs` lines 1-425 and checked the callers and helpers it depends on. I found no defect I could tie to a line and show reachable from a client packet or save. Nothing is reported.

What I checked, and why each candidate was dropped:

- **26/19 parsing (`select_menu`, 199-203):** the length check runs before `inner[..4]`, and `inner[12..20]` is in bounds for the 20-byte length. The `try_into().unwrap()` on an 8-byte slice cannot fail.
- **26/10 parsing (`choose_entry`, 241-250):** the length is checked first, and the `try_into` slices are in bounds. A non-matching guid returns `Ok(None)` and leaves the open menu alone. A matching guid consumes the menu before any refusal, which the doc comment at 231-233 says is intended.
- **Reach and NaN (`visible_name`, 300-306):** a NaN distance would pass the `>` check. The target comes from `nearby_sessions`, which returns an empty set for a non-finite viewer position (`players.rs:222-224`). Pose is rejected when non-finite (`RegistryError::InvalidPose`, `players.rs:149`), so a stored target position is finite. The NaN path is closed upstream.
- **Name truncation (`truncate`, 318-324):** the char-boundary loop stops at 0 at the latest, so it cannot underflow.
- **Look payload (`start_inspect_packet`, 360-425):** profiles are capped at 64 and items at 17 before anything is written. The slot range is checked before `1 << slot`, so the shift is valid. `record[..4]` is guarded by `len() >= 4`. The `levels` sum saturates. The payload size is checked before the length cast to u32. The stats loop matches its comment (38 entries of id, type, value).
- **Look source:** `public_look` (`gameplay.rs:1232-1263`) builds the look from server state, not client input. Worn slots are validated against profile slots in `inventory.rs:1238-1239`.
- **Trade and atomicity:** the trade path returns `Chosen::Trade` after the reach check, and `TradeService::invite` re-checks. The gateway's `unwrap_or_default` on invite is a deliberate silent drop, per the comment at `osfr-gateway.rs:2071`. The one-shot menu and the inspect state changes are intended, not ordering bugs.
- **Stop inspect (`stop_inspect`, 270-276):** an exact-match check, no state that can go wrong.

Dropped as not defects: the payload cap is checked after the build, but the build is bounded (about 1.1 MB at most), so that is not an unbounded allocation; and the NoLook/NotVisible distinction is not observable, since both paths send nothing.
