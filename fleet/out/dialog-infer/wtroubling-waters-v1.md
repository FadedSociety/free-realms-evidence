<!-- fleet job=dialog-infer id=wtroubling-waters-v1 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5853, 7579, 6, 1919] model=claude-haiku-5-5 -->
# Troubled Waters

{"quest": {"key": "Troubled Waters (Seaside, Heroes Journal: The Seaside Gloam Invasion)", "title": "Troubled Waters"},
 "offer": null,
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 5101819, "role": "other", "speaker": null},
  {"locale_id": 5101820, "role": "other", "speaker": null},
  {"locale_id": 5101821, "role": "objective_hint", "speaker": null},
  {"locale_id": 5101824, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Troubled Waters' (Seaside).", "source": "locale:5101823 (quest_title, Seaside, Troubled Waters)"},
  {"claim": "Objective text is 'Escape the caverns!'.", "source": "locale:5101821 (quest_objective, Seaside, Troubled Waters)"},
  {"claim": "Two in-quest lines address Ty (flooding caverns, fight way out); they are tagged to this quest but name no speaker and are not tied to an NPC or dialog slot.", "source": "locale:5101819, locale:5101820"},
  {"claim": "Line 5101824 reports the Cray freed from Gloam control and peace restored; it reads like a closing line but no client link ties it to a completion event or speaker.", "source": "locale:5101824"},
  {"claim": "Chapter membership and neighbouring quests (Tides of Change next) come from the wiki chapter list only.", "source": "wiki: Heroes Journal: The Seaside Gloam Invasion"},
  {"claim": "Wiki gives Mayor Gilly and Captain Sunspark as candidate givers; neither is confirmed as this quest's giver.", "source": "wiki: Mayor Gilly Appearances; Quests list (prior answer)"},
  {"claim": "No rewards found.", "source": "prior pass; no reward line tagged to quest 5101823 in client search"}
 ],
 "confidence": 0.25,
 "open": [
  "Offer, progress and complete slots left null: no client line is tied to a dialog slot for this quest, and none of the tagged lines names its speaker (rule: null without an attributed speaker).",
  "Candidate roles only: 5101819/5101820 read as in-progress or situational lines addressed to Ty; 5101824 reads as a closing/complete line. These are unverified and should not be wired without a client NPC-quest link.",
  "Giver unresolved (Captain Sunspark vs Mayor Gilly); no quest record id, so no record link.",
  "Predecessor unknown; Tides of Change as next step rests on wiki chapter order only.",
  "Objective target and count not sourced.",
  "Live status unsure; do not wire until a client record or NPC-quest link is found."
 ]}
