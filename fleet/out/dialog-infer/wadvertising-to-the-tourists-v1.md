<!-- fleet job=dialog-infer id=wadvertising-to-the-tourists-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[16218, 8801, 8, 2918] model=claude-haiku-5-5 -->
# Advertising to the Tourists

{"quest": {"key": "advertising_to_the_tourists", "title": "Advertising to the Tourists"},
 "offer": {"locale_id": 95037, "speaker": "Kelpy"},
 "progress": {"locale_id": 95052, "speaker": null},
 "complete": {"locale_id": 95040, "speaker": null},
 "other_lines": [
  {"locale_id": 95030, "role": "objective_hint", "speaker": null},
  {"locale_id": 95039, "role": "objective_hint", "speaker": null},
  {"locale_id": 95050, "role": "objective_hint", "speaker": null},
  {"locale_id": 95032, "role": "objective_hint", "speaker": null},
  {"locale_id": 95034, "role": "objective_hint", "speaker": null},
  {"locale_id": 95036, "role": "objective_hint", "speaker": null},
  {"locale_id": 95042, "role": "objective_hint", "speaker": null},
  {"locale_id": 95044, "role": "objective_hint", "speaker": null},
  {"locale_id": 95046, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer text 95037 asks the player to deliver flyers to buyers for Kelpy's luxurious home", "source": "locale:95037 (confirmed by locale lookup); Kelpy NPC answer attributes 95037 as quest_offer"},
  {"claim": "Completion thanks the player for delivering the flyers; this is the complete line", "source": "locale:95040 'Thanks for delivering those flyers. Let's hope someone is interested!' (confirmed by locale lookup)"},
  {"claim": "95050 is an objective step ('Return to Kelpy and let him know...'), not spoken dialog, so it is not the complete line; the Kelpy answer's quest_complete attribution is a misclassification", "source": "locale:95050 tagged quest_objective; text is instruction to the player"},
  {"claim": "95052 is a progress reminder asking whether all flyers were delivered to people on the list", "source": "locale:95052 (confirmed by locale lookup), tagged quest_objective in client data"},
  {"claim": "Quest title is locale 95029", "source": "locale:95029 quest_title tagged Seaside / Advertising to the Tourists"},
  {"claim": "Seven flyer-delivery steps: Pablo Gable, Gemi Winkie, Emuzz, Egona, Fergus, Tootsie (six named deliver targets in the pack's list; Tootsie's step text is 95046)", "source": "locale:95032, 95034, 95036, 95042, 95044, 95046; 'Deliver to X' label lines 95031/95033/95035/95041/95043 are titles, not steps"}
 ],
 "confidence": 0.6,
 "open": [
  "Complete speaker left null: 95040 is tagged to the quest but its text does not name Kelpy, and no NPC answer attributes it. Kelpy is the plausible speaker (the offer says 'my home' and the quest is Kelpy's), but that is not sourced.",
  "Progress speaker left null: 95052 is not attributed to any NPC answer; its text refers to 'the list I gave you' but does not name a speaker.",
  "The pack's complete=95050 is rejected: 95050 is a quest_objective instruction, not a thanks/pay line. The pack's own Kelpy answer lists it as quest_complete, which should be corrected.",
  "No record_id exists for this quest; record_id left unset (the pack's repo title id 279129978 was unverified and conflicts with locale 95029).",
  "Rewards: none found in client text, wiki or articles, so other_lines has no reward entry.",
  "Next quest in the chain is unconfirmed (Feminine Touch is only a candidate). Previous quest Open House Clean-Up's ids (46813/46815) were not rechecked.",
  "Deliver counts are assumed 1 per step from 'a flyer' wording; no explicit count was found.",
  "Giver Kelpy (npc_id 2004, locale 21308) is supported by the offer attribution but not by a trigger record."
 ]}
