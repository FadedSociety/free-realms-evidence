<!-- fleet job=dialog-infer id=wrob-robbie-daily-v1 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[5256, 6467, 6, 1483] model=claude-haiku-5-5 -->
# Rob Robbie daily

{"quest": {"key": "rob_robbie_daily", "title": "Rob Robbie daily"},
 "offer": null,
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 430055, "role": "objective_hint", "speaker": null},
  {"locale_id": 430019, "role": "reward", "speaker": null},
  {"locale_id": 430064, "role": "reward", "speaker": null},
  {"locale_id": 430065, "role": "reward", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Rob Robbie daily' (430036).", "source": "locale:430036"},
  {"claim": "Only quest-related prompt is the junkpile confirmation 'Take something from Robbie's abandoned junkpile?'. It is a ui confirmation, not an NPC offer/progress/complete line, so it is listed as an objective_hint with no speaker.", "source": "locale:430055"},
  {"claim": "Reward item names: Robbie's Loot (common), Robbie's Loot (rare), Robbie's Loot (chest). These are item names, not NPC reward text.", "source": "locale:430019, 430064, 430065"},
  {"claim": "Full-text and regex searches for Robbie / junkpile in the client found no offer, progress or completion dialog for this daily. Other Robbie lines belong to the Camp Robbie treasure-hunter and Bigfoot quests (e.g. 429097, 429119, 429189) and were not used.", "source": "lookup client 'Robbie junkpile'; locale regex (?i)robbie"},
  {"claim": "Earlier pass found no quest record id and no giver NPC; the trigger is a world object (Robgoblin Junkpile), so no NPC speaker can be attributed.", "source": "quest answer open items"}
 ],
 "confidence": 0.35,
 "open": [
  "No offer, progress or complete dialog line exists in the client tagged to this daily or naming the junkpile task; all three slots left null rather than guessed.",
  "Giver/speaker unknown: trigger is a world object, no NPC attribution from npc answers (all unanswered).",
  "430055 is a UI confirmation prompt; it may not be shown as dialog. Included only as objective_hint.",
  "Reward ids 430019/430064/430065 are item names; item ids unresolved, so they are not wired as reward grants.",
  "Quest record id, live status, chain position and reset/streak logic remain unverified (see earlier answer)."
 ]}
