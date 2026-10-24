<!-- fleet job=citem-infer id=copal-wand-13999-v1 status=done turns=7 usd=0.0074 tokens(read,write,in,out)=[102874, 31580, 16, 4911] model=claude-haiku-5-5 -->
# Opal Wand

{"item": {"name": "Opal Wand", "locale_id": 13999, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale of the Opal Wand (tint group 1; item 7312). Tints 7313 and 7314 carry the same 3522-coin price. Other definitions in the 7312 range (7315-7323) have no price row in our store data.", "where": "Coin store (category 207, weapons)", "price": "3522 coins (member price 3169 coins with 10% member discount; sell-back 352 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 7312 (also items 7313, 7314); copied from FreeRealms-Legacy CoinStoreItems.json per the file header"},
  {"type": "quest_reward", "detail": "Wizard line, Osgood the wand maker: the opal gems (from Tormented Spirits in Blackspore Swamp, gathered with Sandbur's transfiguring crystals) are used to make the wand. Osgood tells the player to return at level 15 to receive it.", "where": "Sanctuary (Osgood); quest chain via Blackspore Swamp and Briarwood", "price": null, "currency": null, "source": "http://www.tentonhammer.com:80/node/69770 (article snippet: Osgood asks you to return at level 15 to get the wand); repo:notes/Build Guides/Content/Jobs/Wizard.md rows 15, 17, 20-22 (Osgood level 10/15 gates, Things Left Unfinished, Filling in the Gaps: 'Take the opal gems to Sandbur in Sanctuary')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Opal Wand' is locale 13999, class 10 (Wizard wand class), slot 7, 42 definitions, model wand_ar_ag_weapon_diadem.adr.", "source": "locale:13999; client definition for definition ids 7312-7323 (as given in the pack)"},
  {"claim": "Coin store row for item 7312 (category 207) lists purchase price 3522 coins, member price 3169, sell 352, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 1957 (items 7312-7314 at lines 1957-1959)"},
  {"claim": "The opal gems come from Tormented Spirits in Blackspore Swamp and Sandbur's transfiguring-crystal errand; Osgood gives the wand at level 15.", "source": "http://www.tentonhammer.com:80/node/69770; repo:notes/Build Guides/Content/Jobs/Wizard.md lines 53-54, 106, 225"},
  {"claim": "Osgood is the wand maker in the Wizard line and gates wands at levels 10 and 15.", "source": "repo:notes/Build Guides/Content/Jobs/Wizard.md line 52"},
  {"claim": "Wand-finale wand is the Wand of Spectral Fire (level 20), a different item from the Opal Wand.", "source": "repo:notes/Build Guides/Content/Jobs/Wizard.md line 127"}
 ],
 "confidence": 0.5,
 "open": [
  "The quest-reward source rests on one Tentonhammer article snippet (truncated) and the Wizard wiki reward column, which reads 'unknown' for nearly every Wizard quest. The exact quest that hands out the wand is not confirmed; the level-15 Osgood return is the best lead.",
  "No wiki page, image, video frame or vendor row names the Opal Wand. The article's 'wand' is not explicitly the item 13999 (the snippet does not name it).",
  "Only tints 7312-7314 have a coin price row; definitions 7315-7323 and the remaining of the 42 variants are unpriced in our store data. Their source is unknown.",
  "Coin store listing: no zone or shop location is recorded; the price is from the FreeRealms-Legacy CoinStoreItems snapshot and its date is unknown, so whether it was live in 2009-2014 is unconfirmed.",
  "Retirement status unknown. The store row has no_sale false, but nothing on the wiki or in the client says whether it was pulled. Live status is 'unsure'.",
  "Client description is empty, so no in-game text confirms the wand's role or its opal/crystal crafting."
 ]}
