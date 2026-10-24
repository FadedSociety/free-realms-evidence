<!-- fleet job=citem-infer id=cswift-sting-cap-548-v2 status=nothing_found turns=2 usd=0.0024 tokens(read,write,in,out)=[5782, 11568, 6, 1792] model=claude-haiku-5-5 -->
# Swift Sting Cap

{"item": {"name": "Swift Sting Cap", "locale_id": 548, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text locale:548 is 'Swift Sting Cap'. It sits in the Swift Sting archer set cluster (locale:543 Gloves, 553 Leggings), and the client definition has slot 1, class 16, model archer_<race>_<gender>_head_baseballhat.adr, 34 definitions (12 ids listed).", "source": "locale:548; locale:543; locale:553"},
  {"claim": "Client definition lists coin_store_prices [270]. This is a candidate coin-store price, not a verified sale: the pack gives no store item id, and the repo has no CoinStoreItems-to-definition mapping. A repo search for the listed definition ids (355, 1267, 1296, 11534-11550) as stores.json item_id returned no matches, so none of those ids is confirmed as a store entry.", "source": "client definition (evidence pack); repo:prototype/osfr-tools/data/content/stores.json (search for item_id of the listed ids: no matches)"},
  {"claim": "The wiki Swift Sting Bow page says the bow is a Green Text weapon that can only be acquired through trade. This is about the bow only and says nothing about the cap.", "source": "wiki page 'Swift Sting Bow'; wiki page 'Green Text weapon'"},
  {"claim": "No wiki page, article, video frame, vendor stock, quest, drop or event names the Swift Sting Cap. A lookup of 'Swift Sting Cap' across client, wiki, articles and video returned only the client name line locale:548. Repo search for 'Swift Sting' / 'Sting Cap' found only the bow in reference weapons.json.", "source": "lookup 'Swift Sting Cap' (client, wiki, articles, video); repo:prototype/osfr-tools/data/reference/weapons.json:44286"},
  {"claim": "The first-pass 'vendor' guess and the previous answer's sources carry no evidence and are not counted.", "source": "evidence pack jev_first_pass; previous_answer"}
 ],
 "confidence": 0.15,
 "open": [
  "No verified source. Sources are left empty by rule: no vendor, quest, drop, event, wiki, or video source names this cap.",
  "Candidate coin store price: 270 coins (client definition coin_store_prices). Needs the store item id for this definition, which requires the CoinStoreItems-to-definition mapping. Many other stores.json entries also price at 270, so the price alone does not identify a source.",
  "Repo stores.json has no entry keyed to the listed definition ids (355, 1267, 1296, 11534-11550), so the 'coin store 355/1267/1296' link in the previous answer is not supported.",
  "The set's trade-only status (wiki 'Swift Sting Bow') does not transfer to the cap without a source. Check whether the set is tradeable or crafted.",
  "34 definitions and tint/race variants were not checked individually; only 12 ids are listed in the pack.",
  "Live status unsure and retired null: no source places the cap in or out of the current game."
 ]}
