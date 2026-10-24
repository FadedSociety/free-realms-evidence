<!-- fleet job=note-refresh id=Pieces-033-Warrior-progression status=done turns=18 usd=0.0202 tokens(read,write,in,out)=[664036, 61272, 38, 11811] model=claude-haiku-5-5 -->
# notes/Research/Pieces/033 Warrior progression.md

**Verdict:** minor drift. The code-side claims hold at the tip. One gap statement is stale because the server now carries a reconstructed Warrior ability table.

**Corrections:**

- `old:` a server-side or client-side Warrior ability table was not recovered.
  `new:` the repo already carries a reconstructed Warrior ability table: `data/content/job_abilities.json` profile 32, slots 1-4 (Kick `min_level` 1, Spinning Blade 5, Quake 10, Commanding Shout 15), tagged `(R)`. No original server or client Warrior ability table has been recovered.
  `why:` repo:prototype/osfr-tools/data/content/job_abilities.json:216-356 (profile_id 32; definition ids 62004-62007; `min_level` 1/5/10/15; the source tag reads "client + guide + reconstructed (R)"). The gap is still real because the table is not original data, but "was not recovered" now misleads a reader into thinking no server-side table exists.

**Checked and holding (no change needed):**

- `src/restoration/piece_033.rs` exists. `check_warrior_equip(job_level, class_id, slot, item_min_profile_rank)` (line 447) and `skill_unlocked(job_level, name_id)` (line 432) match the note's description: Warrior-owned class, slot in spool, and both gates at or below the job level.
- `tests/piece_033.rs` has 9 `#[test]` functions, matching "9 passed". It includes the module with `#[path]` (line 9), as the note says. `src/` has no registration of piece_033, so the note's "until the lead registers it" is still accurate.
- `tests/pieces/test_piece_033.py` has 4 test methods in `CheckerTests` (lines 423-456), matching "4 passed" and the four named cases.
- `scripts/pieces/piece_033.py` and `scripts/cargo.ps1` exist.
- The class table (15/17/45/55), the creation kit, the level-test chest family and the gate ladders match `piece_033.rs` lines 62-280.
- The slot names in `Resources/EquipmentSlotDefinitions.txt` match: Head through Accessory1 are slots 1-8, SquareRune is 12, DiamondRune is 13.
- Locale ids 24540 "Kick", 4908 "Spinning Blade", 24706 "Commanding Shout", 4664 "Warrior", 442458 "Spinning Attack" resolve as stated.
- The locale "Achieve Level 5/10/15 as a Warrior" and "Warrior: Achieve Level 5/10/15/20" strings exist.

**Unsure:**

- `MembersOnly false` (profile 32, from the pinned Legacy `Profiles.json`). The pinned Legacy file lives outside the repo, so I could not check it. Our own `data/content/jobs.json:1395-1401` lists the Warrior job with `"members_only": true`. One of the two is wrong, or they describe different things. Someone should settle this before a build relies on either.
- The profile-packet facts (`references/rust-opening/profiles.json`, offsets 319/339, the 9-triple equipment count) and the report `../lab/reports/piece-033-20261009T035724Z/` (15 checks, status pass) sit outside the repo and were not verified.
- The rank damage ladders (133/150/... and 50/56/... and 83/94/...) appear only as numbers in the note and the Rust file. I did not verify them against `reports/locale-id-to-text.json`.
- Build Ledger line 72 says Warrior has no basic attack in runtime content. That is not a claim in this note, but it sits uneasily with the server-side Warrior ability table above.
