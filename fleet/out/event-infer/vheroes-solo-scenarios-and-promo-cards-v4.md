<!-- fleet job=event-infer id=vheroes-solo-scenarios-and-promo-cards-v4 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[16809, 9014, 8, 3010] model=claude-haiku-5-5 -->
# Heroes solo scenarios and promo cards

{"event": {"name": "Heroes (Trading Card Game set 4) expansion release", "aliases": ["Heroes", "Héros", "TCG Set 4: HEROES", "Heroes Booster Pack", "Heroes Booster Bundle"]},
"kind": "update",
"live": "unsure",
"occurrences": [{"year": 2012, "when": "August 25, 2012 (provisional launch date; single secondary source)", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (repost of SOE press release, captured 2012-10-24; articles.json:19147-19150)"}],
"recurring": null,
"zones": [],
"npcs": ["Baron von Darkcheat", "Madam Zelda"],
"quests": ["Card Duelist: Stinky Feet", "Card Duelist: Slow and Steady", "Card Duelist: Heart of Darkness", "Card Duelist: Meet the Boss", "A True Hero"],
"activities": ["Playing the Heroes TCG set", "Opening Heroes booster packs", "Completing the Heroes questline against Baron von Darkcheat", "Playing the new solo scenarios (titles not sourced)", "Grand tournament promo cards (names not sourced)"],
"items": [
{"name": "Heroes Booster Pack", "price": "249 (one capture) / 224 (one capture), time-dependent", "currency": "station_cash", "source": "video:fjZluIfbUIo/00058.jpg; video:1LjCvhboCkQ/00190.jpg; video:9NOkMosko1E/00024.jpg"},
{"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:7973 (name only; no price in any source)"}],
"rewards": ["Heroes TCG cards: 76 total per the TTH repost (54 booster, 22 promo), each booster pack has 10 cards and one loot card (locale:17471)", "Solo scenario exclusive rewards (not itemised in sources)", "Grand tournament promo cards (names not sourced)", "New loot cards featuring Heroes (not itemised)"],
"evidence": [
{"claim": "Heroes launched on 2012-08-25 with 76 cards (54 booster, 22 promo) and four quests leading to a final boss, per a Ten Ton Hammer repost of an SOE press release. Single secondary source; provisional.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game"},
{"claim": "Heroes is announced as a new TCG expansion with the Baron von Darkcheat story, a French-language post also naming Madam Zelda and four child Guardians with decks, weapons and vehicles. No date in the article.", "source": "http://www.freerealms.com/article/detail.action?articleId=2742; http://www.freerealms.com:80/article/detail.action?articleId=2733"},
{"claim": "Heroes is the TCG's fourth set (client text 'TCG Set 4: HEROES Available Now!' and 'Realmkeepers stopping Baron von Darkcheat', fourth TCG set).", "source": "locale:17472; locale:17471"},
{"claim": "Client text 'New Quests For Level 20 Card Duelists!' and 'TCG Sets 1 - 4 Quests now free to play!' is a later, undated promotion. It does not give the launch-time level gate or free-to-play status for these quests.", "source": "locale:17473"},
{"claim": "Quest 'A True Hero' has objective 'Complete the Heroes Questline.'", "source": "locale:441609; locale:441610"},
{"claim": "Card Duelist quest titles exist in the client; they cover TCG sets 1-4 per locale:17473, so they are shared TCG quests, not Heroes-only.", "source": "locale:7947; locale:7951; locale:7955; locale:7959; locale:17473"},
{"claim": "Sale text 'Save on TCG Set 4: Heroes Booster Bundles!' is a promotion, not a price, and the Black Friday sale is a separate promotion.", "source": "locale:9403"}],
"confidence": 0.3,
"open": [
"Date: 2012-08-25 rests on one Ten Ton Hammer repost of an SOE release. No dated SOE article in the pack confirms it. Confirm against a dated SOE article or patch note before scheduling.",
"End date: unsourced. Live status cannot be set to yes; marked unsure. Do not infer a duration from other TCG sets.",
"Quest count conflict: the TTH repost says four quests; the client shows four Card Duelist quests plus 'A True Hero' (five). Which quests belong to Heroes, and which are shared TCG quests spanning sets 1-4, is not confirmed.",
"Final boss: the TTH repost says four quests lead to a final boss fight against Baron von Darkcheat. It does not name 'Card Duelist: Meet the Boss' as the final quest; that link is unconfirmed.",
"Gating: level 20 and free-to-play status come from undated locale:17473, a later promotion. The launch-time gate is not sourced.",
"Madam Zelda's quest list and the wiki Baron von Darkcheat line were not verified in this pass (the wiki path was not available). Dropped as evidence; NPC link relies on articleId=2742 only.",
"Solo scenario titles, promo card names, loot card names, and zones are not in the pack or lookup. Solo scenarios, promo cards and loot cards are sub-features that share the expansion's start date; they have no timing of their own.",
"Price: Heroes Booster Pack shows 249 and 224 in captures with no dates; time-dependent, not an event price. Heroes Booster Bundle (25 Pack) has no price; the 5999 and 5399 station_cash prices are a generic digital bundle, not Heroes.",
"Pre-launch teasers articleId=2730 and articleId=2736 (captured 2012-11-03, undated) describe plans and are not occurrences.",
"Aliases: 'Heroes' is a generic word; search with TCG context. The pack merges the expansion release with its sub-features under one name.",
"Excluded: locale:4419490 'Hero of Heroes' (not tied to the set); locale:4419502 FLAGGED not_live; duplicate locale:441611 and 441612 FLAGGED."
]}
