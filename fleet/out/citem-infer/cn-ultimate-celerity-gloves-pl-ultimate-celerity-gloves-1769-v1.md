<!-- fleet job=citem-infer id=cn-ultimate-celerity-gloves-pl-ultimate-celerity-gloves-1769-v1 status=done turns=10 usd=0.0078 tokens(read,write,in,out)=[142328, 26483, 22, 6185] model=claude-haiku-5-5 -->
# {n}Ultimate Celerity Gloves{pl="Ultimate Celerity Gloves"}

{"item": {"name": "Ultimate Celerity Gloves", "locale_id": 1769, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin vendor sale at the Kart Driver rank-20 gear price tier (Cost 1266 coins, 10% member discount); the specific vendor NPC is not identified in our data", "where": null, "price": "1266 coins (client Cost field; member discount 10%)", "currency": "coins", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 37440-37460 (Id 1971, Cost 1266, MinProfileRank 20, Class 24); repo:prototype/osfr-tools/data/content/stores.json item 1783 (Extreme Celerity Jacket, same rank-20 Kart Driver gear, purchase_price_coins 1266) as the price-tier comparison"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 1769 is 'Ultimate Celerity Gloves'; the definition is Id 1971, class 24, slot 2, CategoryId 102, MinProfileRank 20.", "source": "locale:1769; refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 37440-37460"},
  {"claim": "Class 24 is the Kart Driver gear class; rank 20 of the Kart Driver gear table is Extreme Celerity Jacket (item 1783), and rank 19 is Ultimate Celerity Jacket (item 1822). The gloves are a 16-definition family sharing the name, so they belong to the same Kart Racing rank-gated gear set.", "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:132-153 (KART_DRIVER_GEAR, KART_DRIVER_GEAR_CLASS = 24)"},
  {"claim": "Stores data lists Ultimate Celerity Jacket (1822) at 957 coins and Extreme Celerity Jacket (1783) at 1266 coins in category 103, both with 10% member discount. No stores.json row exists for item 1971 (the gloves), so the gloves' coin price rests only on the client Cost field.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 5833 and 5856"},
  {"claim": "The client's nearby sale lines (locale 1766-1774: 'Twas the Night Before Sale', TCG Set 1 sale, Furry Friend Sale, Masquerade Madness, Massive Transit Sale) are unrelated promotions and do not name the gloves.", "source": "locale:1766-1774"},
  {"claim": "Kart Racing reward and gear data (rank-unlock tables) is reconstructed; no wiki page, article, video frame or quest/drop row names these gloves.", "source": "repo:prototype/osfr-tools/src/kart_rewards.rs lines 15-16 (payout numbers RECONSTRUCTED)"}
 ],
 "confidence": 0.35,
 "open": [
  "No wiki page, article, video or vendor row names the gloves; the vendor NPC, zone, and whether they are sold at all are unverified.",
  "The 1266 price is the client Cost field of definition 1971; stores.json has no item 1971 row. The pack's 957 price belongs to Ultimate Celerity Jacket (1822), not to these gloves; the other 15 definitions (14449-14462 etc.) were not checked for their own Cost.",
  "Whether the gloves come from the Kart Racing rank-20 reward or only from a coin vendor is unresolved. The rank table lists one representative per rank, so the gloves are not shown as the rank-20 unlock; the rank-20 row there is Extreme Celerity Jacket.",
  "Whether the item is live: the first-pass tag says yes, but no source confirms it is still sold. It is treated as unsure.",
  "The 'Kart Driver' job rank requirement (MinProfileRank 20) needs the job-rank progression to confirm it is reachable.",
  "Other variants (16 definitions) and their Cost, race and tint variants were not reviewed."
 ]}
