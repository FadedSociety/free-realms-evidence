<!-- fleet job=dialog-infer id=wthe-great-scavenger-hunt-v1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[22121, 9004, 10, 3059] model=claude-haiku-5-5 -->
# The Great Scavenger Hunt

{"quest": {"key": "the_great_scavenger_hunt", "title": "The Great Scavenger Hunt"},
 "offer": {"locale_id": 429101, "speaker": "Counselor Jenny"},
 "progress": {"locale_id": 429341, "speaker": null},
 "complete": {"locale_id": 429344, "speaker": null},
 "other_lines": [
  {"locale_id": 429343, "role": "objective_hint", "speaker": "Counselor Jenny"},
  {"locale_id": 429347, "role": "objective_hint", "speaker": null},
  {"locale_id": 429346, "role": "objective_hint", "speaker": null},
  {"locale_id": 429349, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer is Jenny's invitation 'Yoohoo! Hey there... I call it, Jenny's Great Scavenger Hunt. Interested?'", "source": "locale:429101 (text verified); npc answer for Counselor Jenny attributes 429101 to this quest"},
  {"claim": "Quest title is 'The Great Scavenger Hunt'", "source": "locale:429342 (quest_title, tagged to the quest)"},
  {"claim": "Jenny's intro objective text", "source": "locale:429343 (npc answer attributes to Jenny, same quest)"},
  {"claim": "Progress line explains the chest starts the timer and gives the bonus for a fast finish; it is the start-of-hunt instruction, not a reminder", "source": "locale:429341 (text verified; tagged to quest; speaker not named in text)"},
  {"claim": "Complete line thanks the player for finding everything quickly", "source": "locale:429344 (text verified; tagged to quest; speaker not named in text)"},
  {"claim": "Chest step objective 'Click the chest'", "source": "locale:429347 (quest_objective tagged to quest; the word 'chest' is locale 431624)"},
  {"claim": "Play step objective text", "source": "locale:429346 (quest_objective tagged to quest)"},
  {"claim": "Completion-step objective 'Complete Jenny's Great Scavenger Hunt'", "source": "locale:429349 (quest_objective tagged to quest)"},
  {"claim": "Minigame name 'Jenny's Great Scavenger Hunt'", "source": "locale:429101 text and the minigame name in 429101 / 429349"},
  {"claim": "Certified Treasure Hunter (429173) lists the scavenger hunt as one of two routes to the branch", "source": "locale:429173 (text verified)"},
  {"claim": "Reward is a bonus for a fast finish, amount not stated", "source": "locale:429341 (text verified); no coin or item amount found"}
 ],
 "confidence": 0.6,
 "open": [
  "Offer 429101 is attributed to Counselor Jenny by the NPC answer; Jenny is the quest giver (npc 9500000300).",
  "Progress 429341 and complete 429344 are tagged to the quest but their text names no speaker and the NPC answer attributes only 429343 and 429101 to Jenny. Speaker left null per the attribution rule; Jenny is the likely speaker but is not confirmed by an attribution.",
  "Progress 429341 is the chest-start instruction (explains the timer and bonus) rather than a reminder shown while the hunt is underway. No separate in-progress reminder line was found.",
  "Reward: the only reward reference is the unquantified fast-finish bonus in 429341. No coin, item or amount is sourced, so no reward locale is recorded as a reward line.",
  "Quest key is a placeholder derived from the title; no quest record exists. Title id conflict noted by the earlier pass (repo notes give 3084618415) was not verified. Client text uses 429342.",
  "Chain: the hunt feeds Certified Treasure Hunter (429173) as an optional route, not a sequential prerequisite. Previous quest in the line is unknown; Rags to Riches is unverified.",
  "The chest's object id is not in the client text; only the word 'chest' (locale 431624) is available.",
  "Locales 429328 and 429326 belong to Defensive Strategy and were excluded."
 ]}
