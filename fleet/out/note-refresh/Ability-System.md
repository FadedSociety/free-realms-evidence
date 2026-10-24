<!-- fleet job=note-refresh id=Ability-System status=done turns=13 usd=0.0152 tokens(read,write,in,out)=[308165, 46328, 28, 12567] model=claude-haiku-5-5 -->
# notes/Research/Ability System.md

**Verdict:** minor drift. The core candidate description holds: `use_ability` validation order, charge-at-acceptance, success packet order, 36/1 failures, 38/16 tag row, 36/5 opaque tails, knockout bit 7 and the 41/125 window all match the tip. The status line and the integration section are stale because the module is now partly wired into the player route.

**Corrections:**

1. old: `Status: isolated Rust candidate for lead review; not registered or native-accepted.`
   new: `Status: Rust candidate for lead review; registered in \`lib.rs\` and its 36/12 and 36/10 helpers are routed from \`gameplay.rs\`. \`use_ability\` and \`tick_effects\` have no production caller; not native-accepted.`
   why: repo:prototype/osfr-tools/src/lib.rs:3 (`pub mod abilities;`); repo:prototype/osfr-tools/src/gameplay.rs:4622-4633 (calls `parse_definition_request`, `definition_reply`, `unsupported_cast`); `use_ability_on_enemy` (src/enemies.rs:554) has no caller in src, and `tick_effects` is referenced only from its own module.

2. old: `1. Lead registers the module and owns gateway dispatch.`
   new: `1. The module is already registered (\`lib.rs:3\`) and the 36/12 definition replies and 36/10 refusals are dispatched from \`gameplay.rs\`. Lead still owns wiring \`use_ability\` into dispatch.`
   why: repo:prototype/osfr-tools/src/lib.rs:3; repo:prototype/osfr-tools/src/gameplay.rs:4622-4633.

3. old: `Reconcile shared cooldown and health ownership before connecting these messages to \`gateway.rs\`.`
   new: `Reconcile shared cooldown and health ownership before connecting \`use_ability\` and its success packets to the player route; served mode-0 casts on bar 1 already go to \`encounter.rs\` \`job_ability\` (\`gameplay.rs\`).`
   why: repo:prototype/osfr-tools/src/gameplay.rs:4653-4676 (served casts call `self.encounter.job_ability`, not `abilities::use_ability`).

4. old: `286 says “You can't use abilities right now.”`
   new: `286 says “You can't use abilities right now!”`
   why: locale table, string 286 reads "You can't use abilities right now!" (the code comment at repo:prototype/osfr-tools/src/abilities.rs:442 has the period; the shipped text has "!"). Minor.

**Unsure:**

- Verification line: "final run passed 8 tests". `tests/abilities.rs` now has 9 `#[test]` functions (lines 13, 159, 225, 285, 326, 358, 484, 521, 564), plus one `#[cfg(test)]` unit test in `src/abilities.rs:981`. This is a record of a past run, so I did not change it, but the count no longer matches the file.
- Locale id 4168670255 (First Aid rank 1) is not returned by the `locale` tool, but it does appear in the client's `en_us_data.dat` (`FreeRealmsLocaleTools` test data and opening-* locale dumps: "Heals yourself and any ally near you for 250 health"), and `Medic.md:148` cites it. I could not verify it through the tool.
- Locale ids 287 and 288 are not returned by the `locale` tool, so the "ability not ready" and "choose a target" texts are unchecked.
- The client decode claims (`00a2fc70` field shape, `00a2e540` 1,000 ms lockout, `00a309c0`/`00a30d20` names) were not re-checked against the client.
