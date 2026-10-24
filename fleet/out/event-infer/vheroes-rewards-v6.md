<!-- fleet job=event-infer id=vheroes-rewards-v6 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[15537, 10563, 8, 3296] model=claude-haiku-5-5 -->
# Heroes rewards

{"event": {"name": "Heroes (TCG Set 4 expansion)", "aliases": ["TCG Set 4: HEROES", "TCG Set 4", "Heroes Booster Pack", "Heroes Booster Bundle (25 Pack)", "Heroes rewards (pack title)"]},
 "kind": "update",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["single-player TCG scenarios (article 2744)", "TCG tournaments with promo cards (article 2744)", "buying and opening Heroes booster packs and bundles (store text)"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": "station_cash", "source": "locale:17470 (name); video:fjZluIfbUIo/00058.jpg and video:1LjCvhboCkQ/00188.jpg, 00190.jpg (249 station_cash, undated); video:9NOkMosko1E/00024.jpg (224, conflicting). Price unresolved."},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": "station_cash", "source": "locale:7973 (name); locale:9403 ('Save on TCG Set 4: Heroes Booster Bundles!'); refs/FreeRealms-Legacy/src/Resources/StoreBundles.json:24963 (cited by critique, not opened by me)"}
 ],
 "rewards": ["exclusive single-player scenario rewards (http://www.freerealms.com/article/detail.action?articleId=2744)", "tournament promo cards (article 2744)", "new loot cards (article 2744)"],
 "evidence": [
  {"claim": "Heroes is the newest TCG expansion, adding single-player scenarios with exclusive rewards, promo cards at major tournaments, and new loot cards.", "source": "http://www.freerealms.com/article/detail.action?articleId=2744 (German article; relative date only, '2 Monate, 6 Tage' ago, so no absolute date)"},
  {"claim": "Store title names the set: 'TCG Set 4: HEROES Available Now!'", "source": "locale:17472 (title only; 'Amazing new loot!' is not in this string)"},
  {"claim": "Heroes Booster Pack is a client item name.", "source": "locale:17470"},
  {"claim": "Store message ties Heroes Booster Bundles to TCG Set 4.", "source": "locale:9403"},
  {"claim": "Pumpkin Prince seasonal bundle includes two Heroes packs; it is a separate seasonal promotion and is excluded as the event.", "source": "locale:9922"},
  {"claim": "Client quest text 'Complete the Heroes Questline.' exists, attached to one objective.", "source": "locale:441610 (441612 is a flagged duplicate)"},
  {"claim": "Madam Zelda, Realmkeepers and Baron von Darkcheat storyline text exists in client (Sacred Grove, Blackspore Swamp, Seaside), but these strings do not name 'Heroes'.", "source": "locale:7948, 7960, 7961, 7966, 439496. Not tied to Heroes by name; Darkcheat also names the Series 3 TCG set (locale:2150-2158, 2165-2167), so do not conflate."}
 ],
 "confidence": 0.35,
 "open": [
  "Launch date: the only absolute date (2012-08-25) comes from a Ten Ton Hammer summary of an SOE release (articles.json around 19147-19150). I could not confirm it in the archive or the client, so no occurrence is listed. Verify against the original article before wiring. Article 2744 gives only a relative date. A Spanish/Portuguese capture dated 2012-11-03 is a cross-check only, not a launch date.",
  "Live status: this is a TCG product expansion. The client shows store text, not a dated in-game event window. Treat as a product release, not a timed live event, until a dated source confirms otherwise.",
  "Quests: the TTH summary says four quests lead to a final boss, but no titles are confirmed. The quests.json 'Heroes' chain (Madam Zelda, Blackspore Swamp, 'Finish Baron von Darkcheat', 'Fight the Baron's cronies while the four Realmkeepers train', 'Final reckoning with Baron von Darkcheat') cites article 2734, which is a separate later 'quest packs free to play' announcement, undated. It is not confirmed as Heroes content. No quest titles are listed.",
  "Baron von Darkcheat: the name collides with the Series 3 TCG set. Keep the Heroes questline separate from Series 3 when citing.",
  "Realm Guardians (Geisterschatten, Magotron, Wildkralle, Adlersehne) come only from articles 2744 and 2742. No client NPC entries matched, so the npcs list is empty.",
  "Price conflict: 249 vs 224 station_cash across undated frames. Price left null.",
  "Bundle source StoreBundles.json:24963 was not opened by me.",
  "Other article dates (2727, 2720, 2726, 2732, 2733, 2736, 2737, 2738, 2751, 2734) are unknown.",
  "Excluded: article 2876 (Rumbledome), article 2764 (Sets 1-3 weekend sale), 'Hero of Heroes' (locale 4419490-4419502, flagged not_live), generic 'hero' tournament text (e.g. locale 391785), and locale:17473 (general banner covering Sets 1-4)."
 ]
}
