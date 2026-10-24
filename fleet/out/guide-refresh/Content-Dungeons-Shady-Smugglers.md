<!-- fleet job=guide-refresh id=Content-Dungeons-Shady-Smugglers status=done turns=22 usd=0.0210 tokens(read,write,in,out)=[702988, 56642, 46, 13781] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Shady Smugglers.md

**Verdict:** current, with minor drift. The note is almost entirely client and wiki evidence, and nearly every `loc` id, quoted string and item name checks out. The repo side is consistent: `prototype/osfr-tools/data/content/dungeons/shady_smugglers.json` exists, uses name id 3618485654, difficulty 4, minimum combat job level 9, and `members_only: false`, and `Dungeons.md:140` lists it as written. One client claim overstates what the locale holds.

**Corrections:**

1. `old:` Members get "Members Only Bonus: 44 Coins" (client label `loc 1925651180`). No "Bonus: 44 Coins!" string was found.
   `new:` Members get a "Members Only Bonus!" block (client label `loc 1925651180`). The client holds no amount; the 44 Coins figure is wiki-only. No "Bonus: 44 Coins!" string was found.
   `why:` refs:opening-journal-text-v2/locale/en_us_data.dat:50759 is `1925651180 ucdt Members Only Bonus!` with no amount. A search of the same file finds no "Bonus: 44 Coins" or "44 Coins" string, so the amount comes from the wiki only.

2. `old:` The same name is used for the Croaking Vale smuggler bosses in quest text (`loc 2452316691`), so details of this fight are not separable.
   `new:` The Croaking Vale quest text (`loc 2452316691`) says "defeat the smuggler bosses" in lowercase, not the exact name "Smuggler Boss", so details of this fight are not separable.
   `why:` refs:opening-journal-text-v2/locale/en_us_data.dat:64578 has the words "defeat the smuggler bosses". The exact "Smuggler Boss" appears only at line 59441 (`2256920343`) and at the ugdt `3272578542` line 86444. The same wording is also at lines 29317, 71635 and 1106899801/2719286545. (Minor; the Conflicts item 4 wording "shared with the Croaking Vale bosses" is looser but defensible.)

**Checked and holding:**
- Client ids and strings: 3618485654, 2463636203 (Shady Smugglers), 4090735730, 2646282689, 1113081375, 1324389113, 3028504823, 2280067896, 2279780909, 3682335856, 3917535716, 60850863, 272777734, 1291047686, 1882811692, 3256084479 and 2091820560 (Shady Smuggler), 2256920343 and 3272578542 (Smuggler Boss), 873625915 (Smuggler). All match the locale files. The note's loc numbers are the hash ids, not the sequential ids the `locale` tool uses.
- No "Shady Smugglers!" form, "Shady Smugglers Bonus Objective", "Win Combat Encounter Shady Smugglers" or "97 Stars" string exists in the client.
- All 27 prize-wheel item names exist in the locale. Example ids 801720612, 2476281039 and 3019306483 match.
- Links: `Ninja.md`, `Archer.md` and `Croaking Vale.md` exist. "Contract: That'll Teach 'Em" is on `Archer.md:129`.

**Unsure:**
- Video frame claims (piWfe7lXZ9I/00162, 00168; 15 m marker distance) and "not placed on the Adventurer page" for `loc 60850863` could not be checked from the repo.
- The repo's `dungeons/shady_smugglers.json` has empty `goals`/`rewards`, and the note's Gaps section already says so. The note does not claim otherwise, so I left it alone.
