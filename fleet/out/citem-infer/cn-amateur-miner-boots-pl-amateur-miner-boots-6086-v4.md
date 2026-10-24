<!-- fleet job=citem-infer id=cn-amateur-miner-boots-pl-amateur-miner-boots-6086-v4 status=nothing_found turns=3 usd=0.0043 tokens(read,write,in,out)=[24144, 23210, 8, 2377] model=claude-haiku-5-5 -->
# {n}Amateur Miner Boots{pl="Amateur Miner Boots"}

{"item": {"name": "Amateur Miner Boots", "locale_id": 6086, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 6086 'Amateur Miner Boots'; one definition (2452); slot 5; class 12; model worker_<race>_<gender>_feet_strappedboots.adr. Client description is blank.", "source": "locale:6086"},
  {"claim": "Lookup of 'Amateur Miner Boots' across client, wiki, articles and video returns only the client line locale:6086. No wiki page, article, video frame, quest, drop, crafting or event names the item.", "source": "lookup client/wiki/articles/video 'Amateur Miner Boots'"},
  {"claim": "Coin store row for item 2452: category 105, tint group 1, purchase 291 coins, member 261, sell 29, no_sale false, legacy tags L1, L2, L4, R2, T633, R1. The row has no vendor, NPC or store-name field, so it is a price-only lead and not a vendor source.", "source": "repo:prototype/osfr-tools/data/content/stores.json:656"},
  {"claim": "The identical 291/261/29 category-105/101/102 rows also cover items 2239, 2242, 2471, 2483, 2484 (lines 650-665), so the price does not single out this item or its seller.", "source": "repo:prototype/osfr-tools/data/content/stores.json:650-665"},
  {"claim": "Repo search for 'Amateur Miner' finds only the Amateur Miner Shovel (1036920426) in the Miner job notes, where starter gear is said to be given in a way that is unknown. Amateur Miner Boots is not named in any repo vendor, quest or drop file.", "source": "notes/Build Guides/Content/Jobs/Miner.md:307"},
  {"claim": "The repo has tier-named Miner boots in vendor data (e.g. Slop Miner Boots in vendors_unresolved.json:10068; Mountaintop Miner Boots in vendors.json:836), but no 'Amateur' tier entry.", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:10068; repo:prototype/osfr-tools/data/content/vendors.json:836"}
 ],
 "confidence": 0.2,
 "open": [
  "No confirmed source. The only lead is the unlinked coin price (291 coins; member 261; sell-back 29) on stores.json:656. It is not a vendor source. Which vendor, if any, sells item 2452 must be found before it can be published. Wireable: false.",
  "Do not list a vendor source. The prior answer's 'vendor' type is withdrawn, since no vendor-to-store link exists in the repo or the wiki.",
  "Live status unknown. Legacy store tags (L1, L2, L4, R2, T633, R1) show past store presence only. No wiki, article or video confirms a sale in the 2009-2014 game, and no retirement is recorded. Do not imply a current sale.",
  "Miner vendor absence is not proven. Only lookup listings were read for Witts, Boddington, Grasberg, Yanaco, Kallie, Cortez and Vaal. Full vendor pages were not read, so this does not rule any vendor in or out.",
  "The Amateur set (Boots 6086, Gloves 6106, Pants 35474, Shirt 6063, Hat 35358, Shovel 2180) is named in the cluster only. Its sources were not checked here and may explain the item's source once checked.",
  "Critiques addressed: vendor source removed to open; shared-price issue stated; live and retired left unknown; Miner-vendor absence limited to the listings read; wireable set to false."
 ]}
