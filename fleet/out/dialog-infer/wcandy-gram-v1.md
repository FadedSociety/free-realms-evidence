<!-- fleet job=dialog-infer id=wcandy-gram-v1 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[17279, 9771, 8, 2335] model=claude-haiku-5-5 -->
# Candy Gram

{"quest": {"key": "candy_gram", "title": "Candy Gram"},
 "offer": {"locale_id": 415310, "speaker": "Halloween Harry"},
 "progress": null,
 "complete": {"locale_id": 415313, "speaker": "Halloween Harry"},
 "other_lines": [
  {"locale_id": 415312, "role": "objective_hint", "speaker": null},
  {"locale_id": 415311, "role": "other", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer line 415310 asks the player to deliver the candy to the kids ('In the spirit of Halloween, can you deliver the candy to them?'), so it is the offer, not progress.", "source": "locale:415310 (quest_dialog, Sanctuary, Candy Gram)"},
  {"claim": "Complete line 415313 thanks the player ('Welcome back... The kids of Sanctuary think you're a hero!') and then leads into A Formal Report (Bella's brother missing).", "source": "locale:415313 (quest_dialog, Sanctuary, Candy Gram); next quest 415314-415316"},
  {"claim": "Objective text is 'Halloween Harry has asked you to return the bags of candy to the kids of Sanctuary.'", "source": "locale:415312 (quest_objective, Candy Gram)"},
  {"claim": "Quest title is 'Candy Gram'.", "source": "locale:415311"},
  {"claim": "Halloween Harry is the giver and lists Candy Gram among his quests.", "source": "npc answer: halloween harry quests_given; wiki Halloween Harry page"},
  {"claim": "Previous quest is Bag Snatchers (415302-415305); its completion line 415305 is Greyli-related and is not a Candy Gram line.", "source": "locale:415302-415305 tagged Bag Snatchers"}
 ],
 "confidence": 0.7,
 "open": [
  "Speaker for 415310 and 415313 is attributed to Halloween Harry on the basis of the quest giver and the Harry-style 'Kek' voice; no NPC answer directly attributed these two lines to him. Treat as likely, not confirmed.",
  "No progress line found: no client line is tagged Candy Gram as a mid-quest reminder, so progress is null.",
  "No reward text found (no coins, items or xp) in the pack; reward is null.",
  "Zone conflict: wiki places Halloween Harry's quests in Pixiewood Hills; client tags and repo say Sanctuary. Sanctuary kept per client tags.",
  "415386 and 415974 ('Let the general know Bella's brother has gone missing') and 415979 belong to the follow-on A Formal Report, not this quest; excluded from other_lines.",
  "415314-415316 belong to A Formal Report (next in chain), excluded from this quest's lines.",
  "No bag count or number of kids is given in the client text."
 ]}
