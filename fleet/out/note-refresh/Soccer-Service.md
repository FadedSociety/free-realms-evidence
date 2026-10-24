<!-- fleet job=note-refresh id=Soccer-Service status=done turns=20 usd=0.0259 tokens(read,write,in,out)=[751458, 78745, 42, 17061] model=claude-haiku-5-5 -->
# notes/Research/Soccer Service.md

**Verdict:** minor drift. The service-rule claims (roster, bots, start gate, grant settlement, disconnect, timeout, tie and win mapping, 180 s fallback) match the tip. Only the W50 housing-warning line and the `soccer_match` count look stale. The native-map facts cannot be checked from this repo.

**Corrections:**

1. `old:` One unrelated dead-code warning remains at `src/housing.rs:567`.
   `new:` The W50 run reported one unrelated dead-code warning at `src/housing.rs:567`. At the tip, that line is the `#[derive(Debug)]` above `struct Lot` (line 568), and no `instance_index` method exists in `src/`, so the warning does not reproduce from the current tree.
   `why:` `repo:prototype/osfr-tools/src/housing.rs:567-568` (`#[derive(Debug)]`, `struct Lot`). A search for `instance_index` in `prototype/osfr-tools/src` finds only `restoration/piece_046.rs`, which has a local variable of that name.

**Checked and current:**
- Four slots per team (`TEAM_SLOT_COUNT = 4`), `soccer_match.rs:40`. Passive solo bots, `soccer_service.rs:605-649`, and bots never score.
- 180-second fallback halves (`HALF_SECONDS = 180.0`), `soccer.rs:19`.
- `start()` requires every joined session to be `RunState::Playing`, `soccer_service.rs:816-831`. `mark_started` also gates on this, `:726-748`.
- Settlement goes through `MinigameRuns::finish` → `rewards::apply_grant`, with key `minigame-run:{instance_id}`, `minigame.rs:580-582`. The service passes a settlement only on a win, `soccer_service.rs:755-772`.
- Win = one star, tie as loss, `elapsed.round()`, `soccer_service.rs:124-138`.
- Disconnect and timeout, `soccer_service.rs:777-812`: the run is cancelled via `runs.disconnect()`, the held ball is released, and the match cancels when no session remains.
- `ClientPacket::ReadOnly` refuses client GoalMade and registration, `soccer_service.rs:971-976`.
- Sub-13 is the only `ImpulseBall` emitted, `soccer_service.rs:378-392` and `:414-422`.
- Test counts: `soccer_service` 16 (16 `#[test]`), `soccer` 11 passed plus 1 ignored, `soccer_native_wire` 8, `soccer_review` 10 (all match the tip).
- The W50 `GoalMade` → `Evidence::Reconstructed` expectation, `soccer_review.rs:127-145`. The W50 charge-policy and pass-target wording, `soccer_native_wire.rs:104`.
- `notes/Reviews/Soccer Direction Semantics Review.md`, `Build Guides/Gameplay/Soccer.md`, and `scripts/native_map/nmq.py` exist.

**Unsure:**
- **`soccer_match` count.** The note records `soccer_match: 27 passed` (W37, line 84) and `soccer_match` 27 in the W50 total of 72 (line 107). `tests/soccer_match.rs` has 20 `#[test]` functions at the tip (lines 184–776), with no macros or `#[path]` includes that would add more. Either the file shrank after those runs or the counts were taken differently. I could not rerun the suite, so I left the line unchanged.
- **Native-map claims** (lines 17–29 addresses, labels, byte layouts) cite `lab/native-map/run/map.sqlite`, which is not in the repo. I did not check them.
- **Line 84 housing warning** (`Lot::instance_index`) is the same stale warning as correction 1, from the W37 run. I did not change it.
- **Line 86 "seven owned Rust files"** and the `rustfmt` run are not checkable from the tree.
