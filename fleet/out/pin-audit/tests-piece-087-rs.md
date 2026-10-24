<!-- fleet job=pin-audit id=tests-piece-087-rs status=nothing_found turns=3 usd=0.0011 tokens(read,write,in,out)=[5240, 4620, 8, 883] model=claude-haiku-5-5 -->
# tests/piece_087.rs

No findings for `prototype/osfr-tools/tests/piece_087.rs:222` (`friend_list_encodes_the_inferred_layout_byte_for_byte`).

The `110` is not read from a data file. It comes from the test's own fixture: `fn status()` at line 70 sets `status: 110`, and `nova_row()` is built from that fixture. The assertion checks that the encoder writes that fixture value into the status slot (bytes 42..46). The test would pass for any value the fixture sets, so retuning a data file cannot break it. The code under test is not a tunable gameplay value either. The screening note's "player health" label does not match this code: the field is a friend-status code, and the file's own header says its meaning is unknown.
