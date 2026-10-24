<!-- fleet job=citem-infer id=csilent-screen-jersey-403510-v1 status=done turns=5 usd=0.0033 tokens(read,write,in,out)=[27721, 13208, 12, 2703] model=claude-haiku-5-5 -->
# Silent Screen Jersey

{"item": {"name": "Silent Screen Jersey", "locale_id": 403510, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale, vendor not identified in repo data (stores.json gives only item and category 103, no NPC or shop name)", "where": null, "price": "750 coins (member price 675 coins, 10% member discount; sell-back 75 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:8423 (item_id 61080, tint_group 1); same price on 61081 and 61082 (lines 8424-8425) and 61115-61117 (lines 8428-8430)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client name is 'Silent Screen Jersey' (base), with Elite Pink and Elite Black variants", "source": "locale:403510, locale:403515, locale:403516"},
  {"claim": "Silent Screen is a Soccer Star job clothing set (base, Elite Black, Elite Pink), with the jersey listed as slot 3 of the set", "source": "repo:notes/Build Guides/Content/Jobs/Soccer Star.md:223-225"},
  {"claim": "Item 61080 (tint group 1) is in the coin store at 750 coins, member price 675, sell price 75", "source": "repo:prototype/osfr-tools/data/content/stores.json:8423"},
  {"claim": "No wiki page, image, article or video mentions Silent Screen Jersey; the Soccer Star achievements page is the only related wiki hit", "source": "lookup for 'Silent Screen' (wiki, articles, video: no matches); wiki page:ns0 Achievements"}],
 "confidence": 0.4,
 "open": ["Vendor or shop name for the 750-coin sale is not in repo data and no wiki page confirms it; the coin-store listing is the only sale source.",
  "Store data covers item 61080-61082 and 61115-61117 at 750 coins. The client's 34 definitions and Elite Pink/Elite Black variants (403515/403516) are not mapped to store item ids, so it is unknown which variants are sold for coins.",
  "The 'T633' and 'R1' source tags in stores.json are unexplained; they may mark a sale window or channel but I did not verify this.",
  "The Soccer Star job guide says whether Elite is a stat tier, recolour or gender variant is unknown, so the Elite variants' sources are unverified.",
  "The pack says vendor_stock is empty, which conflicts with the coin store price; the store data is treated as the evidence, but no in-game vendor was confirmed.",
  "Whether the item was retired or is still sold is unknown; no retirement source was found.",
  "No quest, drop, prize wheel or crafting source was found; the pack did not list any."]}
