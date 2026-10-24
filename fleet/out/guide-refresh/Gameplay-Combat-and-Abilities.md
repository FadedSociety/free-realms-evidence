<!-- fleet job=guide-refresh id=Gameplay-Combat-and-Abilities status=done turns=26 usd=0.0332 tokens(read,write,in,out)=[1287108, 91778, 56, 17607] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Combat and Abilities.md

**Verdict:** minor drift. Most checkable server claims hold at the tip (melee reach, repeat gate, 36/10 size check, 32/7 field layout, post-damage health write, 35/5 follow-up, boss display, knockout bit 7). One damage range is stale.

**Corrections:**

- `old:` flat per-profile damage of 70 to 110 (doubled for non-basic slots)
  `new:` flat per-profile damage of 70 to 130 (doubled for non-basic slots; the Wizard, profile 12, is 130 and profile 35 is 80)
  `why:` repo:prototype/osfr-tools/src/encounter.rs:2893-2905 (`profile_stats`: 35 => (30.0, 80), 12 => (20.0, 130), default 70, `slot == 0 ? d : d * 2`). The Wizard value was raised from 90 to 130 per notes/Autopilot/T010.md:36 ("Wizard 20 m/130").

**Checked and holding (no change):**
- 3.0 m player melee reach and 2.5 m creature reach: encounter.rs:299-301 and 2893-2903.
- 600 ms repeat gate: encounter.rs:1877.
- Ranged reach 30 (profile 35) and 20 (profile 12): encounter.rs:2895, 2898.
- 36/10 request accepted at 24 or 32 bytes: abilities.rs:832.
- 32/7 layout with post-damage health in the +0x34 slot, followed by 35/5: encounter.rs:3015-3036 and 1952-1960.
- Boss display 32/9 on and off: encounter.rs:1526, 1977, 2564.
- Knockout bit 7 (`KNOCKED_OUT_BIT = 1 << 7`): abilities.rs:21, 683-684.
- Player health 1000 (`PLAYER_MAX`): encounter.rs:37.
- Wolves, Gloam and Mac content exists: restoration/piece_051.rs:13, 400; encounter.rs:1668; tests cite the wolf field.

**Unsure:**
- Line 307 ("Accept all three entry points ... 32/1 and 32/3 ... and 36/10 slot 0") is written as a requirement, so it may not be false. I found no 32/1 or 32/3 match arm anywhere in src. The only accepted basic-attack entries are 26/10 with entry 103 (encounter.rs:1643-1677) and 36/10 bar 1 slot 0 (encounter.rs:1682-1744; combat.rs:205-222). If the note is meant as status, it should say 32/1 and 32/3 are not routed.
- Line 346 says the paid-revive price is "not in the client". The code comment at encounter/revive.rs:28-30 cites `setReviveCost_lua(1000)` in `UI/revive_window.gfx`. My client search for that string returned nothing, so I could not settle it.
- Line 103 says bits 14 and 18 have no message. Line 345 says bits 15 and 18 have no name and no message. These contradict each other. I did not check the client mapping.
- I did not check the 36/7 ability purchase or 36/8 reply in the gateway. No handler was found in src (only the `SUB_PURCHASE_ABILITY = 7` constant at restoration/piece_035.rs:64), but I did not confirm that the gateway never routes it.
- I did not check the many client-address claims, which can't be verified from the repo.
- I ran out of tool budget before sampling the Data section (lines 400 to 1197), so it is unchecked.</result>
</invoke>
