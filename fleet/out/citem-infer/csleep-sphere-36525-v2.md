<!-- fleet job=citem-infer id=csleep-sphere-36525-v2 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[18729, 13444, 8, 2461] model=claude-haiku-5-5 -->
# Sleep Sphere

{"item": {"name": "Sleep Sphere", "locale_id": 36525, "kind": "consumable"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop battle-item sale (category 53, orb family); store row item_id 36525. Price unresolved: repo store row says purchase 2000 coins (member 1800, 10% discount, sell-back 200); wiki says 50 coins. Neighbouring rows in category 53 (36514-36534) run 50-400 coins, so 2000 is likely a data error but is unverified.", "where": "Coin Shop", "price": "UNRESOLVED: 2000 coins per repo (member 1800); 50 coins per wiki", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 11996 (item_id 36525, category_id 53); wiki page 'Sleep Sphere' (\"sells for 50 coins\")"},
  {"type": "prize_wheel", "detail": "Battle Item Mystery Pack (prize-wheel reward granting 3 battle items). Weak, unverified: the wiki says the Sleep Sphere comes from these packs, but the pack page does not name it and no specific wheel is identified.", "where": "combat prize wheels", "price": null, "currency": null, "source": "wiki page 'Sleep Sphere' (acquisition sentence); wiki page 'Battle Item Mystery Pack'"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name 'Sleep Sphere' is locale 36525, description 'A magical orb that puts opponents to sleep.'; definition ids 3011 and 10516; class 9, slot 0", "source": "locale:36525; client definition pack"},
  {"claim": "Store row for item 36525 exists in category 53 with purchase 2000 coins, member 1800, sell 200, no_sale false; the repo row is confirmed by direct read", "source": "repo:prototype/osfr-tools/data/content/stores.json line 11996"},
  {"claim": "Other server data (Lxzxrus-Free-Realms-Server and FreeRealms-Legacy CoinStoreItems.json) lists item 36525 in category 53 but carries no price field, so it adds category membership only, not a price", "source": "refs:Lxzxrus-Free-Realms-Server/src/Resources/CoinStoreItems.json line 53860; refs:FreeRealms-Legacy/src/Resources/CoinStoreItems.json line 53856"},
  {"claim": "Wiki: Sleep Sphere is a level 1 battle item usable in any job; acquired from the Coin Shop (wiki price 50 coins) and from Battle Item Mystery Packs; puts enemies to sleep for about ten seconds", "source": "wiki page 'Sleep Sphere'"},
  {"claim": "Battle Item Mystery Pack is a prize-wheel reward granting 3 battle items; the pack page does not list the Sleep Sphere", "source": "wiki page 'Battle Item Mystery Pack'"},
  {"claim": "Related client abilities 'Improved Sleep Sphere' and 'Improved Sleep Sphere Chain' exist (locale 429992-429995); they are abilities, not separate purchasable items", "source": "locale:429992, locale:429993, locale:429994, locale:429995"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin Shop price conflict: repo store row says 2000 coins (member 1800); wiki says 50 coins. Do not publish a price until a live Coin Shop screen or a dated price source resolves it.",
  "Prize-wheel / Battle Item Mystery Pack source rests only on one wiki acquisition sentence; no pack or wheel listing names the Sleep Sphere.",
  "No retirement date found in wiki, video or articles; store row no_sale is false, so it appears to have been on sale, but the source tags (L1, L2, L4, R2, T633, R1) carry no dates. retired left null.",
  "Client definition has two definition ids (3011, 10516); which one is the sold/used item is not established by the evidence.",
  "Prior answer's 'verified' claim that the client carries no store price was wrong for the repo store data; the store row exists (line 11996), but it is the only priced source."
 ]}
