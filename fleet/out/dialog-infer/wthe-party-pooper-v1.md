<!-- fleet job=dialog-infer id=wthe-party-pooper-v1 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[14993, 8565, 8, 2800] model=claude-haiku-5-5 -->
# The Party Pooper

{"quest": {"key": "the_party_pooper", "title": "The Party Pooper"},
 "offer": {"locale_id": 385596, "speaker": null},
 "progress": {"locale_id": 385599, "speaker": null},
 "complete": null,
 "other_lines": [
  {"locale_id": 385598, "role": "objective_hint", "speaker": null},
  {"locale_id": 385601, "role": "objective_hint", "speaker": null},
  {"locale_id": 385602, "role": "objective_hint", "speaker": null},
  {"locale_id": 385603, "role": "objective_hint", "speaker": null},
  {"locale_id": 385629, "role": "followup", "speaker": null},
  {"locale_id": 385637, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'The Party Pooper'", "source": "locale:385597 (quest_title, Merry Vale)"},
  {"claim": "Offer text: a Merry Vale resident says a chugawug in the east camp is ruining the atmosphere and asks the player to bring cotton candy to cheer him up", "source": "locale:385596 (tagged hint Wugunbump; no speaker named in text)"},
  {"claim": "Progress/reaction text: 'Keep that stuff away from me! Sugar makes me feel so gross!' is the chugawug's refusal of the candy, so it fits an in-progress state rather than an offer or completion", "source": "locale:385599 (tagged to The Party Pooper; speaker not named in text or NPC answers)"},
  {"claim": "Objectives: cheer up Wugunbump at the Chugawug camp; speak to Wugunbump; use cotton candy on him", "source": "locale:385601, 385602, 385603 (and summary 385598)"},
  {"claim": "Wugunbump is a Merry Vale chugawug NPC and this quest is in his appearance list", "source": "wiki page Wugunbump; npc answer dialog 385601"},
  {"claim": "Followup lines 'Talk to the mayor if you hand it all out' and 'check on Wugunbump' are tagged to this quest but name no speaker", "source": "locale:385629, locale:385637"}
 ],
 "confidence": 0.5,
 "open": [
  "Giver/offer speaker unresolved: 385596 does not name its speaker and its tag hint 'Wugunbump' is the subject, not the speaker. Mayor McFairy is wiki-only, so speaker is null.",
  "Progress 385599 is a reaction to being offered candy, not a reminder. It is tagged to this quest, but its speaker is not named, so speaker is null. Treat as weak.",
  "Complete line not found in the client; complete is null. Reward not searched; other_lines has no reward entry.",
  "Wugunbump's NPC name id not verified (40344 is flagged as a fragment), so no npc_id or target_locale_id.",
  "Cotton candy item id is not in the client text; the 'use' objective cannot be wired.",
  "385596 says 'east camp' while 385601 says 'Chugawug camp'; not reconciled.",
  "Successor not confirmed. 385570 (speak to the Mayor) was not included as a followup because it refers to 'spreading cheer to everyone', which does not clearly tie to this quest alone. next is left empty.",
  "Wugunbump's dialog lines 19417-19420 and 74198-74285 belong to other quests (Suspicious Serenity, Lugunwump, Rainbow) and are not used here."
 ]}
