<!-- fleet job=test-audit id=tests-opening-world-rs-L1 status=nothing_found turns=6 usd=0.0058 tokens(read,write,in,out)=[38698, 17429, 14, 6423] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/opening_world.rs lines 1-98 of 98

Reviewed `prototype/osfr-tools/tests/opening_world.rs` lines 1-98 against `src/opening_world.rs` (load/spawn/menu/initialization) and the fixture `tests/fixtures/opening-world-community-vectors.json` (present, with `template`, `spawn_before`, `spawn_after`, `menu_npc`, `menu_prop`).

No finding meets the five categories:

- **Cannot fail:** The main oracles are external. `spawn` is compared with the community-captured `spawn_after` vector (line 61-65), and `menu` with `menu_npc` / `menu_prop` (lines 84-86). The `initialization` expectation (lines 94-97) is hand-built from the protocol layout (count 1, the one non-enemy same-zone actor's guid, flags `[1,5,0]`). None of these are derived from the code under test. I checked the fixture: `spawn_before` has zeros where `spawn_after` has `00005040` (3.25f) at the radius offset, so the test does distinguish the fix. The template is also loaded from a fixture, not regenerated.
- **Asserts nothing that matters:** Not the case. The actor filter (`zone_id` and `kind != "enemy"`, src line 50) is exercised by the enemy and other-zone actors at lines 87-92, and the expected output would change if either filter broke.
- **Name overclaims:** The name promises a full community packet match, a native prompt radius with a UTF-8 name, and a preserved menu. Line 61 covers the packet, lines 75-77 cover the radius float, and lines 84-86 cover the menu. The name matches the body.
- **Silently skipped:** No `#[ignore]` and no early return. The fixture file exists.
- **Over-pinned:** Lines 68-83 pin the name-length offset (106), the radius offset (237 + name length), and the legacy int offset (133 + name length). These are redundant with the full-packet equality at line 61, but they are the field semantics the test is about, not incidental detail, so I do not count them as churn. The `1i32`/`4` at line 82 is a hand-written constant matching `ceil(3.25)`, which is correct.

Minor note, not a finding: the test writes its own `combat.json` with a hash computed from the same fixture bytes, so the evidence-hash rejection path in `OpeningWorld::load` (src lines 36-40) is not exercised here. The test name does not claim that coverage.
