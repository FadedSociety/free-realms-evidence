<!-- fleet job=citem-infer id=cknockdown-brawler-mask-132918-v2 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6002, 10299, 6, 1785] model=claude-haiku-5-5 -->
# Knockdown Brawler Mask

{"item": {"name": "Knockdown Brawler Mask", "locale_id": 132918, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin vendor; store row only (category 101, tint group 1, tags L1/L2/L4/R2/T633/R1). The vendor is not named in the store data, so no placeable vendor is known.", "where": null, "price": "1500 Coins (member price 1350 Coins, 10% member discount; sell price 150 Coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75910 (line 16298)"},
  {"type": "prize_wheel", "detail": "Brawler prize wheel, Forest Troll Fort. Listed as '[Knockdown] [Brawler] [Mask]' among the wheel's items, alongside a 214 Coins slot (a wheel result, not a price). No odds on record.", "where": "Forest Troll Fort", "price": null, "currency": null, "source": "wiki page Forest Troll Fort (Brawler wheel); repo:notes/Build Guides/Content/Dungeons/Forest Troll Fort.md:72"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for id 132918 is 'Knockdown Brawler Mask' (second definition id 900024, model brawler_<race>_<gender>_head_ubermask.adr)", "source": "locale:132918; client definition in pack"},
  {"claim": "Store data sells item 75910 for 1500 coins, member price 1350, sell price 150, no_sale false; the vendor is not identified in the row", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75910 (line 16298)"},
  {"claim": "The Forest Troll Fort Brawler prize wheel lists the Knockdown Brawler Mask", "source": "wiki page Forest Troll Fort (Brawler wheel); repo:notes/Build Guides/Content/Dungeons/Forest Troll Fort.md:72"},
  {"claim": "forest_troll_fort.json:2910 is a prize-wheel entry (target_id null, 'Prize wheel item is named but no item definition ID is supplied'), not a dungeon bonus-goal list", "source": "repo:prototype/osfr-tools/data/content/dungeons/forest_troll_fort.json:2910"}
 ],
 "confidence": 0.5,
 "open": [
  "Vendor for the 1500-Coin sale (stores.json item 75910) is unidentified; category 101 and tags T633/R1 need tracing to a named vendor before it can be placed.",
  "Dungeon bonus-goal source removed: the wiki names the Brawler Knockdown set, but no source lists the mask as a member of that set's dungeon drop, so membership is unconfirmed.",
  "Live/retired status is unconfirmed: the store row is not marked no_sale, but no wiki or article source dates the item or says whether it was retired.",
  "Second definition id 900024 is unexplained.",
  "Prize-wheel odds are not on record.",
  "No event, promotion, or video source was found for this item."
 ]}
