<!-- fleet job=citem-infer id=cfragile-ancient-chalice-66994-v2 status=done turns=4 usd=0.0030 tokens(read,write,in,out)=[30258, 13019, 10, 2086] model=claude-haiku-5-5 -->
# Fragile Ancient Chalice

{"item": {"name": "Fragile Ancient Chalice", "locale_id": 66994, "kind": "collection"},
 "sources": [
  {"type": "other", "detail": "Not a purchasable item. It is one of the 8 parts of the 'Ancient Chalice Artifacts' collection (collection id 172, name_id 67538, item definition 23381, entry 3). How the part itself is obtained (dig, drop or other) is not documented in any source found.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13554-13589; locale:67538; locale:132431"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Fragile Ancient Chalice' is locale 66994; the description (locale 132431) reads 'This item can be added to the Ancient Chalice Artifacts Collection'.", "source": "locale:66994; locale:132431"},
  {"claim": "Entry 3 of collection 172 (Ancient Chalice Artifacts, name_id 67538) maps name 66994 to item definition 23381, icon tint 123.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13554-13589"},
  {"claim": "The collection's reward is 8 coins + 50 XP (profile 43). The previous answer's '2 coins' was wrong; the 50 XP is correct.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13636-13644"},
  {"claim": "The wiki's List of Collections (rev 27852, 2013-07-13) lists '[Ancient] [Chalice] Artifacts' under Archaic > Common.", "source": "https://freerealms.fandom.com/wiki/List_of_Collections (refs: freerealms-wiki/raw/73b7c9e131faa8012f4d9572dcc58520fc2b4fc08940a6469920b0bd1d01247f.json)"},
  {"claim": "Video frame shows the collection progress '[Ancient] [Chalice] Artifacts 1/20'.", "source": "video:p5sDafXSQtQ/00114.jpg"},
  {"claim": "The Relic Excavation Site in Blackspore Swamp is an archaeology dig site, the only dig site named in the wiki. Nothing found ties it to the chalice parts specifically.", "source": "wiki: Relic Excavation Site; wiki: Blackspore Swamp"},
  {"claim": "No coin store price (coin_store_prices empty), no vendor stock, no quest reward, no drop, and no wiki page for this part or the chalice set were found.", "source": "client definition; lookup over client, wiki, articles, video"}
 ],
 "confidence": 0.4,
 "open": [
  "Acquisition method for individual chalice parts is unknown. The Relic Excavation Site dig (Blackspore Swamp) is a plausible source for the Archaic artifact sets, but no source ties it to these parts. Needs a wiki page for the chalice set or a video frame of a dig/drop.",
  "The previous answer's 'Ancient Artifact Plates' reward of 20 Coins was not verified; leave it out until the wiki line is checked.",
  "No price and no retirement evidence. The 2013 list is the latest dated source.",
  "The catalogue's item_link 'sanctuary' is a link tag, not an acquisition source."
 ]}
