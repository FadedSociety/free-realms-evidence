<!-- fleet job=dialog-infer id=wbacks-against-the-wall-v1 status=done turns=4 usd=0.0031 tokens(read,write,in,out)=[24111, 9403, 10, 3456] model=claude-haiku-5-5 -->
# Backs Against the Wall

{"quest": {"key": "Backs Against the Wall", "title": "Backs Against the Wall"},
 "offer": {"locale_id": 438471, "speaker": null},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 438473, "role": "followup", "speaker": null},
  {"locale_id": 438499, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "438472 is the quest title 'Backs Against the Wall' (Shrouded Glade).", "source": "locale:438472 / client tag"},
  {"claim": "438471 is a quest_dialog tagged to this quest; it explains the druids are hit hard and says to talk to Headmaster Merk. It fits an offer/explanation role.", "source": "locale:438471 / client tag Backs Against the Wall"},
  {"claim": "438473 is a quest_dialog tagged to this quest: Captain Sunspark suggested talking to Headmaster Merk. It is the hand-off step; the speaker is not named as Sunspark in the text (he is referred to in third person).", "source": "locale:438473 / client tag Backs Against the Wall"},
  {"claim": "438499 'Talk to Headmaster Merk' is the step objective text, but its client tag hint is 'Choose a Side' (Sunstone Valley) and the pack notes it is shared generic text, so it is listed only as a hint.", "source": "locale:438499 / client tag Choose a Side"},
  {"claim": "Captain Sunspark is the giver per the quest record (locale:437145 is his name), but no spawn id or offer line from him for this quest was found.", "source": "locale:437145 / npc answer"},
  {"claim": "Headmaster Merk candidates 437565 (barrier around the bridge to the north) and 437566 (bridge safe, Gloam cut off from Sunstone Valley) were attributed to this quest by an NPC answer, but their client tags are 'Sunstone Valley | Headmaster Merk', not this quest, so they are not used.", "source": "locale:437565, locale:437566 / npc answer"},
  {"claim": "The 2-coin reward is not used: the wiki card caption ties it to this quest but its body text matches locale 726 (Fortify Our Defenses), so attribution is unresolved.", "source": "wiki image: Headmaster Merk.png"}
 ],
 "confidence": 0.3,
 "open": [
  "Giver spawn id unresolved; Captain Sunspark's location is conflicting (Shrouded Glade Warpstone vs Sanctuary), so giver.npc_id is left unwired.",
  "Offer 438471 is the best quest-tagged explanation line, but its speaker is not named by the text or an NPC answer; speaker left null.",
  "No progress or complete line tagged to Backs Against the Wall was found. 437565 and 437566 (Merk quest_dialog/complete text, attributed by an NPC answer) are tagged to Sunstone Valley / Headmaster Merk, not this quest, so they were not assigned; verify whether they are this quest's progress/complete lines before wiring.",
  "Reward of 2 coins is unconfirmed and left out of the output.",
  "438499 is shared generic objective text tagged to 'Choose a Side'; it is listed as a hint only."
 ]}
