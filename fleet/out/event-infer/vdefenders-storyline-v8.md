<!-- fleet job=event-infer id=vdefenders-storyline-v8 status=done turns=3 usd=0.0027 tokens(read,write,in,out)=[16380, 9032, 8, 2832] model=claude-haiku-5-5 -->
# Defenders storyline

{"event": {"name": "TCG Set 4: HEROES (Realmkeepers storyline)", "aliases": ["TCG Set 4: HEROES Available Now! (locale:17472)", "Realmkeepers storyline", "Defenders storyline (Spanish article 2737, 'Defensores')"]},
 "kind": "other",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": ["Blackspore Swamp (http://www.freerealms.com:80/article/detail.action?articleId=2734; wiki 'Madam Zelda')"],
 "npcs": ["Madam Zelda (articleId=2734 fact:quest; articleId=2746 fact:npc)", "Realmkeepers: the four child heroes; the wiki names them Ghostshadow, Magetech, Wildclaw, Crackshot (wiki 'Realmkeepers')", "Baron von Darkcheat (the foe, articleId=2734)"],
 "quests": [],
 "activities": ["Keep Baron von Darkcheat and his cronies busy while the four Realmkeepers train (articleId=2734 quest objective)", "Fight the four Heroes fights, ending in a final reckoning with Baron von Darkcheat (articleId=2734 quest objective; articleId=2746)", "Buy and open TCG Set 4 Heroes booster packs (locale:17472, locale:9403)"],
 "items": [{"name": "TCG Set 4: Heroes Booster Pack", "price": null, "currency": null, "source": "locale:17471 (pack contents: 10 random TCG cards plus one loot card); locale:17472"}, {"name": "TCG Set 4: Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:9403 ('Save on TCG Set 4: Heroes Booster Bundles!'); price unsourced"}],
 "rewards": ["Each Set 4 pack holds 10 random TCG cards plus one loot card (locale:17471)"],
 "evidence": [{"claim": "Set 4 is named 'TCG Set 4: HEROES Available Now!'", "source": "locale:17472"}, {"claim": "The fourth set introduces the Realmkeepers, who help stop Baron von Darkcheat; each pack has 10 random cards plus one loot card.", "source": "locale:17471"}, {"claim": "Heroes is the fourth series. It begins after Baron von Darkcheat is defeated; Madam Zelda in Blackspore Swamp starts it; players keep the Baron busy while four Realmkeepers train; it ends in a final reckoning with the Baron.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2734 (fact:quest)"}, {"claim": "Madam Zelda gathers four child heroes, the Realmkeepers, and trains them against Darkcheat.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733 (fact:npc)"}, {"claim": "Heroes quest line objective 'Complete the Heroes Questline.'", "source": "locale:441610"}, {"claim": "The Spanish article describes the Defenders fighting Baron Trampaoscura until training is complete; it has no absolute date.", "source": "http://www.freerealms.com/article/detail.action?articleId=2737 (date null)"}], 
 "confidence": 0.3,
 "open": [
  "No absolute date in any source. Article 2737 has only a relative date ('Publié il y a 2 mois, 6 jours'). Occurrences stay empty; the earlier 2012-08-25 date has no dated source and is dropped. Not wireable to the calendar until a dated source (TCG news post or patch note for locale:17472) is found.",
  "Not a bounded event: no start, end or recurrence is sourced. Live status is unsure.",
  "Preceding arc, not part of this event's record: the Baron von Darkcheat fight (locale:7948-7961: Grimyfoot, Clancy Blackheart, Seaside 'Card Duelist: Meet the Boss') and the Sunstone Valley lead-in ('Card Duelist: The Realmkeepers Are Missing!', locale:5100175/5100176). Neither is tied to Heroes by a source here, so Seaside and Sunstone Valley are removed from zones and the quest list is empty.",
  "No exact quest titles for Heroes are sourced. 'Complete the Heroes Questline.' (locale:441610) is an objective string, not a quest title. Quest titles still need to be found in the client.",
  "Zone conflict: Blackspore Swamp (articleId=2734, 2746) vs Sporeshade Swamp (articleId=2740). Unresolved.",
  "Kid-name conflict: articleId=2733 gives Bryce, Nathan, Kade, Jessica; articleId=2737 gives Onofre for Kade; the wiki gives Ghostshadow, Magetech, Wildclaw, Crackshot. The mappings Ghostshadow=Bryce and Wildclaw=Kade are unsourced equivalences and are not stated as fact.",
  "Possible merge/alias issue: 'Heroes' alone is ambiguous and is not used as an alias. 'Heroes Journal' / Hero Rises is separate content.",
  "Locale 9922 bundles Baron and Heroes packs together with a Pumpkin Prince promo; it is not used as this event's item.",
  "Pack and bundle prices and currency are not in any source: null. The final challenge's special prize is not named in any source; the Baron costume (locale:391) is not verified as this event's reward and is left out.",
  "Calendar and evidence critiques (scores 2 and 3, both not wireable): the name, zones, quests and bundle item were corrected per the critiques. Still not wireable: no dated source."
 ]}
