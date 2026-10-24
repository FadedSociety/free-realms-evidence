<!-- fleet job=citem-infer id=cwizard-s-power-shard-of-vitality-i-131293-v1 status=done turns=8 usd=0.0082 tokens(read,write,in,out)=[150288, 33248, 18, 5033] model=claude-haiku-5-5 -->
# Wizard's Power Shard of Vitality I

{"item": {"name": "Wizard's Power Shard of Vitality I", "locale_id": 131293, "kind": "other"},
 "sources": [
  {"type": "prize_wheel", "detail": "Wizard prize wheel, Tavern Cellar dungeon (difficulty I; the wheel also has 49 Coins, a Battle Item Mystery Pack, Wizard's Ring of Energy I, and Wizard's Sparkle Twig of Glaciers)", "where": "Tavern Cellar (The Wilds, south of Wugachug)", "price": null, "currency": null, "source": "wiki-derived page notes/Build Guides/Content/Dungeons/Tavern Cellar.md lines 73-78 (wiki prize wheel by job, every name client-checked)"},
  {"type": "prize_wheel", "detail": "Wizard prize wheel, Snakes in a Maze dungeon", "where": "Snakes in a Maze", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Snakes in a Maze.md:67 (wiki)"},
  {"type": "prize_wheel", "detail": "Wizard prize wheel, Frostfang Snarlers dungeon", "where": "Frostfang Snarlers", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Frostfang Snarlers.md:67 (wiki)"},
  {"type": "prize_wheel", "detail": "Wizard prize wheel, Hot Springs Haven dungeon (wiki and client names checked)", "where": "Hot Springs Haven", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Hot Springs Haven.md:77 (wiki)"},
  {"type": "vendor", "detail": "Coin store sale; vendor NPC not identified in our data (client store row only)", "where": "Coin store (category 121)", "price": "750 coins (member price 675 coins, 10% member discount; sell-back 75 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 75549 (line 15367, from FreeRealms-Legacy CoinStoreItems)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name exists as locale 131293 \"Wizard's Power Shard of Vitality I\" and sits in the Power Shard of ... cluster (131288-131298).", "source": "locale:131293"},
  {"claim": "Item definition 75549 has a coin store price of 750 coins, member price 675.", "source": "repo:data/content/stores.json item 75549"},
  {"claim": "Wizard's Power Shard of Vitality I is one of the Wizard prize-wheel entries at Tavern Cellar, with the Battle Item Mystery Pack and the 49 Coins slot.", "source": "wiki-derived notes/Build Guides/Content/Dungeons/Tavern Cellar.md:78 (name client-checked)"},
  {"claim": "Same Wizard prize-wheel entry also appears at Snakes in a Maze, Frostfang Snarlers and Hot Springs Haven.", "source": "notes/Build Guides/Content/Dungeons/Snakes in a Maze.md:67; Frostfang Snarlers.md:67; Hot Springs Haven.md:77"},
  {"claim": "The shard's job-equivalent Archer/Brawler/Medic/Ninja/Warrior Vitality I shards are on the same dungeon wheels, so the set is a prize-wheel set across all six jobs.", "source": "Tavern Cellar.md:73-78"},
  {"claim": "The wiki lists Vitality I Power Shards for other jobs in merchant stock (e.g. Archer, Brawler, Warrior at Merry Vale/Greenwood), but no merchant stock line names the Wizard Vitality I shard.", "source": "notes/Build Guides/Content/NPCs/NPCs - Merry Vale.md:137-138; NPCs - Greenwood Forest.md:73; vendors_unresolved.json:3299"}
 ],
 "confidence": 0.6,
 "open": [
  "Which coin vendor sells item 75549 for 750 coins is not in our data: no vendors.json row names it and no merchant page lists the Wizard Vitality I shard (Glenda and Redsden list other Wizard shards). Coin-store vendor needs confirming.",
  "Wiki price (coin-store) for the shard itself is not in the wiki pages checked; the 750/675 figures are from the store data only.",
  "The Tavern Cellar page says the Wizard wheel carries 'Novice Wizard Slacks or Skirt' (both written); this does not change the shard source.",
  "Retired status and any later removal are unknown; no wiki page for this exact item was found, and the lookup tool could not run the apostrophe query (FTS error), so wiki/article/video checks for this name were not completed.",
  "Only the description/kind inference is ours: the client description is empty and class 8 / slot 12 suggest a power shard accessory slot; the first-pass 'tool' tag is not used."
 ]}
