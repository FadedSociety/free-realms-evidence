<!-- fleet job=testaudit-infer id=consumable_effects-v1 status=done turns=4 usd=0.0039 tokens(read,write,in,out)=[42724, 17855, 10, 2517] model=claude-haiku-5-5 -->
# tests/consumable_effects.rs

{"file": "tests/consumable_effects.rs",
 "tests": [
  {"name": "layouts_follow_the_client_readers", "verdict": "keep", "covered_by": null, "reason": "Pins 35/13, 35/14, 35/15 wire layouts to named client readers; no other test in the repo encodes these packets (no match for encode_temporary_appearance or encode_update_scale outside this file)."},
  {"name": "transform_apply_sends_poof_model_then_row", "verdict": "keep", "covered_by": null, "reason": "Only check of the transform apply packet order and buff row fields; no similar test found."},
  {"name": "a_new_transform_replaces_the_old_without_a_revert", "verdict": "keep", "covered_by": null, "reason": "Replacement without revert is a behavioural edge case with no equivalent elsewhere."},
  {"name": "transform_expiry_resyncs_the_aura_and_keeps_its_buff_id", "verdict": "keep", "covered_by": null, "reason": "Expiry resync and buff-id persistence; no equivalent found."},
  {"name": "aura_and_scale_expire_exactly_once", "verdict": "keep", "covered_by": null, "reason": "Exactly-once expiry is a canary-style guard; no equivalent found."},
  {"name": "strip_ends_only_what_the_stack_owns", "verdict": "keep", "covered_by": null, "reason": "Refusal check for foreign ids that change nothing; must be kept."},
  {"name": "stripping_a_transform_reverts_and_resyncs_like_expiry", "verdict": "keep", "covered_by": null, "reason": "Strip path revert; overlaps expiry test in intent but drives the strip path; kept conservatively."},
  {"name": "ids_stay_in_their_ranges_and_never_collide", "verdict": "keep", "covered_by": null, "reason": "Id range and collision invariant; no equivalent found."},
  {"name": "a_delayed_aura_starts_once_after_its_delay", "verdict": "keep", "covered_by": null, "reason": "Delay timing and clock-backwards guard."},
  {"name": "an_aura_that_expires_before_it_starts_sends_only_its_row_removal", "verdict": "keep", "covered_by": null, "reason": "Edge case with distinct assertions."},
  {"name": "the_clock_going_backwards_expires_nothing", "verdict": "keep", "covered_by": null, "reason": "Hostile-input/clock-regression refusal; must be kept."},
  {"name": "refusals_change_nothing", "verdict": "keep", "covered_by": null, "reason": "Refusal check; must be kept."},
  {"name": "an_idle_stack_ticks_to_nothing", "verdict": "keep", "covered_by": null, "reason": "Trivial but not clearly covered elsewhere; conservatively kept."},
  {"name": "resend_shows_the_live_state_with_remaining_time", "verdict": "keep", "covered_by": null, "reason": "Resend path with remaining time; no equivalent found."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Could not verify against the crate: searches of the repo for consumable_effects, EffectStack, Spec/Kind or encode_temporary_appearance return no source match, so src/consumable_effects.rs (the module this file imports) does not appear to exist in the current tree. That either means the file cannot compile or the module lives outside the searched roots. Verdicts are therefore conservative keeps. The five most similar files (kart_service, coin_store_siblings, kart_npc_entry, vendor_sell, housing_service) share only generic patterns (refusal/bounded/gateway wording) and do not drive the consumable effect stack, so no superseded or duplicate claims were made. The only piece_056 test (tests/piece_056.rs) covers the 35/41-42 and 38/16-17 decoders that this file reuses, not the effect stack. A brief (T571-snowball-piles) mentions using the 'consumable effect stack', so the module is likely planned or in progress rather than obsolete. Recommend confirming whether src/consumable_effects.rs exists before any removal decision."}</result>
