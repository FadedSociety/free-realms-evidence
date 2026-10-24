<!-- fleet job=dialog-infer id=wstoke-the-flames-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[9941, 11171, 6, 2029] model=claude-haiku-5-5 -->
# Stoke the Flames

{"quest": {"key": "Stoke the Flames", "title": "Stoke the Flames"},
 "offer": {"locale_id": 72077, "speaker": "Babbina"},
 "progress": {"locale_id": 72079, "speaker": "Babbina"},
 "complete": null,
 "other_lines": [
  {"locale_id": 72078, "role": "other", "speaker": null},
  {"locale_id": 72080, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "72077 is the quest offer: it asks the player to stoke the flames, take the path east and follow it to Gorg's camp", "source": "locale:72077 full text (quest_dialog, hint Stoke the Flames); npc answer babbina dialog kind quest_offer"},
  {"claim": "72077 is spoken by Babbina", "source": "npc answer babbina (quest_offer for Stoke the Flames); giver NameId 73994 'Babbina' per previous pass, not re-verified in this pass"},
  {"claim": "72079 is a reminder of the task, spoken by Babbina, so it serves as the progress line", "source": "npc answer babbina lists 72079 as quest_progress for Stoke the Flames; text 'Babbina would like you to throw coals on the braziers along the path, leading to Gorg's camp.' (quest_objective tag, hint Stoke the Flames) is also the objective text"},
  {"claim": "72078 is the quest title", "source": "locale:72078 quest_title, hint Stoke the Flames"},
  {"claim": "72080 is not a clean completion line: it does not thank or pay, and it refers to Babbina in the third person, so its speaker is not Babbina (likely Gorg, unconfirmed)", "source": "locale:72080 full text; npc answer labels it 'other'"},
  {"claim": "No reward line exists for this quest", "source": "no reward text found in client or wiki lookup for Stoke the Flames"}
 ],
 "confidence": 0.5,
 "open": [
  "Liveness unconfirmed: nothing in the pack shows this quest shipped.",
  "Complete left null: no thank-you or payment line tagged to this quest was found. 72080 is a post-completion-style remark but does not thank or pay, and its speaker is not Babbina; binding it as complete would be a guess.",
  "Progress uses 72079, which is tagged quest_objective; it is bound as progress only because the Babbina NPC answer attributes it as quest_progress. The same text is the objective, so the objective slot should be treated as the same line.",
  "Speaker of 72077 rests on the NPC greeting binding and NameId 73994; NPC id 9500000089 is a reconstructed key and was not verified against the briarwood source.",
  "Brazier lines 74569-74584 are unlinked to this quest by any hint and are excluded.",
  "Locale 72140 is a route description, not quest dialog, and is excluded.",
  "previous/next quest-line placement is unproven and left empty; record_id unknown."
 ]
}
