<!-- fleet job=dialog-infer id=wfresh-ingredients-v1 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[14839, 8838, 8, 1677] model=claude-haiku-5-5 -->
# Fresh Ingredients

{"quest": {"key": "fresh_ingredients", "title": "Fresh Ingredients"},
 "offer": {"locale_id": 390250, "speaker": "Sal Monella"},
 "progress": null,
 "complete": {"locale_id": 390253, "speaker": "Sal Monella"},
 "other_lines": [{"locale_id": 390252, "role": "objective_hint", "speaker": null}],
 "evidence": [
  {"claim": "Offer: Sal asks for swamp lichen and pond scum, explaining the danger of collecting them.", "source": "locale:390250 (quest_dialog, tag Fresh Ingredients; full text re-checked, lists cray marauders as the lichen source)"},
  {"claim": "Complete: Sal thanks the player and offers a taste of his Sal Monella Special.", "source": "locale:390253 (quest_dialog, tag Fresh Ingredients)"},
  {"claim": "Objective: bring Sal swamp lichen from cray marauders and pond scum from venomous frogs.", "source": "locale:390252 (quest_objective, tag Fresh Ingredients)"},
  {"claim": "Quest title is Fresh Ingredients.", "source": "locale:390251"},
  {"claim": "Giver is Sal Monella, Blackspore Swamp.", "source": "quest answer giver locale 45300; NPC answer for Sal Monella lists Fresh Ingredients among quests given"},
  {"claim": "Progress line not found: no client line is tagged to this quest as a reminder.", "source": "locale tag search (only 390250-390253 tagged Fresh Ingredients)"},
  {"claim": "390288 and 390290 (Collect Swamp Lichen / Pond Scum) and 390348 (Zanna's dialog) are excluded.", "source": "critique handling; 390348 mentions poison toads and is another NPC's text"}
 ],
 "confidence": 0.7,
 "open": [
  "Quest record id is not in any source; left out of the JSON since no id exists.",
  "Spawned Sal Monella npc_id unresolved; speaker given by name only.",
  "Chain position unknown; previous and next left empty. Sal's Suggestion is not a verified predecessor.",
  "Progress slot null: no reminder line exists in client text for this quest.",
  "Reward unknown in all sources; the 390253 taste is not a reward; rewards left empty.",
  "Collect counts not in client text; mob ids for cray marauders and venomous frogs unresolved.",
  "Speaker for 390253 and 390250 is attributed from the quest giver and the text's first-person voice; no NPC answer directly tags these ids to Sal."
 ]}
