<!-- fleet job=dialog-infer id=wcertified-treasure-hunter-v1 status=done turns=4 usd=0.0026 tokens(read,write,in,out)=[21777, 8197, 10, 2804] model=claude-haiku-5-5 -->
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
  {"claim": "Title is 'Certified Treasure Hunter' (locale 429174, quest_title, same quest).", "source": "locale:429174"},
  {"claim": "429183 asks the player whether they can be a certified treasure hunter at Camp Robbie, which is an offer-style ask.", "source": "locale:429183"},
  {"claim": "429178 restates the challenge (win a scavenger hunt or dig up artifacts) while the quest is active, so it is a progress reminder. Robbie is the attributed speaker.", "source": "locale:429178 + npc answer robbie (dialog list)"},
  {"claim": "429176 is the completion line: the player hands over the found item and is told to donate it to the camp leader.", "source": "locale:429176"},
  {"claim": "429179 is the quest objective: complete the Artifact Hunt or Jenny's Scavenger Hunt minigame (target 35604).", "source": "locale:429179"},
  {"claim": "429175 is a quest-journal description ('Robbie challenges your treasure hunting skills...'). It is not an offer or progress line.", "source": "locale:429175"},
  {"claim": "No reward text was found for this quest, so no reward line is given.", "source": "absence in client lookup (quest-tagged lines 429174-429183)"},
  {"claim": "429173 is excluded. It is tagged to the 'Confront Bigfoot' hint, not this quest, even though its text describes this same challenge. It is not used as the progress line.", "source": "locale:429173 tag hint"}
 ],
 "confidence": 0.6,
 "open": [
  "Speaker for the offer (429183) and complete (429176) is null. No NPC answer attributed them, and their text does not name a speaker. They read as Robbie's voice (the complete line mentions 'your camp leader'), but this is not confirmed, so the slot is left null.",
  "The pack's NPC answer labels 429178 as a quest_offer. Its text reads as a reminder of an already-given challenge, so it is filed as progress. The offer is 429183.",
  "429173 is tagged to Confront Bigfoot, so it is excluded, even though its text fits this quest. The 'come back and show Robbie' step has no separate quest_objective string. 429178 covers the challenge reminder instead.",
  "No reward line was found. Rewards are empty.",
  "line.previous is unconfirmed. 'Rags to Riches' is only a repo/wiki guess, so the prerequisite is left empty.",
  "Quest record_id is null. The repo quest ids conflict with the client ids, so the client title id 429174 is used.",
  "Giver locale id is null: Robbie's npc_name id was not found. The NPC id ucdt 3021485227 comes from the repo table and is not confirmed in the client."
 ]}
