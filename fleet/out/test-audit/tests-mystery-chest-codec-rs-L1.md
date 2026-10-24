<!-- fleet job=test-audit id=tests-mystery-chest-codec-rs-L1 status=nothing_found turns=5 usd=0.0057 tokens(read,write,in,out)=[41555, 19332, 12, 5708] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/mystery_chest_codec.rs lines 1-392 of 392

Reviewed `prototype/osfr-tools/tests/mystery_chest_codec.rs` lines 1-392 against `prototype/osfr-tools/src/mystery_chest.rs` (parse_request, check_reply, item_reward, read_u16, eof/invalid). No finding meets the report criteria.

Checks performed:
- **Cannot fail:** `expected_item_reward` (lines 46-103) is a hand layout that is not derived from the codec. I counted its fields against the header and body comments: 3 header + 65 base + 42 entry + 4 word = 114, which matches the assertion at line 253. The check-reply expected array (194-203) is hardcoded and matches `check_reply` constants. The `item_reward_preserves_maximal_and_minimal_values` comparison (381-391) uses the same arguments as the codec call, but the expected side is the hand layout, so it is not a tautology.
- **Offsets:** I verified the entry offsets. Entry starts at 68, icon tint is at 77..81, and inventory tint is at 93..97. The `-1` sentinel assertions at lines 354-355 hit the correct fields. The distinct-value offset test (258-336) catches a swap of tint and icon_tint, since it uses -3 and -4.
- **Truncation and trailing bytes (150-178):** `read_u16` returns UnexpectedEof for short headers. Bodies shorter than 8 bytes return eof. Bytes beyond 8 return InvalidData. The assertions match these paths, and the `len < 2` branch is consistent with the code.
- **Non-positive ids (181-189, 339-351):** The codec rejects `item_id <= 0` and `definition_id <= 0` with InvalidData, and the tests cover both fields.
- **Skips:** No `#[ignore]`, no early returns, and no fixture dependencies in this window.
- **Name vs body:** Test names match their bodies. The one soft spot is `item_reward_rejects_non_positive_ids_but_keeps_unknown_fields` (339), where "keeps unknown fields" is checked only through two `-1` sentinel words. That is still a real check, so I did not report it.
- **Minor note, not reported:** `item_reward_matches_the_independent_byte_layout` (221) uses tint = icon_tint = -1, so a swap of those two arguments would not be caught there. The offset test at 258 covers that swap with distinct values, so the gate is not weakened.
