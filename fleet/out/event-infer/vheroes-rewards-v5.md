<!-- fleet job=event-infer id=vheroes-rewards-v5 status=done turns=5 usd=0.0034 tokens(read,write,in,out)=[40208, 11742, 12, 3010] model=claude-haiku-5-5 -->
# Heroes rewards

{"event": {"name": "Heroes (TCG Set 4 expansion)", "aliases": ["TCG Set 4: HEROES", "TCG Set 4", "Heroes expansion", "Heroes Booster Pack", "Heroes TCG questline"]},
 "kind": "update",
 "live": "unsure",
 "occurrences": [{"year": 2012, "when": "2012-08-25 (launch, per Ten Ton Hammer summary of SOE release; no other absolute date found)", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (article summary)"}],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["single-player TCG scenarios", "TCG tournaments (promo cards at major tournaments)"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": "station_cash", "source": "locale:17470; video:fjZluIfbUIo/00058.jpg (249 station_cash); video:1LjCvhboCkQ/00188.jpg and 00190.jpg (249 station_cash); video:9NOkMosko1E/00024.jpg (224 station_cash, conflicting)"},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": "station_cash", "source": "locale:7973 and locale:9403 (store message 'Save on TCG Set 4: Heroes Booster Bundles!')"}
 ],
 "rewards": ["exclusive single-player scenario rewards (http://www.freerealms.com/article/detail.action?articleId=2744)", "tournament promo cards (article 2744)", "new loot cards (article 2744)"],
 "evidence": [
  {"claim": "Ten Ton Hammer reposted an SOE release: Heroes, a free-to-play TCG, launched 2012-08-25 with 76 cards (54 booster, 22 promo) and four quests leading to a final boss.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (article summary; the article body itself gives 'the day of the article' with no absolute date)"},
  {"claim": "Heroes is the newest TCG expansion, adding single-player scenarios with exclusive rewards, promo cards at major tournaments, and new loot cards.", "source": "http://www.freerealms.com/article/detail.action?articleId=2744 (relative date only, '2 Monate, 6 Tage' ago)"},
  {"claim": "Store listing names the set: 'TCG Set 4: HEROES Available Now!'", "source": "locale:17472"},
  {"claim": "Store message 'Save on TCG Set 4: Heroes Booster Bundles!' ties bundles to the set.", "source": "locale:9403"},
  {"claim": "Store frames show '[Heroes] [Booster] [Pack] 249 station_cash' with 'TCG Set 4 Available Now!' banner (undated).", "source": "video:fjZluIfbUIo/00058.jpg; video:1LjCvhboCkQ/00188.jpg; video:1LjCvhboCkQ/00190.jpg"},
  {"claim": "Pumpkin Prince bundle includes Heroes packs but is a separate seasonal promotion, excluded.", "source": "locale:9922"}
 ],
 "confidence": 0.5,
 "open": [
  "Live status: this is a TCG product release, not a dated in-game live event. Kept at live 'unsure'.",
  "Date: 2012-08-25 comes only from the Ten Ton Hammer article summary, which states it as launch date from an SOE release. The article body I could see gives no absolute date, so verify against the archive before wiring.",
  "Quests: the TTH summary says four quests leading to a final boss, but gives no titles. No quest titles confirmed. locale:441610 ('Complete the Heroes Questline.') is an objective of 'A True Hero' only, and 441612 is a flagged duplicate, so it is not used.",
  "Baron von Darkcheat: the name is also the TCG Series 3 set (locale 2150-2158, 2165-2167, 2371, 7971). The wiki Heroes questline pages tie Darkcheat to Heroes, but I did not confirm this in the client. Treat the Heroes questline link as unverified and keep it separate from the Series 3 set.",
  "NPCs: the four Realm Guardians (Geisterschatten, Magotron, Wildkralle, Adlersehne) come from articles 2744 and 2742 only; no client NPC entries matched. Not listed.",
  "Price: 249 vs 224 station_cash conflict across undated frames. Price left null. 224 comes from video:9NOkMosko1E/00024.jpg only. The earlier claim about a Set 3 video at 249 was not checked and is dropped.",
  "Bundle price: none found for Heroes Booster Bundle (25 Pack).",
  "Store line 'Amazing new loot!' is not in locale:17472; it appears in locale:17473 (general TCG banner covering Sets 1-4), so it is not cited as Heroes text.",
  "Other article dates (2727, 2720, 2726, 2732, 2733, 2736, 2737, 2738, 2751) are unknown; article 2744 is relative-date only.",
  "Excluded: article 2876 (Rumbledome), article 2764 (Sets 1-3 weekend sale), 'Hero of Heroes' (locale 4419490/4419491/4419502 flagged not_live), generic 'hero' tournament text."
 ]}
