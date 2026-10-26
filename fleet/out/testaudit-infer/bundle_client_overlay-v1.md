<!-- fleet job=testaudit-infer id=bundle_client_overlay-v1 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5717, 8339, 6, 1119] model=claude-haiku-5-5 -->
# tests/bundle_client_overlay.rs

{"file": "tests/bundle_client_overlay.rs",
 "tests": [
  {"name": "python_bundle_overlay_is_pinned_or_not_built", "verdict": "keep", "covered_by": null, "reason": "Only Rust driver for tests/test_bundle_client_overlay.py, which checks make_bundle.copy_client_overlay (the bundle's overlay folder). tests/client_overlay.rs drives a different script (scripts/bundle/client_overlay.py, the launcher overlay via tests/test_client_overlay.py), so it does not cover the bundle path."},
  {"name": "bundled_login_resources_turn_on_the_creator_allow_list", "verdict": "keep", "covered_by": null, "reason": "Only test that builds a real bundle through copy_fixed_inputs and copy_client_overlay and then checks Resources::load(...).filters_looks() end to end. Related tests/creator_allow_list.rs checks the pinned tables and identity.rs, not the bundled output. Not a duplicate. Also a canary for the T575 wiring (see notes/Autopilot/T575.md mutation check B)."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Both tests skip-or-pass-silently when the lab asset cache is absent (the Python test runs unconditionally). Both were created and last changed by T575 with no later edits, so none is obsolete. I did not open tests/creator_allow_list.rs in full, so the claim that it does not exercise the bundle output is based on its name and cross-references, not its body. Keep both."}
