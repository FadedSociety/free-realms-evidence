<!-- fleet job=citem-infer id=csoaring-eagle-scythe-98713-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[5979, 7451, 6, 1736] model=claude-haiku-5-5 -->
# Soaring Eagle Scythe

{"item": {"name": "Soaring Eagle Scythe", "locale_id": 98713, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Coin store sale row, store category 207; vendor NPC/shop not named in our data. Tint groups 1 and 2 (items 38152, 38155) at 1236 coins; tint group 3 (item 38158) at 1069 coins. Member price 1112 / 962 coins (10% member discount). Sell price 123 / 106 coins.", "where": null, "price": "1236 coins (tint groups 1 and 2); 1069 coins (tint group 3)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12342-12344 (items 38152, 38155, 38158, category_id 207)"},
  {"type": "other", "detail": "Trade only, per wiki (player-to-player trade; trade partner and price not documented)", "where": null, "price": null, "currency": null, "source": "wiki page: Soaring Eagle Scythe ('can only be acquired through trade')"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 98713 = 'Soaring Eagle Scythe'; the item is a Ninja level 12 weapon with a Green Text tag.", "source": "locale:98713; wiki page: Soaring Eagle Scythe"},
  {"claim": "Wiki says the weapon is a level 12 Ninja Green Text weapon that can only be acquired through trade.", "source": "wiki page: Soaring Eagle Scythe"},
  {"claim": "Wiki page is in Category:Retired Weapons.", "source": "wiki page: Soaring Eagle Scythe (categories)"},
  {"claim": "Store rows exist for item 38152 (1236 coins, tint 1), 38155 (1236 coins, tint 2) and 38158 (1069 coins, tint 3), all category 207, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12342-12344"},
  {"claim": "Store rows carry source_tags L1, L2, L4, R2, T633, R1; their meaning is not defined in the pack.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12342-12344"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the wiki says trade-only, while stores.json lists coin sale prices for three tints. Both are kept as sources. Which is current is unresolved.",
  "The vendor NPC or shop for store category 207 is not identified. Category 207 is shared by unrelated items, so it is not a vendor identity; the coin source is labelled 'other' rather than 'vendor'.",
  "Retired status rests only on the wiki Category:Retired Weapons. The store rows have no_sale false and sell prices, which suggests a sale may still be active. Live status is unconfirmed.",
  "Seven of the ten definition ids (38162, 38165, 38168, 38172, 38175, 38180, 38184) have no store row. Their sources are unverified.",
  "The meaning of source_tags L1, L2, L4, R2, T633, R1 is not defined in the pack; they may hint at where the item is sold but are not used as evidence.",
  "No sale date, quest, drop or event source was found. The wiki gives no trade price."
 ]}
