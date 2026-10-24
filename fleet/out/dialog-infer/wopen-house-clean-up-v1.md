<!-- fleet job=dialog-infer id=wopen-house-clean-up-v1 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[20223, 9779, 10, 3488] model=claude-haiku-5-5 -->
# Open House Clean-Up

{"quest": {"key": "open_house_clean_up", "title": "Open House Clean-Up"},
 "offer": {"locale_id": 46813, "speaker": "Kelpy"},
 "progress": {"locale_id": 95010, "speaker": null},
 "complete": {"locale_id": 46817, "speaker": "Kelpy"},
 "other_lines": [{"locale_id": 46815, "role": "objective_hint", "speaker": null}],
 "evidence": [
  {"claim": "46813 is the offer: Kelpy asks how he can sell the house while the beach is covered in litter, and asks the player to pick up litter with a promise to 'make it worth your while'.", "source": "locale:46813 (quest_dialog tagged Open House Clean-Up); giver Kelpy locale 21308 per earlier answer"},
  {"claim": "46817 is the completion: 'Great job, [*player*]!' followed by Kelpy's line about selling the house.", "source": "locale:46817 (quest_dialog tagged Open House Clean-Up)"},
  {"claim": "46815 is the objective text naming Kelpy and the beach cleanup.", "source": "locale:46815 (quest_objective tagged Open House Clean-Up)"},
  {"claim": "95010 is a reminder that the beach litter is not yet cleaned, matching the in-progress state of this quest.", "source": "locale:95010 (quest_objective, no hint tag; text 'Have you cleaned all the litter off that beach yet?')"},
  {"claim": "139575, 139576 and 139578 are Kelpy's lines but belong to a chapter that sends the player to scout Rainchaser, Sundancer, Emuzz and Tazinna; they are not this quest's offer/progress/complete.", "source": "locale:139575 / 139576 / 139578 (npc answer kelpy)"},
  {"claim": "46825 'Open House Litter' is a placeholder junk line and is excluded; 46820 'Get off my lawn! NOW!' is an untagged npc_dialog and is excluded.", "source": "locale:46825, locale:46820"}
 ],
 "confidence": 0.6,
 "open": [
  "No quest record id exists; key is derived from the title. Repo title id 3340780897 conflicts with client id 46814 and was not used.",
  "Speaker for 46813 and 46817 is Kelpy from the text ('my house') and the giver locale 21308; no NPC answer attributes them directly.",
  "Progress 95010 has no quest hint tag and no NPC attribution. Its text names this quest's beach-litter task so it is used, but the speaker is null and the progress slot is only moderately confirmed.",
  "No reward line exists in the client. The 'worth your while' phrase in 46813 is an offer promise, not a reward value, so reward is not listed. No coins, items or xp are sourced.",
  "Objective count is not in the client text; the 'collect' mechanic is inferred from 'pick up' wording and is unconfirmed.",
  "Zone Seaside rests on the repo NPC placement and the earlier answer; it is not a direct client zone tag on these lines.",
  "The follow-up flyer quest Advertising to the Tourists has no verified record and is not included here."
 ]}
