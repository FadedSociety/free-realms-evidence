<!-- fleet job=dialog-infer id=whorrible-hiccups-v1 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[13800, 7913, 8, 2217] model=claude-haiku-5-5 -->
# Horrible Hiccups

{"quest": {"key": "Horrible Hiccups", "title": "Horrible Hiccups"},
 "offer": {"locale_id": 389236, "speaker": "Slinky"},
 "progress": {"locale_id": 390983, "speaker": "Slinky"},
 "complete": null,
 "other_lines": [
  {"locale_id": 390973, "role": "objective_hint", "speaker": null},
  {"locale_id": 101397, "role": "objective_hint", "speaker": null},
  {"locale_id": 101398, "role": "objective_hint", "speaker": null},
  {"locale_id": 389284, "role": "followup", "speaker": null},
  {"locale_id": 389239, "role": "followup", "speaker": "Cutes Dozen"}
 ],
 "evidence": [
  {"claim": "Offer is Slinky's pitch: find Cutes Dozen and scare the hiccups out of her", "source": "locale:389236 text; npc answer slinky lists 389236 as quest_offer for Horrible Hiccups"},
  {"claim": "Progress reminder from Slinky asking whether Cutes has been scared yet", "source": "locale:390983 text; npc answer slinky lists it as quest_progress for Horrible Hiccups"},
  {"claim": "Objective text 'Scare Cutes Dozen to cure her of the hiccups'", "source": "locale:390973; objective titles 101397 'Try to Scare Cutes Dozen' and 101398 'Scare Cutes Dozen to Cure her Hiccups' tagged to the quest title"},
  {"claim": "389284 describes the monster illusion and says to talk to Slinky again if it wears off; it is a status note, not spoken dialog, so it is not used as progress", "source": "locale:389284 text"},
  {"claim": "389239 is Cutes Dozen's scare reaction (she is not hiccupping and blames Slinky); it is a followup, not the completion line", "source": "locale:389239 text; npc answer cutes dozen lists it as quest_progress for Horrible Hiccups"},
  {"claim": "Quest title", "source": "locale:101396 'Horrible Hiccups'"},
  {"claim": "Giver and Cutes Dozen names", "source": "locale:45553 'Slinky', locale:45787 'Cutes Dozen'"}
 ],
 "confidence": 0.5,
 "open": [
  "Complete line not identified in the client: no completion/thank-you string tagged to this quest, so complete is null. 389239 is a scare reaction and is not treated as completion.",
  "Reward (10 coins, Orange-Strapped Flip-Flops) is wiki-only and has no client line; no reward slot is filled.",
  "Live status unsure; the wiki membership gate is unverified.",
  "Previous quest unverified (wiki blank); line placement is 'next: Scaredy Pants' only.",
  "389284 is the illusion status note; it is kept as a followup, not as progress dialog.",
  "npc_id values for Slinky and Cutes Dozen are not available in the pack; no quest record id exists.",
  "'Return to Slinky' (390975) was not re-verified and is omitted."
 ]}
