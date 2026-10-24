<!-- fleet job=bug-hunt id=src-restoration-piece-065-rs-L801 status=nothing_found turns=6 usd=0.0053 tokens(read,write,in,out)=[49383, 19748, 14, 4645] model=claude-haiku-5-5 -->
# prototype/osfr-tools/src/restoration/piece_065.rs lines 801-1135 of 1135

No reportable defect in `prototype/osfr-tools/src/restoration/piece_065.rs` lines 801-1135.

What I read: the tail of `rewards` (801-809), `exit` (811-857), `reconnect` (859-922), `evaluate` (924-949), and `synthetic_reference_replay` (951-1135). I also read the helpers they depend on (`passed`/`failed`/`not_evidenced`, `first_after`, `terminal_result`/`terminal_frame`, lines 340-520) and the head of `rewards` (744-800).

Why nothing is reported:

- **No client-reachable input.** `ReplayTranscript` and `evaluate` are not used by any server code under `src/`. The only consumers are `tests/piece_065.rs`, which pulls the file in with `#[path]`, and the offline Python decoder `scripts/pieces/piece_065.py`, which builds transcripts from preserved captures. A remote player cannot feed a `ReplayTranscript` into this code, so the panic, unbounded-growth and trust-the-client categories do not apply here.
- **No panic path in the window.** `evaluate` clones and stable-sorts the rows, which is safe. The `expect` in `ReplayReport::gate` is only reached for gates that `evaluate` always emits. The `unreachable!` arms in `rewards` are guarded by the pattern match directly above them.
- **Gate logic matches its doc comments.**
  - `exit` finds the close request strictly after the terminal result, then a world-zone transition strictly after the close, then checks the last session's end state.
  - `reconnect` grades the sessions after the first rewarded one. It checks identity fingerprint, unchanged reward set, world start zone and no active encounter, and returns `not_evidenced` when no later session exists.
  - The `rewards` tail checks the reward set on the last session.
- **Fixture is internally consistent.** The synthetic replay's frames are strictly increasing. Its result (200), exit selection (230) and zone return (240) line up with what `exit` expects, and its two sessions share a fingerprint and reward set, as `reconnect` requires.

Non-defect observations, not reported: `evaluate` takes a whole-replay clone, which is harmless for offline grading. The `reconnect` check is weaker than its name implies in one respect, since it does not require the later session to contain no reward rows. That affects only grading strictness, not safety or correctness of a server path.
