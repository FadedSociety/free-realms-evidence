<!-- fleet job=bug-hunt id=src-kart-progress-native-rs-L1 status=nothing_found turns=4 usd=0.0028 tokens(read,write,in,out)=[20930, 12370, 10, 2075] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/kart_progress_native.rs lines 1-298 of 298

Reviewed `prototype/osfr-tools/src/kart_progress_native.rs` lines 1-298 in full. No defect I can tie to a line and reach from client input.

What I checked:

- **Panics on client input.** `decode_progress` (l.202-236) runs `require_len(payload, 73)` before any read, so every `u32_at`/`u64_at`/`payload[...]` access (max index 0x41+8 = 73) is in range. `decode_game_state` (l.260) and `decode_destroy_racer` (l.271) check length first. The helpers `u32_at`/`u64_at` (l.182-199) only index inside those checked lengths. No `unwrap`, division, or client-sized allocation.
- **Overflow.** `results_row_finished` (l.287-289) uses `wrapping_add`, so it cannot panic in debug builds. The wrap is documented and the doc comment matches the code.
- **Logic against doc comments.** The NaN policy (l.224-232) checks only the 0x0c and 0x10 fields, as the `RefuseNaN` doc (l.91-94) says. `results_screen_trigger` (l.296-297) matches its doc. The encoders write fields in the order the decoder reads them, so the layout round-trips.
- **Trust.** The codecs do not decide finishes, rewards, or phases. The reporting helpers are documented as read-only. I searched the crate: the only callers of `decode_progress`, `results_row_finished`, and `results_screen_trigger` are in `tests/`. Nothing in production code reaches these functions in this repository, so no client packet currently reaches this module through this crate.

Nothing qualifies as a finding.
