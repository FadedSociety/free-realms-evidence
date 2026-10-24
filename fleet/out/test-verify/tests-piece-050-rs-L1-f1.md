<!-- fleet job=test-verify id=tests-piece-050-rs-L1-f1 status=done turns=6 usd=0.0059 tokens(read,write,in,out)=[50202, 18472, 14, 6103] model=claude-haiku-5-5 -->
# high: prototype/osfr-tools/tests/piece_050.rs:209

**Verdict:** `confirmed`

**Evidence:**

I could not refute the claim. Its mechanics check out, and no other assertion in the test catches the regression it names.

1. **The write corrupts the opcode.** `request.encode()` lays out bytes as `[0xD2, 0x00]` (opcode 210, LE u16), then the u32 length `128` at indices 2..6, then 128 `a` bytes. `too_long[1..5].copy_from_slice(&129u32.to_le_bytes())` (tests/piece_050.rs:210) sets indices 1..4 to `[0x81, 0, 0, 0]`. The opcode becomes `0x81D2`.

2. **The decoder rejects on the opcode, before any length check.** `NameCheckRequest::decode` (src/restoration/piece_050.rs:228-232) returns `invalid("not a check-name request")` when `r.u16() != CHECK_NAME_REQUEST_OPCODE`. `Slice::string` (line 193-197) is never reached.

3. **The `is_err()` at line 212 is vacuous.** It passes whether `NAME_FIELD_MAX_BYTES` is 128 or 1000, and whether the `length > max` check at line 195 exists or not. Walking the test against each change:
   - Constant → 1000: `request` becomes 1000 bytes, and line 208 still passes. Line 210 writes 1001, but the opcode is still `0x81D2`, so line 212 still errors. **Passes.**
   - Remove `if length > max` (line 195): line 208 (128 bytes) still decodes. Line 212 still fails on the opcode. **Passes.**

4. **No other assertion in the test fails under those changes.** The other bound checks use `NAME_PART_MAX_CHARS` (lines 189-198), which is a character count and never reaches the 128-byte path. Lines 214-226 use short names. The earlier round-trip test (lines 77-93) uses short fields and only checks truncation and trailing bytes. `grep` finds no other `repeat(` or over-128-byte input in this file. Only a shrink of the constant below 128 would be caught, by line 208.

**Suggested fix check:** The proposed repair is sound. Writing `129` at `too_long[2..6]` and `too_long.insert(6, b'a')` keeps the opcode intact and leaves a 129-byte field. Under the constant→1000 change or the removed-check change, decode would then succeed, so `is_err()` would fail and catch the regression. The extra "128-byte variant decodes to the same first_name" assertion is a reasonable addition, though line 208 already covers the round trip without comparing `first_name`.

**Minimal fix:** Replace lines 209-211 with:
`let mut too_long = request.encode(); too_long[2..6].copy_from_slice(&((NAME_FIELD_MAX_BYTES + 1) as u32).to_le_bytes()); too_long.insert(6, b'a'); let err = NameCheckRequest::decode(&too_long).unwrap_err(); assert_eq!(err.to_string(), "check-name string exceeds bound");`
</result>
