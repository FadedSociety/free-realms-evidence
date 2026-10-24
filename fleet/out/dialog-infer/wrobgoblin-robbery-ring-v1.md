<!-- fleet job=dialog-infer id=wrobgoblin-robbery-ring-v1 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[28479, 11358, 10, 2898] model=claude-haiku-5-5 -->
# The Great Robgoblin Robbery Ring

{"quest": {"key": "the_great_robgoblin_robbery_ring", "title": "The Great Robgoblin Robbery Ring"},
 "offer": {"locale_id": 420286, "speaker": "Candi Ivy"},
 "progress": null,
 "complete": {"locale_id": 420290, "speaker": "Candi Ivy"},
 "other_lines": [
  {"locale_id": 420287, "role": "objective_hint", "speaker": null},
  {"locale_id": 420289, "role": "objective_hint", "speaker": null},
  {"locale_id": 420536, "role": "followup", "speaker": null}
 ],
 "evidence": [
  {"claim": "Quest title is locale 420288 'The Great Robgoblin Robbery Ring'", "source": "locale:420288 (quest_title, Snowhill)"},
  {"claim": "Offer line: Candi says the robgoblins are making snowmen to steal presents", "source": "locale:420286 (quest_dialog, tagged to this quest); Candi Ivy is the giver per the earlier answer and candi ivy NPC answer lists the quest"},
  {"claim": "Complete line: thanks the player for slowing snowman production", "source": "locale:420290 (quest_dialog, tagged to this quest, text is thanks/payoff)"},
  {"claim": "Objective text for the robgoblin camp/destroy supplies task", "source": "locale:420287, 420289 (quest_objective); locale:420607 'Head into the robgoblin camp and destroy their snowman making supplies!' and 420602 'Robgoblin Robbery Ring' (camp objective title)"},
  {"claim": "420536 is a reminder to the player to tell Candi, so it is an objective line, not Candi's speech", "source": "locale:420536 ('Let Candi Ivy know that the robgoblins are building evil snowmen...'); the NPC answer labelled it quest_progress but the text is addressed to the player"},
  {"claim": "Excluded 420983 and 420282", "source": "420983 is tagged to 'Bye-Bye Supplies!'; 420282 is tagged to Guarding the Gifting Tree"}
 ],
 "confidence": 0.6,
 "open": [
  "No client line is a true progress reminder from Candi for this quest; progress left null. The candi ivy NPC answer's progress entry 420536 is an objective instruction, not dialog.",
  "Offer 420286 and complete 420290 are tagged to this quest, but no NPC answer attributes them to Candi by id; speaker Candi Ivy is inferred from the quest giver and the text. Confirm in game.",
  "Title split: offer/complete/fight text uses 420288, camp objectives use 420602 'Robgoblin Robbery Ring'. Treated as one quest; confirm which title Candi offers.",
  "Reward: the Subarctic Winterwear Hat is supported only by wiki text. Its name id 134504 did not resolve in locale, so no reward locale line is given.",
  "Objective 420603 ('Head into the robgoblin camp...') and 420605 ('Knock out some robgoblin troublemakers...') were in the earlier answer but not confirmed as tagged client lines here; counts and order unknown.",
  "Previous quest 'The Perfect Disguise' (locale 420284) is not this quest's line and was not used for dialog. Candi Ivy npc_id not found."
 ]}
