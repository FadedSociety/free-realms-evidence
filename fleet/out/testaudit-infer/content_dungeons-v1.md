<!-- fleet job=testaudit-infer id=content_dungeons-v1 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[35279, 15120, 10, 1814] model=claude-haiku-5-5 -->
# tests/content_dungeons.rs

{"file": "tests/content_dungeons.rs",
 "tests": [
  {"name": "every_dungeon_file_loads_and_validates", "verdict": "keep", "covered_by": null, "reason": "Only loader gate for all 75 shipped dungeon files: checks schema_version, one record per file, source provenance tags (reconstructed evidence must start with (R)), file stem == dungeon id, no duplicate ids, required dungeon_data keys, then ContentDb::load of the scratch copy with count 75. sheep_watch_dungeon.rs:1179-1182 explicitly defers to this test as the canonical loader proof, so it is not duplicated there."},
  {"name": "external_references_resolve_or_are_listed", "verdict": "keep", "covered_by": null, "reason": "Pins the dungeons_unresolved.json list against the live catalogues: every reference either resolves (and must not be listed) or is listed, no duplicate references or rows. No other test in the suite reads dungeons_unresolved.json; it is a data-consistency guard, not a duplicate of content.rs's dangling-reference fixtures, which use synthetic fixtures."},
  {"name": "opening_cave_matches_the_native_accepted_content_definition", "verdict": "keep", "covered_by": null, "reason": "Parity check of the converted opening_cave.json against the accepted lab encounters.json (encounter 411): ids, strings, zone, guide, enemy stats, rewards, and the typed Dungeon record. No other test in the pack compares against the lab reference source. Not clearly covered elsewhere; keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Pack gave only the three test names and an excerpt; I read the full file (lines 200-437) and sheep_watch_dungeon.rs:1170-1200 for cross-references. Similar files (power_ups, opening_abilities, content, world, progression_extras) were judged by name only; content.rs tests use synthetic fixtures for ContentDb::load error paths, which does not overlap the shipped-data gates here. Minor observation, not a removal basis: validation_fixture is a shared helper that copies tests/fixtures/content and injects zone 411 and item 1195 for the opening cave; if the shipped zones/items gain those rows, the injection becomes a no-op but the test still holds."}
