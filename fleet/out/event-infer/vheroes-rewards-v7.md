<!-- fleet job=event-infer id=vheroes-rewards-v7 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[6856, 9466, 6, 2612] model=claude-haiku-5-5 -->
# Heroes rewards

{"event": {"name": "Heroes (TCG expansion, TCG Set 4)", "aliases": ["TCG Set 4: HEROES", "TCG Set 4", "Heroes Booster Pack", "Heroes Booster Bundle (25 Pack)", "Heroes (Free Realms Trading Card Game expansion)"]},
 "kind": "update",
 "live": "unsure",
 "occurrences": [
  {"year": 2012, "when": "2012-08-25 (launch, per secondary source; day given, no month/day confirmed from the SOE original)", "source": "articles/articles.json:19147-19150 (Ten Ton Hammer repost of SOE press release: Heroes 'launched' 2012-08-25, 76 cards, four quests ending in boss fight vs Baron von Darkcheat)"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["single-player TCG scenarios (http://www.freerealms.com/article/detail.action?articleId=2744)", "TCG tournaments with promo cards (articleId=2744)", "buying and opening Heroes booster packs and bundles (store text)"],
 "items": [
  {"name": "Heroes Booster Pack", "price": null, "currency": "station_cash", "source": "locale:17470 (name); price conflicts across video frames (249 vs 224), so null"},
  {"name": "Heroes Booster Bundle (25 Pack)", "price": null, "currency": "station_cash", "source": "locale:7973 (name); locale:9403 ('Save on TCG Set 4: Heroes Booster Bundles!'). refs/FreeRealms-Legacy/src/Resources/StoreBundles.json:24963 not yet opened"}
 ],
 "rewards": ["exclusive single-player scenario rewards (articleId=2744)", "tournament promo cards (articleId=2744)", "new loot cards (articleId=2744, articleId=2733)"],
 "evidence": [
  {"claim": "Heroes is the newest TCG expansion, with single-player scenarios, exclusive rewards, promo cards at major tournaments and new loot cards (German text; relative date only).", "source": "http://www.freerealms.com/article/detail.action?articleId=2744"},
  {"claim": "Heroes 'was released' and adds new features, single-player scenarios, tournament promo cards and new loot cards; headline 'Heroes ... is here!'.", "source": "http://www.freerealms.com/article/detail.action?articleId=2733"},
  {"claim": "Heroes launched 2012-08-25 as a free-to-play TCG with 76 cards (54 booster, 22 promo) and four quests ending in a boss fight against Baron von Darkcheat (secondary source, Ten Ton Hammer repost of SOE press release).", "source": "articles/articles.json:19147-19150"},
  {"claim": "Store title names the set: 'TCG Set 4: HEROES Available Now!'", "source": "locale:17472"},
  {"claim": "Heroes Booster Pack and Heroes Booster Bundle (25 Pack) are client item names.", "source": "locale:17470, locale:7973"},
  {"claim": "Store message ties Heroes Booster Bundles to TCG Set 4.", "source": "locale:9403"},
  {"claim": "Pumpkin Prince seasonal bundle contains two Heroes packs; separate seasonal promotion, not the event.", "source": "locale:9922"}
 ],
 "confidence": 0.5,
 "open": [
  "Launch date 2012-08-25 rests on one secondary source (Ten Ton Hammer repost of SOE release, articles.json:19147-19150). Verify against the SOE original or article 2733's posting date before wiring as fact.",
  "Article 2744 and 2733 give no absolute date in the pack.",
  "Live status: this is a TCG product release, not a timed in-game event window. Set live to 'unsure' until a dated in-game source is found.",
  "Pre-launch teaser (articles.json:19136) and 'Meet Free Realms' Newest Heroes' (articles.json:19164) are undated previews; not counted as live occurrences.",
  "Quests: articles.json:20158 (German quest-pack-free post) lists a Heroes quest series as the fourth of four series in a free progression (Meet the Card Players, Shattered Past, Baron von Dunkelschwindel, Heroes), and articles 19248, 20046, 20116, 20144 describe the same chain as the Heroes story. Quest titles are not confirmed: 'Stinky Feet' and 'Meet the Boss' are named in a Ten Ton Hammer 2012-08-25 mention per other notes, but I did not verify the article text, and 'Complete the Heroes Questline.' (locale:441610) is a single objective string. Left the quests list empty. Keep separate from the Series 3 'Baron von Darkcheat' set.",
  "Realm Guardians (Geisterschatten, Magotron, Wildkralle, Adlersehne; articles 2744, 2742) have no matching client NPC entries; npcs left empty.",
  "Price conflict: 249 vs 224 station_cash across undated frames. Left null.",
  "StoreBundles.json:24963 not opened; bundle item price and details unverified.",
  "Excluded: article 2876 (Rumbledome), article 2764 (Sets 1-3 sale), 'Hero of Heroes' (locale 4419490-4419502, not_live), generic 'hero' tournament text (locale 391785), locale:17473 (banner covering Sets 1-4), and Madam Zelda/Darkcheat strings (locale 7948, 7960, 7961, 7966, 439496) not tied to Heroes by name.",
  "Pack may conflate Heroes with the Series 3 TCG set via Baron von Darkcheat; treated separately."
 ]}
