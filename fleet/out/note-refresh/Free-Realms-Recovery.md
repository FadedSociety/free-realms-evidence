<!-- fleet job=note-refresh id=Free-Realms-Recovery status=done turns=13 usd=0.0210 tokens(read,write,in,out)=[403020, 64389, 28, 17910] model=claude-haiku-5-5 -->
# notes/Research/Free Realms Recovery.md

**Verdict:** Drifted. The headline and several current-status sentences are stale, though most path and evidence claims check out. The later "Verified" sections already supersede the old pending-gateway wording, but the top line and the table still say the opposite.

**Corrections:**

1. `old:` **The game is not yet running on the Rust implementation.**
   `new:` **The original client now runs against the Rust implementation for a local one-character, one-zone slice; broad game content is not yet restored.**
   `why:` repo:notes/Research/Rust Gateway Milestone.md:3 (actual client logs in, enters the reference zone, walks, restores after restart); repo:notes/Research/Gameplay Milestone.md:3 (local quest, reward, equipment and checkpoint loop in the actual client).

2. `old:` Initialization still uses 46 private captured emulator messages.
   `new:` World entry is built from the startup snapshot (`lab/content/startup-snapshot/startup.json`, loaded at prototype/osfr-tools/src/gateway.rs:2037). The 46 captured templates are still loaded and hash-checked at startup but are no longer replayed.
   `why:` repo:notes/Design/Build Ledger.md:39 (the ledger row says the templates "are no longer replayed"); repo:prototype/osfr-tools/src/gateway.rs:2037; repo:prototype/osfr-tools/src/startup_messages.rs:1-4 (builders "without consulting captured packet bytes").

3. `old:` A persistent socket server, reliable sender/retransmission, multi-message application decoding, other channels, encryption, and gateway logic remain unimplemented.
   `new:` The persistent socket server, reliable sender/retransmission and gateway logic are now implemented in the Rust gateway (see [[Rust Gateway Milestone]]); other channels and encryption were not re-checked here.
   `why:` repo:notes/Research/Rust Gateway Milestone.md:28 (Rust owns loopback UDP sessions, reliable sending, retransmission, selective/cumulative ACK); repo:prototype/osfr-tools/src/soe_send.rs (exists); repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:3342 (`UdpSocket::bind` in the gateway binary).

4. `old:` 43 ordinary tests pass
   `new:` the ordinary Rust suite passes 1,713 tests (0 failed, 82 ignored, October 9 gate; the 43 figure is the October 8 count)
   `why:` repo:notes/Current Progress.md:34 ("Whole Rust 1713 passed/0failed/82ignored"); repo:notes/Autopilot/D006.md:81 (`cargo test -- --list`: 3,192 entries). The count moved; the milestone's 43 is a dated figure.

5. `old:` category browsing is verified, search remains unresolved.
   `new:` category browsing is verified; search is partly resolved: a later native check shows the "hammer" query no longer crashes, but the cause is not proven for every query.
   `why:` repo:notes/Design/Build Ledger.md:91 ("hammer no longer crashes, cause not proven for every query"); repo:notes/Research/Inventory Search Crash.md:3-7 (static diagnosis of the unguarded definition lookup).

**Unsure:**
- Row "Rust implementation": "local one-character/one-zone gateway" matches the milestone's scope (GUID 1 and zone 0 only, repo:notes/Research/Rust Gateway Milestone.md:30). Current Progress (repo:notes/Current Progress.md:9-19) describes a broader world, so the tip's zone scope is not settled here.
- Line 68, "Nine initial checks plus ten new transport checks pass": not counted against the test files.
- Line 16's other claims ("three private-input oracles", "seven live session checks") are consistent with repo:notes/Research/Rust Gateway Milestone.md:62-64, but I did not re-run them.
- Cited lab/ paths and `LibSOE/` paths are outside the repo and were not checked.
- Build Ledger row 39 cites `gateway.rs:1366-1403`, which now holds reset/session code, not the startup builder. This is outside the note but may mislead anyone following that link.
- Current Progress reports 2,065 passing tests at line 31 and 1,713 at line 34. I used 1,713 because it is the later checkpoint, but the two figures disagree.
