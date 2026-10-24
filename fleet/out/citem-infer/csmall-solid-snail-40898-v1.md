<!-- fleet job=citem-infer id=csmall-solid-snail-40898-v1 status=done turns=9 usd=0.0059 tokens(read,write,in,out)=[123339, 23777, 20, 3436] model=claude-haiku-5-5 -->
# Small Solid Snail

{"item": {"name": "Small Solid Snail", "locale_id": 40898, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Small Solid Snail' is locale 40898; its description is 'This item can be added to the Solid Snails Collection' (locale 132346 / ucdt 287716274).", "source": "locale:40898; locale:132346"},
  {"claim": "'Solid Snails' is a collection name (locale 7738), with description 'A collection of solid-shelled snails.' (locale 7814).", "source": "locale:7738; locale:7814"},
  {"claim": "The wiki's List of Collections (revision 27852, 13 July 2013) lists 'Solid Snails' as a collection, with no entries recorded and no reward or source fields filled in. It is the only wiki evidence for the set.", "source": "https://freerealms.fandom.com/wiki/List_of_Collections (via repo:prototype/osfr-tools/data/content/collections.json:9086-9113, key wiki:5:145)"},
  {"claim": "The set has 11 snail variants: Small, Large, Smart, Angry, Slimy, Smelly, King, Queen Solid Snail, plus the Solid Snail Platoon item (locale 66697) and the client cluster at locale 40898-40903. Small Solid Snail is defined once (definition_ids [3682], one variant).", "source": "locale:40898-40905, locale:66697; client cluster from pack"},
  {"claim": "No coin-store price exists for this item in the client definition or in repo stores.json, so no coin vendor sale is evidenced.", "source": "client definition coin_store_prices []"},
  {"claim": "A Spotted-snail collection and a Checkered-snail collection also exist in the same wiki list, which suggests the snail sets were gathered together, but the pack gives no acquisition method for any of them.", "source": "repo:prototype/osfr-tools/data/content/collections.json:8838, 9230"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is evidenced. The first-pass guess of 'drop' has no support in the pack, and no wiki page, article, video frame, vendor, quest or drop answer names this item. Do not record a drop source until one is found.",
  "The wiki List of Collections entry for Solid Snails has entries_known=false and no reward data, so the collection's rewards and how its members are collected are unknown.",
  "Whether the item is still obtainable is unknown. The wiki list is dated July 2013, so the set was live then; nothing shows it being retired or still sold later.",
  "Possible sources to check: a snail or bug harvest/collection mechanic, a Solid Snail Platoon reward (locale 66697, not researched here), or an event. None is confirmed.",
  "The pack's wiki_page, images, article_facts, video and vendor_stock were all empty, so the search could not confirm any source. The critique field was not in the pack."
 ]}
