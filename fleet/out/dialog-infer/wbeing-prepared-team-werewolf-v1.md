<!-- fleet job=dialog-infer id=wbeing-prepared-team-werewolf-v1 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[15820, 9718, 8, 2574] model=claude-haiku-5-5 -->
# Catch a chicken for Lon

{"quest": {"key": "catch_a_chicken_for_lon", "title": "Catch a chicken for Lon"},
 "offer": {"locale_id": 432260, "speaker": null},
 "progress": {"locale_id": 432262, "speaker": "Lon Blackforest"},
 "complete": null,
 "other_lines": [
  {"locale_id": 432266, "role": "other", "speaker": null},
  {"locale_id": 432268, "role": "objective_hint", "speaker": "Lon Blackforest"},
  {"locale_id": 432263, "role": "other", "speaker": null},
  {"locale_id": 432265, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is 'Catch a chicken for Lon' (quest_title, Blackspore).", "source": "locale:432266"},
  {"claim": "Objective 'Speak to Lon Blackforest' is a quest_objective tagged to this quest.", "source": "locale:432268"},
  {"claim": "Offer text explains the task: gain werewolves' trust, approach Lon, catch the chicken fleeing south and bring it as a meal offering.", "source": "locale:432260 (full text checked)"},
  {"claim": "Reminder text tells the player to find the stray chicken and give it to Lon Blackforest to feed on; the Lon Blackforest NPC answer attributes 432262 to this quest.", "source": "locale:432262 (full text checked); npc answer lon blackforest"},
  {"claim": "Lon Blackforest is the npc_name 432270 and the NPC answer attributes 432268 to him.", "source": "locale:432270; npc answer lon blackforest"},
  {"claim": "Madam Zelda is the quest giver per the earlier answer (npc_name 432157), but no dialog line of hers is attributed to 432260 by any source, so the offer speaker is left null.", "source": "npc answer madam zelda (432260 not listed); locale:432157"},
  {"claim": "432263 and 432265 are quest-tagged banter with no named speaker, so they are not assigned to any NPC.", "source": "locale:432263, locale:432265"},
  {"claim": "No reward line and no complete line exist in the tagged cluster; 432286 and 432296 belong to Howl of Warning and Dance-off.", "source": "locale:432286, locale:432296 (different quests)"}
 ],
 "confidence": 0.4,
 "open": [
  "Offer speaker is null: the text 432260 does not name its speaker and the Madam Zelda NPC answer does not attribute it. Zelda is only the giver per the earlier answer, which is not dialog attribution.",
  "Progress 432262 is assigned to Lon Blackforest from the NPC answer; the earlier answer had progress null. This is a judgment that a reminder fits progress.",
  "No complete line or reward line was found for this quest. Complete is left null, and no reward is given.",
  "Quest title identity is content-matched (wiki '(Team Werewolf) Being Prepared' is not in the client). The earlier answer's line and previous/next chain are unverified.",
  "npc_id is unresolved: two Madam Zelda npc_name rows exist (432157, 439704), and no source ties either one to the offer.",
  "432263 and 432265 are unattributed banter and are not used as progress or complete.",
  "The chicken collect has no separate locale id; the count of 1 is inferred from the text."
 ]}
