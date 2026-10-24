<!-- fleet job=note-refresh id=Verified-Recovery-Workflow status=done turns=12 usd=0.0161 tokens(read,write,in,out)=[323490, 55100, 26, 11982] model=claude-haiku-5-5 -->
# notes/Research/Verified Recovery Workflow.md

**Verdict:** Stale in its status claims. Two status statements are false at the tip (opening-stage count, captured-init dependency), and the test-count row presents a dated figure as current. The script names, flags, output paths and the bounded-script claims hold. Most of the note is `lab/` material outside the repo, so I could not check it.

**Corrections:**

1. `old:` Twelve of 17 local opening stages are rewarded; the campaign stops at the Queen checkpoint (stage 13 unaccepted).
   `new:` All 17 reconstructed local opening stages are rewarded (the Queen checkpoint was 12 of 17, see [[Reviews/Native Queen and Prompt 203139]]); stage 13 (Cooking at Mae) and stages 14–17 were completed in later native runs.
   `why:` repo:notes/Current Progress.md:62 ("all 17 reconstructed local opening stages"), repo:notes/Current Progress.md:92 (remaining stages, including 16–17, completed in `client-baseline-20261009T103605Z`), repo:notes/Reviews/Native Developer Standoff 013155.md:16 (stage 13 accepted). The Queen review at repo:notes/Reviews/Native Queen and Prompt 203139.md:7 is the historical 12-of-17 point.

2. `old:` Rust gateway initialization still depends on **46 private captured emulator messages**; replacing them with typed serialization is an open task.
   `new:` Rust world entry builds the 46 startup messages server-side from the startup snapshot (`gateway.rs:1895-1923`). The 46 captured templates are still loaded and hash-checked at startup (`gateway.rs:312-323`), and self-data (message 7) is still seeded from captured template #7 (`gateway.rs:853-855`). Removing that template dependence is the remaining open part.
   `why:` repo:prototype/osfr-tools/src/gateway.rs:1895-1923 (Kind::Ready 8..46 built via `snapshot.build_packet` / `build_zone` / `build_self_message`), repo:notes/Design/Build Ledger.md:39-40 ("no longer replayed", "still seeded from captured template #7"), repo:notes/Tasks.md:39 (marked done). The Build Ledger says the 10-13 "replayed 46 captured messages" statement was fixed on 10-14.

3. `old:` `cargo test` (154 pass, 29 ignored)
   `new:` `cargo test` (154 pass, 29 ignored at the 2026-10-08 milestone; not current, re-list before quoting)
   `why:` The note's own line 81 says the count is timestamped. repo:notes/Current Progress.md:31 reports "Test suite: 2065 passed, 0 failed", and repo:notes/Current Progress.md:34 reports "Whole Rust 1713 passed/0 failed/82 ignored". The two figures conflict, so the table should not state 154 as current.

4. `old:` then use `mkdir(exist_ok=False)` / `open("x")` so a re-run fails immediately
   `new:` then the pack script uses `mkdir(exist_ok=False)` / `open("x")` and the asset script uses a bare `mkdir()` (fails on an existing directory) with `write_text` for its report, so a re-run fails immediately
   `why:` repo:scripts/check-community-pack.py:60,65,91 (`exist_ok=False`, `open("x")`); repo:scripts/check-community-assets.py:24 (`output.mkdir()  # Refuse to overwrite`), :81 (`write_text`). Minor: the outcome (refusal) is the same.

**Checked and holding:** `scripts/check-community-pack.py` hardcodes `lab/extracted/community-pack-check` and `lab/manifests/community-pack-check.json` and takes `--pack` (default `Assets_008.pack`) (check-community-pack.py:23,44,90). `scripts/check-community-assets.py` hardcodes `lab/extracted/community-asset-check` (line 23). `scripts/check-gateway-session.py` takes `--run` (line 81). `scripts/cargo.ps1` forwards `-CargoArgs` (line 1). All linked notes that I checked exist.

**Unsure:**
- The independent-review verdict. The note says lead acceptance of the guide "remains open". repo:notes/Reviews/Delegated Lead Acceptance October 8.md:5 says "The recovery guide is accepted after author corrections and independent re-derivation." I did not settle which is current, so I left the note's wording alone.
- The inventory-search access violation is still listed as open. That matches repo:notes/Tasks.md:35 ("Mitigated"; cause unproven). repo:notes/Research/Inventory Search Crash.md:7 claims a high-confidence cause, so the status is contested. I did not change the note.
- The ILSpy, Ghidra and pack counts, the `lab/` hashes and the `lab/manifests` paths live outside the repo. I could not check them.
- I did not count `#[test]` / `#[ignore]` across the crate, because the search tool caps results at 60 lines.
