<!-- fleet job=dialog-infer id=whunting-treasure-v1 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[8026, 9907, 6, 2958] model=claude-haiku-5-5 -->
# Hunting Treasure

{"quest": {"key": "Hunting Treasure", "title": "Hunting Treasure"},
 "offer": null,
 "progress": null,
 "complete": {"locale_id": 5102731, "speaker": null},
 "other_lines": [
  {"locale_id": 5102589, "role": "followup", "speaker": null},
  {"locale_id": 5102590, "role": "followup", "speaker": null},
  {"locale_id": 5102591, "role": "followup", "speaker": null},
  {"locale_id": 5102592, "role": "followup", "speaker": null},
  {"locale_id": 5102593, "role": "followup", "speaker": null},
  {"locale_id": 5102594, "role": "followup", "speaker": null},
  {"locale_id": 5102588, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is Hunting Treasure", "source": "locale:5102587"},
  {"claim": "Only objective text is 'Use the clue to find the lost treasure chest.'", "source": "locale:5102588"},
  {"claim": "5102731 says 'C'mon back tomorrow... more Lost Treasure Chests', a return/closing line tagged to Hunting Treasure, used as complete", "source": "locale:5102731"},
  {"claim": "5102729 is a UI message about an active quest or returning to Kara, so it is not dialog for any slot", "source": "locale:5102729"},
  {"claim": "5102589-5102594 are six Hunting Treasure riddle variants, each a clue ending 'That must be where your treasure is!'; they explain the clue given during the quest but are one-of-six, so no single one is chosen as offer or progress", "source": "locale:5102589-5102594"},
  {"claim": "5102595-5102602 are tagged Lost Treasure Chest, not this quest, so excluded", "source": "locale hint tags"},
  {"claim": "Giver Kara Loft (npc_id 9500000501, name 5102585); NPC answer attributes no dialog lines", "source": "npc answer kara loft"}
 ],
 "confidence": 0.4,
 "open": [
  "Offer slot left null: the only Hunting Treasure dialog that explains the task are the six riddle variants 5102589-5102594, and nothing in the pack says which one (or whether they are offer-time) is spoken on offer. Picking one would be a guess.",
  "Progress slot left null: no client line is a reminder tagged to this quest. 5102729 is a UI message, not NPC dialog.",
  "Complete = 5102731 is inferred from its 'come back tomorrow' wording and the lead's note that it is a return message; no NPC answer attributes it, so speaker is null. A builder should confirm it fires on turn-in.",
  "Speaker null for all lines: the hint is the quest name, not an NPC, and no NPC answer attributed any dialog. Kara Loft is the giver per wiki, but that does not name the speaker of these lines.",
  "Riddle-to-location mapping and chest spawn points remain unverified, so the 'use' objective cannot be wired to a location.",
  "Reward: no reward line is client-verified. Coin amount is wiki-only ('Random') and the Merry Vale Bouquet is omitted. Reward slot is therefore not in the JSON schema and is left out.",
  "Repeatable daily status is not in our records; the builder must add it."
 ]}
