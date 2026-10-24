<!-- fleet job=event-infer id=vcontest-start-announcement-v5 status=done turns=4 usd=0.0033 tokens(read,write,in,out)=[26702, 10557, 10, 3440] model=claude-haiku-5-5 -->
# Contest start announcement

{
 "event": {
   "name": "Vampires vs. Werewolves dance contest (Spooktacular season)",
   "aliases": ["Vampires vs Werewolves Dance-off", "Vampire vs Werewolf dance contest", "Concurso de baile Vampiros vs Hombres Lobos", "Dance Off for the Pumpkin Prince", "Contest start announcement (the in-game trigger, not a separate event)"]
 },
 "kind": "contest",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [
   "Bone Marsh outskirts (article 1866: contest held on the outskirts of Bone Marsh, per lookup summary)",
   "Boneyard cemetery area, Blackspore (article 1878, 'Boneyard cemetery, just north of the Haunted Mines')",
   "Bone Bog Cemetery (article 1857: contest near Bone Bog Cemetery)"
 ],
 "npcs": ["Pumpkin Prince (article 1857, 1867 judges the contest)", "Madame Zelda (article 1878: starts the side-choice quest at Black Spore; article 1866 quest giver per pack summary)"],
 "quests": [],
 "activities": [
   "Finish the side-choice mission from Madame Zelda (article 1866)",
   "Go to the contest area when the in-game announcement says the dance contest is about to begin (article 1866, 1867)",
   "Wear vampire or werewolf costume pieces to join a side (articles 1866, 1867, 1857)",
   "Dance for your side; the Pumpkin Prince judges (article 1867, 1878)"
 ],
 "items": [],
 "rewards": [
   "A piece of the Pumpkin Prince's (King's) special cake for the side with the most supporters (article 1867)",
   "Scariest monster title for the side with the scariest dance (article 1878)"
 ],
 "evidence": [
   {"claim": "Once the mission is complete, players go to Bone Marsh when an in-game announcement says the dance contest is about to begin, and wear vampire or werewolf costume pieces. No date is given.", "source": "http://www.freerealms.com/article/detail.action?articleId=1866"},
   {"claim": "The announcement trigger ('the dance contest is about to begin') is repeated in the same terms.", "source": "http://www.freerealms.com/article/detail.action?articleId=1867"},
   {"claim": "Vampire and werewolf sides compete in a dance contest during the Spooktacular season; the side with the most supporters gets a piece of the Pumpkin King's special cake.", "source": "http://www.freerealms.com/article/detail.action?articleId=1866 (summary) and 1867 (summary)"},
   {"claim": "Werewolves and vampires compete in a dance contest for the Pumpkin Prince near Bone Bog Cemetery; players wear costumes to support a team.", "source": "http://www.freerealms.com/article/detail.action?articleId=1857"},
   {"claim": "Madame Zelda at Black Spore starts the quest and lets players choose a side; the contest location is Boneyard cemetery, north of the Haunted Mines. The scariest dance wins the scariest monster title.", "source": "http://www.freerealms.com/article/detail.action?articleId=1878"},
   {"claim": "The Pumpkin Prince judges the contest himself.", "source": "http://www.freerealms.com/article/detail.action?articleId=1867"}
 ],
 "confidence": 0.35,
 "open": [
   "No dated occurrence. Article 1866 has no date in the pack, and no article in the pack gives dance-contest dates. The 2011 window (Oct 13 to Nov 23, article 2304) and 2013 window (Oct 1 to Nov 12, article 2949) belong to the parent Super Spooktacular holiday; put them on that entry, not here.",
   "Recurrence unsourced. The 'second annual' wording in articles 1854/1860/1861 has no year. Do not schedule the contest on its own. It can only be tied to the Spooktacular/Super Spooktacular holiday window when that runs.",
   "Live status unsure. The articles are official news posts with no date in this pack, and no pre-launch wording was found. Treat as live-era content only if the holiday entry confirms it ran.",
   "Name issue: 'Contest start announcement' is the in-game trigger text in article 1866, not an event. It is merged here into the dance contest. The pack also merges two names: the Pumpkin King (1866, 1867) and the Pumpkin Prince (1857, 1854, 2304, wiki). Treated as one NPC, unconfirmed.",
   "Location conflict not resolved: Bone Marsh outskirts (1866, 1860), Bone Bog Cemetery (1857, 1854, 1862, 2304), Cienaga de los Huesos (1861), Boneyard cemetery / Blackspore (1878). Article 1878 may be a separate edition; not merged with the others in any source. The 'Cursed Mines' wording was dropped: no source in the pack supports it. Madame Zelda's location conflicts too (Shadowbrook per 1866 summary, Black Spore per 1878, Esporaumbria per 1866 Spanish text).",
   "Quests: the side-choice mission is named in 1866 but its exact title is not sourced here. The wiki titles 'Being Prepared (Team Vampire/Werewolf)' and 'Pre-Emptive Bite' are on the Super Spooktacular holiday list, not tied to the contest, so they are left out. Pre-Emptive Bite giver conflicts (Drake vs Ed Sullenfangs), unresolved.",
   "Items: no item is tied to the contest by a source. The wiki Team Vampire list (Bat, Team Vampire T-Shirt, Vampire Outfit, Vampire Fangs), the Team Werewolf outfits in article 2304, and Werewolf Tail (locale 7365) are holiday costume items. Prices are not sourced. Attach them to the holiday entry.",
   "Cake reward: article 1867 supports it. Article 1862 was not re-verified in this pass. Locale 436401 (dance-off rumor in Blackspore) has its event tag inferred from the id, not the text.",
   "Wireable: no. Hold as a sub-activity of the Super Spooktacular holiday entry until that entry is built and its dates are sourced."
 ]
}
