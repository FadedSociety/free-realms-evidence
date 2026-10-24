<!-- fleet job=dialog-infer id=wchef-craving-something-tasty-v1 status=done turns=4 usd=0.0031 tokens(read,write,in,out)=[24826, 10494, 10, 3089] model=claude-haiku-5-5 -->
# Craving Something Tasty

{"quest": {"key": "craving_something_tasty", "title": "Craving Something Tasty"},
 "offer": {"locale_id": 101061, "speaker": "Seaspray"},
 "progress": {"locale_id": 101070, "speaker": "Seaspray"},
 "complete": {"locale_id": 101064, "speaker": "Seaspray"},
 "other_lines": [
  {"locale_id": 101054, "role": "objective_hint", "speaker": null},
  {"locale_id": 101056, "role": "objective_hint", "speaker": "Diggy"},
  {"locale_id": 101058, "role": "objective_hint", "speaker": null},
  {"locale_id": 101060, "role": "objective_hint", "speaker": null},
  {"locale_id": 101059, "role": "objective_hint", "speaker": null},
  {"locale_id": 101063, "role": "objective_hint", "speaker": null},
  {"locale_id": 101065, "role": "followup", "speaker": "Diggy"},
  {"locale_id": 101067, "role": "followup", "speaker": "Diggy"}
 ],
 "evidence": [
  {"claim": "Quest title is 'Craving Something Tasty' (id 101053, tagged Seaside / Seaspray)", "source": "locale:101053"},
  {"claim": "Offer line: Seaspray asks the player to bring something special from the Ocean Treasures Cafe", "source": "locale:101061 (quest_dialog, Seaside, Seaspray)"},
  {"claim": "Progress line: Seaspray reminds the player to get food from Ocean Treasures Cafe", "source": "locale:101070 (quest_dialog, Seaside, Seaspray)"},
  {"claim": "Completion line: Seaspray thanks the player after the meal is delivered", "source": "locale:101064 (quest_dialog, Seaside, Seaspray)"},
  {"claim": "Talk objective to Diggy at Ocean Treasures Cafe", "source": "locale:101056 (quest_objective, Speak with Diggy)"},
  {"claim": "Minigame objective, started by speaking with Diggy", "source": "locale:101058 (quest_objective, Diggy's cooking minigame)"},
  {"claim": "Deliver objective to Seaspray at Seaspray Inn (locale text has typo 'Seapsray')", "source": "locale:101060"},
  {"claim": "Collect objective: get meal for Seaspray from Ocean Treasures Cafe", "source": "locale:101063"},
  {"claim": "Return objective 'Return to Seaspray'", "source": "locale:101059"},
  {"claim": "Minigame intro and start lines are Diggy's (cafe cook offering help; reply 'Awesome! Just let me know when you are ready')", "source": "locale:101065 and 101067 tagged to Diggy's cooking minigame; Diggy npc answer lists 101058 and 101056 as this quest's progress lines"},
  {"claim": "Seaspray is the giver: offer, progress and complete lines are all spoken by Seaspray", "source": "Seaspray npc answer (101061, 101070, 101064); Diggy npc answer does not list this quest as given"}
 ],
 "confidence": 0.6,
 "open": [
  "Giver conflict: the Seaside repo note and Chef notes name Diggy as giver, but the dialog lines are Seaspray's and the Seaspray answer lists the offer. Seaspray (npc 9500000623, locale 21301) is used.",
  "Seaspray name id: the Seaside note cites 2595179637; the client uses 21301 and that is used here.",
  "Ocean Treasures Cafe has no verified live locale id (93476 is flagged), so no target id is given for it.",
  "Line 101054 ('Get something tasty from the Ocean Treasures Cafe for Seaspray') is unplaced. It may be an earlier step or a sibling quest. Its order is unknown, so it is listed as an objective_hint with null speaker.",
  "Objective order (talk, minigame, deliver, collect) is inferred from the text, not from step data. Line 101060 is chosen over 100291 (Hasty Food Delivery) by wording.",
  "No reward line exists in client text for this quest; reward is empty. Whether the minigame counts as Chef progress is not stated.",
  "Diggy's npc_id 9000000070 is unverified and is left out. Speaker for 101065/101067 is Diggy by cafe/minigame context, not an explicit name in the text.",
  "Quest record does not exist yet. Create one with title 'Craving Something Tasty', title_locale_id 101053, giver npc_id 9500000623 (Seaspray)."
 ]}
