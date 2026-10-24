<!-- fleet job=citem-infer id=cshimmering-dreadful-triangle-shard-86225-v1 status=done turns=5 usd=0.0049 tokens(read,write,in,out)=[49126, 22676, 12, 3081] model=claude-haiku-5-5 -->
# Shimmering Dreadful Triangle Shard

{"item": {"name": "Shimmering Dreadful Triangle Shard", "locale_id": 86225, "kind": "other"},
 "sources": [{"type": "vendor", "detail": "Coin store, store category 121 (the store row is for item 22234; the vendor NPC/shop that holds category 121 is not identified in the repo)", "where": null, "price": "866 coins (member price 779 coins, 10% member discount; sell-back 86 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 22234 (line 6649)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client item name is locale 86225 'Shimmering Dreadful Triangle Shard', definition id 22234, slot 12, class 50", "source": "locale:86225"},
  {"claim": "Store row for item 22234 is in category 121 at 866 coins, member price 779, sell price 86, not marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json item 22234 (line 6649)"},
  {"claim": "Sibling shards in the same 'Shimmering/Glowing <Element> Triangle Shard' series (locale 86216-86232) share the same store category and 866-coin price (e.g. item 22233, 22235-22241), and the Glowing/Pulsing variants show this is a tiered stat-shard family", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6648-6656; locale:86216, 86224, 86226"},
  {"claim": "Triangle shards in the game are equippable stat items (e.g. 'increases Defense strength for any Combat Job as long as it is equipped')", "source": "locale text in opening-harvesting-native-20261009T142624Z/locale/en_us_data.dat lines 664 and 1139"},
  {"claim": "A sibling 'Shimmering Air [Triangle] [Shard]' was a quest reward from Posy's Missing Bowl (Farnum Farmstead), showing shards also come from quests", "source": "video:3JXpHghLOTs/00014.jpg"}],
 "confidence": 0.35,
 "open": ["The vendor that sells store category 121 was not identified. vendor_stock was empty and vendors.json has no row for item 22234, so the NPC and zone are unknown.",
  "No wiki page, article, or video names this specific shard. The 'Shimmering' tier and the 'Dreadful' element were not confirmed as a coin-store-only item.",
  "Retired status is unknown. The store row has no retire flag, and no source says the item was removed.",
  "The 'Pulsing Dreadful Triangle Shard' (FreeRealms-Legacy ClientItemDefinitions.json line 192401) and 'Glowing Dreadful Triangle Shard' (locale 86216) are sibling tiers. Their sources were not checked and may differ.",
  "Other shard sources (crafting, enemy drops, prize wheel, collections) were not checked for this item."]}
