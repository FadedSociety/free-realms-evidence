<!-- fleet job=testaudit-infer id=spine_rules-v1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[7936, 11962, 6, 835] model=claude-haiku-5-5 -->
# tests/spine_rules.rs

{"file": "tests/spine_rules.rs",
 "tests": [{"name": "spine_rules_only_ratchet_down", "verdict": "keep", "covered_by": null, "reason": "The only test of the spine ratchet. It is a structural guard that fails when hub line counts or banned patterns (plain fs::write, hex outside trace.rs, busy-state checks outside occupation.rs) grow past tests/spine_rules.ceilings. It also checks that Cargo.toml keeps panic = \"unwind\" for the gateway isolation boundary. No other test in the suite measures these rules. The similar files in the pack (progression_extras, piece_053, piece_037, mining, chess) test gameplay behaviour and do not overlap it. A repo-wide search for the ratchet and production_sources helpers found no other copy."}],
 "whole_file_removable": false,
 "confidence": 0.9,
 "notes": "One test, a lint-style guard rather than a behavioural test. It is not redundant. Its side effect (SPINE_RATCHET_LOWER=1 rewrites tests/spine_rules.ceilings) is intended and run by integrate.sh, so it is not a candidate for removal. The test is cheap, but removing it would lose the ratchet, so it should stay. The similar-file list was based on name overlap only (shared_score 2) and was not used as evidence."}
