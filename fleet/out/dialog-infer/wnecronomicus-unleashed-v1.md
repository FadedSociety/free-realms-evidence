<!-- fleet job=dialog-infer id=wnecronomicus-unleashed-v1 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[7909, 10170, 6, 2176] model=claude-haiku-5-5 -->
# Necronomicus Unleashed

{"quest": {"key": "necronomicus_unleashed", "title": "Necronomicus Unleashed"},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 442599, "speaker": null},
 "other_lines": [
  {"locale_id": 442598, "role": "objective_hint", "speaker": null},
  {"locale_id": 442600, "role": "objective_hint", "speaker": null},
  {"locale_id": 442601, "role": "objective_hint", "speaker": null},
  {"locale_id": 442597, "role": "other", "speaker": null},
  {"locale_id": 442602, "role": "reward", "speaker": null},
  {"locale_id": 442603, "role": "reward", "speaker": null},
  {"locale_id": 442604, "role": "reward", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Necronomicus Unleashed'", "source": "locale:442596 (quest_title, tagged to this quest)"},
  {"claim": "Completion text: Necronomicus is placed in a holding cell and the player is thanked and rewarded", "source": "locale:442599 (quest_dialog, tagged to this quest)"},
  {"claim": "Travel objective: secret passage behind the mushrooms near the Den of Secrets, Merry Vale, level 20 group warning", "source": "locale:442598 (quest_objective, Merry Vale, tagged)"},
  {"claim": "Defeat objective: Awakened Necronomicus beneath Merry Vale", "source": "locale:442600 (quest_objective, tagged)"},
  {"claim": "Final objective 'Complete Necronomicus Unleashed'", "source": "locale:442601 (quest_objective, tagged)"},
  {"claim": "Pre-fight objective text referencing defeat at full power", "source": "locale:442597 (quest_objective, tagged, no zone)"},
  {"claim": "Rewards: Level 20 Awakened Weapon, Random Wilds Wearable, Random Wilds Building Materials", "source": "locale:442602, 442603, 442604 (item strings tagged to the quest's title cluster)"},
  {"claim": "Locale 4420197 ('You should probably return to Sanctuary and tell someone the news!') is not tagged to this quest and reads as a post-fight line for the earlier Necronomicus encounter (Encounter 432 / Rumbledome lair), so it is excluded", "source": "locale:4420197 (dialog, untagged); locale:5100662/5100664 Encounter 432 cluster"},
  {"claim": "No offer or in-progress dialog line exists in the client for this quest", "source": "lookup and locale searches on 'Necronomicus' return no other quest_dialog lines"},
  {"claim": "No NPC attribution for any line: the NPC answers are unanswered or empty, and 442599 names no speaker", "source": "npc_answers (blank key and 'necronomicus' with empty dialog)"}
 ],
 "confidence": 0.5,
 "open": [
  "Offer and progress slots are null: the client has no quest_dialog line tagged to this quest for either. A builder needs to decide whether the Fighter's Guild message board offers it, or whether it is started by the battle entry itself.",
  "Speaker for complete 442599 is null: the text names no NPC, the tag hint is '-', and no NPC answer attributed it. The line is written as a narrator-style message, possibly from the Sanctuary guard or a board, but nothing in the data confirms that.",
  "Giver is unverified: the Fighter's Guild Message Board in Sanctuary is wiki-sourced only, with no npc_id or locale id, so it is not used here.",
  "Previous/next quest links are unresolved; no source confirms a line. The earlier pass's link to 'Unmasking the Villain' was dropped as unsupported.",
  "Passage target has no locale id, so target_locale_id is null.",
  "Reward lines 442602-442604 are item-name strings, not reward dialog. The random weapon-to-job mapping and the random reward tables are not in our data.",
  "Repeatability is unknown. The 'spotted again' wording suggests a repeatable fight, but no record settles it.",
  "Light Boots reward is wiki-only and was not tied to this quest by client text, so it is excluded.",
  "Locale 442597 is a progress-like objective reminder ('Defeat him at his full power'). It is listed as other rather than progress, because it is an objective string with no speaker and no NPC attribution.",
  "The pack carried no explicit critiques to fix."
 ]}
