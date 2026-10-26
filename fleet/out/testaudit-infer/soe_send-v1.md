<!-- fleet job=testaudit-infer id=soe_send-v1 status=done turns=5 usd=0.0045 tokens(read,write,in,out)=[63181, 20485, 12, 2708] model=claude-haiku-5-5 -->
# tests/soe_send.rs

{"file": "tests/soe_send.rs",
 "tests": [
  {"name": "selective_ack_holes_keep_window_bounded_and_unsent_packets_safe", "verdict": "keep", "covered_by": null, "reason": "Only test of selective-ack hole handling and window bounding on the sender; includes refusal assertions for stale/future acks."},
  {"name": "loss_reordering_and_duplicates_reassemble_multiple_messages_once", "verdict": "keep", "covered_by": null, "reason": "End-to-end sender+receiver loss/reorder/duplicate run; receiver-side pieces in tests/soe_transport.rs and tests/transport_fuzz.rs are per-receiver and do not drive ReliableSender through loss. Not clearly covered elsewhere."},
  {"name": "every_wire_packet_fits_limits_even_when_zlib_expands_binary_data", "verdict": "keep", "covered_by": null, "reason": "Unique matrix over CRC length, compression and datagram limit asserting the wire size bound for the sender; the zlib-bound checks in transport_fuzz.rs are receiver-side parsing."},
  {"name": "retries_are_identical_timed_and_terminal_when_exhausted", "verdict": "keep", "covered_by": null, "reason": "Pins exact retry timing, identical retransmissions and terminal SenderFailed. tests/piece_094.rs::a_stalled_client_fails_at_its_retry_limit_without_disturbing_others checks only RetryLimit at gateway level, so it is weaker and does not cover timing or the terminal state."},
  {"name": "queue_limits_and_failed_enqueue_preserve_sequences_and_release_on_ack", "verdict": "keep", "covered_by": null, "reason": "Refusal checks (QueueFull, MessageTooLarge, EmptyMessage) that prove failed enqueue does not consume a sequence; no equivalent elsewhere (transport_fuzz only checks MessageTooLarge once)."},
  {"name": "wire_sequences_roll_over_without_acknowledging_queued_future_packets", "verdict": "keep", "covered_by": null, "reason": "Sender-side 16-bit wrap over 65,540 messages with future-ack refusal. Receiver-side wrap in transport_fuzz::t2_sequence_wrap_and_half_range_are_unambiguous and soe_transport rollover tests do not exercise sender ack handling; piece_094::sequence_rollover_with_a_small_queue is gateway-level. Keep."},
  {"name": "malformed_ack_clock_and_configuration_errors_do_not_mutate_sender", "verdict": "keep", "covered_by": null, "reason": "Refusal test: invalid configuration, malformed acks and backwards clock must not mutate state. No equivalent sender-side check found."}
 ],
 "whole_file_removable": false,
 "confidence": 0.8,
 "notes": "Every test drives ReliableSender directly with distinct assertions. Overlap exists only at the edges: piece_094 (gateway retry-limit and rollover scenarios), transport_fuzz (MessageTooLarge and receiver-side wrap), and soe_transport (receiver reassembly and rollover). None of these is the same path with the same or stronger assertions, so nothing is marked superseded or duplicate. The file's tests are unusually specific, and the whole file has no obsolete markers. Only the retry test has a partial overlap, with piece_094, and it is kept."}
