<!-- fleet job=citem-infer id=cchef-s-power-shard-of-talent-v-132118-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5941, 9620, 6, 1725] model=claude-haiku-5-5 -->
# Chef's Power Shard of Talent V

{"item": {"name": "Chef's Power Shard of Talent V", "locale_id": 132118, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing, store item 75672 (store category 121). No named NPC vendor or wiki page names this item, so no vendor is evidenced.", "where": "Coin store (category 121)", "price": "2152 coins purchase; member price 1936 coins (10% member discount); sell-back 215 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15470 (item_id 75672, category_id 121, purchase_price_coins 2152, member_price_coins 1936, sell_price_coins 215)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale:132118 \"Chef's Power Shard of Talent V\"; definition id 75672; slot 12, class 21; client coin_store_prices value 2152 matches the store row", "source": "locale:132118; client definition in pack"},
  {"claim": "Store row for item 75672 is in category 121 with purchase 2152 coins, 10% member discount, member price 1936, sell price 215, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json:15470"},
  {"claim": "Same store category and identical tags (L1, L2, L4, R2, T633, R1) and price tier as neighbouring rows 75668-75673, so the row belongs to a batch of Chef-named shards; that grouping is name-based inference only", "source": "repo:prototype/osfr-tools/data/content/stores.json:15466-15471"},
  {"claim": "A search of the repo for 75672 finds only the store row (no vendors.json, quest, recipe or drop entry). Wiki Chef NPC sell lists in the pack (Mikael, Nadia, Skye, Zamzani, Ingrid, Rachael, Lorraine) show other tiers or Timing V, not Talent V, so they are not evidence for this item", "source": "repo search for 75672; wiki pages named in the pack"},
  {"claim": "Miner's Power Shard of Talent V (Kallie, Sunstone Valley) is a different item and is not a source for this one", "source": "pack critique (evidence lens)"}
 ],
 "confidence": 0.4,
 "open": [
  "No NPC vendor, quest, drop, crafting, collection or prize-wheel source is evidenced for this item. The coin store row is the only source.",
  "Store category 121 is not named in the repo data, so the 'Coin Shop' label is not confirmed; the row is recorded as a coin store listing only.",
  "Live status unsure: the store row carries source tags with no retirement note, and no date or patch evidence was found. A lookup on the exact item name failed (FTS5 syntax error on the apostrophe), so wiki, article and video coverage of the name was not re-checked here.",
  "The 'Chef vendor' link in the first answer is not supported. Do not present any Chef NPC as a seller of this item until a wiki or vendor list names it."
 ]}
