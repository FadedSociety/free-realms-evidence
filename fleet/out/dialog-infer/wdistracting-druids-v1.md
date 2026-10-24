<!-- fleet job=dialog-infer id=wdistracting-druids-v1 status=no_submit turns=5 usd=0.0040 tokens(read,write,in,out)=[46773, 15018, 12, 3376] model=claude-haiku-5-5 -->
# Distracting Druids

```json
{"quest": {"key": "Distracting Druids", "title": "Distracting Druids"},
 "offer": {"locale_id": 413091, "speaker": "Honeydew"},
 "progress": {"locale_id": 413361, "speaker": "Sadie"},
 "complete": {"locale_id": 413094, "speaker": "Sadie"},
 "other_lines": [
  {"locale_id": 413093, "role": "objective_hint", "speaker": null},
  {"locale_id": 413544, "role": "objective_hint", "speaker": null},
  {"locale_id": 413546, "role": "objective_hint", "speaker": null},
  {"locale_id": 413545, "role": "objective_hint", "speaker": null},
  {"locale_id": 413090, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Distracting Druids'", "source": "locale:413092 (quest_title, Pony Vale)"},
  {"claim": "Offer line sends the player to find Sadie near Green Watch; it is tagged to this quest and is the only quest_dialog that explains the task before the objective", "source": "locale:413091 (quest_dialog, Distracting Druids)"},
  {"claim": "Offer speaker is Honeydew, inferred and not stated in the line", "source": "locale:413226 says Honeydew wants you to meet Sadie; Honeydew's NPC dialog list has no other fit"},
  {"claim": "Progress line: Sadie reminds the player to distract Yarith by chatting at Green Watch, which is this quest's distraction step", "source": "locale:413361 (untagged; text names Yarith, Green Watch and distracting the druids; first-person voice matches Sadie's 'Sadie thinks...' in 413091)"},
  {"claim": "Complete line thanks the player for the distraction and reports the Sneezing Unicorns finding, matching the 'Return to Sadie' step", "source": "locale:413094 (quest_dialog, Distracting Druids); objective 413545 'Return to Sadie'"},
  {"claim": "Objective lines for the find, distract, report and return steps", "source": "locale:413093, 413544, 413546, 413545 (all quest_objective, Distracting Druids / Pony Vale)"},
  {"claim": "No reward line exists for this quest", "source": "no client line tagged to the quest contains reward text; the earlier pass also found no reward data"}
 ],
 "confidence": 0.6,
 "open": [
  "The offer speaker is not named in 413091. Honeydew is inferred from the chain and 413226, so the speaker is uncertain. Sadie could also be the speaker.",
  "Progress 413361 has no quest tag. It is included because its text names this quest's distraction step. Treat it as moderate confidence. Sadie is the speaker by text, and no NPC answer attributes it.",
  "No progress line is tagged to this quest. 413544 is quest_objective text and is not a dialog line.",
  "413090 is tagged to this quest, but its text is mostly about Princess Dreamdust and only leads into druids. It is listed as followup with no speaker. It may belong to the Meeting the Princess hand-off.",
  "No reward line was found. rewards is empty.",
  "No quest record exists, so the quest key is the title. live is unsure: the client text exists, but server liveness is not confirmed.",
  "Previous and next links (Meeting the Princess, Allergy Season Already?) are inferred from the chain and wiki, not from a client line that names them."
 ]}
```
