<!-- fleet job=testaudit-infer id=creator_allow_list-v1 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[23644, 15340, 8, 1393] model=claude-haiku-5-5 -->
# tests/creator_allow_list.rs

{"file": "tests/creator_allow_list.rs",
 "tests": [
  {"name": "only_the_looks_the_pinned_tables_offer_resolve", "verdict": "keep", "covered_by": null, "reason": "Exhaustive 8x8 skin/head allow-list check against the pinned SkinTone/FaceType tables via Resources::resolve, tied to piece_049 SUPPORTED_* sets. No other test in the similar files or login.rs drives this allow-list; it is the only check of this behaviour."},
  {"name": "hidden_skin_or_face_is_refused_and_writes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal test: hidden skin 7/8 and face 5-8 are refused with create_reply(2,0) and the snapshot of all files is unchanged. login.rs::malformed_creation_and_invalid_appearance_do_not_save covers a different refusal (choices[0]=4, malformed bytes, invalid names), not the hidden skin/face allow-list, so it is not a duplicate. Refusal and persistence check, so kept."},
  {"name": "a_client_tree_without_its_pinned_tables_does_not_load", "verdict": "keep", "covered_by": null, "reason": "Security/tamper check: an unpinned (original) SkinTone table and a missing item-mapping join must refuse Resources::load. Notes/Autopilot/T444.md records that canary D (SHA-256 pin check disabled) fails this test. No equivalent pin-hash refusal test was found elsewhere."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Searched repo for the allow-list and pin names; the only overlapping creation-refusal test is tests/login.rs::malformed_creation_and_invalid_appearance_do_not_save, which exercises a different path. The file is new (T444) and was not compared line-by-line against identity.rs tests or piece_049.rs tests, which the excerpt says pin the same tables; a reviewer could check whether piece_049 tests assert the same SUPPORTED_* equality, which would make the first test partly duplicative. Shared-score similar files (chess, piece_057, npc_interaction, kart_npc_entry, fishing_entry) are unrelated domains and contributed no overlap."}
