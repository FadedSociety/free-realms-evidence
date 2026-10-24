<!-- fleet job=citem-infer id=cstandard-small-bed-132519-v1 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[21905, 15918, 10, 2792] model=claude-haiku-5-5 -->
# Standard Small Bed

{"item": {"name": "Standard Small Bed", "locale_id": 132519, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store, housing furniture category 53, base definition 2760 (no tint group); listed purchase price 10 coins (member price 9)", "where": "coin store (vendor not named in store data)", "price": "10 coins (member price 9 coins; sell-back 1 coin)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2760 (line 743)"},
  {"type": "vendor", "detail": "Coin store, housing furniture category 53, definition 15590 (tint_group 2); listed purchase price 300 coins (member price 270)", "where": "coin store (vendor not named in store data)", "price": "300 coins (member price 270 coins; sell-back 30 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 15590 (line 3983)"},
  {"type": "vendor", "detail": "Coin store, housing furniture category 53, definition 36106; listed purchase price 300 coins (member price 270)", "where": "coin store (vendor not named in store data)", "price": "300 coins (member price 270 coins; sell-back 30 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 36106 (line 11783)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client item name 'Standard Small Bed' is locale 132519, kind item, sharing a cluster of 'Standard' housing furniture names (Large Bed, Bathtub, Bookcase, Armoire, Barrel, Balloons).", "source": "locale:132519"},
  {"claim": "Three client definitions (2760, 15590, 36106) all use model hsg_bed_small_01.adr, the housing placement model.", "source": "repo:Lxzxrus-Free-Realms-Server/src/Resources/HousingPlacementData.txt lines 257, 562, 879"},
  {"claim": "Store data lists 2760 at 10 coins and 15590 and 36106 at 300 coins, both in category 53 (housing furniture), with source tags T633/R1/R2/L1/L2/L4 consistent with live coin-store stock.", "source": "repo:prototype/osfr-tools/data/content/stores.json items 2760, 15590, 36106"},
  {"claim": "Two 'Standard' housing beds exist as separate SKUs: 'Standard Large Bed' (locale 132518) is in the same cluster; the small bed sells in two price tiers.", "source": "locale:132518; repo:prototype/osfr-tools/data/content/stores.json"}
 ],
 "confidence": 0.6,
 "open": [
  "The store data gives prices but no vendor NPC or shop name for category 53; the specific coin vendor (housing decor vendor) is not confirmed by a wiki page, article, or video.",
  "No wiki page exists for 'Standard Small Bed' in the supplied sources, so the 10-coin vs 300-coin tier difference (which SKU is the cheap version and which is the premium/tinted one) is inferred from the store file, not from a source describing it.",
  "The 300-coin price for 36106 is taken from stores.json only; no second source confirms it.",
  "Retirement status unknown: no source states whether the coin store still sells these beds; the store tags suggest they were sold in the later live period (T633), but that date is not confirmed.",
  "No drop, quest reward, crafting, collection, or event source found."
 ]}
