<!-- fleet job=citem-infer id=cpitiful-fossil-41022-v1 status=done turns=7 usd=0.0053 tokens(read,write,in,out)=[73837, 21670, 16, 3769] model=claude-haiku-5-5 -->
# Pitiful Fossil

{"item": {"name": "Pitiful Fossil", "locale_id": 41022, "kind": "collection"},
 "sources": [
  {"type": "drop", "detail": "Item-collection spawn pickup (sparkling spawn object) for the Mini Fossils collection; one of 8 pieces (entry 8 of 8, item_definition_id 3806). Exact spawn type and location not confirmed.", "where": "Sanctuary-linked area (collection item_link 'sanctuary'); Sunstone Valley/Blackspore fossil spawns are unconfirmed for this set", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8303 (collection id 102, Mini Fossils, name_id 7753); wiki Collections page (freerealms-wiki/wikitext/1991-45236-52bebd9576a3.wiki lines 14-15: item-collection pieces are found in sparkling spawn objects)"},
  {"type": "collection", "detail": "Completing the Mini Fossils collection (collection 102) awards 7 coins, item 3814 x1, and XP; this piece is one of its required entries.", "where": null, "price": "7 coins (collection reward)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8307-8326"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client item 41022 is 'Pitiful Fossil', description 'This item can be added to the Mini Fossils Collection' (locale 132361 / 2732578447).", "source": "locale:41022; locale:132361"},
  {"claim": "Mini Fossils is collection 102 (name_id 7753), entry 8 of 8 is item definition 3806 = Pitiful Fossil; the other entries are Tiny(41017)..Pint-sized(41021) Fossil.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8225-8305"},
  {"claim": "Mini Fossils is listed as a collection on the wiki List of Collections (rev 2013-07-13), so it existed in the 2009-2014 era.", "source": "https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "Item-collection pieces are found in sparkling spawn objects; each spawn yields one item.", "source": "Collections wiki page, freerealms-wiki/wikitext/1991-45236-52bebd9576a3.wiki lines 14-15"},
  {"claim": "No coin store price exists for item 3806 in stores.json; no vendor stocks it; no wiki article or video names this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json (no match); lookup wiki/articles/video (no matches)"},
  {"claim": "Sanctuary's client item definitions include 'Pitiful Fossil' (ClientItemDefinitions.json), confirming it as a shipped item.", "source": "refs: Sanctuary/src/Resources/ClientItemDefinitions.json:69654"}
 ],
 "confidence": 0.5,
 "open": [
  "The acquisition source is inferred from the collection type (sparkling spawn pickups), not from a source that names this piece. Which spawn type and zone yields Pitiful Fossil (common or rare spawn, Sanctuary vs Blackspore/Sunstone) is unverified.",
  "Pitiful Fossil's own drop rate and icon tint variant (icon_tint_id 112) are not sourced.",
  "No wiki page exists for the Mini Fossils set or this item; the list of collection entries in the wiki cannot be verified beyond the 2013 List of Collections.",
  "Collection 102's 7-coin reward is the completion reward for the whole set, not a per-item price."
 ]}
