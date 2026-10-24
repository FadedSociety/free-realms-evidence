<!-- fleet job=citem-infer id=ctoxic-malice-99036-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5678, 9201, 6, 1718] model=claude-haiku-5-5 -->
# Toxic Malice

{"item": {"name": "Toxic Malice", "locale_id": 99036, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store weapon listing (store category 207); the selling NPC/vendor is not identified in any evidence", "where": null, "price": "1431 coins (member price 1287 coins, 10% member discount; sell-back 143 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 38475 (line 12367; purchase_price_coins 1431, member_price_coins 1287, sell_price_coins 143, no_sale false)"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is 'Toxic Malice', locale 99036, definition 38475, weapon slot 7, class 17.", "source": "locale:99036"},
  {"claim": "Store row for item 38475 in category 207 lists purchase 1431 coins, member price 1287, sell-back 143, not no_sale. This matches the client's coin_store_prices value of 1431.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 38475 (line 12367)"},
  {"claim": "Wiki: Toxic Malice is a level 12 Warrior Blue Text weapon, Power 5, Sweeping Slash 2609 dmg, Spinning Attack 4732 dmg, and 'can only be acquired through trade'.", "source": "wiki page: Toxic Malice"},
  {"claim": "Wiki page is in Category:Retired Weapons.", "source": "wiki page: Toxic Malice (category list)"},
  {"claim": "Wiki tooltip 'Resell Value: 143' matches the store sell-back price of 143 coins.", "source": "wiki image: File:Toxic Malice item.jpg (item_tooltip)"},
  {"claim": "The Blue Text weapon page lists [Toxic] [Malice] and Venom's Malice in the Toxic/Venom family.", "source": "wiki page: Blue Text weapon"},
  {"claim": "Conflict: the wiki's trade-only statement is a player-to-player source and is not a vendor source. It conflicts with a live coin store row, so the vendor source is unconfirmed.", "source": "wiki page: Toxic Malice"}
 ],
 "confidence": 0.4,
 "open": [
  "The vendor/NPC that sells item 38475 is not identified. stores.json gives a category (207) and price, but no stock location or NPC. The 'where' field is left null.",
  "Category 207 holds many weapon rows, and the source_tags (L1, L2, L4, R2, T633, R1) are not explained in the pack, so they are not used as vendor IDs.",
  "Whether the coin listing was still sold at the end of the server's run is unknown. The wiki's Retired category and 'acquired only through trade' wording conflict with a live listing. live is 'unsure'.",
  "The 'trade' source has no named trade partner or market, so it is not listed as a source.",
  "Jev's first pass said live: yes; this is overruled by the Retired category and trade-only wording, so live is 'unsure'.",
  "No quest, drop, event, or crafting source was found in the pack. Video frames and article facts were not checked for this item."
 ]}
