<!-- fleet job=citem-infer id=cn-berserk-bruiser-pauldrons-pl-berserk-bruiser-pauldrons-68959-v2 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6062, 8804, 6, 2309] model=claude-haiku-5-5 -->
# {n}Berserk Bruiser Pauldrons{pl="Berserk Bruiser Pauldrons"}

{"item": {"name": "Berserk Bruiser Pauldrons", "locale_id": 68959, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store listing, category 106, tint group 1 (item_id 10699). The vendor NPC and shop name are not identified in any source.", "where": "Coin store, category 106", "price": "1027 coins (member price 924 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:3111 (verified: purchase_price_coins 1027, member_price_coins 924, no_sale false)"},
  {"type": "vendor", "detail": "Coin store listing, category 106, tint groups 2 and 3 (item_ids 10700, 10701). Same listing family as tint 1; the pack's tint-to-listing question is still open.", "where": "Coin store, category 106", "price": "9453 coins each (member price 8507 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:3112-3113 (verified: purchase_price_coins 9453, member_price_coins 8507, no_sale false)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Berserk Bruiser Pauldrons', locale 68959 (slot 6, class 25, model brawler shoulders spikedpadwchain).", "source": "locale:68959"},
  {"claim": "Store data has coin-store rows for item_ids 10699 (1027 coins), 10700 and 10701 (9453 coins each), all in category 106 with no_sale false. The other definitions 10702-10710 have no store row.", "source": "repo:prototype/osfr-tools/data/content/stores.json:3111-3113"},
  {"claim": "Neighbouring category-106 rows (10696-10698, 10715-10717) carry the same source_tags [L1,L2,L4,R2,T633,R1]; these tags are unexplained and do not name a vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json:3108-3116"},
  {"claim": "The wiki page 'Berserk Bruiser Hammer' (same set name) is a level 16 Brawler Green Text weapon that 'can only be acquired through trade'. The 'Green Text weapon' page lists it as Trade only.", "source": "wiki: Berserk Bruiser Hammer; wiki: Green Text weapon"},
  {"claim": "No wiki page, article, video or client line names the pauldrons' trade status. The shared set name does not prove the armor is trade-only; the earlier answer's set-level trade claim is an inference and is not used here.", "source": "locale:121088, 121089, 121090, 121091, 121092 (names only); wiki search 'Berserk Bruiser' (no pauldrons page)"}
 ],
 "confidence": 0.4,
 "open": [
  "The vendor NPC or shop name behind store category 106 is not identified; the store rows give prices only.",
  "Price conflict: tint 1 is 1027 coins, tints 2-3 are 9453 coins. Whether these are tints of one listing or separate listings needs a check against the live store.",
  "Definitions 10702-10710 have no coin price on record; their sources are unknown.",
  "Trade status of the pauldrons is unresolved. The Hammer is trade-only (wiki), but no source says the armor is. This conflicts with the coin-store rows, which must be checked against live data.",
  "Retirement status and whether the coin sale still ran in later years are unknown. The store rows (no_sale false) show data, not current availability.",
  "No quest, drop, crafting, event or collection source was found."
 ]}
