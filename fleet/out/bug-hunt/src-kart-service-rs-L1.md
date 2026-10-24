<!-- fleet job=bug-hunt id=src-kart-service-rs-L1 status=nothing_found turns=8 usd=0.0092 tokens(read,write,in,out)=[141757, 31870, 18, 7616] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/kart_service.rs lines 1-800 of 2709

Window reviewed: `prototype/osfr-tools/src/kart_service.rs` lines 1-800 (module docs, constants, serde content/snapshot types, `ServiceRefusal`/`ServiceError` enums and Display impls, `RacePhase`, `ServiceOutcome`, start of `ServiceSnapshot`). No defect in this window can be tied to a client-reachable panic, unbounded growth, lost atomicity, trusted client authority or wrong comparison.

What I checked against the code outside the window (only to confirm the window's constants and types are enforced):

- `validate_content` (lines 1229-1345): gate count (`<= MAX_GATES`), radius (`!is_finite() || < MIN_GATE_RADIUS_M`), schedule count and order, schedule state `1..=MAX_GAME_STATE`, countdown `<= MAX_COUNTDOWN_VALUE`, player/npc counter `<= MAX_RACERS`, bounds, `progress_template` slot `0..MAX_RACERS`, and band half-extents `(0, MAX_GATE_BAND_HALF_M]`. These match the window's doc comments and the `ServiceError` messages.
- Curtain validation (lines 1142-1167): leaf count `1..=MAX_GATE_CURTAIN_LEAVES`, `half_depth` finite and in `(0, MAX_GATE_CURTAIN_HALF_DEPTH_M]`, and vertical-normal check. No NaN bypass.
- Byte-length constants match their layouts: `GATE_HIT_PAYLOAD_LEN` = 8+12+4 = 24, `COUNTDOWN_PAYLOAD_LEN` = 8+4 = 12, `OWNED_ID_PAYLOAD_LEN` = 8. `default_max_observations()` = 120_000 matches the documented 600 s at 200 Hz.

Non-findings noted but not reported:

- Line 187-188: the `MAX_RACERS` doc says "the recovered 8-slot range bound", but the value is 16, which matches `kart_entry::MAX_RACERS`. This is a comment-only inconsistency with no behavioural effect.
- Line 1302 (outside window): `content.gates.len() as u32 * content.laps.max(1)` can overflow for very large lead-authored `laps`. The input is trusted operator content, not a client packet, so I did not count it.
