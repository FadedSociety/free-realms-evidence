<!-- fleet job=citem-infer id=cjuiced-scythe-46850-v7 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6701, 7756, 6, 1845] model=claude-haiku-5-5 -->
# Juiced Scythe

{"item": {"name": "Juiced Scythe", "locale_id": 46850, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only, per the wiki ('can only be acquired through trade'). No NPC, quest, drop or event is named.", "where": null, "price": null, "currency": null, "source": "wiki page: Juiced Scythe (re-checked via lookup)"},
  {"type": "coin_shop", "detail": "Unattributed coin store row for item 48132, category 207 (category not decoded). Seller and shop not identified. The row sits in a block of template-like rows (stores.json 13176-13200) that repeat the same source_tags and price levels, so it may not be a real sale of this weapon. Unconfirmed.", "where": null, "price": "1236 coins (member price 1112 coins, 10% member discount); sell-back 123 coins, not an acquisition price", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13188 (item 48132, category 207); client definition coin_store_prices [1236]"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Juiced Scythe is locale:46850, a level 8 Ninja Blue Text weapon with Flame Flash (1357 damage) and Dragonstrike (6107 damage), part of the Juiced set listed on the Blue Text weapon page.", "source": "locale:46850; wiki page: Juiced Scythe; wiki page: Blue Text weapon"},
  {"claim": "The wiki states the weapon 'can only be acquired through trade'.", "source": "wiki page: Juiced Scythe"},
  {"claim": "stores.json item 48132 is category 207, purchase_price_coins 1236, member_price_coins 1112, sell_price_coins 123, no_sale false. Matches client coin_store_prices [1236].", "source": "repo:prototype/osfr-tools/data/content/stores.json:13188"},
  {"claim": "The wiki page carries Category:Retired Weapons, which is the basis for retired=true. Not separately fetched as a category page.", "source": "wiki page: Juiced Scythe (category list)"},
  {"claim": "Electric Oil Flair Shard (Cannot Trade) duplicates the Juiced particle effect on Bow, Drill, Saw, Scythe, Hammer and Wand. Cosmetic cross-reference only; it is not an acquisition route for the scythe.", "source": "wiki page: Electric Oil Flair Shard"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict: the wiki says trade-only, while stores.json row 48132 and the client coin_store_prices show a 1236-coin price. The coin row has no named seller or shop, and category 207 is undecoded. The coin source is kept but is unconfirmed; the evidenced route is player trade.",
  "The 48114-48149 block shares source_tags and cycles through 1236/1656/2204 prices, so the row may be a template. Sibling Juiced items' store rows were not checked.",
  "Definition 22100 has no store row. Whether it is a separate sold variant or a duplicate of 48132 is unknown.",
  "No sale start/end dates, so live status is unresolved. No wiki price or vendor_stock entry exists.",
  "Wireable: no evidenced NPC, shop, quest, drop or event route. A builder cannot wire an acquisition from the trade-only source."
 ]}
