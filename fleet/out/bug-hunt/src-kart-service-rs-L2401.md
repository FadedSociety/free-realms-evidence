<!-- fleet job=bug-hunt id=src-kart-service-rs-L2401 status=nothing_found turns=20 usd=0.0253 tokens(read,write,in,out)=[569804, 61680, 42, 23775] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/kart_service.rs lines 2401-2709 of 2709

No reportable defects in `prototype/osfr-tools/src/kart_service.rs` lines 2401-2709.

I read the whole window and the code it depends on: `race_elapsed` (2394), the `start_race` anchor reset (1613-1645), the `tick` and `GATE_HIT`/`PICKUP_HIT` dispatch (1658-1700, 1881-1892), the curtain and band construction (930-1345), `kart_racing.rs` `next_checkpoint` and `on_checkpoint` (485-565), and the snapshot restore (2300-2370). What I checked:

- **Panics on client input.** `decode_claim` checks the 24-byte width before slicing, and `owned_id` checks width first. `attribute_gate`'s `expected as usize - 1` is safe because `claim_gate` returns before it when `expected == 0`. `progress_frame`'s `expect`s hold because `own_guid` runs first and the session exists whenever the phase is Racing. Curtain and band indexing by gate index is safe: `curtain_volume` requires `gate_curtains.len() == gates.len()`, and the checkpoints are built as `1..=gates.len()`. NaN from the triangle distance math only produces a refusal, not a panic.
- **Movement authority.** `check_movement` refuses non-finite positions, clock regressions and oversized steps. The floor branch pays only from saved credit. `accept_movement` banks `allowance - distance` capped at 180 m, so total distance over time T stays within about v·T plus the saved cap, with no minting. The anchor and clock move only on acceptance.
- **Atomicity.** `on_checkpoint` mutates only on accepted or lap outcomes, and `accept_movement` runs only after those, so no refusal leaves a half-applied state. The only pre-refusal mutation in `claim_gate` is `attempts += 1`, which is the documented in-window flood guard and an accepted, reviewer-authorized tradeoff in `notes/Autopilot/F181.md` and `F231.md`. I did not report it as new.
- **Attribution.** Nearest-later skip and nearest-earlier stale match their doc comments, and the expected gate wins on overlap.

Minor observations, not reported: `decode_claim` ignores the trailing f32 of the 24-byte `33/7` payload, which is consistent with the notes (`f32 1.0`) and with the server using its own clock. `ServiceSnapshot` restore does not range-check `claim_credit_m`, `last_position` or `attempts`. I did not find a client path to tamper with saves, so that is outside this window's client-input scope.
