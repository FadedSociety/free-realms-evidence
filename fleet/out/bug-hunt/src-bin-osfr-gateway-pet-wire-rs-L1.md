<!-- fleet job=bug-hunt id=src-bin-osfr-gateway-pet-wire-rs-L1 status=nothing_found turns=3 usd=0.0013 tokens(read,write,in,out)=[5906, 5154, 8, 1136] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/bin/osfr_gateway/pet_wire.rs lines 1-22 of 22

Reviewed `prototype/osfr-tools/src/bin/osfr_gateway/pet_wire.rs` lines 1-22 in full. No defects in the window.

What the window contains: two pure byte-builders, `summon(pet_id: u32)` and `summon_by_item(definition_id: u32, tint: u32)`. Each concatenates a fixed header (`53, 0, subtype`) with `to_le_bytes()` of its u32 arguments. Nothing here parses client input, indexes or slices into a buffer, unwraps, divides, or grows a collection from a client-supplied count. There is no panic, overflow, or unbounded-allocation path.

Checks made:
- Doc comments match the code. `summon` is `53 00 | 4 | u32 | 1` and `summon_by_item` is `53 00 | 32 | u32 | u32`, as stated on lines 8 and 13-14 and in the module header (lines 4-6).
- Reach: the file is test-only. `tests/pet_routing.rs:14-15` includes it via `#[path]`, and `src/bin/osfr_gateway/f161_pet_adoption_persist.rs:9-10` includes it. The module doc says production does not include it. Callers in `f161_pet_adoption_persist.rs:110,151,190` pass constants or test-chosen ids. Even if a client-supplied value reached these functions, the functions only serialise it and cannot corrupt state or panic.

No findings.
