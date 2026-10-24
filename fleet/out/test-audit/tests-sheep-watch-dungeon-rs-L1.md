<!-- fleet job=test-audit id=tests-sheep-watch-dungeon-rs-L1 status=done turns=9 usd=0.0122 tokens(read,write,in,out)=[198016, 42519, 20, 9861] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/sheep_watch_dungeon.rs lines 1-1200 of 1368

Window: `prototype/osfr-tools/tests/sheep_watch_dungeon.rs` lines 1-1200. Helpers read: `tests/common/field_battle_fixture.rs` (`assert_payout` 690-718, `lab` 168, `battle_path` 160), `tests/field_battle_roster.rs:22` (its own `TASK_ROSTER`).

- **[medium] tests/sheep_watch_dungeon.rs:1177 the_existing_battles_and_content_are_unchanged - `assert!(!TASK_ROSTER.contains(&SHEEP_WATCH))` checks a hand-copied local constant against another constant, not the shipped roster.**
  - Why it cannot catch a regression: `TASK_ROSTER` is a literal at line 109 (`[96, 12301, 12302, 12310, 12311]`), and nothing in the file reads the data for it. If someone adds 12350 to the roster in `field_battle_roster`'s data or code, or into the real roster the game uses, this assertion still passes. The doc at line 107-108 says the roster comes from `field_battle_roster`, so the claim is not exercised.
  - Fix: derive the roster from the shipped data (for example, the rows that `field_battle_roster.rs` counts at lines 547/571/591 as the designated set, or a roster flag in `field_battle_roster`) and assert 12350 is absent from it. Otherwise drop the line and the doc claim.

- **[medium] tests/sheep_watch_dungeon.rs:1036-1038 and 1043-1063 the_existing_battles_and_content_are_unchanged - the doc promises "payout" and "the new row is the only addition", but prizes are never compared and no addition check exists.**
  - Why it cannot catch a regression: the `expected` table (1043-1051) pins only title, difficulty, required level and `reward_coins`. Changing a pre-existing row's `prizes` (item ids or count) passes, and so does changing its `enemies` kinds, zone or spawner fields other than GUID/position. The "only addition" claim is also unasserted: the only check is that each id appears once (1161-1167) and that 12350 follows 12303 (1172-1176). The T354 comment at 1158-1160 says later rows are expected, which conflicts with the doc's "only addition" wording.
  - Fix: add `assert_eq!(prize_ids(row), <pinned set>)` (or the pinned item id/quantity list) for each of the eight rows, and correct the doc so it describes what is actually pinned (title, difficulty, required level, coins, GUIDs, positions, uniqueness).

- **[low] tests/sheep_watch_dungeon.rs:973-975 the_row_is_inside_the_loader_and_reward_bounds - the 1..=16 bound is a literal, and the doc calls it "the loader's real cap".**
  - Why it cannot catch a regression: the test never calls the loader with 17 enemies. Changing the loader cap in `src/encounter/field.rs` (for example to 32) does not fail this check, and the real load at 995-998 only proves the five shipped enemies load. Only the contents of the 16 literal are checked.
  - Fix: build a copy of the row with 17 enemies (unique GUIDs), call `load_field_battles`, and assert the error. Or reword the comment to say the bound is a hand-copied sanity range.

- **[low] tests/sheep_watch_dungeon.rs:416-420 the_marker_is_drawable_and_the_portal_publishes_sheep_watch - "model 3284 is present in catalog.tsv" only checks the file name.**
  - Why it cannot catch a regression: `catalog.contains("\twolf_generic.adr\t")` passes for any catalogue row that names that file, whatever its model or path. Only Models.txt at 411-413 ties 3284 to the file.
  - Fix: check the catalogue row for `wolf_generic.adr` against the same model id or a full path, or reword the message to "wolf_generic.adr is in catalog.tsv".

- **[low] tests/sheep_watch_dungeon.rs:336 the_marker_is_drawable_and_the_portal_publishes_sheep_watch - `assert_eq!(disc.len(), 105)` pins the terrain helper's sampling density, which is unrelated to the marker's standability claim.**
  - Why it cannot catch a regression: it is not a regression check. A change to the disc sampling in `support/terrain.rs` (step size or ring count) fails this test even when every sampled point is still on ground and under 25 degrees, which is what the test is about.
  - Fix: drop the exact count and assert `disc.len() >= 100`, or assert only that every disc point has ground (already done at 337-342).

- **[low] tests/sheep_watch_dungeon.rs:979 the_row_is_inside_the_loader_and_reward_bounds - `reward_coins <= 1_000_000` is an arbitrary ceiling that does not enforce the "bounded coin payout" doc.**
  - Why it cannot catch a regression: a shipped row changed to 999,999 coins passes. Exact payout is pinned elsewhere (test 1 at 293 and 1048-1062), so the risk is limited, but this bound adds no protection.
  - Fix: remove it, or tie it to the content's declared maximum reward if one exists.

Not reported (checked, fine): the 8-25 m Pappy distance and terrain/NPC/enemy clearance checks (300-361), the duplicate and forged-request refusals with state-and-save comparisons (602-796), and the two-session isolation checks (867-937). The `lab()` fixtures (Models.txt, catalog.tsv, locale report) are unwrapped reads, so they fail rather than skip when missing.
