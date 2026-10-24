<!-- fleet job=guide-refresh id=Gameplay-Kart-Racing status=done turns=25 usd=0.0315 tokens(read,write,in,out)=[1359416, 91162, 54, 12962] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Kart Racing.md

**Verdict:** minor drift. Most server-side claims I checked hold at the tip. One checkable claim about gate entry is false.

**Corrections:**

- `old:` Gate entry on the Kart Driver job and send the job-switch message the client shows (R for the exact gating).
  `new:` Admit entry from any kart gate NPC when a race is configured, the player is not already racing, is not busy, and the reward cooldown has passed. Entry then unlocks (first use only) and activates Kart Driver (job 48) and sends the job-switch message the client shows (R for the exact gating).
  `why:` repo:prototype/osfr-tools/src/kart_gateway.rs:422-438 (admission checks gate, race content, AlreadyRacing, Busy and Cooldown; no job check). repo:prototype/osfr-tools/src/gameplay/npc.rs:862-894 (`begin_kart_race` unlocks and activates job 48, then sends the profile activation reply). The payout path separately requires the Kart Driver job (repo:prototype/osfr-tools/src/kart_rewards.rs:266).

**Checked and holding (no change needed):**

- Item queue cap of 3: repo:prototype/osfr-tools/src/kart_service.rs:150.
- Respawn about 8 s with a cap of 16 per pickup: repo:prototype/osfr-tools/data/content/kart_entry.json:8564-8567.
- Activation status flag 0x401: repo:prototype/osfr-tools/src/kart_gateway.rs:592-594.
- One 33/14 progress frame per accepted gate, and the race finishes at the final accepted gate: repo:prototype/osfr-tools/src/kart_service.rs:2616-2626.
- Shield expiry sent as 33/21 with value 4: repo:prototype/osfr-tools/src/kart_pickups.rs:57-61.
- Pickup claim replies in the order 33/18 grant then 33/16 destroy: repo:prototype/osfr-tools/src/kart_pickups.rs:740.
- Lap limit is copied from content: repo:prototype/osfr-tools/src/kart_service.rs:2699.

**Unsure:**

- "Five speedways, each with a kart gate". The repo has five gate NPCs (repo:prototype/osfr-tools/data/content/kart_gates.json:3-9) but only one race configuration, speedway 31 with 3 laps and reward 50 coins / 25 XP (repo:prototype/osfr-tools/data/content/kart_entry.json:7119-7123). The note's "Where" bullet describes the world, so I did not change it. Worth a look.
- "26/42 in our native runs" as the Close message. I did not find a kart-specific Close handler in the kart modules; I did not check the generic 26/42 path.
- "Gate volumes are reconstructed from the track's GCNK actors". I saw GCNK in repo:prototype/osfr-tools/src/terrain.rs:4 but did not trace it into the kart gate data.
- Client-side function addresses and pseudocode labels: not checked (outside the scope of the repo).
- Only part of the 687-line note was read. Lines 230-560 and 600-687 are mostly client function tables and were not checked line by line.
