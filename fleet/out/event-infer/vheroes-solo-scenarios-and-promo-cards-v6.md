<!-- fleet job=event-infer id=vheroes-solo-scenarios-and-promo-cards-v6 status=done turns=3 usd=0.0048 tokens(read,write,in,out)=[24241, 17869, 8, 4689] model=claude-haiku-5-5 -->
# Heroes solo scenarios and promo cards

{
 "event": {"name": "Heroes (Free Realms Trading Card Game expansion, Set 4)", "aliases": ["Heroes", "Héros", "TCG Set 4: HEROES", "Heroes Booster Pack", "Heroes Booster Bundle", "Heroes TCG questline"]},
 "kind": "other",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "launch 2012-08-25 per the Ten Ton Hammer repost, which is dated 2012-08-25 and whose summary says the SOE press release announced launch on 2012-08-25. Provisional: the SOE original is not in the pack.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (articles/articles.json:19147-19150)"},
  {"year": 2012, "when": "December 2012, Snow Days: a Heroes TCG Bundle (two Baron von Darkcheat booster packs, two Heroes booster packs, one Abominable Snowman promo card) was sold. Shows Heroes packs were on sale in Dec 2012.", "source": "wiki: Abominable Snowman (TCG section); wiki: Pumpkin Prince (bundle text, also cites Heroes packs)"}
 ],
 "recurring": null,
 "zones": ["Blackspore Swamp (Heroes quest location per articles/quests.json:632)", "Sporeshade Swamp (location in the second quest record, articles/quests.json:714; conflicts with Blackspore, unresolved)"],
 "npcs": ["Baron von Darkcheat", "Madam Zelda", "Realmkeepers: Crackshot, Magetech, Wildclaw, Ghostshadow (wiki, Category:Realmkeepers; four child Guardians/Defenders per SOE posts)", "Bryce, Nathan, Kade, Jessica (Realmkeeper kids named in articleId=2733; Spanish/German posts name Onofre/Adlersehne-style variants, unresolved)"],
 "quests": [
  "Heroes (giver Madam Zelda, Blackspore Swamp; steps: Finish Baron von Darkcheat; Fight the Baron's cronies while the four Realmkeepers train; Final reckoning with Baron von Darkcheat) (articles/quests.json:632)",
  "Card game series 4 (HEROES) (giver Madam Zelda, Sporeshade Swamp; steps name Baron Trampaoscura, a localized villain name; ends 'Face Baron Trampaoscura in the final showdown') (articles/quests.json:714). Probably the same questline in another language; treat as a variant.",
  "Shared TCG quests, not Heroes-only (locale:7947 Heart of Darkness, 7951 Slow and Steady, 7955 Stinky Feet, 7959 Meet the Boss): Card Duelist quest series for sets 1-4 per the free-quest posts (articles/articles.json:19262, 20074, 20088)"
 ],
 "activities": ["Playing Heroes TCG cards", "Opening Heroes booster packs", "Playing Heroes single-player scenarios with exclusive rewards (titles not sourced)", "Playing grand tournaments for Heroes promo cards (sourced in articleId=2742 and facts; tournament names not sourced)", "Completing the Heroes questline (objective 'Complete the Heroes Questline.', locale:441610)"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": null, "source": "locale:17470; locale:17472 ('TCG Set 4: HEROES Available Now!')"},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:7973 (name only)"},
  {"name": "Heroes Booster Bundle (sale text)", "price": null, "currency": null, "source": "locale:9403 ('Save on TCG Set 4: Heroes Booster Bundles!', promotion, no price)"},
  {"name": "Gloamstone Hoverboard", "price": null, "currency": "reward", "source": "wiki: Rides (only obtainable by completing the Baron von Darkcheat TCG questline; whether it is Heroes-specific is not stated)"}
 ],
 "rewards": [
  "Heroes TCG cards: 10 random cards plus one loot card per booster pack (locale:17471)",
  "76 cards total: 54 booster, 22 promo (Ten Ton Hammer repost only, articles/articles.json:19150; facts.json:35769)",
  "Grand tournament promo cards (articleId=2742 and articles/facts.json:17422; card names not sourced)",
  "Single-player scenario exclusive rewards (articles/facts.json:17390; not itemised)",
  "New loot cards featuring Heroes (not itemised)",
  "Gloamstone (wiki: The Gloamstone, obtained at the end of the TCG Heroes/Baron questline)"
 ],
 "evidence": [
  {"claim": "Heroes is a new Free Realms TCG expansion with the Baron von Darkcheat story, Madam Zelda and four child Guardians. Undated.", "source": "http://www.freerealms.com/article/detail.action?articleId=2742"},
  {"claim": "Heroes adds single-player scenarios with exclusive rewards, tournament promo cards and new loot cards. Undated.", "source": "articles/facts.json:17390, 17470 (from SOE posts)"},
  {"claim": "Heroes is the TCG's fourth set: client text 'TCG Set 4: HEROES Available Now!'.", "source": "locale:17472"},
  {"claim": "Each booster pack holds 10 random cards plus one loot card.", "source": "locale:17471"},
  {"claim": "Heroes launched 2012-08-25 with 76 cards (54 booster, 22 promo) and four quests ending in a fight with Baron von Darkcheat. Date is the repost date and the summary's launch date; single secondary source.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (articles/articles.json:19147-19150)"},
  {"claim": "A Spanish post says Heroes 'had just been released' (undated), which corroborates a release window.", "source": "articles/facts.json:17358, 17361"},
  {"claim": "Heroes packs were sold in the December 2012 Snow Days bundles.", "source": "wiki: Abominable Snowman; wiki: Pumpkin Prince"},
  {"claim": "Quest objective 'Complete the Heroes Questline.' exists in client text.", "source": "locale:441610"},
  {"claim": "Heroes questline quest record with Madam Zelda as giver.", "source": "articles/quests.json:632"}
 ],
 "confidence": 0.5,
 "open": [
  "Launch date 2012-08-25 rests on one Ten Ton Hammer repost (articles/articles.json:19147-19150). No dated SOE article in the pack confirms it. Label it provisional. Do not schedule it as confirmed until an SOE source or patch note is found.",
  "End date and any retirement date are unsourced. Live status 'yes' rests on the Dec 2012 bundle wiki text and the launch post, not on a dated end-of-sale. Treat as unsure for scheduling.",
  "Quest chain conflict: quests.json:632 names Blackspore Swamp with Baron von Darkcheat; quests.json:714 names Sporeshade Swamp with Baron Trampaoscura, and the Spanish/German posts use other villain and kid names. Probably one questline in different localizations, but not confirmed. Quest 'A True Hero' is not verified and is dropped.",
  "Gating: level 20 and free-to-play status for Heroes quests are not sourced for launch. locale:17473 is undated and general, so it is not used as a Heroes gate.",
  "Card Duelist quests (locale:7947-7959) are shared TCG content across sets 1-4, not Heroes-only.",
  "Heroes Booster Pack prices (249, 224) appear only in video frames, undated and time-dependent. Not stored. No Heroes bundle price is sourced.",
  "Solo scenario titles, grand tournament names, promo card names and loot card names are not in the pack. Zones for scenarios are unknown.",
  "Pre-launch teasers (articleId=2720, 2730, 2732, 2736; captured 2012-11-03 for some, undated) describe plans and are not occurrences.",
  "Alias merge: 'Heroes' is a generic word. The name covers the expansion release, its booster products, its questline and its sub-features. Match only with TCG context.",
  "Excluded: locale:4419490/4419492/4419502 'Hero of Heroes' (unrelated achievement); locale:441611 and 441612 are flagged duplicates of 441609/441610 (441612 is not separate evidence); locale:9922 is the Pumpkin Prince seasonal bundle (cited only as wiki context); locale:2169 is a different set ('146 New Cards')."
 ]
}
