<!-- fleet job=citem-infer id=cn-amateur-demo-derby-pants-pl-amateur-demo-derby-pants-69389-v1 status=done turns=8 usd=0.0067 tokens(read,write,in,out)=[110010, 27951, 18, 4260] model=claude-haiku-5-5 -->
# {n}Amateur Demo Derby Pants{pl="Amateur Demo Derby Pants"}

{"item": {"name": "Amateur Demo Derby Pants", "locale_id": 69389, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (vendor not identified in the repo; stores.json category 104 has no vendor mapping)", "where": "coin store, category 104", "price": "270 coins (member price 243 coins with 10% member discount; sell-back 27 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 622 (line 300: purchase_price_coins 270, member_price_coins 243, sell_price_coins 27)"},
  {"type": "quest_reward", "detail": "Not a quest reward in the evidence. Demo Derby Driver job gear: the item is the rank-4 representative of the Demo Derby Driver gear table (rank gate MinProfileRank 4, 5 catalogue rows at that rank). This gates purchase by job rank; it does not name a vendor or a grant.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:160 (rank_unlock(4, 622, 69389, \"Amateur Demo Derby Pants\", 5)); repo:prototype/osfr-tools/src/restoration/piece_041.rs:1-22 (job gear class 22, ranks gate catalogue rows)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 69389, 'Amateur Demo Derby Pants', item class 22 (Demolition Derby Driver Gear), slot 4 (legs), definition 622, model freestyle_<race>_<gender>_legs_tuckedpantswpads.adr", "source": "locale:69389; client definition supplied in pack"},
  {"claim": "Coin store entry item 622 is category 104 with purchase price 270 coins, member price 243, sell price 27, tint group 1", "source": "repo:prototype/osfr-tools/data/content/stores.json item 622 (line 300)"},
  {"claim": "Same-price coin store rows with tint groups 1-3 sit beside it (items 624, 626, 627), consistent with colour variants of one name", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 301-303"},
  {"claim": "Amateur Demo Derby Pants is the rank-4 gear unlock of the Demo Derby Driver job (job id 49), part of the 'Demolition Derby Driver Gear' class, with 5 catalogue rows at rank 4", "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:160"},
  {"claim": "Demo Derby Driver is a members-only job per the January 2014 monthly member pack update; the wiki notes it was made members-only again", "source": "wiki: User blog:Soe amnerys/Weekly Update - 01/15/14 and Template:News (January Monthly Member Pack)"},
  {"claim": "Client cluster neighbours (Student, Elite Pink/Black Wacky Crash Pants, Elite Pink Wonky Ram Shirt) are other Demo Derby gear rows; no source gives them a vendor either", "source": "client cluster in pack; locale:69386-69394"}
 ],
 "confidence": 0.5,
 "open": [
  "The coin vendor that sells item 622 is not identified. stores.json has category 104 rows but no vendor-to-category map, and the vendor_stock list in the pack is empty. Needs the store-to-NPC mapping for category 104 (the Demo Derby equipment vendor is listed as unknown in repo:prototype/osfr-tools/data/content/npcs_unresolved.json around line 2150).",
  "No wiki page or article names this item, so the 270-coin price is from our store data only, not a second wiki price. No sale-price source was found.",
  "Live status is unsure: the store row has no_sale false and the item is in the current store table, but no dated source confirms it is still sold. Retired status is unknown.",
  "Job-rank gating (rank 4) is recorded as a purchase restriction, not a separate source. Whether rank-4 gear is also bought from a job trainer or given as a rank reward is not evidenced.",
  "Variant count: the client gives 1 definition, but store rows 624, 626, 627 share the price and tint groups. Confirm whether these are colour variants of this same name or separate items.",
  "Demo Derby Driver is members-only per the Jan 2014 update, so the member price (243 coins) may be the one a non-member can't use; access rules at the store are unconfirmed."
 ]}
