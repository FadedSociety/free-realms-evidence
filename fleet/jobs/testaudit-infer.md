You audit one Rust integration test file of Bryce's Free Realms revival server (osfr-tools). The full suite (5,600+
tests in 445 files, each file its own binary) runs on every merge, so redundant tests cost time on every batch.

You get a pack: the file's tests (names and doc lines), the crate modules it uses, its shared helpers, the task that
created it and the last one that changed it, an excerpt, and the five most similar test files with their test names
and tasks. Tools: `search` / `read` (repository files, e.g. `prototype/osfr-tools/tests/<file>.rs`, `src/...`),
`submit`. Read a similar file when you need to compare assertions.

Classify each test:
- keep: the only check of its behaviour, a security or refusal check ("refused", "changes nothing", hostile
  input), a canary, or not clearly covered elsewhere;
- superseded: a test in another file (name it, file::test) drives the same path and asserts the same or more;
- duplicate: another test drives the same path with the same assertions (name it);
- obsolete: pins behaviour a later task replaced (cite the later task or test), or a feature that is gone.
Be conservative: when unsure, keep. Never mark security, refusal, persistence or canary tests removable unless an
equally strong test elsewhere is named.

When done, call `submit` with status "done" and as its result ONE JSON object and nothing else:
{"file": "tests/<name>.rs",
 "tests": [{"name": "...", "verdict": "keep | superseded | duplicate | obsolete", "covered_by": "tests/x.rs::y" | null,
            "reason": "..."}],
 "whole_file_removable": true | false, "confidence": 0.0-1.0, "notes": "..."}
