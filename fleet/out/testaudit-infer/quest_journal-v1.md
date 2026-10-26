<!-- fleet job=testaudit-infer id=quest_journal-v1 status=done turns=2 usd=0.0036 tokens(read,write,in,out)=[12050, 17689, 6, 2513] model=claude-haiku-5-5 -->
# tests/quest_journal.rs

{"file": "tests/quest_journal.rs",
 "tests": [
  {"name": "decodes_exact_native_widths", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the exact 47/12, 47/13 and 49/15 wire layouts and sizes (7/4/10 bytes) of the decoder; the other quest tests go through these helpers, so this is the sole wire-width check."},
  {"name": "other_packets_are_left_to_the_rest_of_the_dispatch", "verdict": "keep", "covered_by": null, "reason": "Boundary check that foreign families/subtypes (49/2, 47/14, 49/15 subtype 271, truncated headers) are not claimed by the journal decoder; a refusal-style guard not found elsewhere in this form."},
  {"name": "malformed_journal_packets_are_refused_without_panicking", "verdict": "keep", "covered_by": null, "reason": "Hostile-input and canary test (trailing byte, short id, non-bool flag) plus an edge-byte sweep; security-relevant, so kept."},
  {"name": "a_breadcrumb_with_a_non_positive_id_is_a_request_for_id_zero", "verdict": "keep", "covered_by": null, "reason": "Latest behaviour change (T497) replacing the old malformed-session rule; it is the current contract and is not superseded by any other test."},
  {"name": "selecting_an_owned_active_quest_persists_and_survives_a_reload", "verdict": "keep", "covered_by": null, "reason": "Persistence/reload check of selection state; kept under the persistence rule."},
  {"name": "forged_or_ineligible_selections_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal test: forged selections must not change state."},
  {"name": "selecting_a_completed_quest_is_refused", "verdict": "keep", "covered_by": null, "reason": "Refusal test for completed quests; a small, distinct assertion from the forged-selection test (Unavailable denial plus unchanged state after reload)."},
  {"name": "lock_flag_is_the_inverse_of_the_client_auto_switch_flag", "verdict": "keep", "covered_by": null, "reason": "Pins the 47/13 byte polarity and persistence; no equivalent found in the sampled similar files."},
  {"name": "locking_touches_neither_selection_nor_progress", "verdict": "keep", "covered_by": null, "reason": "Refusal/no-side-effect check for lock; kept as a state-unchanged guard."},
  {"name": "breadcrumb_makes_the_normal_offer_and_never_completes_anything", "verdict": "keep", "covered_by": null, "reason": "Core breadcrumb contract (offer, no award); unique to this file's handle() path."},
  {"name": "breadcrumb_for_an_active_quest_just_selects_it", "verdict": "keep", "covered_by": null, "reason": "Distinct branch (owned quest selects, no outbound) with no-award assertion."},
  {"name": "breadcrumb_refusals_leave_state_untouched", "verdict": "keep", "covered_by": null, "reason": "Refusal test covering prerequisite, level, hollow and hostile ids with state equality; kept."},
  {"name": "breadcrumb_cannot_be_used_to_skip_an_open_offer_or_finished_quest", "verdict": "keep", "covered_by": null, "reason": "Security/refusal test for skipping open offers and completed quests."},
  {"name": "breadcrumb_respects_the_quest_limit_and_sends_the_limit_notice", "verdict": "keep", "covered_by": null, "reason": "Quest-limit refusal plus QuestLimit notice; unique assertion of the notice message."},
  {"name": "a_replayed_breadcrumb_burst_makes_one_offer_and_one_quest", "verdict": "keep", "covered_by": null, "reason": "Replay/idempotence canary; kept under the replay rule. Overlaps in spirit with tests/quest_breadcrumb.rs but drives a different path (handle over a live engine), so not claimed as a duplicate."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Checked only the test file itself, its tail (lines 285-462), and grep hits for breadcrumb/49-15 across tests/. Related files: tests/quest_breadcrumb.rs (translate/crosswalk path, different API) and tests/npc_interaction.rs (line ~842 BREADCRUMB_REFUSED and ~1013 49/15 request; a refusal-line check, not the same assertions). I did not read quest_breadcrumb.rs or npc_interaction.rs bodies, so possible overlap with breadcrumb_refusals_leave_state_untouched or the 49/15 refusal path is unverified; I kept everything conservatively. Candidate for a follow-up: compare breadcrumb_refusals_leave_state_untouched against npc_interaction.rs journal_49_15_unlisted_id_is_refused_with_one_line."}
