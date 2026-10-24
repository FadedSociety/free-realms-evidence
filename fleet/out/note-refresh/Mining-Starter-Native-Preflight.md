<!-- fleet job=note-refresh id=Mining-Starter-Native-Preflight status=nothing_found turns=16 usd=0.0185 tokens(read,write,in,out)=[533957, 63698, 34, 10453] model=claude-haiku-5-5 -->
# notes/Research/Mining Starter Native Preflight.md

**Verdict:** current. The repo-checkable claims in `notes/Research/Mining Starter Native Preflight.md` hold at the tip. Most of the note describes a private package under `C:\Users\Bryce\...\lab`, which is outside the repo and cannot be checked directly. Its numbers match the repo notes and the code.

**Corrections:** none.

**Checked and holding:**
- **Frozen release and gate (line 7):** `notes/Current Progress.md:63` gives release `21233dc79cc0…` and "1536 ordinary tests passed, 0 failed, 66 ignored; 12 explicit private checks passed". `MODLOG.md:532` agrees.
- **Model result (lines 7, 16):** 85 chains / 340 s, 17/17 checks, pre-close `collected [6,6]`, 9 reshuffles, score 59200, remaining 546000 ms, wall 340000 ms. `notes/Reviews/Mining Starting Round Candidate Review.md` and `MODLOG.md:550` agree. `notes/Research/Mining Starting Round Playable Candidate.md:24` gives `percent40_quotas6_6 … 85 … 340 s`.
- **Won / GameOver / Close lifecycle (lines 7, 16):**
  - `OnNextLevelMsg` in `LevelComplete` sets `Won` and increments `completed` (`prototype/osfr-tools/src/mining.rs:870-880`).
  - `FRServer_GameOver` is guarded by `!presented` and sets `end_sent` (`mining.rs:882-893`); `results_presented` is persisted at `mining.rs:922`, so a duplicate is a no-op.
  - `FRServer_GameClose` sets `next.active = None` (`mining.rs:894-900`).
- **Quota and timing rules:** `tests/mining_lifecycle.rs:422` asserts `collected == [6, 6]`, and `:428` caps the round at the 10-minute model limit.
- **Ordinary Quit (line 9's "Select… normally" is not claimed, but related):** `mining.rs:601-608` cancels only pre-win runs, as the note implies.
- **Cross-links:** `notes/Research/Mining Starting Round Playable Candidate.md`, `notes/Reviews/Mining Starting Round Candidate Review.md` and `notes/Current Progress.md` all exist.
- **Snapshot and run names (line 9):** `client-baseline-20261009T111125Z` is the accepted restart run (`notes/Reviews/Native Opening 17 103605.md:42`). `151307` is recorded as failing by wall cap (`notes/Current Progress.md:68`), which the engine's `tick` handles as `Lost` (`mining.rs:552-554`).

**Unsure:**
- "Outputs remain empty; no minigame payout is introduced" (line 7) is true for the private candidate: `notes/Research/Mining Starting Round Playable Candidate.md:5` says `outputs []`. The repo's shipped Mining18 default (`prototype/osfr-tools/src/mining.rs:1020-1033`) does define outputs (definition 2739) and calls `reward_transaction` on win (`mining.rs:877-879`). The note is scoped to the candidate package, so I left it unchanged. A reader should not take it as a statement about the tip default.
- Package file counts (46/47 base files, 2 metadata files), the receipt and `independent-acceptance.json` paths, and the frozen release's SHA-256 prefix cannot be checked from the repo; I found no contradicting evidence.
