<!-- fleet job=bug-hunt id=src-restoration-piece-056-rs-L801 status=nothing_found turns=5 usd=0.0044 tokens(read,write,in,out)=[29767, 15527, 12, 4310] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_056.rs lines 801-969 of 969

Window `prototype/osfr-tools/src/restoration/piece_056.rs` 801-969 (plus 700-808 for the caller context) reviewed. No defect I can tie to a line and show is reachable from client input.

What I checked:

- **`decode_profile_rows` (780-808), the count-driven loop.** The client-supplied `count` is rejected if negative (789). It is then checked against the real buffer length, `bytes.len() == 4 + count*89` (795-801), before `Vec::with_capacity(count)` (802). So allocation and the loop are bounded by the bytes actually received. The `count as usize * 89` product cannot overflow on a 64-bit server. Every per-row read goes through bounds-checked helpers.
- **Reach for `decode_profile_rows`.** A grep of `repo` shows no caller in `src/`. The only references are the definition and `encode_profile_rows` in `tests/piece_056.rs`. It is therefore not reachable from a packet or save today, so the findings above do not become a remote defect. I did not report it.
- **Row size constants.** `EFFECT_TAG_LEN` is 72 (line 74), so `CLIENT_EFFECT_TAG_LEN` is 85 (line 76). `read_payload` consumes 85 bytes and `push_payload` writes 85 bytes. I counted both field by field and the layouts match, so the per-row stride is correct.
- **`read_payload` (848-912) and `push_payload` (814-846).** Field order and widths are symmetric and match the `EffectTagPayload` struct (243-268). The only asymmetry is that `read_bool` maps any non-zero byte to `true`, so a byte value of 2 re-encodes as 1. That is a normalisation, not a defect.
- **`check` (914-929).** The length is validated before the `bytes[..2]` and `bytes[2..4]` slices. All callers pass constant lengths of at least 4, so the slices cannot go out of range.
- **`read_bool`, `read_i32`, `read_i64`, `read_u64` (931-969).** All use `.get(..)` with `ok_or` and return `BadLength`. No unwrap can panic on a short buffer, since the `try_into().unwrap()` calls run only after a successful slice of the exact width.
- **`encode_profile_rows` (770-778).** The `i32::try_from(...).unwrap_or(i32::MAX)` saturation only matters past 2^31 rows, which cannot happen; it is also encode-only, not client input.

No findings.
