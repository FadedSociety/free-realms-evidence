<!-- fleet job=event-infer id=vheroes-new-content-v7 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[16911, 10028, 8, 3917] model=claude-haiku-5-5 -->
# Heroes new content

{
 "event": {
  "name": "Heroes (Free Realms Trading Card Game Set 4: Heroes)",
  "aliases": ["TCG Set 4: HEROES", "Heroes Booster Pack (item name, not the event)"]
 },
 "kind": "update",
 "live": "unsure",
 "occurrences": [
  {
   "year": 2012,
   "when": "Aug 2012, day unverified (Ten Ton Hammer repost of an SOE release gives 2012-08-25; no dated freerealms.com page confirms the day)",
   "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (summary: launched with 76 cards, 54 booster and 22 promo, and four quests leading to a final boss)"
  }
 ],
 "recurring": null,
 "zones": ["Blackspore Swamp (locale:7952, locale:7956, locale:7960; article 2734)", "Seaside (locale:7961)"],
 "npcs": ["Madam Zelda (article 2734; locale:7952)", "Baron von Darkcheat (locale:7961; locale:17471)", "Ghostshadow, Magetech, Wildclaw (Realmkeepers) (article 2733 summary; wiki: Wildclaw)", "Crackshot (wiki category: Realmkeepers only; not in article 2733)"],
 "quests": ["Card Duelist: Stinky Feet (locale:7955)", "Card Duelist: Slow and Steady (locale:7951)", "Card Duelist: Heart of Darkness (locale:7947)", "Card Duelist: Meet the Boss (locale:7959)"],
 "activities": [
  "Play Free Realms Trading Card Game matches, including against Baron von Darkcheat in Seaside (locale:7961)",
  "Work through the Madam Zelda Heroes questline in Blackspore Swamp, distracting the Baron's men while the Realmkeepers train (article 2734; locale:7952, 7956, 7960)",
  "Open Heroes booster packs for loot cards (locale:17471, locale:17473)"
 ],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": "station_cash", "source": "locale:17471 (10 random TCG cards plus one loot card). Price conflict 249 vs 224 station_cash is unresolved, so price is null."}
 ],
 "rewards": [
  "Heroes loot cards (locale:17471, locale:17473)",
  "Outfit from opening a Heroes TCG pack (wiki: Crackshot)",
  "Baron von Darkcheat's ride and in-game poster after defeating him (wiki: Magetech)"
 ],
 "evidence": [
  {"claim": "Heroes is the fourth set of the Free Realms Trading Card Game; the Realmkeepers help stop Baron von Darkcheat.", "source": "locale:17471"},
  {"claim": "Store announcement 'TCG Set 4: HEROES Available Now!' (undated).", "source": "locale:17472"},
  {"claim": "Launch text: 'The newest Free Realms Trading Card Game Set is here!', 'New Quests For Level 20 Card Duelists!', and later 'TCG Sets 1 - 4 Quests now free to play!' (the free-quest line is an undated later change).", "source": "locale:17473"},
  {"claim": "Set launched with 76 cards (54 booster, 22 promo) and four quests leading to a final boss; date 2012-08-25 from a secondary repost only.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game"},
  {"claim": "Madam Zelda in Blackspore Swamp starts the Heroes series; players keep Baron von Darkcheat busy while four Realmkeepers train, ending in a final reckoning with the Baron.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2734"},
  {"claim": "Article 2733 names the four Realmkeepers as Ghostshadow (Bryce), Magetech (Nathan), Wildclaw (Kade) and a fourth kid (Jessica). Wiki Wildclaw confirms Kade is Wildclaw.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2733; wiki: Wildclaw"},
  {"claim": "Quest titles verified by locale: 7947 Heart of Darkness, 7951 Slow and Steady, 7955 Stinky Feet, 7959 Meet the Boss. Ids 7952, 7956, 7960 and 7961 are objective text, not titles.", "source": "locale:7947; locale:7951; locale:7955; locale:7959"},
  {"claim": "Quest objective text 'Complete the Heroes Questline.' exists, but it is an objective string, not a quest title.", "source": "locale:441610"},
  {"claim": "Article 2737 (Spanish, relative date only) describes expansion features: single-player scenarios with prizes, discount cards, large tournaments, hero loot cards. Undated, used only as a feature description.", "source": "http://www.freerealms.com/article/detail.action?articleId=2737"}
 ],
 "confidence": 0.4,
 "open": [
  "Date: 2012-08-25 rests on one Ten Ton Hammer repost of an SOE release. Treat as 'Aug 2012, day unverified' until a dated freerealms.com release is found.",
  "Merge: this record covers only the TCG Set 4 card release. The Madam Zelda Heroes questline (article 2734, quest locales) and the article 2737 expansion features are linked activities here, not separate dated events. Split them into their own calendar entries if the rebuild needs that. The pack title 'Heroes new content' is not an alias: it is a pack title, not a name the event carried.",
  "Article 2746 was cited for the Zelda series start but was not checked. Article 2734 is the verified source for that claim.",
  "Article 2733 is cited for the Realmkeeper names. The pack's roster list for article 2737 (Onofre, Jessica) is not tied to the event and is left out, apart from Jessica as the fourth Realmkeeper in 2733.",
  "Article 2736 is a pre-launch preview describing a plan, not a live event. Undated, not counted as an occurrence.",
  "Live status: the 2012 run is sourced, but whether it runs today is unknown, so 'unsure'.",
  "Price conflict 249 vs 224 station_cash is unresolved; price is null.",
  "Excluded name collisions, each with its own date or event: Heroes Booster Bundle sales (locale 7973, 7974, 9403; Black Friday frames); the December 2012 Snow Days bundle; article 2764 (sale of TCG Sets 1-3); locale 9922, a Halloween seasonal bundle with two Heroes packs, two Baron von Darkcheat packs and a Pumpkin Prince promo.",
  "Bud Grimyfoot is a dialog line (locale 7958), not a quest. Gloamstone and Sparky are left out for lack of Heroes-tied text (Sparky appears only as Magetech's hoverboard in article 2733).",
  "Articles 2735 and 2738 were not read."
 ]
}
