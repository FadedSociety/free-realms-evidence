<!-- fleet job=citem-infer id=cfiligree-long-sleeve-8577-v4 status=done turns=4 usd=0.0025 tokens(read,write,in,out)=[20410, 8563, 10, 2472] model=claude-haiku-5-5 -->
# Filigree Long-Sleeve

{"item": {"name": "Filigree Long-Sleeve", "locale_id": 8577, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "UNVERIFIED: unidentified coin-store vendor. Only evidence is the store row for item 8577 (category 6, purchase 270 coins, member 243, sell null, no_sale true). No NPC, zone or vendor_stock row names this item. The row's no_sale=true contradicts a live purchase, so purchasability is unproven.", "where": null, "price": "270 coins (member 243, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:2255 (item 8577; re-read this pass)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Filigree Long-Sleeve' is locale 8577, item class 1, slot 3, model freestyle_<race>_f_chest_hoodedlongsleeve.adr.", "source": "locale:8577; client definition in evidence pack"},
  {"claim": "Store row for 8577 is category 6, 270 coins, member 243, sell_price null, no_sale true, tags [L1,L2,L4,R2,L3,L3].", "source": "repo:prototype/osfr-tools/data/content/stores.json:2255 (verified)"},
  {"claim": "Sibling rows 8572-8581 (except 8577) are sellable at 270/243 with sell 27 and tags [L1,L2,L4,R2,T633,R1]; 8582 is also no_sale with L3 tags.", "source": "repo:prototype/osfr-tools/data/content/stores.json:2250-2260 (verified)"},
  {"claim": "Wiki Farmer and Adventurer pages list 'Filigree Long Sleeve' in a clothing list alongside other job clothing (One Shoulder Shirt, Cardigan Sweater, etc.); no acquisition method is given.", "source": "wiki: Farmer (ns0); wiki: Adventurer (ns0)"},
  {"claim": "Video frame shows 'One-Shoulder Shirt Filigree Long-Sleeve' during an Artifact Hunt minigame at Adventurer level 20; shows the item in play, not how it was obtained.", "source": "video:f3ZJ9i5YnaI/00144.jpg"}
 ],
 "confidence": 0.3,
 "open": [
  "No confirmed vendor: the 270-coin price is store-data only. Vendor NPC and zone are unknown. Do not wire this as a live coin-vendor purchase until an NPC or vendor_stock row is found.",
  "Conflict: stores.json:2255 has no_sale=true, but sibling rows are sellable. Unclear whether 8577 is purchasable. The L3 tags on 8577 and 8582 are not explained in the repo.",
  "Definition count mismatch: the pack says 66 definitions but lists only 12 definition_ids. Only 8577, 416 (stores.json:201, category 103, 270/243) and 939 (stores.json:5726, category 103, 270/243, tint group 2) were checked. The other same-name definitions are unverified.",
  "Unresolved lead: the Farmer and Adventurer wiki pages list this item among job clothing, and the Artifact Hunt frame fits. This may be a job-level or job-outfit reward, but no wiki text states an acquisition method. Not counted as a source.",
  "The first-pass 'live: yes' is not supported by any store, vendor or wiki source. Retirement status is unknown.",
  "Not checked: whether the L/R/T source tags and category 6 vs 103 are documented anywhere in the repo."
 ],
 "wireable": false}
