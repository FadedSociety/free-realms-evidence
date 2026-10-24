<!-- fleet job=test-audit id=tests-medic-entry-content-rs-L1 status=nothing_found turns=6 usd=0.0028 tokens(read,write,in,out)=[32941, 11814, 14, 2020] model=claude-haiku-5-5 -->
# prototype/osfr-tools/tests/medic_entry_content.rs lines 1-16 of 16

No findings in `prototype/osfr-tools/tests/medic_entry_content.rs` lines 1-16.

What I checked:
- The test `enabled_medic_chapter_records_are_complete_and_others_stay_disabled` (lines 13-16) only calls `medic_entry::assert_enabled_medic_chapter_records()`. The real assertions are in `support/medic_entry.rs:62-197`, which I read.
- The name's "others stay disabled" claim is backed by an exact-equality check on the enabled ID list (`medic_entry.rs:69-82`). `SURGICAL_PRECISION` (3_090_008) is not in that list, so a regression that enables it would fail.
- The "complete" claim is backed by per-record checks: giver NPC binding in both `quest_ids_given` and `quests_given`, title id match, Medic job, non-empty objectives and rewards with provenance, Medic XP on rewards, and no invented items.
- Silent-skip risk: `content_dir()` (`support/npc_quest_chain.rs:48-50`) is a fixed path under `CARGO_MANIFEST_DIR`, and `read_json` (`npc_quest_chain.rs:61-66`) panics on a missing or unparseable file. There is no early return or `#[ignore]` in this path.
- Header doc (lines 1-5) accurately describes the target as the focused, packet-free run of the same check.

The window is a thin wrapper around a non-trivial, non-tautological check. I did not read the rest of `medic_entry.rs` (lines 200-392), which is outside my window.
