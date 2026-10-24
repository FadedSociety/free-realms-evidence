<!-- fleet job=test-audit id=tests-soe-transport-rs-L1 status=nothing_found turns=8 usd=0.0134 tokens(read,write,in,out)=[138965, 34298, 18, 15405] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/soe_transport.rs lines 1-432 of 432

No findings in `repo:prototype/osfr-tools/tests/soe_transport.rs` lines 1-432 that fit the five categories.

I read the whole window and checked the assertions against the code they exercise (`src/soe.rs`: `Codec::new/encode/decode` at 97-171, `receive_at` at 376-456, `expire_reassembly` and `process_ordered` at 461-539, constants at 20-27, and `tests/check-legacy-decode.ps1`).

- **Golden vectors (33-72):** expected payloads and CRCs come from the TSV fixture, not from the code under test. The compressed-over-100 branch checks the flag byte and round-trip only, and the comment explains why (zlib output may differ by encoder).
- **CRC and truncation (75-100):** every byte is flipped and every short length is checked. Both paths are reached, since `decode` returns `BadCrc` before any length or flag check.
- **Compression, zlib and bounds (103-144):** the error variants match the branches in `decode`/`inflate_bounded`. The 65,507 datagram boundary matches `MAX_DATAGRAM`.
- **Ordered delivery, windows and buffer limits (147-211):** `buffered_bytes` counts the two-byte sequence header, which is why the 5-byte limit trips on `"x"`. Ack expectations follow `contiguous_ack` and the `SELECTIVE_ACK` branch.
- **Oversized future data (214-242):** the 6-byte data limit (`max_message` + header) and the 10-byte first-fragment allowance both match `receive_at`.
- **Fragments (245-310):** the `ack.packet()` expectation of opcode 21 with payload `[0,1]` matches `CUMULATIVE_ACK` = 21 and the big-endian sequence encoding. The "interrupt" case reaches `UnexpectedDataDuringFragment` through the ordered path, since `next` has already advanced past the first fragment.
- **Invalid buffered fragment (313-337):** `rejected_buffered == (1, InvalidFragment)` and the cumulative ack at 0 follow from the drain loop in `receive_at`. The poisoned-receiver checks match line 378.
- **Reordered rollover (340-382):** the expected values are built independently of the receiver (`0..131_104`, `start + 131_104`), and `max_message` is 8, large enough for the 4-byte payloads.
- **Ignored test (384-432):** `#[ignore]` carries a reason. The fixture script exists and does a real comparison (CRC and decoded-payload mismatch, plus a row count), so the test can fail when the environment is present.

Two things I looked at and did not count as findings: the `count == 105` pin at line 71 (it guards against silently dropping fixture rows, and I did not verify the fixture has exactly 105 rows), and the uncompressed-mode decode at 129-133, which asserts only the size check and does not test the flag byte. Neither is a hole in the gate.
