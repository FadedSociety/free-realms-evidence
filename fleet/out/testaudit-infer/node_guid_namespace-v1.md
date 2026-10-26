<!-- fleet job=testaudit-infer id=node_guid_namespace-v1 status=done turns=5 usd=0.0028 tokens(read,write,in,out)=[40129, 12470, 12, 1661] model=claude-haiku-5-5 -->
# tests/node_guid_namespace.rs

{"file": "tests/node_guid_namespace.rs",
 "tests": [
  {"name": "no_two_live_node_guids_share_a_tag_or_a_value", "verdict": "keep", "covered_by": null,
   "reason": "Its distinctive assertions are the per-source tag checks (each source placed under exactly one tag, tag < 256, no two sources sharing a tag, no live source on tag 4) and the T524 collection companion collision check. Nothing else in the suite asserts these. The only overlapping part is the all-guids-distinct check, which is partly covered by tests/gathering_nodes.rs::node_content_is_bounded_and_unique (it dedups guids across the combined GatheringNodes load and asserts 18 actors). That test does not check tags, per-file loading, or companions, so it does not supersede this one."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Single-test file, created and last changed by F701. It guards a cross-source guid namespace that the T524 companion design depends on. Partial overlap with gathering_nodes.rs::node_content_is_bounded_and_unique on guid uniqueness only. Note that that overlap is the only redundancy, and it is small. Not a candidate for removal."}
