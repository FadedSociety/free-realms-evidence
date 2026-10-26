<!-- fleet job=testaudit-infer id=power_ups-v1 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[9857, 13325, 6, 1598] model=claude-haiku-5-5 -->
# tests/power_ups.rs

{"file": "tests/power_ups.rs",
 "tests": [
  {"name": "shipped_file_loads_and_references_resolve", "verdict": "keep", "covered_by": null, "reason": "Only check that the shipped power_ups.json loads and exposes the standard/elite/boss tables and the flame_wave/energy kinds with the expected auto flags; the similar power_up_drops.rs tests exercise the engine, not this module-level load."},
  {"name": "every_bound_rejects_a_bad_file", "verdict": "keep", "covered_by": null, "reason": "Canary with about 40 bound edits that must each be rejected, plus an accept-the-untouched-file check. Only partly overlapped by power_up_drops.rs::participation_settings_are_bounded (participation fields only); pickup, kind, area, burn, and table bounds are not covered elsewhere."},
  {"name": "non_finite_and_unknown_fields_and_oversize_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Hostile-input refusal: NaN-as-string, unknown field, oversize document, and malformed JSON. Security/refusal check, so kept."},
  {"name": "roll_is_deterministic_for_a_fixed_seed", "verdict": "keep", "covered_by": null, "reason": "Pins the splitmix64 output for seed 0 as a generator canary and checks seeded reproducibility. No other file pins this value."},
  {"name": "guaranteed_drops_always_come_first_and_skip_the_rolls", "verdict": "keep", "covered_by": null, "reason": "Checks that guaranteed kinds are returned first and bypass the rolls. Engine-level power_up_drops.rs tests are about boss/guaranteed content, not this roll ordering; kept conservatively."},
  {"name": "roll_distribution_matches_chances_and_weights", "verdict": "keep", "covered_by": null, "reason": "Statistical check of drop rate and pool weights over 400k rolls at the module level. power_up_drops.rs has a group-multiplier sample but not this per-weight share check. Costly but not a duplicate; possible candidate to shrink, not to remove."},
  {"name": "zero_chance_never_drops", "verdict": "keep", "covered_by": null, "reason": "Boundary check that chance 0.0 never drops. Not clearly covered; power_up_drops.rs line ~88 uses chance 0.0 only in a fixture for a different purpose."}
 ],
 "whole_file_removable": false,
 "confidence": 0.5,
 "notes": "Based on the pack plus a repo-wide grep for Rng::seeded, from_json and chance in tests/. I did not read power_up_drops.rs in full, so the superseded/duplicate calls are conservative. The distribution test is the slowest (400k rolls) and could be sped up, but it is not redundant. Nothing in this file is clearly obsolete: no later task replaced its behaviour, and the file has no creator or changer recorded in the pack."}
