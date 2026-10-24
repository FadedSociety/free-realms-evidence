<!-- fleet job=dialog-infer id=wambush-recovery-v1 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[18999, 12440, 8, 2322] model=claude-haiku-5-5 -->
# Ambush Recovery

{"quest": {"key": "Ambush Recovery", "title": "Ambush Recovery"},
 "offer": {"locale_id": 29648, "speaker": "Noggle Cogloose"},
 "progress": null,
 "complete": {"locale_id": 29652, "speaker": "Noggle Cogloose"},
 "other_lines": [
  {"locale_id": 29651, "role": "objective_hint", "speaker": "Noggle Cogloose"},
  {"locale_id": 29649, "role": "other", "speaker": null},
  {"locale_id": 439878, "role": "objective_hint", "speaker": null},
  {"locale_id": 29650, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer is 29648: Noggle asks about his lost Power Crystals and 'what are you going to do about it?', an opening hook.", "source": "locale:29648 text; npc answer Noggle Cogloose dialog list (offer 29648 pack claim)"},
  {"claim": "Complete is 29652: Noggle reacts to receiving the Power Crystals ('Ah ha! My Power Crystals!'), a thank-you/payoff line.", "source": "locale:29652 text; quest_dialog tagged Ambush Recovery"},
  {"claim": "29654 is NOT the completion line. Its text ('Noggle has his Power Crystals! ... install his Power Crystals in several nearby Small Dwarf Tech Jump Pads') is the opening of the next quest, Power Crystals Not Included (locale:29653).", "source": "locale:29654 text and title 29653 tag"},
  {"claim": "29651 is NPC speech tagged quest_objective that asks the player to 'bring back my Power Crystals' and urges them to get on with it; it reads as a reminder but is tagged as objective text, so it is listed as an objective hint rather than a clean progress line.", "source": "locale:29651 text; quest_objective tag"},
  {"claim": "Objective text 439878 'Noggle Cogloose wants you to retrieve his Power Crystals in Sunstone Valley' is the collect objective.", "source": "locale:439878"},
  {"claim": "Title 29649 'Ambush Recovery' is the quest_title line.", "source": "locale:29649"},
  {"claim": "No reward line found for this quest; reward left null.", "source": "search of tagged client lines: 29644 reward text belongs to the Rizzle quest chain, not Ambush Recovery"}
 ],
 "confidence": 0.5,
 "open": [
  "Progress: no clean progress/reminder line confirmed. 29651 is the closest reminder but is tagged quest_objective NPC speech; left as objective_hint, progress null.",
  "Complete 29652 is a reaction line with no explicit reward; reward not confirmed.",
  "Offer 29648 is the best opening candidate but no server record or script confirms the binding.",
  "Giver name 'Noggle Cogloose' is supported by the wiki and the 29648 speech context but no locale name id is confirmed.",
  "Pack's note that 29654 is a quest_complete line was rejected: its text belongs to Power Crystals Not Included.",
  "Locale id 439879 ('Return to Noggle Cogloose') was not re-verified in this pass; kept only as pack-supplied objective text, not used in the bindings.",
  "Quest-level title 439874 'Find Noggle's Power Crystals' may be the real client title; 29649 is kept as the quest_title-tagged string."
 ]}
