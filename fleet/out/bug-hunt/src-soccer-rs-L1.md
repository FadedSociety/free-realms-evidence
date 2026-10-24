<!-- fleet job=bug-hunt id=src-soccer-rs-L1 status=done turns=11 usd=0.0114 tokens(read,write,in,out)=[213098, 33042, 24, 10226] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/soccer.rs lines 1-800 of 1069

Window `prototype/osfr-tools/src/soccer.rs` 1-800 read in full. No high or medium defects found. One low-severity, platform-dependent finding:

- **[low] prototype/osfr-tools/src/soccer.rs:617 - `asset_end = CONFIG_ASSET_OFFSET + length` is unchecked `usize` addition on a client-supplied `u32` length, so on a 32-bit target it can wrap and then panic on the slice at line 621.**
  - **Failure scenario:** on a 32-bit build, a client sends sub 7 (SetClientConfig) with a payload of at least 173 bytes and `payload[124..128]` = `0xFFFF_FFF0`. `128 + 0xFFFF_FFF0` wraps to `0x70` (112). The check `asset_end > payload.len()` at line 618 is then false, so the code reaches `&payload[128..112]` at line 621, which panics ("slice index starts at 128 but ends at 112") in debug and release alike. On a 64-bit build the sum cannot overflow, so the check at line 618 rejects it cleanly.
  - **Reach:** `decode(bytes)` (soccer.rs:460) → `decode_packet(sub=7, inner)` (soccer.rs:519) → `decode_client_config` (soccer.rs:608). The live path is `client_packet` (soccer_match.rs:299-300), which calls `decode` on raw client bytes. The only guard is the length check at soccer.rs:609 (≥173 bytes), which does not bound the length field. This is reachable from a remote client only on a 32-bit build; I did not find a 32-bit target configuration in the window.
  - **Fix:** `let asset_end = CONFIG_ASSET_OFFSET.checked_add(length).filter(|&end| end <= payload.len()).ok_or_else(|| invalid("client config ball asset length"))?;`

Checked and cleared:
- `decode` (460-489): the `bytes.len() < 11` guard covers `bytes[0..2]`, `[2]`, `[3..7]` and the `bytes.len() - 7` subtraction.
- `take` / `read_*` / `read_bytes`: every `try_into().unwrap()` follows a `take` of the exact length, so no panic.
- `decode_team_colours` (636-660): names are capped at 64 bytes before `take`, and invalid UTF-8 returns an error.
- `decode_client_config` 64-bit path: the 173-byte minimum covers the spawn reads at 157..173 and the length read at 124..128.
- Unbounded growth: all arrays are fixed-size. `Unknown` copies only the frame it was given. Nothing in 1-800 grows a collection from a client count.
- Trailing-byte handling: `end()` runs for every sub except 7 and Unknown. Sub 7 is deliberately raw, and its offsets match the test `vec_config` (tests/soccer.rs:83-97).
- Packet size comments (lines 116-221) match the layouts in `decode_packet`.
- Client-side authority: `Match::handle` (soccer.rs:835-843) rejects client-sent non-`CLIENT_PACKET_IDS` packets, and the live path `client_packet` (soccer_match.rs:339-343) rejects client `GoalMade` and `ImpulseBall`. Neither is a finding.
