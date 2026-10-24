<!-- fleet job=event-infer id=vheroes-new-content-v6 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[7174, 7789, 6, 3306] model=claude-haiku-5-5 -->
# Heroes new content

{
 "event": {
  "name": "Heroes (Free Realms Trading Card Game Set 4: Heroes)",
  "aliases": ["TCG Set 4: HEROES", "Heroes Booster Pack (item)"]
 },
 "kind": "update",
 "live": "unsure",
 "occurrences": [
  {"year": 2012, "when": "Aug 2012, day unverified (Ten Ton Hammer repost of an SOE press release gives 2012-08-25; not confirmed on a dated freerealms.com page)", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (articles summary: 'launched on 2012-08-25 with 76 cards (54 booster, 22 promo) and four quests leading to a final boss')"}
 ],
 "recurring": null,
 "zones": ["Blackspore Swamp (Madam Zelda starts the Heroes series; http://www.freerealms.com/article/detail.action?articleId=2746)", "Seaside (locale:7961)"],
 "npcs": ["Madam Zelda (articleId=2746)", "Baron von Darkcheat (locale:17471)", "Ghostshadow (articleId=2733)", "Magetech (articleId=2733)", "Wildclaw (articleId=2733)", "Crackshot (wiki category: Realmkeepers only)"],
 "quests": ["Card Duelist: Stinky Feet", "Card Duelist: Slow and Steady", "Card Duelist: Heart of Darkness", "Card Duelist: Meet the Boss"],
 "activities": ["Play Free Realms Trading Card Game matches, including against Baron von Darkcheat (locale:7961)", "Complete the Heroes questline (locale:441610 objective 'Complete the Heroes Questline.')", "Open Heroes booster packs for loot cards"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": "station_cash", "source": "locale:17471 (10 random TCG cards plus one loot card per item description at locale:17471 family). Price conflict 249 vs 224 station_cash, unresolved, so null."}
 ],
 "rewards": ["Heroes loot cards (locale:17471)", "Outfit from opening a Heroes TCG pack (wiki: Crackshot)", "Baron von Darkcheat's ride and in-game poster after defeating him (wiki: Magetech)"],
 "evidence": [
  {"claim": "Heroes is the fourth set of the Free Realms Trading Card Game; the Realmkeepers help stop Baron von Darkcheat.", "source": "locale:17471; locale:17473"},
  {"claim": "Set launched with 76 cards (54 booster, 22 promo) and four quests leading to a final boss; date 2012-08-25 from a secondary repost.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game"},
  {"claim": "Store frame shows TCG Set 4 Available Now (undated frame).", "source": "video:fjZluIfbUIo/00058.jpg; locale:17473"},
  {"claim": "Quest title 'Card Duelist: Heart of Darkness' confirmed at locale 7947 (earlier cited 7948/7949 not re-verified).", "source": "locale:7947"},
  {"claim": "Other quest titles: Stinky Feet (locale 7955/7956), Slow and Steady (locale 7951/7952), Meet the Boss (locale 7960/7961). Locale 7966 is a flagged duplicate and is not used.", "source": "locale:7951; locale:7952; locale:7955; locale:7956; locale:7960; locale:7961"},
  {"claim": "Madam Zelda in Blackspore Swamp starts the Heroes series, gathers the Realmkeepers, and sets up a final showdown with the Baron.", "source": "http://www.freerealms.com/article/detail.action?articleId=2746; http://www.freerealms.com:80/article/detail.action?articleId=2734"},
  {"claim": "Article 2733 names Ghostshadow, Magetech and Wildclaw as Realmkeepers (Bryce=Ghostshadow, Nathan=Magetech, Kade=Wildclaw). Crackshot's Realmkeeper status rests on the wiki category only.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733; wiki: Realmkeepers, Crackshot"},
  {"claim": "Quest objective 'A True Hero' reads 'Complete the Heroes Questline.' (objective string, not a quest title)", "source": "locale:441610"},
  {"claim": "Later state change (undated): 'TCG Sets 1 - 4 Quests now free to play!'", "source": "locale:17473"},
  {"claim": "Article 2737 (Spanish, relative date only) describes expansion features: single-player scenarios with prizes, discount cards, large tournaments, hero loot cards. Undated; used only as a feature description.", "source": "http://www.freerealms.com/article/detail.action?articleId=2737"}
 ],
 "confidence": 0.4,
 "open": [
  "Date: 2012-08-25 rests on one Ten Ton Hammer repost of an SOE release. Treat as 'Aug 2012, day unverified' until a dated freerealms.com release is found.",
  "Merge: the pack combined three things: (a) the TCG Set 4 card release (this entry), (b) the Madam Zelda Heroes questline (a linked activity here, with no separate dated source), and (c) article 2737 expansion features (undated). Split into separate calendar entries if the rebuild needs them. The pack title 'Heroes new content' is not used as an alias because it is a pack title, not a name the event carried.",
  "Roster conflict: article 2737 (per pack summary) names Bryce, Nathan, Onofre and Jessica. Only article 2733 is used for the Realmkeeper mapping; Onofre and Jessica are not sourced to the event and are left out.",
  "Pre-launch preview: article 2736 describes a plan, not a live event. Undated, not counted as an occurrence.",
  "Live status: the 2012 run is sourced; whether it runs today is unknown, so 'unsure'.",
  "Price: 249 vs 224 station_cash conflict unresolved; price null.",
  "Quest id check: Heart of Darkness now cites locale 7947 (verified). The earlier ids 7948/7949 were not re-verified and are not cited as title ids. Ids for Stinky Feet, Slow and Steady and Meet the Boss come from the earlier pack and were not re-checked here.",
  "Excluded name collisions: Heroes Booster Bundle sales (locale 7973, 7974, 9403; Black Friday frames); the December 2012 Snow Days bundle; article 2764 (sale of TCG Sets 1-3); and locale 9922, a Halloween seasonal bundle with two Heroes packs, two Baron von Darkcheat packs and a Pumpkin Prince promo. Each has its own date and is not this event.",
  "Bud Grimyfoot is a dialog line (locale 7958), not a quest. Gloamstone and Sparky left out for lack of Heroes-tied text.",
  "Articles 2735 and 2738 were not read."
 ]
}
