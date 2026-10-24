<!-- fleet job=pin-audit id=tests-opening-journal-rs status=nothing_found turns=4 usd=0.0019 tokens(read,write,in,out)=[13808, 9054, 10, 1189] model=claude-haiku-5-5 -->
# tests/opening_journal.rs

No findings. All four screened assertions (lines 364, 365, 382, 383) check the 10 and 30 values in the trailing bytes of the journal. Those values come from the test's own fixture: `old_journal()` in `tests/opening_journal.rs` lines 31-32 writes `10i32` and `30i32` directly. The journal code (`src/opening_journal.rs`) has no such constants; the only "10" there is a packet type (`packet(10)`, line 376). So the test is comparing against its own synthetic input, not a value from `data/content/*.json`, and retuning data would not affect it.
