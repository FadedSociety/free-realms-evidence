<!-- fleet job=note-refresh id=Rust-Gateway-Milestone status=done turns=16 usd=0.0149 tokens(read,write,in,out)=[329796, 41559, 34, 12864] model=claude-haiku-5-5 -->
# notes/Research/Rust Gateway Milestone.md

**Verdict:** Minor drift in the core claims, badly stale in the scope, status, and next-step text. The transport, character-store, and session-check claims still hold at the tip. The "unimplemented" list and the test count were true on Oct 8 and are now false.

**Corrections:**

1. `old:` GUID 1 and the reference zone ID 0 are the supported scope. Zone ID 0 is distinct from the captured geometry/type value 5; other zones are rejected rather than assigned incompatible geometry.
   `new:` GUID 1 and the reference zone ID 0 are the supported scope of the milestone. Zone ID 0 is distinct from the captured geometry/type value 5. With no gameplay overlay, other zones are rejected. When an encounter or kart entry is active, the saved location must pass that overlay's `supports_location` check, so zones beyond 0 are no longer rejected unconditionally.
   `why:` repo:prototype/osfr-tools/src/gateway.rs:876-884 (rejects only when `gameplay` is none and the zone differs from the initial zone, or when the overlay refuses the location); repo:prototype/osfr-tools/src/gameplay.rs:1628-1638 (`supports_location` delegates to encounter/kart/soccer, else `zone_id == 0`).

2. `old:` Quests, combat, reward/inventory mutations, multiple accounts, multiplayer, further zones, long-running stability, and a replacement Rust client remain unverified or unimplemented.
   `new:` This milestone did not verify quests, combat, reward/inventory mutations, multiple accounts, multiplayer, further zones, long-running stability, or a replacement Rust client. Later work covers some of these: the guide/quest/reward/wallet/equipment loop is verified in [[Research/Gameplay Milestone]] (notes/Research/Gameplay Milestone.md:3-17), and account-store, multiplayer, and zone-transition code now exists (`src/account_store.rs`, `tests/multiplayer.rs`, `src/zone_transition.rs`).
   `why:` repo:notes/Research/Gameplay Milestone.md:3-17; repo:prototype/osfr-tools/src/account_store.rs; repo:prototype/osfr-tools/tests/multiplayer.rs; repo:prototype/osfr-tools/src/zone_transition.rs; repo:prototype/osfr-tools/src/gameplay.rs:1628 (quest/encounter overlay present).

3. `old:` Next: select one NPC/quest with surviving evidence, implement the interaction/objective/reward path in Rust, and verify its reward survives another restart. Track evidence and implementation coverage separately.
   `new:` Next: superseded. [[Research/Gameplay Milestone]] implements and verifies one guide, quest, and reward loop that survives restart. Track evidence and implementation coverage separately.
   `why:` repo:notes/Research/Gameplay Milestone.md:3, 11, 17.

4. `old:` Formatting, release build, and **43 ordinary tests** pass. Three private-input tests are ignored by default rather than silently passing without input.
   `new:` At this milestone, formatting, the release build, and **43 ordinary tests** passed. The current tree is far larger: the latest whole-suite gate is 1,549 ordinary tests with 70 private-input tests ignored, and `prototype/osfr-tools/tests/` alone has dozens of `#[ignore = ...]` private-input tests.
   `why:` repo:notes/Current Progress.md:57; repo:prototype/osfr-tools/tests/gateway.rs:131 and tests/combat.rs:262 (among many other `#[ignore]` sites).

**Verified, no change needed:**
- The character store validates GUID and coordinates, rejects corrupt or unsupported saves rather than resetting them, and replaces saves through a synced same-directory temp file: repo:prototype/osfr-tools/src/character_store.rs:33-45, 61-86, 91-130.
- The 46-template check on the captured initialization messages: repo:prototype/osfr-tools/src/gateway.rs:311, 320.
- The seven live UDP checks (nonloopback bind, duplicate handshake, CRC-zero replacement, distinct seed, old-seed ignored, new-seed accepted, bounded stop): repo:scripts/check-gateway-session.py:138-210.
- The `--drop-server-sequence`, `--rust-reference`, and `--state-file` flags, and the three scripts named in the Reproduce block: repo:scripts/run-local-baseline.py:37-60, repo:scripts/check-gateway-session.py, repo:scripts/prepare-gateway-reference.py.
- The `--reference` and `--state` binary options: repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:338-339.

**Unsure:**
- "geometry/type value 5" as a captured value: I found no code that encodes it. The nearby code (repo:prototype/osfr-tools/src/world.rs:1456-1462) falls back to geometry 0 and type 2 when content metadata is missing. I left the sentence as written.
- The gateway now accepts private-network binds with `--allow-lan` (repo:prototype/osfr-tools/src/bin/osfr-gateway.rs:368-377). The note's "nonloopback bind rejection" check still matches the default behavior, so I did not change it.
- The lab run paths, manifests, SHA-256 values, and timings live outside the repo (`lab/`), so I could not check them.
