<!-- fleet job=dialog-infer id=wcertified-treasure-hunter-v4 status=done turns=1 usd=0.0022 tokens(read,write,in,out)=[0, 9366, 4, 1985] model=claude-haiku-5-5 -->
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
  {"claim": "Quest title is 'Certified Treasure Hunter'", "source": "locale:429174 (quest_title)"},
  {"claim": "Offer asks whether the player has what it takes to be a certified treasure hunter at Camp Robbie; unflagged and tagged to this quest", "source": "locale:429183"},
  {"claim": "Progress reminder restates the challenge (win a scavenger hunt or dig up artifacts); tagged to this quest; Robbie is attributed by the Robbie NPC answer's dialog list for this quest", "source": "locale:429178 + npc answer robbie"},
  {"claim": "Complete text thanks the player for the find and asks for a donation to the camp lead; tagged to this quest; no text names the speaker and no NPC answer attributes it", "source": "locale:429176"},
  {"claim": "Objective hint names the Artifact Hunt or Jenny's Scavenger Hunt minigame", "source": "locale:429179 (quest_objective)"},
  {"claim": "429175 is the journal description (quest_dialog), not an NPC line", "source": "locale:429175"},
  {"claim": "Robbie is the giver of this quest", "source": "npc answer robbie (quests_given)"}
 ],
 "confidence": 0.6,
 "open": [
  "Progress: 429173 has the strongest Robbie-voice text for this step, but its client tag is 'Confront Bigfoot' (429172), a different quest, so the tag rule excludes it. If that tag is confirmed as a mis-tag, 429173 would be the better progress line with speaker Robbie. Kept 429178 because it is tagged to this quest and the Robbie NPC answer attributes it. 429178 is third-person narration and the NPC answer files it under quest_offer, so this slot is a judgment call.",
  "Complete speaker is null. The text reads as Robbie's voice, but no text names him and no NPC answer attributes 429176 to him. Set to Robbie only if a source confirms it.",
  "Offer speaker is null. No text names the speaker and no NPC answer attributes 429183.",
  "No quest record id exists; record_id is null.",
  "line.previous is unconfirmed. 'Rags to Riches' is a guessed prerequisite, not bound by any client text.",
  "No reward line was found in any source; reward is null.",
  "Robbie's npc_name locale id was not found, so no giver locale id is given. The NPC id ucdt 3021485227 comes from the repo table and is not verified in client text.",
  "No quest_objective string exists for the 'come back and show Robbie' step; 429173 is the only candidate and is excluded by tag (see progress note)."
 ],
 "critiques_addressed": "Critique asked to bind progress to 429173. Not applied because the tag rule excludes lines tagged to another quest. The alternative is recorded in open. Critique asked for Robbie attribution on complete and offer; not applied because no source attributes them. Both are recorded in open."
}
