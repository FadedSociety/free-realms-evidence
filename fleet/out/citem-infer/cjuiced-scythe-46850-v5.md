<!-- fleet job=citem-infer id=cjuiced-scythe-46850-v5 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6459, 10024, 6, 2369] model=claude-haiku-5-5 -->
# Juiced Scythe

{"item": {"name": "Juiced Scythe", "locale_id": 46850, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin store listing (stores.json category 207, undecoded; seller/shop not identified). Store row for item 48132 with the client definition's coin_store_prices [1236]. Not confirmed as a named NPC or shop.", "where": null, "price": "1236 coins (member price 1112 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13188 (item 48132); client definition coin_store_prices [1236]"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki. No NPC, shop, quest or drop named.", "where": null, "price": null, "currency": null, "source": "wiki page: Juiced Scythe ('can only be acquired through trade')"}
 ],
 "retired": true,
 "live": "unsure",
 "evidence": [
  {"claim": "Juiced Scythe is locale:46850, a level 8 Ninja Blue Text weapon with Flame Flash (1357 damage) and Dragonstrike (6107 damage); it is listed in the Juiced set on the Blue Text weapon page.", "source": "locale:46850; wiki page: Juiced Scythe; wiki page: Blue Text weapon"},
  {"claim": "The wiki says the weapon 'can only be acquired through trade'.", "source": "wiki page: Juiced Scythe (lookup result, re-checked)"},
  {"claim": "stores.json item 48132 is category 207, purchase_price_coins 1236, member_price_coins 1112 (10% discount), sell_price_coins 123, no_sale false. The client definition 48132 carries coin_store_prices [1236].", "source": "repo:prototype/osfr-tools/data/content/stores.json:13188; client definition"},
  {"claim": "The 48132 row sits in a block (48122-48144) where many rows share the same source_tags and only three price levels (1236, 1656, 2204) repeat, so the price pattern looks template-like rather than item-specific.", "source": "repo:prototype/osfr-tools/data/content/stores.json:13178-13200 (re-checked)"},
  {"claim": "The Electric Oil Flair Shard duplicates the Juiced particle effect (Bow, Drill, Saw, Scythe, Hammer, Wand). It is Cannot Trade and does not describe how the scythe is obtained.", "source": "wiki page: Electric Oil Flair Shard"},
  {"claim": "Retired status comes from the wiki Category:Retired Weapons listing given in the pack. No sale end date is recorded.", "source": "wiki page: Juiced Scythe (category list, as carried in the evidence pack; not re-verified by a direct category lookup)"}
 ],
 "confidence": 0.5,
 "open": [
  "The coin store row (stores.json item 48132, 1236 coins) is the only price evidence. Category 207 is undecoded, so the shop and seller are unknown. The 'vendor' type is backed only by the client coin_store_prices rule, not by a named NPC or shop.",
  "The row is one of a repeating template-like block (48122-48144) with the same tags and price levels. It may not be a real individual sale of this weapon, which conflicts with the wiki's trade-only statement.",
  "Definition 22100 has no store row, so it is unclear whether it is sold or is a variant of 48132.",
  "No dated sale start or end exists. Whether the coin store listing was ever live, and when it stopped, is unknown.",
  "The wiki's Category:Retired Weapons claim was not re-verified by a direct category lookup.",
  "Sibling Juiced items (Bow, Drill, Saw, Hammer, Wand) were not checked for their own store rows, so the set pattern is unconfirmed.",
  "Trade is player-to-player, with no trade counterpart or trade-era detail in the pack.",
  "sell_price_coins 123 is a sell-back value and is not used as an acquisition price.",
  "Wireable only in the weak sense: the 1236-coin listing is the one priced source, but its seller is unnamed, so the vendor source needs a named shop before a live vendor can be wired."
 ]
}
