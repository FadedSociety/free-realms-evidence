<!-- fleet job=test-audit id=tests-kart-direct-transport-rs-L1 status=done turns=5 usd=0.0055 tokens(read,write,in,out)=[26258, 15575, 12, 6571] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/kart_direct_transport.rs lines 1-95 of 95

Window: `prototype/osfr-tools/tests/kart_direct_transport.rs` lines 1-95. I read the window in full and the code under test (`soe.rs` `Codec::new`, `decode_kart_pose_datagram`, `inflate_bounded`, `seeded_crc32`). The main assertions are meaningful: the forged-header and truncation loops, the 95/97/4096 length cases, the flag 2/255 cases, and the trailing-bytes cases all reach the intended rejection arms in the code. Findings:

- **[medium] prototype/osfr-tools/tests/kart_direct_transport.rs:19 (`wire`, used by every test; also lines 79 and 86) - the CRC trailer is computed with the production `seeded_crc32`, so the framing check is self-derived.**
  - Why it cannot catch a regression: if `seeded_crc32` changes (seed byte order, polynomial, reflection, or final inversion), `wire()` and `decode_kart_pose_datagram` change together. The roundtrip still passes, and the "bad CRC" and "forged" cases still error for the same reason as before. Nothing in this file pins the legacy CRC to a known value.
  - Fix: add an assertion that `seeded_crc32(0x12345678, <fixed bytes>)` equals a hard-coded constant, computed independently (for example from `scripts/bundle/check_bundle.py`, which has its own implementation, or a published CRC-32/ISO-HDLC vector with the seed prefix). Also assert one fixed wire vector byte-for-byte, so that a CRC change fails this file.

- **[low] prototype/osfr-tools/tests/kart_direct_transport.rs:90-94 `direct_pose_requires_single_complete_zlib_stream_and_supported_flag` - the name overclaims for the tiny-limit case.**
  - Why it cannot catch a regression: the block at lines 90-94 checks only the expansion bound (`max_payload` 94, so the 95-byte pose is rejected). It does not exercise stream completeness or the flag, and the assertion is a bare `is_err()`, so any error variant passes.
  - Fix: either rename the test, or move this block into a separate test named for the expansion bound, and assert `matches!(err, Error::PayloadTooLarge)`.

- **[low] prototype/osfr-tools/tests/kart_direct_transport.rs:38-49 `direct_pose_rejects_forged_use_headers_lengths_and_crc` - the single-byte mutation loop skips the 89 length field.**
  - Why it cannot catch a regression: the indices are `[0,1,2,3,7,8,9,10]`, so app bytes 4-6 (the little-endian `89` at payload[2..6]) are never flipped. The `payload[2..6] != 89u32.to_le_bytes()` check in `soe.rs:210` could be loosened (for example, to ignore the high bytes) with no test failing from this loop. The length-field coverage here is only the whole-message length cases at lines 57-65.
  - Fix: extend the array to `0..=10` (or add 4, 5, 6 explicitly) so every fixed header byte of the 96-byte pose is mutated and must be rejected.
