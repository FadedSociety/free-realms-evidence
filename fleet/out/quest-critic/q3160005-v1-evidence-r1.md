<!-- fleet job=quest-critic id=q3160005-v1-evidence-r1 status=no_submit turns=4 usd=0.0044 tokens(read,write,in,out)=[49671, 21411, 10, 2494] model=claude-haiku-5-5 -->
# Sticky Spell Book

{"lens": "evidence", "pass": true, "score": 4, "problems": [{"field": "rewards", "issue": "The answer records the reward as 'other' with no verified reward. Its open list says payouts should not be enabled until a reward source exists, yet the source record has enabled: true and carries 5 coins and 25 Wizard XP. Those values are reconstructed fallbacks (T303, W110 fallback), so a builder would pay unverified rewards.", "fix": "Either set enabled to false or mark the coins and job XP as provisional in the record. A real reward needs a source (the client has no reward line for 3160005, per the answer's own open list)."}, {"field": "objectives[0].target_locale_id", "issue": "Nurble's name locale id is null. The answer's own evidence, the locale tool, and the grep of en_us_data.dat show the text 'Nurble' at ucdt 1550230613, which is a candidate, but it is not confirmed as Nurble's NPC name string. The null is honest, so this is a gap rather than an error.", "fix": "Confirm 1550230613 against the NPC name table or leave the field null with a note."}]}

Checks I ran, all confirmed:
- Title 22193 = "Sticky Spell Book" (unflagged).
- Objective 22211 = "Give the spell book to Nurble"; its hash matches 1281056681.
- Objective 22227 = "Return the spell book to Fizzlesticks at the Robgoblin Camp."
- Description 22194 is unflagged; the offer 24949 and completion 22373 texts match the answer.
- 103130 = "Give the Spell Book to Nurble in the Robgoblin Camp."
- Progress 22212 exists ("Hopefully Nurble can get this sticky stuff off of the spell book!").
- Fizzlesticks 9000000324 gives Wizard quests in wilds.json. Nurble 9000000415 is in wilds.json.
- The T303 canary note confirms the two-objective structure: removing the return step broke the test, so the Fizzlesticks return objective is supported.

I did not find a wrong id, a flagged line treated as live, or a broken chain link. The previous and next links (3160004, 3160006) match the other records in the pack.
