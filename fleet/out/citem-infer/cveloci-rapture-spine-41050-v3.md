<!-- fleet job=citem-infer id=cveloci-rapture-spine-41050-v3 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[30031, 13896, 10, 2624] model=claude-haiku-5-5 -->
# Veloci-rapture Spine

{"item": {"name": "Veloci-rapture Spine", "locale_id": 41050, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: item definition 3834, name locale 41050, description locale 132365 'This item can be added to the Spine Fossils Collection'. No coin store price and no model files.", "source": "locale:41050; locale:132365; repo:prototype/osfr-tools/data/content/collection_catalogue.json line 8679 (item_definition_id 3834, collection 106 'Spine Fossils', name_id 7757)"},
  {"claim": "The wiki List of Collections (revision 27852, 2013-07-13) lists '[Spine] [Fossils]' as a collection. In the page text it appears in the block before the '[Rare]' heading, not under Rare. The Rare section holds Skull [Fossils] and Bird Wing [Fossils].", "source": "wiki: List of Collections (page_id 2038, revision 27852); repo:prototype/osfr-tools/data/content/collections.json lines 11074-11101 (key wiki:7:216, name_id 7757)"},
  {"claim": "The wiki collection record for Spine Fossils has no entries, no reward and no spawn type. It names no item and no source.", "source": "repo:prototype/osfr-tools/data/content/collections.json lines 11074-11101 (entries [], reward null, spawn_type null)"},
  {"claim": "The wiki Blackspore Swamp Gathering node '[Pile of] [Fossils] ([Rare] [Collection])' and the Spawn Types entry '[Pile of] [Fossils]' exist. The 'Pile of Fossils' wiki image and a video frame (yv37TmrcE-M/00522) show that node. None of them names the Veloci-rapture Spine, so they are not a source for this item.", "source": "wiki: Blackspore Swamp (Gathering); wiki: Spawn Types; image:world_screenshot 'Type fossilR.jpg'; video:yv37TmrcE-M/00522.jpg"},
  {"claim": "No vendor stock, coin store price, quest reward, enemy drop or event naming this item was found in the client, wiki, articles or video lookups.", "source": "lookup 'Veloci-rapture Spine' (client, wiki, articles, video): only locale:41050; search of repo json for item 3834: only collection_catalogue.json line 8679"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is evidenced. The item is a collection-only piece and the Spine Fossils collection has no reward or entry data. Whether it comes from the Pile of Fossils gathering node, an enemy, or a collection reward is unknown. Check a dated wiki page, video, or the collection reward data for collection 106.",
  "The previous answer's 'Pile of Fossils (Rare Collection)' source is removed. The wiki does not tie that node to this item.",
  "The previous answer's claim that Spine Fossils sits in the Rare section is wrong. The list places it before the Rare heading.",
  "Retirement status is unknown. The collection was listed on a 2013 wiki revision, which does not show the item was obtainable in the 2009-2014 era.",
  "Price unknown: no coin store entry and no Station Cash listing.",
  "The collection_catalogue row for item 3834 carries item_link 'sanctuary'. This is a catalogue field, not an acquisition source.",
  "Jev first-pass tag 'drop' is a hint only and is not used as evidence."
 ]}
