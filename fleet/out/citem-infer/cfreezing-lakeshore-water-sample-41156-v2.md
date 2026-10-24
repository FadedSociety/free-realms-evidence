<!-- fleet job=citem-infer id=cfreezing-lakeshore-water-sample-41156-v2 status=nothing_found turns=3 usd=0.0038 tokens(read,write,in,out)=[17502, 17359, 8, 2840] model=claude-haiku-5-5 -->
# Freezing Lakeshore Water Sample

{"item": {"name": "Freezing Lakeshore Water Sample", "locale_id": 41156, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 3940 is named 'Freezing Lakeshore Water Sample' (name locale 41156). Its description says it 'can be added to the Lakeshore Water Samples Collection', so the client defines it as a collection item, not a standalone purchasable.", "source": "locale:41156; client definition (definition_ids [3940]); critique cites locale 132378 for the description"},
  {"claim": "Client-side lookup finds only the name line (locale:41156). No wiki page, article fact, video frame, vendor stock, quest, drop or event names this item.", "source": "lookup client/wiki/articles/video for 'Freezing Lakeshore Water Sample' (client hit: locale:41156 only)"},
  {"claim": "The Lakeshore Water Samples collection is listed on the wiki's List of Collections (category 8), with no entry list.", "source": "repo:prototype/osfr-tools/data/content/collections.json:11242-11268 (https://freerealms.fandom.com/wiki/List_of_Collections)"},
  {"claim": "The collection_catalogue block at lines 9899-9907 (name_id 41156, item 3940) is unparented: it has no collection key or client_id, and every row carries item_link 'sanctuary'. So the link to the Lakeshore collection (wiki:8:222) is unproven.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9899-9907 (critique)"},
  {"claim": "Repo store data has a row with item_id 41156, category 102, purchase price 1027 coins (member price 924), sell price 102. Its item_id equals this item's name locale id, not its definition id (3940). Whether store item_id keys on definition id or name id is unverified, so this row is not attributed to this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12569"}
 ],
 "confidence": 0.15,
 "open": [
  "No verified source for how a player obtains this item. The Lakeshore collection membership is unproven (catalogue block 9899-9907 has no collection key; wiki:8:222 has no entry list). The earlier answer's 'collection sample chain' source is withdrawn, and the Embir Clearwell chain evidences only a plain Lakeshore sample, not this variant.",
  "Possible coin vendor lead, unverified: stores.json line 12569 lists item_id 41156 at 1027 coins (member 924, sell 102), category 102. The sibling rows 41155, 41160, 41161 and 41166 carry the same price. Verify whether store item_id keys on definition id (here 3940, which has no store row) or on name id. Only after that check can it be a vendor sale, and then it needs a vendor or wiki page naming the store.",
  "The variant is possibly made by a boil/freeze/treat step (the 'Boiling' and 'Freezing' names; Merri boil-water lines locale 2053523967, 3259048059; 'Liquid Concoction' and 'Mixture' items locale 66788-66837). Unproven.",
  "Retirement and live status are unknown. The first-pass 'live: yes' is a hint only and no date or retirement source exists.",
  "Price and currency unknown beyond the unverified 1027-coin store row above."
 ]}
