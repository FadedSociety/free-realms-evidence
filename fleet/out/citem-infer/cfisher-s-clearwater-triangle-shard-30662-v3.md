<!-- fleet job=citem-infer id=cfisher-s-clearwater-triangle-shard-30662-v3 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[6290, 14488, 6, 2113] model=claude-haiku-5-5 -->
# Fisher's Clearwater Triangle Shard

{"item": {"name": "Fisher's Clearwater Triangle Shard", "locale_id": 30662, "kind": "other"},
 "sources": [{"type": "coin_shop", "detail": "Coin-store data row only (item 2142, category 121, unnamed). Reconstructed store-data price, not confirmed by a wiki page, article or video. No vendor NPC or shop resolved; the same category 121 block lists other tiers at 540/866/1780 coins.", "where": "Coin store, category 121 (unnamed)", "price": "866 coins (member price 779 coins with 10% member discount; sell-back 86 coins), data-build value", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:612 (item_id 2142, category_id 121, purchase_price_coins 866, member_price_coins 779); client coin_store_prices [866] for definition 2142 (same data, not independent)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 30662 \"Fisher's Clearwater Triangle Shard\", in a cluster with 30657 Angler's Biomass, 30661 Troller's Clearwater, 30663 Angler's Clearwater, and 8349 Pro Clearwater Triangle Shard.", "source": "locale:30662; locale:30657; locale:30661; locale:30663; locale:8349"},
  {"claim": "Store row 612 gives item 2142 a 866-coin price in category 121. Category 121 rows all share the same source_tags [L1, L2, L4, R2, T633, R1] and three price tiers (540, 866, 1780), so the tags and the price do not identify this item or its live status.", "source": "repo:prototype/osfr-tools/data/content/stores.json:596-626"},
  {"claim": "The Fisherman note lists Clearwater Triangle Shards as a Fisherman slot family with tier prefixes Amatuer, Fisher's, Angler's, Troller's, Pro and All-Star. Tier order, stats and sources are not given.", "source": "notes/Build Guides/Content/Jobs/Fisherman.md:291"},
  {"claim": "Lookup of the name across client, wiki, articles and video returns only client text. No wiki page, article or video frame names this shard.", "source": "lookup (client, wiki, articles, video) for 'Clearwater Triangle Shard'"}
 ],
 "confidence": 0.3,
 "open": [
  "The 866-coin price is a reconstructed data-build value (stores.json built from the wiki-catalogue script; vendors_unresolved.json states non-client prices are reconstructed references with no claim of complete final-2014 stock). It is not confirmed by any wiki page, article or video. Do not treat it as a verified live coin-store listing.",
  "Which NPC or shop sells category 121 is unresolved. No vendor is named.",
  "Tier mapping is inferred: no source states that Fisher's = 866 coins. The 866 price is shared by other category 121 rows, so it does not single out this item.",
  "Live or retired status is unknown. Shared tags do not show whether the row is current.",
  "The Fisherman note places Clearwater shards in the Fisherman job family, which may point to a crafted or job-loot source rather than a coin store. Neither source is confirmed; the conflict is unresolved.",
  "No quest reward, drop, crafting, collection or prize-wheel source was found. Collection 'Fisherman Shards' (4157167645) was not checked for membership.",
  "Stats, level, and in-game purpose are unknown; kind 'other' is a placeholder.",
  "Wireable only as 'data price available, not confirmed'. The pack's evidence critique (price not independent of the client value; coin_shop labelled as vendor) is addressed above by relabelling the source as a data-build row with no named vendor."
 ]}
