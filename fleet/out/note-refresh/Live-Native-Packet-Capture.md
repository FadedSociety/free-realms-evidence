<!-- fleet job=note-refresh id=Live-Native-Packet-Capture status=done turns=8 usd=0.0099 tokens(read,write,in,out)=[141476, 36656, 18, 7885] model=claude-haiku-5-5 -->
# notes/Research/Live Native Packet Capture.md

**Verdict:** minor drift. The code claims check out at the tip. The one stale line is the status sentence at the end, which still says acceptance is pending even though real native runs have since been captured with `--live-capture` and checked against their final manifests.

**Checked and holding:**
- `--live-capture` exists as a `store_true` option (`scripts/run-local-baseline.py:45`), and `LiveCapture(run)` is built only when it is set (`:275`).
- The forwarding loop sends before it captures (`:381` send, `:395-400` capture into memory), and the only live action is `live_capture.submit(frames[-1], data)` (`:403-404`).
- `submit` is a `put_nowait` into a `queue.Queue(maxsize=4096)` (`scripts/live_capture.py:11, 19, 26-32`). Overflow sets `error`, and later submits return early.
- The worker writes `frames/NNNNNN.bin` (`:55`, the same path format as `run-local-baseline.py:391`) before it appends the index line (`:56`). A write error therefore leaves the frame unpublished.
- `live-status.json` carries `"authoritative": False` (`live_capture.py:35`).
- `live_capture.close()` runs at `run-local-baseline.py:438-439`, before the final `write_bytes` loop at `:442-443`.
- The reader keeps only newline-terminated lines (`live_capture.py:76-79`).
- Nonpositive queue limits and an existing capture are rejected (`live_capture.py:12-13, 17-18`).

**Corrections:**

- `old:` Native live-capture acceptance remains pending the next real run; this offline proof does not establish scheduling/latency under a live game load.
  `new:` Real native runs have since used `--live-capture` and matched their final manifests. Examples are `client-baseline-20261008T235041Z`, where the live prefix equals the final manifest 6699/6699 with `closed`, `authoritative:false` and no error (`notes/Reviews/Native Return and Click Movement 235041.md:9`), and native run 203139, where the live-index/final-manifest hashes pass and the writer is closed (`MODLOG.md:382`). This offline proof still does not establish scheduling or latency under a live game load.
  `why:` `MODLOG.md:382`; `notes/Reviews/Native Return and Click Movement 235041.md:9`; `scripts/run-local-baseline.py:45, 403-404, 438-439`.

**Unsure:**
- The lab-side claims could not be checked, because `lab/` is not in the repo. These are the `lab/reports/check-native-live-capture.py` and `native-live-capture-proof.json` evidence and their SHA256 values, the runner and helper SHA256 values, the "four Python files compile" claim, the `--live` mode of `analyze-native-created-character.py` writing `analysis-live`, and the "authoritative: false" flag on every live decoder proof.
- The "pending tail at shutdown is explicitly incomplete" line is only partly true. On a clean stop with no error, `finally` writes `state: "closed"` (`scripts/live_capture.py:65`), not "incomplete". The payload's `incomplete` field is still true whenever the queue was non-empty (`:37`), so the tail is flagged, but not in the state name. This may not be worth a change.
- "Deterministic blocked-write backpressure returns from submit under 0.1s" is plausible, since `submit` is non-blocking, but no test in the repo shows the timing.
