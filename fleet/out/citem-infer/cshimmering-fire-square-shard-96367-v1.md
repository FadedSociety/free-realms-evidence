<!-- fleet job=citem-infer id=cshimmering-fire-square-shard-96367-v1 status=unsure turns=4 usd=0.0033 tokens(read,write,in,out)=[25928, 14269, 10, 2520] model=claude-haiku-5-5 -->
# Shimmering Fire Square Shard

{"item": {"name": "Shimmering Fire Square Shard", "locale_id": 96367, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text for the name exists: 'Shimmering Fire Square Shard' is item-typed locale 96367, sitting in a cluster with Glowing Fire (96362), Glowing Air (96365), Glowing Void (96366), Shimmering Air (96370), Shimmering Void (96371), Beaming Fire (96372).", "source": "locale:96367; locale:96362; locale:96365; locale:96366; locale:96370; locale:96371; locale:96372"},
  {"claim": "The client definition lists 'coin_store_prices': [866] but this is a price value, not a store item id. A search of the repo data for definition id 30961 finds no entry in data/content/stores.json, so no coin vendor sale is tied to this item. The 866 value recurs across many unrelated stores.json entries (e.g. item_id 1170, 2108), so it cannot be used as evidence of a sale of this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json (no item 30961; price 866 appears on items 1170, 2108, 6415, etc.)"},
  {"claim": "The same 'Square Shard' naming family is used by Trading Card Game virtual rewards. The wiki's Briarheart Bandage [Square] [Shard] is a Medic power shard acquired by redeeming a TCG Series 2 Virtual Reward loot card. This suggests the Shard family is TCG-reward-related, but it does not name the Shimmering Fire variant.", "source": "wiki page: Briarheart Bandage Square Shard; wiki file: File:Briarheart bandage square shard tcg.png"},
  {"claim": "No wiki page, article fact, video frame, vendor stock list, or other answer names the Shimmering Fire Square Shard. The first-pass tag 'vendor' is a guess and is not supported by evidence.", "source": "lookup over client, wiki, articles, video (only locale hits for the name)"}
 ],
 "confidence": 0.2,
 "open": [
  "No verified acquisition source. The first-pass 'vendor' guess is unsupported. The coin price 866 in the client definition does not link to definition 30961 in stores.json, so it is not a sale record.",
  "Likely origin is the TCG virtual-reward / power-shard family (compare Briarheart Bandage Square Shard, TCG Series 2). Verify the Shimmering Fire tier against a TCG reward list or the wiki before assigning a source.",
  "Power level, job (Medic/other), and tier meaning (Glowing vs Shimmering vs Beaming) are not established. Their effect and the ones for the cluster variants need a check.",
  "Retired status and live status are unknown. The wiki has no page for this item.",
  "The client description is empty, so the in-game tooltip text could not be confirmed."
 ]}
