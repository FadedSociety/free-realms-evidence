<!-- fleet job=dialog-infer id=wmedic-so-you-want-to-be-a-medic-v1 status=no_submit turns=3 usd=0.0035 tokens(read,write,in,out)=[17647, 11183, 8, 3865] model=claude-haiku-5-5 -->
# So You Want to be a Medic?

```json
{"quest": {"key": "So You Want to be a Medic?", "title": "So You Want to be a Medic?"},
 "offer": {"locale_id": 23054, "speaker": null},
 "progress": null,
 "complete": {"locale_id": 24259, "speaker": "Nurse Naia"},
 "other_lines": [
  {"locale_id": 23049, "role": "other", "speaker": null},
  {"locale_id": 23051, "role": "objective_hint", "speaker": null},
  {"locale_id": 23055, "role": "objective_hint", "speaker": null},
  {"locale_id": 23052, "role": "objective_hint", "speaker": null},
  {"locale_id": 23080, "role": "objective_hint", "speaker": null},
  {"locale_id": 23086, "role": "objective_hint", "speaker": null},
  {"locale_id": 23057, "role": "followup", "speaker": null},
  {"locale_id": 23063, "role": "followup", "speaker": null},
  {"locale_id": 23069, "role": "followup", "speaker": null},
  {"locale_id": 23061, "role": "followup", "speaker": null},
  {"locale_id": 23067, "role": "followup", "speaker": null},
  {"locale_id": 23073, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'So You Want to be a Medic?'", "source": "locale:23048"},
  {"claim": "Giver is Nurse Naia (npc 7611 name)", "source": "locale:7611; prior answer giver npc_id 9000000161"},
  {"claim": "Offer text: 'I understand you have come for training to become a medic?... Nurse Naia has a test for you'", "source": "locale:23054"},
  {"claim": "Objective: take Nurse Naia's test (talk step)", "source": "locale:23051, 23055"},
  {"claim": "Completion line: player has shown Nurse Naia they have what it takes to be a great medic", "source": "locale:24259; Naia NPC dialog list attributes 24259 to this quest"},
  {"claim": "23069 is the mid-quiz line asking question three, not a progress reminder", "source": "locale:23069 text"},
  {"claim": "Quiz question and fail lines exist but are not progress/complete slots", "source": "locale:23057, 23063, 23061, 23067, 23073"},
  {"claim": "No reward line is recovered for this quest", "source": "locale search: no quest_reward line tagged to this quest; prior answer rewards empty"}
 ],
 "confidence": 0.5,
 "open": [
  "Offer speaker left null: 23054 is third-person ('Nurse Naia has a test for you') and no NPC answer attributes it to Naia. Naia is the record giver, so 'Nurse Naia' is plausible but unconfirmed. Candidate 73603 ('Step right on over to begin your test... Nurse Naia will be issuing the test!') is attributed to Naia as quest_offer by the NPC answer, but its text reads as narration; it was not chosen.",
  "Progress set to null, not 23069 as the earlier pass had it. 23069 asks question three in the quiz and does not remind the player of the task. No reminder line is tagged to this quest with a speaker; 23055 ('Talk to Nurse Naia when you are ready') is an objective string and was put in other_lines as objective_hint. 384185 and 387980/387981 are quest-progress lines from Naia's list but belong to other objectives or to Become a Medic.",
  "Complete 24259 is a narration sentence ('#Cap(player) has shown Nurse Naia...') rather than a spoken thank-you. Speaker 'Nurse Naia' comes from the NPC answer's dialog list. No payout line exists.",
  "Rewards are unknown; no reward line is tagged to this quest, so the reward slot is empty. The 5 coins / 15 XP in the repo are an unsourced fallback.",
  "Quiz answers and scoring are not recovered. The server models only the talk step. 23057 (Q1) and 23063 (Q2) speaker is not attributed; they were listed as followup without speaker.",
  "Chain order is unresolved (wiki lists Operation: Revival before House Call; repo notes conflict). Not verified here.",
  "Locale 23056 says Doctor Gordon informed Naia. Gordon is not the giver.",
  "Pass/fail lines 23061 and 23073 were verified as quest-tagged text. They are retry/fail lines, not progress or complete lines."
 ]}
```
