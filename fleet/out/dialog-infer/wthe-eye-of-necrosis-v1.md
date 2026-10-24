<!-- fleet job=dialog-infer id=wthe-eye-of-necrosis-v1 status=done turns=2 usd=0.0035 tokens(read,write,in,out)=[6172, 12442, 6, 3711] model=claude-haiku-5-5 -->
# Locate The Eye of Necrosis

{"quest": {"key": "locate_the_eye_of_necrosis", "title": "Locate The Eye of Necrosis"},
 "offer": {"locale_id": 71183, "speaker": null},
 "progress": {"locale_id": 141822, "speaker": null},
 "complete": {"locale_id": 71186, "speaker": null},
 "other_lines": [
  {"locale_id": 71185, "role": "other", "speaker": null},
  {"locale_id": 71189, "role": "objective_hint", "speaker": null},
  {"locale_id": 71184, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "71183 is the pitch: it names the gem, the Haunted Mines, and asks the player 'Would you see if you can find it?'. It is the only candidate that reads as an offer.", "source": "locale:71183 (quest_dialog, hint 'The Eye of Necrosis')"},
  {"claim": "141822 is a progress reminder: 'Did you find The Eye of Necrosis? No? ... it's supposed to be somewhere in the Haunted Mines.' It is tagged to this item and has no FLAG.", "source": "locale:141822 (quest_dialog, hint 'The Eye of Necrosis')"},
  {"claim": "71186 is the completion line: 'You found it!'.", "source": "locale:71186 (quest_dialog, hint 'Locate The Eye of Necrosis')"},
  {"claim": "71185 is the rumor/intro line that sets up the search. It is not a clean offer, so it is listed as other.", "source": "locale:71185"},
  {"claim": "71189 is the go-objective text for the quest.", "source": "locale:71189 (quest_objective)"},
  {"claim": "71184 is the item name for the gem. It is not dialog.", "source": "locale:71184 (item)"},
  {"claim": "No reward string exists for this quest in the client.", "source": "locale search for tags on this quest: none found"},
  {"claim": "The only speaker hint is 'quarry' in 141822 and 71183 ('get this quarry up and running'). Dalton is the quarry NPC in repo notes, but no client line or NPC answer names him as the speaker, so speaker stays null.", "source": "locale:141822, locale:71183; repo NPCs - Blackspore Swamp.md (Dalton)"}
 ],
 "confidence": 0.45,
 "open": [
  "Speaker unresolved for all three dialog lines. Dalton (Quagmire Quarry) is only a candidate; no Blackspore spawn data or dialog tree confirms him, so the speaker fields are null.",
  "Offer is inferred. 71183 is the best pitch candidate, but 71185 (rumor) could also be the offer. The dialog tree is needed to choose between them.",
  "Progress 141822 is tagged to the 'Haunted Mines' hint, not this quest's title. It is kept because its text names The Eye of Necrosis and reads as a reminder. Confirm against the dialog tree.",
  "No reward line exists. The Haunted Mines reward block on the wiki belongs to the dungeon bonus, not this quest.",
  "No collect objective exists. 71184 is an item name only, with no count.",
  "Chain position is unknown. Locale 141825 ('The spiders lay their eggs inside the Haunted Mines...') may link to Breaking a Few Eggs but is unconfirmed, so previous and next are empty.",
  "Previous-record hashes from the earlier pass (1594866426, 2872111849, 1619711539, 1597218519, 3438722063) are not confirmed locale ids and are not used.",
  "The earlier answer marked live status as 'unsure'. The lines are unflagged, but no play record was checked."
 ]}
