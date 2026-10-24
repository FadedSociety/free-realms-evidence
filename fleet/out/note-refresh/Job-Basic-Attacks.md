<!-- fleet job=note-refresh id=Job-Basic-Attacks status=done turns=16 usd=0.0186 tokens(read,write,in,out)=[506213, 50975, 34, 14282] model=claude-haiku-5-5 -->
# notes/Research/Job Basic Attacks.md

**Verdict:** badly stale. The weapon-enforcement section is now false, the JSON description is out of date, and most `path:line` citations have moved since the W85 work.

**Corrections:**

1. `old:` attacks do not check the equipped weapon; this was reproduced by the unarmed bots. Starter delivery alone does not add that check. Weapon/line-of-sight enforcement needs lead-owned runtime work if required for playtest policy.
   `new:` that gap is closed at the tip. Basic and job attacks require the weapon class from the equipped slot 7 (`abilities::equipped_weapon_matches`, reached through `OpeningAbilities::weapon_matches`). A refusal is logged by `refuse_weapon`. The unarmed W85 bot runs predate this check. Line-of-sight was not checked here.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:505-515; repo:prototype/osfr-tools/src/opening_abilities.rs:290-304; repo:prototype/osfr-tools/src/encounter.rs:1167-1177; repo:prototype/osfr-tools/data/content/opening-abilities.json:89-90 (provenance: "This supersedes W85 no-enforcement statement.")

2. `old:` Therefore the passing runs prove the server's current unarmed compatibility route; they do **not** prove the weapon, wield state or animation can render in the native client.
   `new:` Therefore the passing runs prove only the pre-W113 unarmed route. At the tip an unarmed basic is refused, so the bots would need a granted and equipped starter weapon. They still do not prove the weapon, wield state or animation can render in the native client.
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:506-515 (`weapon_matches` gate before the ability runs); repo:prototype/osfr-tools/src/opening_abilities.rs:290-304.

3. `old:` **three additive rows only**, in the existing private `OpeningAbilities` schema. Only profiles 2, 32 and 12 are owned here.
   `new:` a six-row W113 canonical roster (profiles 2, 11, 12, 32, 35, 43) in the existing `OpeningAbilities` schema, with `weapon_class` and `weapon_definition_id` on each row. The W85 rows are profiles 2, 32 and 12.
   `why:` repo:prototype/osfr-tools/data/content/opening-abilities.json:5-63 (six `profile_id` rows), :66-92 (W113 provenance).

4. `old:` `gameplay.rs:275` calls `OpeningAbilities::load(directory)`
   `new:` `gameplay.rs:691` calls `OpeningAbilities::load(directory)`
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:691.

5. `old:` `gameplay.rs:478-481` separately loads the repository's `job_abilities.json`
   `new:` `gameplay.rs:911-916` separately loads the repository's `job_abilities.json` (via `load_job_abilities`).
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:911-916; `load_job_abilities` also called from repo:prototype/osfr-tools/src/gameplay/content_reload.rs:42-45.

6. `old:` `opening_abilities.rs:130-165` permits only consecutive extra slots **1..7**
   `new:` `opening_abilities.rs:217-260` permits only consecutive extra slots **1..7** (`a.slot == i + 1` at :246; `valid()` range `1..=7` at :88)
   `why:` repo:prototype/osfr-tools/src/opening_abilities.rs:88, :217-260.

7. `old:` `encounter.rs:2976` already defines Ninja range/base 3 m/100, Warrior 3 m/110, Wizard 20 m/130.
   `new:` `encounter.rs:2893` (`profile_stats`) already defines Ninja range/base 3 m/100, Warrior 3 m/110, Wizard 20 m/130.
   `why:` repo:prototype/osfr-tools/src/encounter.rs:2893-2906 (values match).

8. `old:` `encounter.rs:2009` enforces 600 ms between hits; line 2063 sends swing 1099.
   `new:` `encounter.rs:1877` enforces 600 ms between basic hits; `encounter.rs:1966` sends swing 1099. The job-ability path is `encounter/skills.rs:203` (600 ms) and `encounter/skills.rs:305` (1099 fallback).
   `why:` repo:prototype/osfr-tools/src/encounter.rs:1875-1878, :1964-1967; repo:prototype/osfr-tools/src/encounter/skills.rs:201-206, :299-307.

9. `old:` (`gameplay.rs:4646`, `encounter.rs:1166`)
   `new:` (`gameplay.rs:5152`–`5162` in `sync_player_level`, `encounter.rs:1181`)
   `why:` repo:prototype/osfr-tools/src/gameplay.rs:5152-5162; repo:prototype/osfr-tools/src/encounter.rs:1181.

10. `old:` `weapon_tier` (`encounter.rs:35`)
    `new:` `weapon_tier` (`encounter.rs:52`)
    `why:` repo:prototype/osfr-tools/src/encounter.rs:52-60 (level tiers 1, 4, 5, 8, 12 match the note).

11. `old:` refused inside the opening cave by the existing guard (`gameplay.rs:3349`)
    `new:` refused inside the opening cave by the existing guard (cite not re-found; `goto` parsing is at `gameplay.rs:3165-3169`, and `gameplay.rs:3349` is the soccer lifecycle exit)
    `why:` repo:prototype/osfr-tools/src/gameplay.rs:3165-3169, :3349-3356. I found no goto-specific cave refusal.

**Unsure:**
- The private campaign's `opening-abilities.json` containing only 43/11/35 (gameplay.rs:691 claim). It is outside the repo, so I could not check it.
- The `realm goto` refusal inside the opening cave: I found no such guard.
- Client animation/WieldType lines and the 150 Gloamling health: not checked against the client resources.
- Test counts (8/8, 4/4 and 1 ignored) and the content-check totals: these are historical logs and were not re-run.
- Whether the bot's `realm level` / `realm battle` path still behaves as the note describes: `gameplay.rs:2899` and `:2959` exist, but I did not trace the full path.
- Line-of-sight enforcement: not checked, so the note's mention of it stays open.
