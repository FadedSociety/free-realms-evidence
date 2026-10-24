<!-- fleet job=citem-infer id=cilluminating-scythe-71952-v2 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6352, 9810, 6, 1853] model=claude-haiku-5-5 -->
# Illuminating Scythe

{"item": {"name": "Illuminating Scythe", "locale_id": 71952, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store row, unnamed vendor and store. Store row lists purchase 1656 coins, member price 1490 coins (10% member discount), sell 165 coins, category 207 (category name not given in the data). Wiki does not mention this sale.", "where": null, "price": "1656 coins (member price 1490 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48134 (line 13190)"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki. No counterparty, price, or era.", "where": null, "price": null, "currency": null, "source": "wiki: Illuminating Scythe (\"can only be acquired through trade\")"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client name is locale 71952 'Illuminating Scythe'.", "source": "locale:71952"},
  {"claim": "Level 12 Ninja Blue Text weapon. Effects: Flame Flash 2372 damage, Dragonstrike 10674 damage. Wiki category: Retired Weapons.", "source": "wiki: Illuminating Scythe (Category:Retired Weapons)"},
  {"claim": "Wiki says the item can only be acquired through trade.", "source": "wiki: Illuminating Scythe"},
  {"claim": "Store row for item 48134 exists with purchase 1656, member 1490, sell 165, category 207, and matches the client coin_store_prices value 1656. Row names no vendor, store, or category name.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48134 (line 13190)"},
  {"claim": "The wiki 'Blue Text weapon' page lists Illuminating Scythe among Illuminating weapons, but the text I could retrieve contains no dungeon, drop, or members-only wording. The earlier dungeon-drop claim is removed.", "source": "wiki: Blue Text weapon"},
  {"claim": "Definition 22202 has no store row; the price applies only to definition 48134.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48134"}
 ],
 "confidence": 0.4,
 "open": [
  "The coin store row 48134 is not tied to a named vendor, store, or zone. Its category 207 is not named in the data, so calling it a weapon category is unverified. It is kept as a vendor-type source only because the rules treat a coin store price as vendor evidence; a builder should treat it as an unplaced row.",
  "Conflict: the wiki says trade-only and lists the item as retired, while the store row shows a coin sale. No live-era source confirms the coin sale was ever active. Treat the sale as unconfirmed until one is found.",
  "No drop source is supported. The earlier claim about Blue Text dungeon drops was not found in the wiki page and is dropped.",
  "No date for sale or retirement is given by any source; the Retired status rests on the wiki category alone.",
  "Trade is a player-to-player source with no price or era, so it cannot be wired as a source path."
 ]}
