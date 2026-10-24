<!-- fleet job=dialog-infer id=wpotent-love-potion-v1 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[16681, 9864, 8, 2497] model=claude-haiku-5-5 -->
# Potent Love Potion

{"quest": {"key": "Potent Love Potion", "title": "Potent Love Potion"},
 "offer": {"locale_id": 427152, "speaker": null},
 "progress": null,
 "complete": null,
 "other_lines": [
  {"locale_id": 427154, "role": "objective_hint", "speaker": null},
  {"locale_id": 427155, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "427153 is the quest title 'Potent Love Potion', tagged Merry Vale / Potent Love Potion", "source": "locale:427153"},
  {"claim": "427152 is a quest_dialog tagged to this quest that explains the stakes and points at Cudip's potion, which fits an offer-style explanation", "source": "locale:427152"},
  {"claim": "427154 is the quest objective for this quest (heart flower restoration)", "source": "locale:427154"},
  {"claim": "427155 is a quest_dialog tagged to this quest about softening Stone Heart, which matches the next quest Softening the Stone (427157)", "source": "locale:427155"},
  {"claim": "Potent Love Potion is listed as given by Cudip on the wiki Festival of Hearts page; Yvelle's NPC answer also lists it under quests_given", "source": "wiki Festival of Hearts / npc answer talespinner yvelle"},
  {"claim": "427163 is tagged Sleeping Pixie, not this quest, so it is excluded as a completion line", "source": "locale:427163 tag"},
  {"claim": "427457 is tagged Merry Vale Heartbreaker, not this quest; excluded from other_lines", "source": "locale:427457 tag"}
 ],
 "confidence": 0.3,
 "open": [
  "Speaker is null for every slot: no client line or NPC answer names who says 427152 or 427155. 427152 refers to Cudip in the third person, so the speaker is not Cudip by its own text; Yvelle's attribution is only for the separate A Tale of Two Hearts line set.",
  "Giver conflict: wiki Festival page says Cudip gives this quest; the earlier pass said Yvelle (repo NPC row, wiki-supported only by a Festival-page line for another quest). Giver is unresolved, so no speaker is assigned.",
  "No complete line: no client line tagged to this quest thanks or pays the player. 427163 (Splendid job...) is tagged Sleeping Pixie and is excluded. No reward line exists for this quest (427179 is Mending Hearts).",
  "No progress line: no client line reminds the player of the fruit or flower task for this quest. The only reminder-like text is 427457, tagged Heartbreaker, which is excluded.",
  "The offer slot (427152) is a best fit by content, not confirmed by a quest record, so the mapping is low confidence.",
  "Previous-quest order is unsettled (Where is the Love? vs A Tale of Two Hearts). A Tale of Two Hearts has no answer record here.",
  "Objective 427457 (red/pink fruit, Gummyfruit Plants) is wiki-only for this quest and has no locale id tied to Potent Love Potion; excluded.",
  "No quest record_id, so no slot can be confirmed against a server-side quest definition."
 ]}
