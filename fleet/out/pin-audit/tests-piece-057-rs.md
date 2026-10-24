<!-- fleet job=pin-audit id=tests-piece-057-rs status=nothing_found turns=2 usd=0.0011 tokens(read,write,in,out)=[1856, 6114, 6, 646] model=claude-haiku-5-5 -->
# tests/piece_057.rs

No findings in `prototype/osfr-tools/tests/piece_057.rs` for the screened lines.

- **piece_057.rs:119 pinned_weighted_selection_matches_community_semantics** - expects `total_weight() == 2`. This is the sum of the weights in the test's own fixture (`DropTable::new("dev-test-reward", vec![WeightedDrop::item(205, 1, 1), WeightedDrop::coins(50, 1)])`, weights 1 + 1). It does not come from any data file, so it is not a finding.
- **piece_057.rs:185 a_kill_is_registered_once_and_granted_once** - expects `granted(&kill) == Some(WeightedDrop::item(205, 1, 1))`. Item 205 and weight 1 are literals in the same fixture table built at line 172. The test sets them itself, so it is not a finding.

The file's other constants (loot event opcode, model ids, locale ids, documented drop lists) are protocol or recovered-evidence values held in the source, not tunable gameplay values in `data/content`. None of them is a finding.
