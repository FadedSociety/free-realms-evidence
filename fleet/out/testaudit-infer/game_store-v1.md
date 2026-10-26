<!-- fleet job=testaudit-infer id=game_store-v1 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[25034, 17760, 8, 2165] model=claude-haiku-5-5 -->
# tests/game_store.rs

{"file": "tests/game_store.rs",
 "tests": [
  {"name": "version_one_migrates_without_changing_coordinates_and_corruption_is_preserved", "verdict": "keep", "covered_by": null, "reason": "Only test that drives game_store's version-1 envelope migration with coordinates preserved, no implicit write on load, and the corrupt/oversized/unknown-version refusals leaving bytes unchanged. save_schema.rs covers the character_store v1 migration and later game-store schemas, not this path. Refusal and persistence check, so keep."},
  {"name": "pet_state_uses_the_current_schema_constant", "verdict": "superseded", "covered_by": "tests/game_store.rs::one_save_writes_character_and_roster_and_none_keeps_the_disk_roster", "reason": "Its only assertion is saved[\"schema_version\"] == PET_SCHEMA_VERSION after saving a pets snapshot. The sibling test in the same file makes the same assertion on a pets save and also checks character, roster, and housing persistence, so this test adds nothing. Removable, though it is cheap and low-risk to keep if preferred."},
  {"name": "one_save_writes_character_and_roster_and_none_keeps_the_disk_roster", "verdict": "keep", "covered_by": null, "reason": "Covers the atomic character+roster envelope, housing preservation, the None-keeps-roster rule, and a refused NaN write leaving the file byte-identical. save_schema.rs schema_five covers None-keeps-roster only after migration, not the atomic refusal. Persistence and refusal check, so keep."},
  {"name": "replace_pose_changes_only_the_pose_and_refusals_change_nothing", "verdict": "keep", "covered_by": null, "reason": "The only test of game_store::replace_pose anywhere in tests/. It checks that only position and rotation change, that None keeps the facing, that a wrong-zone or out-of-range save is refused, and that a missing save is not created. Refusal and persistence check, so keep."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Three of four tests are unique or carry refusal/persistence checks. Only pet_state_uses_the_current_schema_constant is a subset of a sibling test in this file. The similar-file overlap (save_schema.rs, housing_session.rs) is shallow: save_schema covers migrations and None-keeps-roster after migration, not the refusal paths or replace_pose. The file is small and cheap, and its doc lines cite the gateway f161 tests, which I did not open."}
