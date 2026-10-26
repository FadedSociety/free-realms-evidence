<!-- fleet job=testaudit-infer id=telemetry_labels-v1 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[25177, 16368, 8, 1919] model=claude-haiku-5-5 -->
# tests/telemetry_labels.rs

{"file": "tests/telemetry_labels.rs",
 "tests": [
  {"name": "quiet_shapes_seen_in_native_traces", "verdict": "keep", "covered_by": null, "reason": "Exact per-shape table asserting handler label, outcome \"handled\", no reason, no replies, and exact forwarded application bytes for both outer 5 and outer 6 tunnels. app_fuzz.rs (around lines 849-898) sends similar quiet-family seeds, but as a fuzz/no-panic style inventory without these per-label trace and forwarding assertions, so it is not an equally strong check. Not clearly covered elsewhere."},
  {"name": "real_unknowns_still_log_unknown", "verdict": "keep", "covered_by": null, "reason": "Refusal check: neighbours of the quiet list (104, 106, 192, 195, 193 server-side subs, longer 16) must still be rejected as unknown with no application forwarded. Guards against over-broad quiet routing. Keep."},
  {"name": "log_text_never_reaches_the_trace", "verdict": "keep", "covered_by": null, "reason": "Privacy canary: asserts body_head_hex is None for a client_log body. Nothing equivalent found in the similar files. Keep."},
  {"name": "native_trace_replay_leaves_no_unknown_quiet_family", "verdict": "keep", "covered_by": null, "reason": "Replays real native trace shapes, but only when private traces exist under lab/runs; otherwise it returns early and passes vacuously. Its assertions (handled, one forwarded application) overlap quiet_shapes_seen_in_native_traces, but it is the only test that checks the real captured shape distribution. Keep, though its value on machines without traces is nil."}
 ],
 "whole_file_removable": false,
 "confidence": 0.6,
 "notes": "No test is clearly redundant. The strongest overlap is app_fuzz.rs lines 849-898, which exercises the same quiet families (105, 109, 194, 193, 16, 26) with weaker assertions; a possible consolidation is to have app_fuzz rely on this file, but that is a refactor, not a removal. The replay test silently passes when lab/runs is absent, so its pass signal is not evidence on CI. Only the native replay depends on private data; the other three run standalone. The file's created_by and last_changed_by are null in the pack, so obsolescence against later tasks could not be checked."}
