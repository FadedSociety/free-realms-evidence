<!-- fleet job=test-verify id=tests-piece-073-rs-L1-f1 status=done turns=6 usd=0.0063 tokens(read,write,in,out)=[70082, 26872, 14, 4555] model=claude-haiku-5-5 -->
# high: tests/piece_073.rs:277-284

**Verdict:** `confirmed`

**Evidence:** I could not refute the claim. No assertion in the test would fail under the proposed mutation (drop `distance < best` at `src/restoration/piece_073.rs:409`, so the first in-range candidate wins).

Walk-through of `nearest_candidate_inside_the_caller_radius_is_discovered_once` (`tests/piece_073.rs:252-285`) with that change:
- Fixture: POI 3 at (0,0,0), POI 11 at (30,0,0), radius 10.
- Call 1, position (2,5,2): POI 3 is at distance ≈2.83 (in range). POI 11 is at ≈28.07 (out of range). Only one in-range candidate, so the mutant also returns `Discovered(3)`. The assertion at line 264 passes.
- Call 2 (replay): `AlreadyDiscovered(3)` at line 274. Passes.
- Call 3, position (29,0,0): POI 3 is at 29 (out of range). POI 11 is at 1 (in range). Again only one in-range candidate, so `Discovered(11)` at line 282. Passes.

So the "nearest wins" comment at line 277 is not exercised. The other tests have the same gap:
- `out_of_range_reports_the_nearest_candidate_without_granting` (288-302) and `distance_is_planar_so_height_does_not_decide_the_trigger` (304-331) each use a single definition. Mutating `distance < nearest.distance` at `src:403` (the `nearest_any` choice) changes nothing they assert.
- `zone_filter_keeps_unrelated_locations_out_of_the_candidate_set` (334-348) filters by location before the distance comparison, so it has one candidate in the filtered set.
- `invalid_radius_and_non_finite_positions_are_refused` (351-367) checks only the error paths.
- The `#[ignore]` private gate (394-565) asserts only decode equality and exports vectors. It does not assert outcomes. Its exported vectors also have a single candidate per filter where I checked (e.g. the location-281 vectors).
- `tests/pieces/test_piece_073.py` has no nearest-selection assertion either (its test names cover decode, rejection, table comparison and Lua column parsing).
- `warpstone_travel.rs` uses only `decode_poi_definitions` and `PoiTable`, not `DiscoveryTracker::evaluate`.

Because the selection rule is never checked with two in-range candidates, the first-in-range mutant passes the full Rust suite. The claim's line references (252-268, 277-284, 288-301, src 403-409) match the code.

**Minimal fix:** In the 277-284 step, or in a new table test, add a second definition at (6,0,0) inside radius 10 and assert that `evaluate(Position::new(7,0,0), None, 10.0)` returns `Discovered` with id 11 (nearer than POI 3 at distance 7). Also add a `NoCandidate(Some(n))` case with two out-of-range definitions at distances 20 and 30 and assert `n.poi_id` is the closer one.
