<!-- fleet job=testaudit-infer id=piece_070-v1 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[9751, 15780, 6, 1203] model=claude-haiku-5-5 -->
# tests/piece_070.rs

{"file": "tests/piece_070.rs",
 "tests": [
  {"name": "recovered_constants_and_opening_tail_serialization", "verdict": "keep", "covered_by": null, "reason": "Only test pinning the 17-byte opening journal root tail serialization and the recovered 10/30 constants; a repo-wide search for JournalRootTail and RECOVERED_FIELD_0X1100 finds no test elsewhere in tests/ that drives this path."},
  {"name": "locate_reads_the_reference_tail_and_replace_changes_only_those_bytes", "verdict": "keep", "covered_by": null, "reason": "Only check that locate/from_span read the preserved reference tail (241, 2513, true, 10, 30) and that replace_in_span changes only the tail bytes. No equivalent test exists elsewhere; it also guards the byte-preservation property."},
  {"name": "malformed_spans_and_tails_are_rejected", "verdict": "keep", "covered_by": null, "reason": "Hostile-input and refusal test (truncated/trailing spans, negative and oversized quest counts, invalid bools, unsupported reward entry type, NaN progress, bad tail length and domain). Refusal checks are not removable without an equally strong named replacement, and none exists."},
  {"name": "private_reference_tail_is_written_not_copied", "verdict": "keep", "covered_by": null, "reason": "Not visible in the excerpt; its name indicates a write-versus-copy canary for the reconstructed tail. Nothing in the similar files (coin_store, login, player_radial, piece_097, piece_048) covers journal root serialization, so it is not clearly covered elsewhere. Kept by the conservative rule. Full body was not read."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "All four tests are the only checks of JournalRootTail, which is not exercised anywhere else in the repo's tests. The five similar files share only a generic piece/test naming style and are not about the quest journal root. The fourth test's body was not read (the excerpt cut off), so its verdict rests on its name and the absence of any other coverage. The file includes src/restoration/piece_070.rs by path because the module is not yet registered in lib.rs. That is a lead-owned integration seam, not a redundancy issue."}
