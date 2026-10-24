<!-- fleet job=dialog-infer id=wfarewell-feast-v2 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[9012, 13383, 6, 2516] model=claude-haiku-5-5 -->
# Farewell Feast

{"quest": {"key": "farewell_feast", "title": "Farewell Feast"},
 "offer": {"locale_id": 428199, "speaker": "Diggy"},
 "progress": {"locale_id": 428203, "speaker": "Diggy"},
 "complete": null,
 "other_lines": [
  {"locale_id": 428201, "role": "objective_hint", "speaker": null},
  {"locale_id": 428218, "role": "objective_hint", "speaker": null},
  {"locale_id": 428242, "role": "objective_hint", "speaker": null},
  {"locale_id": 428200, "role": "other", "speaker": null},
  {"locale_id": 428207, "role": "followup", "speaker": "Diggy"},
  {"locale_id": 428202, "role": "followup", "speaker": "Diggy"},
  {"locale_id": 428219, "role": "followup", "speaker": null},
  {"locale_id": 428221, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Title is Farewell Feast (quest_title, Seaside)", "source": "locale:428200"},
  {"claim": "Offer: Diggy, a chef, is asked to cater the pirates' party and asks what they want for dinner", "source": "locale:428199 text; wiki Diggy page lists Quest:[Farewell] [Feast]"},
  {"claim": "Progress: Diggy asks what the scurvy searats want to eat, reminding the talk objective", "source": "locale:428203 text; locale:428218 objective 'Tell Diggy what food the pirates want for the party'"},
  {"claim": "Diggy says he will whip up a sample after being told the food", "source": "locale:428207 text"},
  {"claim": "Deliver objective: give the sample to Jolly Rogers", "source": "locale:428242 text"},
  {"claim": "428202 is Diggy's reply answering the pirates' 'sick of seafood' complaint (428221), so it is a followup, not a verified turn-in closer", "source": "locale:428202 text vs locale:428221 text"},
  {"claim": "Pirate reactions: approve (428219) and reject (428221); speakers not named in text", "source": "locale:428219, locale:428221"},
  {"claim": "Giver Diggy is at Ocean Treasures Cafe, Seaside; quest listed on wiki Diggy page", "source": "npc answer diggy; wiki ns0 Diggy"},
  {"claim": "Jolly Roger NameId 436629 resolves to 'Jolly Roger' (Npcs.json Id=1915 per legacy reference); NPC notes list Jolly Roger in Seaside", "source": "repo seaside.json ~line 23064; notes NPCs - Seaside.md row 61"},
  {"claim": "No reward line found for this quest", "source": "no client line tagged to quest with reward wording"}
 ],
 "confidence": 0.5,
 "open": [
  "No quest record exists; record_id is null and a new record must be created keyed on title 428200.",
  "complete left null: no client line is verified as the turn-in. 428202 answers the reject line 428221 ('sick of seafood'), so it is a retry/reject followup, not a thank-you for a delivered sample. 428219 (approve) is a pirate reaction with no thanks or payment and no named speaker. Needs an approve-branch Diggy closer or a turn-in line to bind.",
  "Pirate speakers for 428219 and 428221 are not named in the text or by any NPC answer; speaker left null although the dialect suggests the pirate crew. Jolly Roger is the deliver target only.",
  "Cooking step not present in client text: chain shown is talk (428218) then deliver (428242). 428207 is a followup, not an objective.",
  "Deliver target: 436629 'Jolly Roger' is the NameId of Jolly Roger (Npcs.json Id 1915 in legacy reference), but the Seaside NPC record's npc_id is not confirmed in current NPC data. Objective text says 'Rogers' while the NPC name is 'Roger'.",
  "Giver npc_id 9000000070 comes from jobs.json and seaside.json reference; quests_given is empty there, so the giver link is wiki/dossier-sourced.",
  "No rewards sourced. The treasure map mentioned in 428202 is not shown to be a reward.",
  "previous/next prerequisite unknown; none assumed.",
  "428204 'Seaweed' is a FLAGged fragment and is not used.",
  "Critique corrections applied: complete removed (was 428202); offer speaker kept as Diggy from the text, with the false npc-answer quest_offer citation dropped (Diggy's npc dialog list has no Farewell Feast offer entry)."
 ]}
