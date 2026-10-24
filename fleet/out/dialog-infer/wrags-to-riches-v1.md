<!-- fleet job=dialog-infer id=wrags-to-riches-v1 status=done turns=1 usd=0.0021 tokens(read,write,in,out)=[0, 7577, 4, 2241] model=claude-haiku-5-5 -->
# Rags to Riches

{"quest": {"key": "rags_to_riches", "title": "Rags to Riches"},
 "offer": {"locale_id": 429095, "speaker": "Robbie"},
 "progress": {"locale_id": 429107, "speaker": null},
 "complete": null,
 "other_lines": [
  {"locale_id": 429097, "role": "objective_hint", "speaker": null},
  {"locale_id": 429110, "role": "objective_hint", "speaker": null},
  {"locale_id": 429119, "role": "objective_hint", "speaker": null},
  {"locale_id": 429098, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Rags to Riches' (locale id 429096); the repo's 40276724 is a stale value.", "source": "locale:429096"},
  {"claim": "Offer line: Robbie welcomes the player to his camp and sends them to speak with the counselors.", "source": "locale:429095 text; npc answer robbie lists 429095 as quest_offer for Rags to Riches"},
  {"claim": "Progress reminder asks whether the player has met all the camp counselors, matching the 'meet the counselors' objectives.", "source": "locale:429107 text; objectives 429110, 429111, 429113, 429115, 429117, 429119"},
  {"claim": "No completion/turn-in line exists in the tagged client text for this quest.", "source": "locale tag search for Rags to Riches; no quest_dialog after 429107 tied to it"},
  {"claim": "429098 is Robbie's hand-off of a further challenge, which points to the follow-on quest, not a payout.", "source": "locale:429098 text; Robbie's answer lists 429178 as the Certified Treasure Hunter offer, not 429098"},
  {"claim": "Objective lines for the counselors and the Robbie return step.", "source": "locale:429097, 429110, 429111, 429113, 429115, 429117, 429119"},
  {"claim": "Reward list is empty; no reward line found.", "source": "earlier pass rewards: [] and no reward-tagged locale line"}
 ],
 "confidence": 0.6,
 "open": [
  "complete is null: no turn-in quest_dialog was found for this quest in the client text. 429098 is a hand-off to a new challenge, not a completion line.",
  "progress 429107 has no speaker attribution. The text says 'my camp', which fits Robbie as camp leader, but no NPC answer or name in the text confirms it, so speaker is left null.",
  "429098 has no speaker attribution in the NPC answers (Robbie's list does not include it), so its speaker is null.",
  "Objective lines are kept as objective_hint with null speaker because they are quest-log text, not NPC dialog.",
  "No reward data exists in the pack or locale; rewards are empty.",
  "npc_id ucdt:3021485227 for Robbie is from repo notes and is not verified against client NPC data.",
  "Next quest 'Certified Treasure Hunter' is inferred from 429098 and 429173, not from a chain record. Counselor quests (Unearthing Treasures, Scavenger Hunt, What's for Dinner?, Bigfoot's Endangered) are not successors and are excluded.",
  "Whether any quest precedes this one is unconfirmed."
 ]}
