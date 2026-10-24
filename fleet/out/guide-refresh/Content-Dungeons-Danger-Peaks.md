<!-- fleet job=guide-refresh id=Content-Dungeons-Danger-Peaks status=done turns=12 usd=0.0120 tokens(read,write,in,out)=[247336, 38693, 26, 9315] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Dungeons/Danger Peaks.md

**Verdict:** minor drift. The note is almost entirely client-locale and wiki sourced. Its only checkable claim about the client was wrong on one point. Our code has no Danger Peaks logic; the only footprint is `data/content/dungeons/danger_peaks.json`, which copies the note's prose and has empty goals and rewards. Nothing in `notes/Autopilot/` mentions Danger Peaks.

**Corrections:**

1. Overview, Panel description row.
   - `old:` **No client string with that text was found.** The nearest client lines are
   - `new:` The client has this exact line (locale 16024, directly above "Release the 10 Caged Birds."). Other client lines on the same subject are
   - `why:` The locale table has `16024: Shadow Talon ninjas are rumored to have a camp here. Head in and defeat any ninjas you encounter!`, identical to the wiki quote. Searching the locale for "rumored to have a camp" returns it. The same claim is repeated in `prototype/osfr-tools/data/content/dungeons/danger_peaks.json` (`description` / panel text), which the same fact check should also update if it carries the claim.

2. Conflicts, item 2.
   - `old:` 2. **Panel description.** The wiki quote is not in the client. Other client descriptions exist (see Overview).
   - `new:` 2. **Panel description.** The wiki quote is in the client (locale 16024), so the wiki and client agree on it. Other client descriptions also exist (see Overview).
   - `why:` locale 16024 (same as correction 1). The conflict is not real, so it should not stay listed as one.

**Unsure:**

- Requirements, Combat job level cell: "No level-3 string exists in the client." Literally false in the locale: there are many "Wearable by a level 3 or higher Ninja" style strings (for example 42521, 42551) and "Battle Pet - Level 3" (10031). The narrower claim, that no dungeon-entry recommended-level string exists, looked true in my searches (no dungeon hit for "recommended level" or "levels 3"), but my search output was capped at 30 hits, so I did not confirm it. Consider rewording to say "no dungeon-entry level-3 string" if you want the claim kept.
- Checked and consistent: `Win Combat Encounter Danger Peaks` (locale 119163), `Group: Danger Peaks` (31057), `Complete the Danger Peaks encounter with a full group.` (31095), `Danger Peaks Bonus Objective` (140184), `Release the 10 Caged Birds.` (16026), `Defeat twelve ninjas in Danger Peaks` (20617), `Taka's Blade` (423107), "Shadowtalon Apprentices … in southern Sacred Grove" (130826), and `dungeons/danger_peaks.json` (`members_only: false`, `recommended_player_level: 3`, difficulty 2).
- The locale tool does not look up the note's hash-style `loc` ids (for example 3016521866, 2268990247, 2109427437 return "no such id"). I could not verify the ids themselves, only the text they point to, so I used the tool's own numbering (16024) in the corrections.
- Video claims ("Goals (1)", frame keys 92VCAHXkLGQ/…) are outside what I could check from the repo.
