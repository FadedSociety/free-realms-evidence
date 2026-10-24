<!-- fleet job=citem-infer id=copal-wand-13999-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5395, 9435, 6, 1772] model=claude-haiku-5-5 -->
# Opal Wand

{"item": {"name": "Opal Wand", "locale_id": 13999, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale of Opal Wand, tint group 1 (item 7312); tint groups 2 and 3 (items 7313, 7314) carry the same price", "where": "Coin store, category 207 (category label not verified in repo)", "price": "3522 coins (member price 3169 coins, 10% member discount; sell-back 352 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 1957-1959 (items 7312-7314); copied from FreeRealms-Legacy CoinStoreItems snapshot of unknown date"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Opal Wand' is locale 13999, class 10, slot 7, 42 definitions, model wand_ar_ag_weapon_diadem.adr.", "source": "locale:13999; client definition ids 7312-7323 (as supplied in the pack)"},
  {"claim": "Coin store rows for items 7312-7314 (category 207, tint groups 1-3) list purchase 3522 coins, member 3169, sell 352, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 1957-1959 (verified)"},
  {"claim": "Tentonhammer article says Osgood (Sanctuary) asks the player to return at level 15 to get the 'wand', and that Sandbur gathers transfiguring crystals and opal gems from Tormented Spirits in Blackspore Swamp.", "source": "http://www.tentonhammer.com:80/node/69770 (article snippet, truncated; does not name item 13999)"},
  {"claim": "Osgood blocks wand-making until levels 10 and 15; wiki-derived quest list for him names Reach Level 10, Helping a Friend, Reach Level 15, Missing Student Sven, Parts and Labor, and no quest that grants the Opal Wand.", "source": "repo:notes/Build Guides/Content/Jobs/Wizard.md line 52 (verified)"}
 ],
 "confidence": 0.5,
 "open": [
  "Quest reward source removed: no quest is shown to grant Opal Wand (13999). The Tentonhammer snippet says only 'get the wand' from Osgood at level 15 and does not name the item; the Wizard.md rows list no wand reward. Lead to check: the Osgood level-15 hand-off in the Wizard line, with the granting quest unidentified.",
  "The coin store price is the only directly evidenced source. It comes from a FreeRealms-Legacy snapshot of unknown date, and the store row's source_tags do not establish live status in 2009-2014.",
  "Category 207 is recorded only as a number; the label 'weapons' is unverified.",
  "Tints 7315-7323 (9 of the 42 definitions) have no price row in our store data; their source is unknown.",
  "No wiki page, image, video frame, or vendor row names the Opal Wand. Client description is empty.",
  "Retirement status unknown; the store row has no_sale false, but nothing says whether the item was pulled. Live status is unsure."
 ]}
