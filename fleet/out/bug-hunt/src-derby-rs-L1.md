<!-- fleet job=bug-hunt id=src-derby-rs-L1 status=nothing_found turns=10 usd=0.0096 tokens(read,write,in,out)=[183191, 30656, 22, 7837] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/derby.rs lines 1-800 of 1960

Reviewed `prototype/osfr-tools/src/derby.rs` lines 1-800 in full, plus the `Reader` helpers (1864-1930) and `put_*` encoders (1932-1956), and the callers that matter for reachability (`handle_client` at 1086-1125 and `derby_gateway.rs` 373-387). No finding survives verification.

What I checked:

- **Decode bounds (`decode_inner`, 514-628).** `Reader::bytes` uses `checked_add` and `get(..)`, so truncation returns `TooShort`. The `CreateVehicle` path (subtype 10, 551-575) reads `name_len`, rejects negative values and values above `MAX_OPAQUE_BYTES`, and requires `remaining >= 69` before computing `remaining - 69`, so the subtraction cannot underflow. The 69-byte tail matches 16 words + 1 flag byte + 1 dword. `finish` rejects trailing bytes for known subtypes. Unknown subtypes are kept as raw bytes and are never re-encoded from client input.
- **Client-to-server handling.** `handle_client` acts only on RegisterPlayer, PlayerPhase, CountdownStatus, VehiclePose, PickupHitRequest and VehicleHit, and each requires the key to equal the authenticated sender. CreateVehicle, Unknown and the other server-to-client subtypes fall through to `_ => Ok(Vec::new())`, so the encode-side refusals in `write_body` are not reachable from a client packet.
- **Atomicity.** `DerbyGateway::handle` (derby_gateway.rs:380-386) clones the service, runs `handle_client` on the clone, and commits `self.service` only on success. A failed packet leaves state untouched.
- **Encoders.** Endianness is consistent (`to_le_bytes` everywhere, matching the `from_le_bytes` reads). The `CreateVehicle` name-length conversion is checked with `try_from`.
- **Outside the window, briefly.** `read_i32` (derby.rs:1958) is only called at 1028-1030 and 1065-1067. The 1028 call sits behind a `packet.len() != 15` guard, so it cannot go out of bounds. `DerbyRules` is validated at 814-820 (`max_drivers` 2..=8, `contact_radius_m` finite and in (0, 1000]).

Only non-reachable asymmetries remain, and I am not reporting them: `decode_inner` accepts a CreateVehicle definition longer than `MAX_OPAQUE_BYTES` that `encode_inner` would refuse. No code path re-encodes a client-sent CreateVehicle, so this has no effect on the server.
