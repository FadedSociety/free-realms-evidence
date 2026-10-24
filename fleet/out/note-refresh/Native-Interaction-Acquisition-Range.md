<!-- fleet job=note-refresh id=Native-Interaction-Acquisition-Range status=done turns=13 usd=0.0137 tokens(read,write,in,out)=[302838, 48883, 28, 9045] model=claude-haiku-5-5 -->
# notes/Research/Native Interaction Acquisition Range.md

**Verdict:** minor drift. The code matches the note's central claims. Only the "next steps" status wording is now stale.

I checked the one-field write, the int133 retention, the 12 m reach source, the test, the enemy filter and the integration status against the tip. The client-side addresses (0x1818 store in `FUN_008b3320`, AddNpc reader `FUN_00921a10`, datasource `FUN_00baf6e0`) also match the note's descriptions. I could not check the preserved template bytes or the lab receipts, which are outside the repo.

**Corrections:**

1. `old:` Production integration and native UX acceptance are root-owned next steps.
   `new:` Production integration is done: the float237 write is in `opening_world.rs` (see "Integrated source verification"). Native UX acceptance is recorded in "Bounded native acceptance203139".
   `why:` `repo:prototype/osfr-tools/src/opening_world.rs:74-75` has the comment and `bytes[237..241].copy_from_slice(&actor.interaction_radius.to_le_bytes())`. The note's own line 42 says the same thing, so the "next steps" line contradicts it.

2. `old:` Following reviewed integration, a fresh native session must prove12.0 in the actual actor packet
   `new:` Following reviewed integration, fresh native session 203139 has proved 12.0 in the actual actor packets and the ordinary facing/X paths (see "Bounded native acceptance203139"). The exact 12.000 m boundary, collision, terrain approach, line of sight and UI gates remain separate.
   `why:` The float write exists at `repo:prototype/osfr-tools/src/opening_world.rs:75`. The reach source is `repo:scripts/prepare-opening-content.py:73` (`'interaction_radius': 12.0`). The note's "Bounded native acceptance203139" section records the 12.0 packets and the facing/X results, and its own text says the exact boundary is not proved.

3. `old:` ## One-field candidate and remaining gate
   `new:` ## One-field candidate and acceptance record
   `why:` The float237 write is now in production (`repo:prototype/osfr-tools/src/opening_world.rs:75`). The "remaining gate" heading is stale; the section describes work that has landed.

**Checked and holding (no change):**
- `bytes[237..241]` float write before the name splice: `repo:prototype/osfr-tools/src/opening_world.rs:75-82`. The float sits at 237 + UTF8 name length.
- int133 retained as `ceil() as i32`: `repo:prototype/osfr-tools/src/opening_world.rs:73`, and `repo:prototype/osfr-tools/src/combat.rs:337`.
- Enemy actors are excluded from the initialization packets: `repo:prototype/osfr-tools/src/opening_world.rs:50`.
- The server reach guard (`distance_squared > actor.interaction_radius.powi(2)`): `repo:prototype/osfr-tools/src/gameplay.rs:4498-4509`. The 12.0 value comes from content, not a hard-coded constant.
- One ordinary test in `repo:prototype/osfr-tools/tests/opening_world.rs:30-98`, using the `Artéfact 猫` name and fractional radius 3.25. This matches the "1 passed" claim.
- Client: `FUN_008b3320` stores to `param_1+0x1818` (`client:fn 008b3320`), and `FUN_00baf6e0` is the closest-interaction datasource.

**Unsure:**
- "The current preserved template has0.0 there" (byte 237). The template is a lab/content artifact and is not in the repo, so I could not check its bytes.
- The lab receipts (SHA-256 values, run counts such as "1 passed", "18 actor packets", "7065 datagrams") and the Autopilot-style counts are outside the repo and were not re-derived.
- The "adds only ..." sentence in the one-field section describes the patch in the present tense. It is accurate as a description of the change, but the change is now applied, so the tense may mislead.</result>
</invoke>
