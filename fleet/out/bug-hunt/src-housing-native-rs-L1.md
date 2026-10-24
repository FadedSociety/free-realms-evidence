<!-- fleet job=bug-hunt id=src-housing-native-rs-L1 status=nothing_found turns=5 usd=0.0069 tokens(read,write,in,out)=[62410, 23563, 12, 6691] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/housing_native.rs lines 1-800 of 1258

## housing_native.rs lines 1-800: no reportable defects

I read the full window (1-830, including the end of `InstanceList::decode` at 800-812 so the function is complete). I checked each candidate against its callers and found nothing that meets the defect criteria.

What I verified:

- **Bounds and panics.** `Reader::take` uses `checked_add` and compares against `data.len()` before slicing (65-76). `subtype`, `u32`, `i32`, `u64` and `f32` only call `try_into().unwrap()` on slices that `take` has already sized exactly, so they cannot panic. `string` (116-128) rejects negative or over-`MAX_STRING` lengths before `take`, and refuses invalid UTF-8 with `map_err`, not `unwrap`.
- **Unbounded growth.** Every count goes through `count()` (130-136), which caps it at `MAX_COUNT` (4096). Pre-allocation is `count.min(64)` (375, 482, 565). Nested loops (actions, unknown GUIDs, the `InstanceList` records at 803-805) each consume at least one payload byte per iteration, so the total work and memory are bounded by the input size.
- **Encode/decode symmetry.** I compared field order for `FixtureInstance`, `Customization`, `CouplingDisplay`, `FixtureInstanceInfo`, `FixtureDefinition`, `FixtureUpdate`, `PlayerHousingInstanceInfo`, `ZoneData` and `InstanceList`. The orders match. String and count limits match between `Writer` (189-204) and `Reader`.
- **Floats and bools.** Every float goes through `finite()` on both encode and decode. Bools are strict 0/1 on decode.
- **Atomicity.** The codecs write into a local `Writer` and return `Err` without side effects, so there is no partial state to undo.
- **Size claims in doc comments.** The stated byte sizes (42, 10, 22, 50, 28) add up to the field widths.

Two points I considered and rejected:

- `PlaceFixture::first_dword` is a `u32`, while the doc says it carries an inventory item GUID. If that GUID is 64-bit, the high bits are lost. However, the client writes this field as a dword per the doc's own reader evidence, so the truncation is on the client side. It is not a server-side defect in this window. The consumer is `housing_service.rs:447-449`, which is outside my window.
- `FixtureUpdate::TAIL_BYTES_EMPTY` (528) is a test-facing constant and is not used in production code.
