<!-- fleet job=dialog-infer id=wa-dark-future-v2 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[19496, 10574, 8, 2617] model=claude-haiku-5-5 -->
# A Dark Future

{"quest": {"key": "A Dark Future", "title": "A Dark Future"},
 "offer": {"locale_id": 432194, "speaker": "Madam Zelda"},
 "progress": {"locale_id": 432199, "speaker": null},
 "complete": {"locale_id": 432197, "speaker": "Madam Zelda"},
 "other_lines": [
  {"locale_id": 432195, "role": "other", "speaker": null},
  {"locale_id": 432196, "role": "objective_hint", "speaker": null},
  {"locale_id": 432200, "role": "objective_hint", "speaker": null},
  {"locale_id": 432202, "role": "objective_hint", "speaker": null},
  {"locale_id": 432181, "role": "objective_hint", "speaker": null},
  {"locale_id": 432176, "role": "followup", "speaker": null},
  {"locale_id": 432201, "role": "other", "speaker": null},
  {"locale_id": 432204, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer is Zelda's quest-offer line; text says she will tell how to avoid disaster if the player brings gassy water", "source": "locale:432194 / npc answer (Madam Zelda, quest_offer, A Dark Future) / video:yWuHe_jYyc4/00188.jpg"},
  {"claim": "Quest title is A Dark Future", "source": "locale:432195 (quest_title)"},
  {"claim": "Progress reminder: 'Madam Zelda claims... Bring her some gassy water'. Third-person text, so speaker not attributed by text or NPC answer", "source": "locale:432199 (quest_dialog, tagged A Dark Future)"},
  {"claim": "Complete line is a first-person reaction to receiving the water ('My throat's been rather dry... *BURP* Ooh, swamp gas!'); it is the receiver's reply in Zelda's quest flow, so speaker set to Madam Zelda. The text does not print her name, so this is an inference from the quest flow", "source": "locale:432197 (quest_dialog, tagged A Dark Future); locale:432194 offer ('bring me some gassy water')"},
  {"claim": "Objective 1: Find Gassy Water, target item Gassy Water, count 5", "source": "locale:432200, 432181; video:yWuHe_jYyc4/00194.jpg tracker reads 'Find Gassy Water - 0/5'"},
  {"claim": "Objective 2: Return to Madam Zelda", "source": "locale:432202 (quest_objective)"},
  {"claim": "No reward text is tagged to this quest; 432197 is the only completion line and pays nothing", "source": "locale tag search"}
 ],
 "confidence": 0.7,
 "open": [
  "Progress speaker left null: 432199 is third-person ('Madam Zelda claims...') and no NPC answer attributes it. The Zelda NPC answer lists 432202 as quest_progress, but 432202 is tagged quest_objective in the client, so it is not used as dialog. 432199 is the only quest_dialog reminder tagged to this quest.",
  "Complete speaker set to Madam Zelda by quest-flow inference, not by a printed name or an NPC answer. Builder should confirm if strict attribution is required.",
  "Objective count corrected to 5 per the video tracker frame (the earlier 'one delivery implied' note is wrong).",
  "Reward: none found in client text.",
  "Previous: unknown. 432176 (Bone Bog Cemetery lead-in) is tagged to this quest but its source quest is unidentified, so it is listed as followup, not previous.",
  "Next: Being Prepared (Team Vampire / Werewolf) per the repo notes; the wiki claim that A Dark Future directly unlocks First Bite could not be rechecked. Being Prepared's previous field is unverified.",
  "No quest record ID found; npc_id for Madam Zelda is unverified (locale 439704 not checked).",
  "432201 and 432204 are tagged to this quest but have no clear speaker; kept as other with speaker null."
 ]
}
