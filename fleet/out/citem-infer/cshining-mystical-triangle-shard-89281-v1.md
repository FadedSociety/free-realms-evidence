<!-- fleet job=citem-infer id=cshining-mystical-triangle-shard-89281-v1 status=done turns=6 usd=0.0063 tokens(read,write,in,out)=[80635, 31040, 14, 3238] model=claude-haiku-5-5 -->
# Shining Mystical Triangle Shard

{"item": {"name": "Shining Mystical Triangle Shard", "locale_id": 89281, "kind": "other"},
 "sources": [{"type": "vendor", "detail": "Unidentified coin vendor: store category 121, listed under item id 10272 at 1236 coins (member price 1112 coins, 10% member discount; sell-back 123 coins)", "where": null, "price": "1236", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:2979 (item_id 10272, category_id 121, purchase_price_coins 1236)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client name is locale 89281 'Shining Mystical Triangle Shard', one definition (definition id 10272), slot 12, item class 50, no description and no model files in the client pack", "source": "locale:89281; client definition pack"},
  {"claim": "Store data lists item 10272 in category 121 at 1236 coins purchase, 1112 coins member price, 123 coins sell price, with source tags L1, L2, L4, R2, T633, R1", "source": "repo:prototype/osfr-tools/data/content/stores.json:2979"},
  {"claim": "The same 1236-coin price is shared by a block of neighbouring shard item ids (10268-10276, 10281-10283 and others) in category 121, so the price alone does not identify this shard's vendor", "source": "repo:prototype/osfr-tools/data/content/stores.json:2975-2990"},
  {"claim": "Sibling shards 89276-89286 (Pulsing/Shining Infernal, Dreadful, Fateful, Spectral, Mystical, Phantasmal, Eternal, Celestial, Ethereal) form one client cluster with no wiki article, article fact, video frame or vendor answer naming any of them", "source": "client cluster in pack; lookup of 'Triangle Shard' (client, wiki, articles, video) returned no page for Shining Mystical"},
  {"claim": "Store category 121 has no name in the repo data, so the vendor that sells it cannot be named", "source": "repo:prototype/osfr-tools/data/content/stores.json (category_id 121 rows, no category name)"}],
 "confidence": 0.35,
 "open": ["Vendor for store category 121 is unidentified: no category name or NPC link in repo data; need the vendor that stocks item 10272 and its zone.",
  "No wiki page, article, or video evidence names this shard; the only sourced fact is the coin store listing at 1236 coins.",
  "Live status is unsure: the store row carries live-build source tags, but the first-pass tag 'live: yes' is only a hint and no wiki or article confirms current availability or retirement.",
  "No quest, enemy drop, crafting, or event source found; 'Shining' shards may be tied to the Mystical class-shard family but this is not evidenced.",
  "The pack gives no description and no model files, so the shard's stat effect is unknown."]}
