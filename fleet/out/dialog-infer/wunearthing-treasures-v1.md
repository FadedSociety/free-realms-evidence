<!-- fleet job=dialog-infer id=wunearthing-treasures-v1 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6647, 8002, 6, 2191] model=claude-haiku-5-5 -->
# Unearthing Treasures

{"quest": {"key": "unearthing_treasures", "title": "Unearthing Treasures"},
 "offer": {"locale_id": 429355, "speaker": "Counselor Cammy"},
 "progress": {"locale_id": 429367, "speaker": "Counselor Cammy"},
 "complete": {"locale_id": 429358, "speaker": null},
 "other_lines": [
  {"locale_id": 429357, "role": "objective_hint", "speaker": null},
  {"locale_id": 429360, "role": "objective_hint", "speaker": null},
  {"locale_id": 429363, "role": "objective_hint", "speaker": null},
  {"locale_id": 429365, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer line: 429355 is a quest_dialog tagged to Unearthing Treasures that invites the player to dig something up and show it to Robbie.", "source": "locale:429355"},
  {"claim": "Offer speaker is Cammy: the Counselor Cammy NPC answer attributes 429355 to her and lists her as giver of this quest.", "source": "npc answer: counselor cammy"},
  {"claim": "Progress line: 429367 asks whether the player has dug up anything worth showing off yet, tagged to this quest and attributed to Cammy by the NPC answer.", "source": "locale:429367 / npc answer: counselor cammy"},
  {"claim": "Complete line: 429358 is a quest_dialog tagged to this quest that pays off the find with a consolation item ('Take this instead').", "source": "locale:429358"},
  {"claim": "Complete speaker is not confirmed: 429358 has no speaker tag and no NPC answer attributes it. Its scheming tone ('Heh heh heh', 'give that old thing to me') suggests Robbie, but Cammy is the objective turn-in ('Return to Counselor Cammy', 429365). Left null.", "source": "locale:429358 / locale:429365"},
  {"claim": "Objective lines: 429360 dig up and show off, 429363 beat first three levels of Artifact Hunt, 429365 return to Cammy; 429357 is the quest description.", "source": "locale:429357, 429360, 429363, 429365"},
  {"claim": "Title is 429356 'Unearthing Treasures'.", "source": "locale:429356"}
 ],
 "confidence": 0.6,
 "open": [
  "Complete speaker unconfirmed: 429358 has no speaker tag and no NPC answer attributes it. Robbie is plausible from the wording, but the objective turn-in is Cammy, so speaker left null.",
  "Locale 429099, which the Counselor Cammy NPC answer lists as a quest_offer for this quest, does not resolve in the locale table, so it is rejected. The offer is 429355 instead.",
  "Reward item 'Take this instead' is not named in the client text; no item id is available, so no reward item id is given.",
  "No quest record id exists in our data, and the earlier hash-style ids are not locale ids. Previous/next line position is unknown, so the chain is left empty.",
  "Locale 429369 'Cammy's Dig Site' is a title with no body and is not linked to this quest.",
  "Quest is repeatable per the wiki; no level, cost or prerequisite is known."
 ]}
