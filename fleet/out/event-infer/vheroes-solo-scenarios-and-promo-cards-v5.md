<!-- fleet job=event-infer id=vheroes-solo-scenarios-and-promo-cards-v5 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[7859, 10604, 6, 3077] model=claude-haiku-5-5 -->
# Heroes solo scenarios and promo cards

{"event": {"name": "Heroes (Trading Card Game Set 4) expansion release", "aliases": ["Heroes", "Héros", "TCG Set 4: HEROES", "Heroes Booster Pack", "Heroes Booster Bundle"]},
"kind": "other",
"live": "unsure",
"occurrences": [{"year": 2012, "when": "2012-08-25 (provisional; launch date as stated in a Ten Ton Hammer repost of the SOE press release, which is dated 2012-10-24 on capture; no dated SOE article confirms it)", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (articles.json:19147-19150)"}],
"recurring": null,
"zones": [],
"npcs": ["Baron von Darkcheat", "Madam Zelda"],
"quests": [],
"activities": ["Playing the Heroes TCG set", "Opening Heroes booster packs", "Playing the Heroes solo scenarios (titles not sourced)", "Completing the Heroes questline (objective: 'Complete the Heroes Questline.')"],
"items": [
 {"name": "Heroes Booster Pack", "price": null, "currency": null, "source": "locale:17470; locale:17472"},
 {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:7973 (name only)"}
],
"rewards": [
 "Heroes TCG cards: 10 random cards plus one loot card per booster pack (locale:17471)",
 "Grand tournament promo cards (names not sourced)",
 "Solo scenario exclusive rewards (not itemised in any source)",
 "New loot cards featuring Heroes (not itemised)"
],
"evidence": [
 {"claim": "Heroes is announced as a new TCG expansion with the Baron von Darkcheat story, naming Madam Zelda and four child Guardians. Undated.", "source": "http://www.freerealms.com/article/detail.action?articleId=2742"},
 {"claim": "Heroes is announced as a new TCG expansion with new solo scenarios, grand tournament promo cards and new loot cards (French post, undated).", "source": "http://www.freerealms.com/article/detail.action?articleId=2742"},
 {"claim": "Heroes is the TCG's fourth set: client text reads 'TCG Set 4: HEROES Available Now!'.", "source": "locale:17472"},
 {"claim": "Each booster pack holds 10 random cards plus one loot card; Heroes is tied to Baron von Darkcheat and Realmkeepers in client text.", "source": "locale:17471"},
 {"claim": "A Ten Ton Hammer repost of the SOE release gives launch 2012-08-25 and 76 cards (54 booster, 22 promo). Single secondary source.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game"},
 {"claim": "Quest objective 'Complete the Heroes Questline.' exists in client text.", "source": "locale:441610; locale:441612"},
 {"claim": "Sale text 'Save on TCG Set 4: Heroes Booster Bundles!' is a promotion, not a price.", "source": "locale:9403"},
 {"claim": "Client text 'The newest Free Realms Trading Card Game Set is here! ... New Quests For Level 20 Card Duelists! ... TCG Sets 1 - 4 Quests now free to play!' is undated and covers sets 1-4, so it is a general TCG promotion, not a Heroes launch gate.", "source": "locale:17473"},
 {"claim": "The 'New Quests For Level 20 Card Duelists!' text with '146 New Cards!' (locale:2169) belongs to a different set and is not this event's gate.", "source": "locale:2169"}
],
"confidence": 0.3,
"open": [
 "Date: 2012-08-25 is provisional. It rests on one Ten Ton Hammer repost (articles.json:19147-19150); the repost date and the stated launch date are not separated by any dated SOE source. Confirm against a dated SOE article or patch note before scheduling.",
 "End date: unsourced. Do not infer a duration from other TCG sets. Live status is 'unsure'.",
 "Quests: the four Card Duelist quests (locale:7947 Heart of Darkness, 7951 Slow and Steady, 7955 Stinky Feet, 7959 Meet the Boss) exist in the client but are shared TCG quests spanning sets 1-4 per locale:17473. Not listed as Heroes-only. Which, if any, is the Heroes final quest is unconfirmed; the TTH repost says four quests lead to a final boss against Baron von Darkcheat.",
 "'A True Hero' was not verified: no id resolved to that title in this pass. Dropped from quests.",
 "Gating: level 20 and free-to-play status for Heroes quests are not sourced for launch; locale:17473 is undated and general.",
 "Solo scenario titles, promo card names, loot card names and zones are not in the pack or lookup.",
 "Prices: the 249 and 224 Heroes Booster Pack prices appear only in video frames, undated and time-dependent; not stored. No Heroes bundle price is sourced (generic digital bundle prices are not Heroes).",
 "Madam Zelda's quest list was not verified. The SOE article summaries for articleId=2733 and 2738 do not give a date or set number.",
 "Pre-launch teasers (articleId=2730, 2736, captured 2012-11-03, undated) describe plans and are not occurrences.",
 "Aliases: 'Heroes' is a generic word; match only with TCG context. The pack merges the expansion release with its sub-features under one name.",
 "Excluded: locale:4419490/4419492/4419502 'Hero of Heroes' (unrelated achievement); locale:441611 flagged duplicate; locale:9922 is a seasonal bundle (Pumpkin Prince), not this event."
],
"notes_on_critique": "Corrections applied: locale:17473 does resolve (critique was wrong) but is undated and general, so it is cited only for that. Dropped the unverified 'A True Hero' title and the 441609 citation. Card Duelist quests moved to a shared note. Prices left null. 76-card total attributed to the TTH repost only. Kind changed from update to other."}
