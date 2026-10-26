<!-- fleet job=testaudit-infer id=job_browser-v1 status=done turns=6 usd=0.0041 tokens(read,write,in,out)=[62878, 14982, 14, 3202] model=claude-haiku-5-5 -->
# tests/job_browser.rs

{"file": "tests/job_browser.rs",
 "tests": [
  {"name": "packet_matches_the_capture", "verdict": "keep", "covered_by": null, "reason": "Byte-exact check of 147/1 against a checked-in 2014 client capture (SHA-256 pinned); no other test pins this packet encoding."},
  {"name": "shipped_rows_resolve", "verdict": "keep", "covered_by": null, "reason": "Verifies shipped Become-a rows against captured rows, jobs.json profiles, locale ids and the crosswalk map; unique data-integrity check."},
  {"name": "world_entry_sends_one_147_1", "verdict": "keep", "covered_by": null, "reason": "Session-scoped send-once behaviour at world entry, zone-ready no-resend and reconnect resend; not covered elsewhere in the similar files."},
  {"name": "two_players_each_get_their_own_147_1", "verdict": "keep", "covered_by": null, "reason": "Per-session isolation (no broadcast) of the list; multiplayer.rs covers sessions generally but not this packet."},
  {"name": "start_quest_with_a_disabled_or_unmapped_id", "verdict": "superseded", "covered_by": "tests/quest_breadcrumb.rs::an_unlisted_original_id_is_refused_and_changes_nothing", "reason": "Unmapped ids (1952 has no regional quest; 1968 disabled) go through the same 49/15 breadcrumb refusal path and assert no change and the BREADCRUMB_REFUSED reply; quest_breadcrumb covers unlisted ids (1814, 10, 14, forged) and disabled/denied listed ids with denial and no change, and npc_interaction::journal_49_15_unlisted_id_is_refused_with_one_line covers the one-line refusal. Only the 1968 disabled-regional case is specific to this file; kept conservative as a possible removal rather than a hard duplicate."},
  {"name": "zero_or_negative_breadcrumb_is_refused_politely", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal (0, -1, i32::MIN) that must not end the session and must change nothing; no equivalent zero/negative case found in the similar files."},
  {"name": "start_quest_with_a_mapped_id", "verdict": "superseded", "covered_by": "tests/quest_breadcrumb.rs::a_listed_original_id_offers_its_regional_quest_once", "reason": "Same path (49/15 breadcrumb on a listed original id offers the regional quest, no award, status Offered, no change on re-press). Different quest ids (1968->3070001 here, 1807->10 there), so moderate confidence; the job-browser variant is the only one tied to the Jobs window route."},
  {"name": "bad_job_browser_data_is_refused", "verdict": "keep", "covered_by": null, "reason": "Load-time refusal of malformed job browser content; a refusal/validation check with no equivalent named elsewhere."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "The file tests/job_browser.rs is not present under prototype/osfr-tools/tests in the repo (searches for its test names returned nothing; read reported 'not a file' for the path given in the pack), so the verdicts rely on the pack excerpt, which was truncated after zero_or_negative_breadcrumb_is_refused_politely; the bodies of start_quest_with_a_mapped_id and bad_job_browser_data_is_refused were not readable and are judged from names and the pack's doc context. Confirm the file's location before acting. Whole file is not removable: its byte-level capture test and 147/1 session tests have no equivalent elsewhere."}
]}
