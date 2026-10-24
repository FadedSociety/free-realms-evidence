<!-- fleet job=dialog-infer id=wcertified-treasure-hunter-v2 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[18041, 9721, 8, 2237] model=claude-haiku-5-5 -->
# Certified Treasure Hunter

{"quest": {"key": "certified_treasure_hunter", "title": "Certified Treasure Hunter"},
 "offer": {"locale_id": 429183, "speaker": null},
 "progress": {"locale_id": 429178, "speaker": "Robbie"},
 "complete": {"locale_id": 429176, "speaker": null},
 "other_lines": [
  {"locale_id": 429179, "role": "objective_hint", "speaker": null},
  {"locale_id": 429175, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Certified Treasure Hunter'.", "source": "locale:429174 (quest_title)"},
  {"claim": "429183 asks whether the player can be a certified treasure hunter at Camp Robbie. It is an offer-style ask, and no NPC answer attributes it to a speaker.", "source": "locale:429183"},
  {"claim": "429178 restates the challenge (win a scavenger hunt or dig up artifacts) while the quest is active. It is a progress reminder. The Robbie NPC answer lists it among his dialog for this quest, so Robbie is the attributed speaker. Its text is narration, which is why the progress speaker rests on the NPC answer alone.", "source": "locale:429178 + npc answer robbie"},
  {"claim": "429176 is the completion line: the player has found something, is thanked in Robbie's voice ('my collection', 'your camp leader'), and is asked to donate it. The text does not name the speaker, and no NPC answer attributes it, so the speaker is left null.", "source": "locale:429176"},
  {"claim": "429179 is the quest objective: complete the Artifact Hunt or Jenny's Scavenger Hunt minigame.", "source": "locale:429179 (quest_objective)"},
  {"claim": "429175 is a journal description of the quest, not an offer or progress line.", "source": "locale:429175 (quest_dialog)"},
  {"claim": "429173 has the closest text (challenge: win the scavenger hunt or dig up an artifact, then come back and show me), but it is tagged to the 'Confront Bigfoot' quest, so under the tag rule it is not used for this quest. It is not bound to progress.", "source": "locale:429173 tag hint 'Confront Bigfoot'"},
  {"claim": "No reward line exists for this quest among the tagged lines.", "source": "absence in client lookup"}
 ],
 "confidence": 0.5,
 "open": [
  "Critique asked to rebind progress to 429173. Not done: 429173 is tagged to Confront Bigfoot (429172), a different quest, so the tag rule excludes it. 429178 stays as progress, with Robbie as speaker taken from the NPC answer.",
  "429178 is third-person narration, not Robbie's direct speech. Its speaker comes only from the NPC answer's dialog list, which also labelled it quest_offer; the text fits a progress reminder better.",
  "Offer (429183) and complete (429176) speakers are null. Neither text names a speaker and no NPC answer attributes them. 429176 sounds like Robbie, but that stays unconfirmed.",
  "line.previous is empty. 'Rags to Riches' is only a guessed prerequisite and is unconfirmed.",
  "No quest record id is known; record_id left out. Giver locale id for Robbie was not found in client text.",
  "No reward line found; reward left empty.",
  "The 'come back and show Robbie' step has no separate quest_objective string; 429179 covers the minigame objective."
 ]}
