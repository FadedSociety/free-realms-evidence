<!-- fleet job=event-infer id=vheroes-expansion-v6 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[6439, 9417, 6, 3011] model=claude-haiku-5-5 -->
# Heroes expansion

{"event": {"name": "Heroes expansion (Free Realms Trading Card Game Set 4: Heroes)", "aliases": ["Heroes", "TCG Set 4: HEROES", "Heroes Booster Pack", "Heroes Booster Bundle", "Series 4 Heroes Expansion"]},
 "kind": "update",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": ["A True Hero"],
 "activities": ["Open Heroes booster packs", "Complete the Heroes questline (TCG)"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": "station_cash", "source": "locale:17470 (name); locale:17471 (10 random TCG cards plus one loot card). Store frames video:1LjCvhboCkQ/00190.jpg (249 station_cash) and video:9NOkMosko1E/00024.jpg (224) conflict and are undated, so no price is fixed."},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": null, "source": "locale:7973 (name only); locale:9403 (store line 'Save on TCG Set 4: Heroes Booster Bundles!'). No price tied to this SKU."},
  {"name": "Pumpkin Prince seasonal bundle (contains 2 Heroes booster packs)", "price": null, "currency": null, "source": "locale:9922 ('two booster packs of Heroes'); wiki Template:News/Archive, 'Update of October 4, 2012'. Shows Heroes packs were sold by October 2012; the bundle is not itself a Heroes item."}
 ],
 "rewards": ["Heroes TCG cards", "One loot card per Heroes booster pack (locale:17471)"],
 "evidence": [
  {"claim": "Heroes is the fourth set of the Free Realms TCG, introduces the Realmkeepers; each booster pack has 10 random cards plus one loot card.", "source": "locale:17471"},
  {"claim": "'TCG Set 4: HEROES Available Now!' is a store/announcement line.", "source": "locale:17472"},
  {"claim": "Heroes expansion had arrived when the Spanish SOE post was written (fourth TCG set; story with Baron von Darkcheat, Madam Zelda and four child Defenders).", "source": "http://www.freerealms.com/article/detail.action?articleId=2738"},
  {"claim": "SOE news post announcing the Heroes expansion and listing new TCG mechanics; the post names the kids as Bryce, Nathan, Kade, Jessica.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733"},
  {"claim": "Article 2737 (Spanish, 'Conoce a los Defensores') introduces four child Defenders and new card mechanics; date is relative only ('Publié il y a 2 mois, 6 jours'), so no absolute date.", "source": "http://www.freerealms.com/article/detail.action?articleId=2737"},
  {"claim": "Heroes booster packs were sold inside the Pumpkin Prince seasonal bundle in the October 4, 2012 update (bundle = new TCG card, 2 Darkcheat packs, 2 Heroes packs).", "source": "locale:9922; wiki Template:News/Archive ('Update of October 4, 2012')"},
  {"claim": "Wiki Sirdo: a Hero card based on Sirdo was introduced on August 23, 2012 in the Series 4 Heroes Expansion (card ID 4R5).", "source": "wiki Sirdo"},
  {"claim": "Quest title 'A True Hero' and objective 'Complete the Heroes Questline.' are client text.", "source": "locale:441609 (title); locale:441610 (objective; 441611 and 441612 are duplicate-flagged entries)"}
 ],
 "confidence": 0.4,
 "open": [
  "Launch date: the earlier 2012-08-25 date is not verified. Wiki Sirdo gives August 23, 2012 for a Heroes-set card introduction, which points to a late-August 2012 release, but no article states the launch day. Occurrences stay empty until a dated launch source is confirmed.",
  "Live status: Heroes packs were on sale by October 2012 (Pumpkin Prince bundle). Whether the set is still sold today is not shown, so live is 'unsure'. End date unknown.",
  "Possible merge: wiki 'Baron von Darkcheat (character)' names a 'TCG [Heroes]/Baron von Darkcheat questline', and locale:9922 pairs Darkcheat packs with Heroes packs. Decide whether the Heroes questline, the Darkcheat questline and the '[Heroes] Journal [questline]' cited by wiki pages Chugzy and Necronomicus are one event before wiring.",
  "Kid names conflict: article 2733 lists Kade; article 2737 lists Onofre. Not resolved; neither is used as a fact in the npcs list.",
  "Heroes Booster Pack price conflicts across store frames (249 vs 224 station_cash) and is undated, so price is null.",
  "Article 2738 is cited for the release statement, but it has no absolute date in the pack. Article 2734 mentions the Heroes series within the quest guide; it is not used as a Heroes fact.",
  "Wiki-based claims (Realmkeepers outfits, Sparky ride, Gloamstone, Madam Zelda, Blackspore/Seaside lines) are not tied to this set by a source in this pack and are left out.",
  "Calendar category: 'update' (card-set release); 'other' is also defensible.",
  "locale:441612 is duplicate-flagged and is not cited as live evidence."
 ]}
