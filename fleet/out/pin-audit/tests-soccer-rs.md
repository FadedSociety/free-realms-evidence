<!-- fleet job=pin-audit id=tests-soccer-rs status=nothing_found turns=4 usd=0.0026 tokens(read,write,in,out)=[20552, 14459, 10, 1170] model=claude-haiku-5-5 -->
# tests/soccer.rs

No findings in `prototype/osfr-tools/tests/soccer.rs` for the three screened lines (221, 242, 250).

- The 120.0 and 110.0 values are the test's own synthetic wire inputs. `vec_time(120.0, 1.0)` at line 218 and `vec_time(110.0, 5.0)` at line 240 build the `UpdateGameTime` packets, and the reducer stores `remaining` straight from the packet. Lines 221, 242 and 250 assert the fixture's own input back, so they do not depend on any tunable value.
- No soccer data file in `data/content` carries a match duration or half-length field. A search for "soccer", "match_seconds" and "half" found only achievement, job, POI and quest rows, none of which hold a match clock.

Nothing to change for these lines.
