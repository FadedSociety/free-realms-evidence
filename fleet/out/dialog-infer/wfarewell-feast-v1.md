<!-- fleet job=dialog-infer id=wfarewell-feast-v1 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[16999, 11153, 8, 3553] model=claude-haiku-5-5 -->
# Farewell Feast

{"quest": {"key": "farewell_feast", "title": "Farewell Feast"},
 "offer": {"locale_id": 428199, "speaker": "Diggy"},
 "progress": {"locale_id": 428203, "speaker": "Diggy"},
 "complete": {"locale_id": 428202, "speaker": "Diggy"},
 "other_lines": [
  {"locale_id": 428200, "role": "other", "speaker": null},
  {"locale_id": 428201, "role": "objective_hint", "speaker": null},
  {"locale_id": 428218, "role": "objective_hint", "speaker": null},
  {"locale_id": 428207, "role": "followup", "speaker": "Diggy"},
  {"locale_id": 428219, "role": "followup", "speaker": null},
  {"locale_id": 428221, "role": "followup", "speaker": null},
  {"locale_id": 428242, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Title is Farewell Feast", "source": "locale:428200"},
  {"claim": "Offer: Diggy, a chef, asks what pirates want to eat", "source": "locale:428199 text, npc answer diggy quest_offer-style entry for this quest"},
  {"claim": "Progress: Diggy asks what the searats want to eat, matching talk objective", "source": "locale:428203 text, locale:428218 objective"},
  {"claim": "Talk objective: tell Diggy the food the pirates want", "source": "locale:428218"},
  {"claim": "Diggy says he will make a sample after the talk step", "source": "locale:428207"},
  {"claim": "Deliver objective: give sample to Jolly Rogers", "source": "locale:428242, target name locale:436629 = 'Jolly Roger'"},
  {"claim": "Complete candidate: Diggy's closing reply (seafood/steak, treasure map, 'Thanks, [*player*]!') is the only line in the set that thanks the player", "source": "locale:428202 text"},
  {"claim": "Pirate reactions approve/reject the sample", "source": "locale:428219 (approve), locale:428221 (reject)"},
  {"claim": "Diggy is giver at Ocean Treasures Cafe, Seaside, and lists Farewell Feast in quests_given", "source": "npc answer diggy"},
  {"claim": "No reward text found for this quest", "source": "no client line tagged to quest with reward wording"}
 ],
 "confidence": 0.5,
 "open": [
  "No quest record exists; record_id is null and a new record is needed.",
  "complete = 428202 is the only thanking line, but its text answers the pirates' rejection (428221: 'sick of seafood'), so it may be the reject-branch closer rather than a general turn-in. Its branch link is unverified; no approve-branch closer was found.",
  "428219 and 428221 are pirate reactions to the sample. Text does not name the speaker (inferred 'Jolly Roger' from the deliver target but not confirmed), so speaker is null. They do not thank or pay, so they are not used as complete.",
  "No cooking objective line in client text; chain shown is talk (428218) then deliver (428242). 428207 is a followup, not an objective.",
  "Deliver target NPC: 'Jolly Roger' string 436629 exists but no Seaside NPC record with that name id was confirmed; npc_id unresolved. Objective text says 'Rogers' while the NPC name is 'Roger'.",
  "Giver npc_id 9000000070 is unconfirmed by a quests_given record; the giver link rests on the wiki and the npc answer.",
  "Rewards: none sourced. The treasure map mentioned in 428202 is not shown to be a reward.",
  "previous/next prerequisite chain unknown; no prerequisite assumed.",
  "428204 'Seaweed' is a flagged fragment and is not used."
 ]}
