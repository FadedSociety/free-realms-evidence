<!-- fleet job=guide-refresh id=Gameplay-Rewards-and-Collections status=done turns=30 usd=0.0368 tokens(read,write,in,out)=[1643185, 92891, 64, 17592] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Rewards and Collections.md

**Verdict:** minor drift. Almost all of this note is client reverse-engineering with almost no statements about our code's status. Only one checked sentence describes the tip's behaviour and no longer matches it. The other repo-facing claims I checked hold.

**Corrections:**

- `old:` Own the list. At login send 150/4 with every achievement and its objectives; send 150/2, 150/5 to 150/8 and 150/3 as progress changes.
  `new:` Own the list. Today the tip builds only 150/7 (objective progress) and 150/3 (complete) in `progression_extras.rs`; no 150/4 initialize and no 150/2 or 150/5 to 150/8 builder exists yet. Still to do: at login send 150/4 with every achievement and its objectives; send 150/2, 150/5 to 150/8 and 150/3 as progress changes.
  `why:` repo:prototype/osfr-tools/src/progression_extras.rs:761 (`packet_u16_u32(150, 7)`) and :772 (`packet_u16_u32(150, 3)`); no other 150 subtype is constructed in src. Achievement sync is event-driven (repo:notes/Autopilot/F121.md:29-32).

**Checked and holding (no change):**
- Claim routing: 108/1, 108/3 and 108/5 route to "claims" and 152/4 and 152/5 to "titles" (repo:prototype/osfr-tools/src/gateway.rs:547-548). The claim list, request and grant path is in `ClaimWindow` (repo:prototype/osfr-tools/src/progression_extras.rs:1197-1240).
- Title packets: 152/1, 152/2 and 152/3 are built (repo:prototype/osfr-tools/src/progression_extras.rs:818, 832, 865); 152/4 and 152/5 have builders (:880, :886).
- Forbidden bundle entry types 2, 4, 5, 9, 16 and 21 match the note's "never send 2, 4, 5, 9, 0x10, 0x15" (repo:prototype/osfr-tools/src/progression_extras.rs:33, :57).
- The 34-byte base entry minimum matches (repo:prototype/osfr-tools/src/rewards.rs:16). The 69-byte empty bundle matches the constant in `minigame.rs` (repo:prototype/osfr-tools/src/minigame.rs:17).
- The 38/14 and 38/18 grant messages are sent (repo:prototype/osfr-tools/src/rewards.rs:181, :191). 38/19 is sent by inventory coin grants (repo:prototype/osfr-tools/src/inventory.rs:859-867).

**Unsure:**
- Collections (note line 258, "At login send 38/8 ... on a new find send 38/10"): the encoders exist (repo:prototype/osfr-tools/src/progression_extras.rs:427-462) and `CollectionProgression::collect` exists (:515), but I found no gameplay call site. Only the test file uses it (repo:prototype/osfr-tools/tests/progression_extras.rs:215). The note does not say collections are wired, so I did not correct it, but it is not routed.
- Titles (note line 260): the note wants 152/4 to broadcast through 35/0x28. The tip's select handler returns only the 152/3 update to the requester (repo:prototype/osfr-tools/src/progression_extras.rs:837-849). No broadcast was found. This is a plan item, not a status claim.
- Daily wheel (note line 261): I found no daily-wheel code in `src` (search for daily wheel, DailyRewards, 26/11 returned nothing). The note frames it as a requirement, so I did not correct it.
- Stub 114 (note line 262): `promotional_packet` exists (repo:prototype/osfr-tools/src/progression_extras.rs:1679) and nothing outside its module calls it. The note's "stub" wording is roughly right.
- Claim-related file references in the note: I did not verify the tunnel gateway ids (6 and 5) or the `0089ae70` / `0089adc0` addresses, since those are client-side.
- Not checked in this pass: the bulk of the client tables and the 478-function map.
