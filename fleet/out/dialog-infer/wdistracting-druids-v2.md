<!-- fleet job=dialog-infer id=wdistracting-druids-v2 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[22972, 12783, 8, 2195] model=claude-haiku-5-5 -->
# Distracting Druids

{"quest": {"key": "Distracting Druids", "title": "Distracting Druids"},
 "offer": {"locale_id": 413091, "speaker": "Honeydew"},
 "progress": null,
 "complete": {"locale_id": 413094, "speaker": "Sadie"},
 "other_lines": [
  {"locale_id": 413093, "role": "objective_hint", "speaker": null},
  {"locale_id": 413544, "role": "objective_hint", "speaker": null},
  {"locale_id": 413546, "role": "objective_hint", "speaker": null},
  {"locale_id": 413545, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is Distracting Druids", "source": "locale:413092 (quest_title, Pony Vale)"},
  {"claim": "Offer line is tagged to this quest and tells the player to find Sadie near Green Watch; it does not name its speaker", "source": "locale:413091 (quest_dialog, Distracting Druids)"},
  {"claim": "Honeydew is the giver: 'Honeydew wants you to meet her friend Sadie... near Green Watch, west of Skysong Ledge'", "source": "locale:413226 (untagged text) plus npc answer for Honeydew (giver 4028, locale:413059)"},
  {"claim": "Complete line is tagged to this quest, is Sadie's voice, thanks the player for the distraction and reacts to Sneezing Unicorns", "source": "locale:413094 (quest_dialog, Distracting Druids)"},
  {"claim": "Find, distract, report and return objectives", "source": "locale:413093, 413544, 413546, 413545 (quest_objective, Distracting Druids)"},
  {"claim": "No reward line exists for this quest", "source": "no tagged client line contains reward text; no reward data in wiki or repo"}
 ],
 "confidence": 0.6,
 "open": [
  "progress left null. Candidate 413361 ('I said distract the druids, not distract me! Just head into Green Watch and start chatting with the one named Yarith...') matches this quest's distraction step and is Sadie's voice, but its client hint is 'Pony Vale investigation', not Distracting Druids, and no NPC answer or quest record ties it to this quest. Excluded per the tag rule; a builder can add it if another source confirms it.",
  "Offer speaker Honeydew is inferred from 413226, not stated in 413091 (which refers to Sadie in the third person). Sadie as speaker is ruled out by the line's own wording.",
  "413090 is tagged to this quest but its text is about Princess Dreamdust; it is dropped from other_lines rather than guessed as a followup.",
  "No quest record exists, so key is the title. live is unsure: client text exists, server liveness is unconfirmed.",
  "Previous link Meeting the Princess and next link Allergy Season Already? are inferred from the wiki chain and from 413087/413226/413234, not named by a client line.",
  "No reward line found; rewards empty."
 ]}
