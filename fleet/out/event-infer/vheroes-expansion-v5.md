<!-- fleet job=event-infer id=vheroes-expansion-v5 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[7751, 8271, 6, 2417] model=claude-haiku-5-5 -->
# Heroes expansion

{"event": {"name": "Heroes expansion (Free Realms Trading Card Game Set 4: Heroes)", "aliases": ["Heroes", "TCG Set 4: HEROES", "Heroes Booster Pack", "Heroes Booster Bundle", "Free Realms TCG Heroes expansion"]},
"kind": "update",
"live": "unsure",
"occurrences": [],
"recurring": null,
"zones": [],
"npcs": [],
"quests": ["A True Hero (title from the earlier pack, not re-confirmed by lookup; objective confirmed at locale:441610)"],
"activities": ["Play the Free Realms trading card game", "Open Heroes booster packs", "Complete the Heroes questline"],
"items": [
 {"name": "Heroes Booster Pack", "price": null, "currency": "station_cash", "source": "locale:17470 (name); locale:17471 (10 random TCG cards plus one loot card). Store frames in video:1LjCvhboCkQ/00190.jpg show 249 station_cash and video:9NOkMosko1E/00024.jpg shows 224; the prices are undated and conflict, so none is fixed."},
 {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:7973; locale:9403 (store line 'Save on TCG Set 4: Heroes Booster Bundles!'). No price tied to this SKU."}
],
"rewards": ["Heroes TCG cards", "One loot card per Heroes booster pack (locale:17471)"],
"evidence": [
 {"claim": "Heroes is the fourth set of the Free Realms TCG and introduces the Realmkeepers; each booster pack has 10 random cards plus one loot card.", "source": "locale:17471"},
 {"claim": "'TCG Set 4: HEROES Available Now!' is a store/announcement line.", "source": "locale:17472"},
 {"claim": "Heroes is described as a new expansion just released (relative date only, no absolute date).", "source": "http://www.freerealms.com/article/detail.action?articleId=2737"},
 {"claim": "Quest objective 'Complete the Heroes Questline.'", "source": "locale:441610"},
 {"claim": "Heroes Booster Bundle (25 Pack) is a client item and the store promo names TCG Set 4: Heroes Booster Bundles.", "source": "locale:7973; locale:9403"}
],
"confidence": 0.4,
"open": [
 "No absolute date is verified. The earlier 2012-08-25 launch date and the Ten Ton Hammer article (http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game) could not be re-checked: the article lookup returned no matches this run and the pack shows no publication date. Occurrences are left empty until a dated source is shown. If the article is dated, the launch month would go here.",
 "Article 2733 ('new features, single-player scenarios, tournament promo cards, new loot cards') was not re-fetched this run, so that claim is dropped. Article 2737 is relative-dated only ('Publié il y a 2 mois, 6 jours').",
 "Quest title 'A True Hero' was not confirmed by lookup; only the objective text at locale:441610 was seen. locale:441612 is a FLAG duplicate and is not cited.",
 "Wiki-based claims (Realmkeepers outfits Crackshot, Wildclaw, Magetech, Ghostshadow; Sparky ride; Gloamstone; Baron von Darkcheat as questline antagonist) were not verified this run and are removed from npcs and rewards. They need wiki page text before they are added back.",
 "Heroes Booster Pack price conflicts across store frames (249 vs 224 station_cash) and is undated, so price is null.",
 "Possible merge: a separate '[Heroes] Journal [questline]' cited by wiki pages Chugzy and Necronomicus (Chugzy introduced 2013-08-13) may be a different questline or part of this event. Bryce should check.",
 "Article 2876 (Rumbledome! questline) mentions HEROES as a later storyline reference; it is not used as a Heroes event fact.",
 "Madam Zelda, Blackspore/Seaside Realmkeepers lines and the card Sirdo (4R5) are not tied to this set by any source, so they are not listed.",
 "End date is unknown. Calendar category 'update' (card-set release); 'other' is also defensible."
]}
