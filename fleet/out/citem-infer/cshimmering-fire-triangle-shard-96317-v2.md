<!-- fleet job=citem-infer id=cshimmering-fire-triangle-shard-96317-v2 status=done turns=3 usd=0.0020 tokens(read,write,in,out)=[10360, 8736, 8, 1678] model=claude-haiku-5-5 -->
# Shimmering Fire Triangle Shard

{"item": {"name": "Shimmering Fire Triangle Shard", "locale_id": 96317, "kind": "other"},
 "sources": [{"type": "coin_shop", "detail": "Coin store sale, vendor/NPC not yet mapped (store category 121; source_tags L1, L2, L4, R2, T633, R1)", "where": null, "price": "866 coins (member price 779 coins, 10% member discount; sell price 86 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:8080 (item_id 30911); client definition coin_store_prices 866"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client text exists for the name: locale:96317 'Shimmering Fire Triangle Shard' (item class 68, slot 12, definition 30911).", "source": "locale:96317"},
  {"claim": "Store row for item 30911 exists: category 121, purchase price 866 coins, member price 779 coins, sell price 86 coins, no_sale:false. This matches the client coin store price of 866. The previous answer's claim that no row exists was wrong.", "source": "repo:prototype/osfr-tools/data/content/stores.json:8080"},
  {"claim": "Category 121 holds many coin-store items priced in the same tiers (540, 866, 1780), so the price tier alone does not identify a single vendor. The row itself is the evidence of a coin sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:596-621"},
  {"claim": "No wiki page, article, video frame, or vendor-stock entry names this shard, so the NPC vendor and the store listing's live date are unverified.", "source": "lookup (client, wiki) for 'Triangle Shard' returned only client text lines"},
  {"claim": "The sibling Shimmering Air Triangle Shard is a quest reward (Peep's Missing Bowl). That is a different item and does not source the Fire shard.", "source": "video:3JXpHghLOTs/00014.jpg; prototype/osfr-tools/data/content/quests/adventurer.json:1451"}
 ],
 "confidence": 0.5,
 "open": [
  "Vendor/NPC that sells item 30911 is not mapped from stores.json; the store row only gives category 121 and the price. Find the NPC whose store lists category 121 or item 30911.",
  "Live status: stores.json has no_sale:false, which suggests it is sold, but no wiki or article source confirms current availability. Treat live as likely yes, unverified.",
  "Retirement is unknown; no source states when, or whether, the item was removed.",
  "Shard family members (Glowing Air/Wind/Void, Shimmering Sun/Light) have no sources in the evidence. Check whether they share the same store category.",
  "The critique's claim that the Fire shard is in no job-set list is unverified here and is not used as evidence."
 ]}
