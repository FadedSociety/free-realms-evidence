<!-- fleet job=event-infer id=vheroes-new-content-v5 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[9042, 9334, 6, 3084] model=claude-haiku-5-5 -->
# Heroes new content

```json
{
 "event": {
  "name": "Heroes (Free Realms Trading Card Game Set 4: Heroes)",
  "aliases": ["TCG Set 4: HEROES", "Heroes Booster Pack (item)", "Heroes new content (pack title; may merge events, see open)"]
 },
 "kind": "update",
 "live": "unsure",
 "occurrences": [
  {"year": 2012, "when": "Aug 25 (card-set launch; day is from one secondary summary, not a verbatim quote)", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game (single source; quote: 'launches with 76 cards made up of 54 booster cards and 22 promo cards')"}
 ],
 "recurring": null,
 "zones": ["Blackspore Swamp (Madam Zelda starts the series; http://www.freerealms.com/article/detail.action?articleId=2746; articleId=2734)", "Seaside (locale:7961)"],
 "npcs": ["Madam Zelda", "Baron von Darkcheat", "Ghostshadow", "Magetech", "Wildclaw", "Crackshot", "Bud Grimyfoot (locale:7958, dialog line)"],
 "quests": ["Card Duelist: Stinky Feet", "Card Duelist: Slow and Steady", "Card Duelist: Heart of Darkness", "Card Duelist: Meet the Boss"],
 "activities": ["Play Free Realms Trading Card Game matches, including against Baron von Darkcheat (locale:7961)", "Complete the Heroes questline (locale:441610)"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": "station_cash", "source": "locale:17471 (item description: 10 random TCG cards plus one loot card). Price conflict: 249 (video:fjZluIfbUIo/00058.jpg, video:1LjCvhboCkQ/00188.jpg, 00190.jpg) vs 224 (video:9NOkMosko1E/00024.jpg). Unsettled, so null."}
 ],
 "rewards": ["Heroes loot cards (locale:17471)", "Outfit from opening a Heroes TCG pack (wiki: Crackshot)", "Baron von Darkcheat's ride and in-game poster after defeating him (wiki: Magetech)"],
 "evidence": [
  {"claim": "Heroes is the fourth set of the Free Realms Trading Card Game; the Realmkeepers help stop Baron von Darkcheat.", "source": "locale:17471; locale:17473"},
  {"claim": "Set launched with 76 cards (54 booster, 22 promo) and four new TCG quests including Stinky Feet and Slow and Steady.", "source": "http://www.tentonhammer.com:80/free-realms/news/free%20Relams%20Gets%20a%20New%20Trading%20Card%20Game"},
  {"claim": "Store frame shows TCG Set 4 Available Now (undated frame).", "source": "video:fjZluIfbUIo/00058.jpg; locale:17473"},
  {"claim": "Quest titles confirmed: Stinky Feet (locale 7955/7956), Slow and Steady (locale 7951/7952), Heart of Darkness (locale 7948/7949), Meet the Boss (locale 7960/7961). Locale 7966 is a flagged duplicate and is not used.", "source": "locale:7948; locale:7949; locale:7951; locale:7952; locale:7955; locale:7956; locale:7960; locale:7961"},
  {"claim": "Madam Zelda in Blackspore Swamp starts the Heroes series, gathers the Realmkeepers, and sets up a final showdown with the Baron.", "source": "http://www.freerealms.com/article/detail.action?articleId=2746; http://www.freerealms.com:80/article/detail.action?articleId=2734"},
  {"claim": "Realmkeepers named in the arc: Ghostshadow, Magetech, Wildclaw, Crackshot.", "source": "wiki: Realmkeepers, Crackshot, Magetech, Wildclaw, Ghostshadow; http://www.freerealms.com:80/article/detail.action?articleId=2733"},
  {"claim": "Quest objective 'A True Hero': Complete the Heroes Questline.", "source": "locale:441610"},
  {"claim": "Later state change (undated): 'TCG Sets 1 - 4 Quests now free to play!'", "source": "locale:17473"},
  {"claim": "Article 2737 (Spanish, undated, relative date only) describes the expansion: single-player scenarios with prizes, discount cards, large tournaments, hero loot cards.", "source": "http://www.freerealms.com/article/detail.action?articleId=2737"}
 ],
 "confidence": 0.4,
 "open": [
  "Date: 2012-08-25 rests on one Ten Ton Hammer repost. The card count is quoted there, but the day is not verbatim in the pack. Confirm against a dated freerealms.com press release before scheduling; treat as 'Aug 2012, day unverified' until then.",
  "Pack merge: 'Heroes new content' may combine (a) the TCG Set 4 card release, (b) the Madam Zelda Heroes questline, and (c) the expansion features of article 2737. Split into separate calendar entries if the rebuild needs them. This record covers all three as one event because the sources tie them together, but it is not decided.",
  "Roster conflict: article 2737 (per pack summary) names the child Defenders Bryce, Nathan, Onofre and Jessica. Article 2733 maps Ghostshadow=Bryce, Magetech=Nathan, Wildclaw=Kade, and Crackshot is unassigned. Onofre and Jessica do not appear in 2733. Do not use 2737 as a roster source.",
  "Pre-launch preview: article 2736 (log in to review the new heroes before release) describes a plan, not a live event. It is undated and not counted as an occurrence.",
  "Live status: the 2012 run is sourced. Whether the set is live today is unknown, so 'unsure'.",
  "Price: 249 vs 224 station_cash conflict is unresolved. Price stays null.",
  "Quests: 'A True Hero' is an objective string (locale 441610), not a quest title, so it is left out. The arc may hold further quest titles not in the pack.",
  "Excluded name collisions: Heroes Booster Bundle sales (locale 7973, 7974, 9403; Black Friday frames), the December 2012 Snow Days bundle, and article 2764 (sale of TCG Sets 1-3). Each has its own date and is not this event.",
  "Bud Grimyfoot is a dialog line (locale 7958), not a quest. Gloamstone and Sparky were left out for lack of Heroes-tied text in the pack.",
  "Articles 2735 and 2738 were not in the pack and were not read."
 ]
}
```
