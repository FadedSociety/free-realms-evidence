<!-- fleet job=testaudit-infer id=quest_breadcrumb-v3 status=no_submit turns=3 usd=0.0046 tokens(read,write,in,out)=[32819, 22462, 8, 2836] model=claude-haiku-5-5 -->
# tests/quest_breadcrumb.rs

```json
{"file": "tests/quest_breadcrumb.rs",
 "tests": [
  {"name": "the_shipped_crosswalk_loads_and_points_at_real_quests", "verdict": "keep", "covered_by": null, "reason": "Only test that checks the shipped data/content/breadcrumb_quests.json against the real quest catalogue (ids exist, no id-space overlap, Cooking starter reachable, unsupported mappings stay unavailable). Data canary."},
  {"name": "every_shipped_row_names_its_points_and_says_how_it_was_decided", "verdict": "keep", "covered_by": null, "reason": "Provenance invariant on the shipped file (legacy-data and client sources, (R) tag on reconstructed decisions). Nothing else reads these tags."},
  {"name": "a_missing_file_is_an_empty_crosswalk", "verdict": "keep", "covered_by": null, "reason": "Loader contract for an absent file; no other test calls load_crosswalk on a missing file."},
  {"name": "unmapped_rows_are_kept_out_of_the_map", "verdict": "keep", "covered_by": null, "reason": "Loader behaviour for regional_quest_id null; unique to this file."},
  {"name": "malformed_crosswalks_are_errors_not_silent_empties", "verdict": "keep", "covered_by": null, "reason": "Refusal and hostile-input check across many malformed documents; no equivalent elsewhere."},
  {"name": "only_breadcrumb_starts_are_rewritten", "verdict": "keep", "covered_by": null, "reason": "Checks translate() passes Select and Lock through untouched and only rewrites Breadcrumb; no other test calls translate directly."},
  {"name": "a_listed_original_id_offers_its_regional_quest_once", "verdict": "superseded", "covered_by": "tests/quest_journal.rs::breadcrumb_makes_the_normal_offer_and_never_completes_anything", "reason": "Offer path (single offer, Offered status, no award, re-press re-shows the same offer, accept to Active with zero counts) is asserted at equal or greater strength in quest_journal. The only extra step here is the 1807->10 translate mapping, which the loader tests above already pin."},
  {"name": "an_unlisted_original_id_is_refused_and_changes_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check for original ids absent from the crosswalk (1814) and for forged values; translate returns None so nothing reaches the journal. quest_journal only covers regional or forged ids sent as breadcrumbs directly, not the unmapped-original gate."},
  {"name": "a_listed_id_the_engine_will_not_offer_is_refused_with_a_denial_and_changes_nothing", "verdict": "superseded", "covered_by": "tests/quest_journal.rs::breadcrumb_refusals_leave_state_untouched", "reason": "Same denials (Prerequisite for 11, Unavailable for hollow 12, Level for 13), same no-change and no-award assertions, driven through the same journal handler. The translate step only maps 1808/1809/1810 to 11/12/13."},
  {"name": "a_full_quest_log_refuses_the_start_and_says_so", "verdict": "superseded", "covered_by": "tests/quest_journal.rs::breadcrumb_respects_the_quest_limit_and_sends_the_limit_notice", "reason": "Same Limit denial, same QuestLimit{member:true} notice, same state-unchanged assertion. Only difference is how the slot is filled (offer+accept of 15 here, activate 14 there)."},
  {"name": "a_listed_id_for_a_quest_already_done_or_held_changes_nothing", "verdict": "superseded", "covered_by": "tests/quest_journal.rs::breadcrumb_for_an_active_quest_just_selects_it", "reason": "Active-quest breadcrumb only selects, no award, and a repeat press changes nothing; quest_journal asserts the same. The completed-quest refusal is covered by quest_journal::breadcrumb_cannot_be_used_to_skip_an_open_offer_or_finished_quest."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "Six of eleven tests are the gateway-shaped journal checks, which quest_journal.rs already covers at equal or greater strength; they could be dropped without loss, though the translate step is their only extra coverage. The loader, shipped-data and provenance tests (about half the file) are unique and should be kept, so the file as a whole is not removable. I did not re-verify the quest_journal assertions beyond reading them, and the previous answer's truncated reasoning was not re-checked."}
```
