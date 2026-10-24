<!-- fleet job=dialog-infer id=wbag-snatchers-v1 status=done turns=6 usd=0.0035 tokens(read,write,in,out)=[48282, 11185, 14, 3212] model=claude-haiku-5-5 -->
# Bag Snatchers

{"quest": {"key": "bag_snatchers", "title": "Bag Snatchers"},
 "offer": {"locale_id": 415302, "speaker": "Halloween Harry"},
 "progress": null,
 "complete": {"locale_id": 415305, "speaker": "Halloween Harry"},
 "other_lines": [
  {"locale_id": 415304, "role": "objective_hint", "speaker": null},
  {"locale_id": 415384, "role": "objective_hint", "speaker": null}
 ],
 "evidence": [
  {"claim": "Offer line: Harry asks about the missing candy bags and says 'If you can recover the stolen candy bags, I'll make sure you're rewarded.'", "source": "locale:415302 (quest_dialog, Sanctuary, Bag Snatchers)"},
  {"claim": "Complete line: thanks the player and pays out ('here's your reward! Kek!'), with the Greyli ghost remark; no amount or item named", "source": "locale:415305 (quest_dialog, Sanctuary, Bag Snatchers)"},
  {"claim": "Objective text: recover the missing candy bags, Halloween Harry asked for it; not a spoken dialog line", "source": "locale:415304 (quest_objective, Sanctuary, Bag Snatchers)"},
  {"claim": "415384 is an objective-style hint ('Help Halloween Harry recover the missing candy bags.') with no quest tag; used only as an extra hint, placement unverified", "source": "locale:415384"},
  {"claim": "Halloween Harry is the giver: wiki lists Bag Snatchers from Halloween Harry; the NPC answer lists him as giver of Bag Snatchers", "source": "wiki page Halloween Harry / npc answer"},
  {"claim": "NPC answer cited 415944 as Bag Snatchers progress, but 415944 reads 'Return the bags of candy to Halloween Harry in Sanctuary.' which is a return step (Candy Gram), so it is rejected for this quest", "source": "locale:415944"},
  {"claim": "Candy Gram return reminders 415057 and 415961 ('Did you return the candy bags yet?') belong to Candy Gram, not Bag Snatchers, so not used as progress", "source": "locale:415057, locale:415961"}
 ],
 "confidence": 0.6,
 "open": [
  "npc_id not established (the 9500000493 key is reconstructed); left out.",
  "Progress: no client line tagged to Bag Snatchers reminds the player while in progress. The NPC answer's 415304 is the objective text, and 415944 belongs to Candy Gram, so progress is null.",
  "Speaker for offer and complete is inferred: the lines are unnamed in the text, and the quest giver is Halloween Harry. Treated as Harry, not explicitly attributed by the text.",
  "Reward amount and item unknown from client text; 415305 only says 'here's your reward'.",
  "Predecessor unverified: Trick-or-Treat is wiki-listed from Harry, with no client link.",
  "Recovery lines 415835/415836 ('Recover candy bags', search just outside Sanctuary) and 415376/415417/415418 (floating candy, Guard Snapdragon) are not confidently tied to Bag Snatchers and are not used. 415959 ('start your search right down the hill') is also untied.",
  "The NPC answer's place (Pixiewood vs Pixiewood Hills vs Sanctuary) is unresolved; zone kept as Sanctuary per the client tags.",
  "Post-Candy Gram chain (415315, 415319) is outside this quest's next link."
 ]}
