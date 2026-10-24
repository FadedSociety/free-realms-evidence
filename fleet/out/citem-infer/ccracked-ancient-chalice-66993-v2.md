<!-- fleet job=citem-infer id=ccracked-ancient-chalice-66993-v2 status=done turns=3 usd=0.0038 tokens(read,write,in,out)=[19661, 17860, 8, 2761] model=claude-haiku-5-5 -->
# Cracked Ancient Chalice

{"item": {"name": "Cracked Ancient Chalice", "locale_id": 66993, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry (index 2) of the Ancient Chalice Artifacts collection (collection id 172, name locale 67538). The entry is a collection slot, not a purchasable item. How a player first obtains the physical item is not evidenced in any source.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13575-13579 (name_id 66993, item_definition_id 23380, item_link 'sanctuary'); wiki: List of Collections, '[Ancient] [Chalice] [Artifacts]' (page_id 2038, revision 27852, 2013-07-13)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: item 23380, name locale 66993 'Cracked Ancient Chalice', description 'This item can be added to the Ancient Chalice Artifacts Collection' (locale:132431). coin_store_prices is empty, so there is no coin store price.", "source": "locale:66993; locale:132431; client definition in pack"},
  {"claim": "The collection 'Ancient Chalice Artifacts' (locale:67538, description locale:67650 'Ancient chalice artifacts in various conditions...') is listed on the wiki List of Collections page. The listing gives the collection name only, not the individual chalice entries or how they are obtained.", "source": "wiki: List of Collections (page_id 2038); lookup '[Ancient] [Chalice] [Artifacts]'; repo:prototype/osfr-tools/data/content/collections.json:10966"},
  {"claim": "Video frame video:p5sDafXSQtQ/00114.jpg carries the collection tracker text '[Ancient] [Chalice] [Artifacts] 1/20', so the collection has 20 entries in the tracker. The same frame's items_seen list shows the Ancient Bone and other artifact collections with x/8 counts, not chalice items.", "source": "video:p5sDafXSQtQ/00114.jpg (lookup, and refs quest-lines/citem-packs.json:9398 other_text 'Ancient Chalice Artif...')"},
  {"claim": "The Cracked Ancient Chalice sits in a 11-item family in the client text (locale:66992-66998 and 66988-66991 for the Bone set), which is the same structure as the Ancient Bone Artifacts collection.", "source": "pack client_cluster; locale:66988-66998"},
  {"claim": "No vendor, quest, enemy drop, event, prize wheel, crafting, or Marketplace source for item 23380 was found in the repo, wiki, articles, or refs.", "source": "repo search for 23380 and 'Ancient Chalice'; refs search; lookup over client, wiki, articles, video"}
 ],
 "confidence": 0.3,
 "open": [
  "The acquisition path for the physical Cracked Ancient Chalice (drop, dig or harvest node, quest, or other) is not documented in any source. The only source is the collection-entry record, so the sources array has no purchase or acquisition route.",
  "The collection catalogue marks every entry, including 23380, with item_link 'sanctuary'. That means the entry link comes from Sanctuary-server data and is not verified against live behaviour.",
  "The 2 coins and 50 XP is the whole-collection completion reward (collection_catalogue.json:13540-13552). It is not a price or a source for this chalice, so it is left out of sources. The earlier critique's point stands.",
  "The tracker frame shows 1/20, so the full set size is 20. The catalogue has fewer entries recorded. Confirm the full entry list before rebuilding the collection.",
  "live stays 'unsure' and retired stays null: the wiki list is dated 2013 and gives no retirement date. The earlier critique's claim that the video frame was unsupported is wrong: the frame text is confirmed by lookup and refs, but it confirms only the collection name and the 1/20 count, not this item."
 ]}
