<!-- fleet job=citem-infer id=csilent-screen-shorts-404385-v1 status=done turns=8 usd=0.0052 tokens(read,write,in,out)=[79609, 20022, 18, 3753] model=claude-haiku-5-5 -->
# Silent Screen Shorts

{"item": {"name": "Silent Screen Shorts", "locale_id": 404385, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Fred Futbol, the \"Soccer Star Gear\" vendor (the vendor is named in video titles; no stock list or item-level price was found, so this item's sale is not confirmed)", "where": "Snowhill Soccer Field, Snowhill", "price": null, "currency": null, "source": "notes/Build Guides/Content/NPCs/NPCs - Snowhill.md row 126 [client][video X35ewgMjcAM/00036, WjpJl2U5OK0/00016]; notes/Build Guides/Content/Jobs/Soccer Star.md line 42; locale:2614216159; prototype/osfr-tools/data/content/npcs/snowhill.json:16192"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Silent Screen Shorts (locale 404385) is the base shorts of the 'Silent Screen' Soccer Star clothing family, with Elite Black (404391 / 2650199705) and Elite Pink (404390 / 2018882118) variants; the set also has bandana, cleats, jersey and shin guards pieces.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md table rows 19-21 [client]; locale:404390; locale:404391"},
  {"claim": "The Silent Screen family is a Soccer Star gear set; the job link is by slot and set name, not a confirmed item-to-job table.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md line 193 [client]"},
  {"claim": "Fred Futbol is the 'Soccer Star Gear' vendor at the Snowhill Soccer Field; stock and prices were not seen.", "source": "notes/Build Guides/Content/NPCs/NPCs - Snowhill.md row 126; video:X35ewgMjcAM/00036"},
  {"claim": "The vendor-stock check found no item-level stock list for Fred Futbol.", "source": "prototype/osfr-tools/data/content/vendors_unresolved.json (Fred Futbol, w118_research)"},
  {"claim": "No wiki page, article fact, or video frame names Silent Screen Shorts; lookup returned only client text.", "source": "lookup (client, wiki, articles, video) for 'Silent Screen Shorts'"},
  {"claim": "The pack's coin store prices 528 and 750 could not be tied to this item: no stores.json entry for the shorts' definition ids 61955-61968 was found (item_id 61960 and 61961 are 9453-coin entries in another category), and no 528-coin entry exists.", "source": "repo:prototype/osfr-tools/data/content/stores.json (search for item_id 61955-61968; purchase_price_coins 528 not found)"}
 ],
 "confidence": 0.3,
 "open": [
  "The coin store price (528 and 750 in the pack) is unverified. The pack gives no item id, and the definition ids 61955-61968 do not appear in stores.json. Price and vendor sale need a store-data check by item id before they are recorded.",
  "Fred Futbol's stock list is not known. Whether Silent Screen Shorts is sold there, and at what price, is unconfirmed.",
  "The pack says 34 definitions but lists only 12 definition ids. Elite and base tiers and any tint variants are not all mapped.",
  "No wiki, forum or article source gives an acquisition date or retirement for the Silent Screen set. Live status is unsure.",
  "The pack's 'coin_store_prices' field may refer to a different item in the family. It needs checking before it is used as a sale price."
 ]}
