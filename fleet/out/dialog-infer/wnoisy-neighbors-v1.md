<!-- fleet job=dialog-infer id=wnoisy-neighbors-v1 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[14567, 7931, 8, 1959] model=claude-haiku-5-5 -->
# Noisy Neighbors

{"quest": {"key": "Noisy Neighbors", "title": "Noisy Neighbors"},
 "offer": {"locale_id": 36809, "speaker": "Clara Chatterhag"},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 36811, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "36809 is the quest's offer line: Clara complains about the music and tells the player to get Flynn to turn down the volume or she will complain to the Mayor. Full text confirmed via locale lookup.", "source": "locale:36809 (quest_dialog, Snowhill, Noisy Neighbors); npc answer for Clara Chatterhag lists 36809 as quest_offer"},
  {"claim": "Clara Chatterhag is the giver and the speaker of the offer line.", "source": "locale:36808 name; npc answer clara chatterhag quests_given=Noisy Neighbors; wiki Quest:Noisy Neighbors To Start"},
  {"claim": "36811 is the quest's objective text, tagged to Noisy Neighbors: talk to Flynn about Bruce's noise level. It is an objective, not spoken dialog, so no speaker is assigned; the Clara attribution in the npc answer is not a spoken-line attribution.", "source": "locale:36811 (quest_objective, Snowhill, Noisy Neighbors)"},
  {"claim": "36818, 36837 and 36816 are Noise Permit lines (Flynn), not this quest's lines, and were excluded.", "source": "locale:36818 / 36837 / 36816 tags = Noise Permit"}
 ],
 "confidence": 0.7,
 "open": [
  "No client-tagged progress line exists for Noisy Neighbors. Progress is null; the Flynn lines in the pack belong to Noise Permit.",
  "No client-tagged completion line exists for Noisy Neighbors. Complete is null.",
  "Reward is unconfirmed (wiki says 30 coins only); no reward line included.",
  "Objective 1 'Speak with Clara Chatterhag' has no client-tagged text (text_locale_id null); it rests on the wiki To Start section only.",
  "Clara's npc_id and Flynn's npc_id are unresolved; the repo snowhill.json keys are reconstructed and do not reconcile with locale 36808.",
  "No quest record exists; record_id must be created by the builder.",
  "previous is empty because no predecessor was found, not because none exists."
 ]}
