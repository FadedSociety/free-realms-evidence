<!-- fleet job=citem-infer id=cghost-cupcake-16642-v1 status=nothing_found turns=4 usd=0.0026 tokens(read,write,in,out)=[20515, 10830, 10, 2084] model=claude-haiku-5-5 -->
# Ghost Cupcake

{"item": {"name": "Ghost Cupcake", "locale_id": 16642, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Ghost Cupcake' is locale 16642; description (locale 16655) reads 'This cupcake is sure to give a haunting good time.'; item class 9, slot 0, definition id 69840, one definition, no coin store price.", "source": "locale:16642; locale:16655; pack client_definition"},
  {"claim": "Client ability text 'Spell for halloween_consumable_ghost_cupcake' (locale 416880) shows the item is a Halloween-themed consumable whose effect is a spell, and it sits with sibling Halloween cupcakes (Bat, Raven) and Halloween spray/shard items in the locale block 16637-16647.", "source": "locale:416880; locale:16639; locale:16646; repo: FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat (ability and item entries)"},
  {"claim": "Community server definition files carry the 'Ghost Cupcake' comment on the same item block (Lxzxrus-Free-Realms-Server, Sanctuary, FreeRealms-Legacy ClientItemDefinitions.json), confirming the item is a defined client item, but none of them list a vendor, price, or drop.", "source": "refs: Sanctuary/src/Resources/ClientItemDefinitions.json; FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json"},
  {"claim": "No wiki page, article, video frame, vendor stock, store entry (data/content/stores.json has no item 69840), or quest/drop answer names Ghost Cupcake.", "source": "lookup (wiki, articles, client, video: no matches for 'Ghost Cupcake' or Halloween cupcake terms); repo search for 69840"}
 ],
 "confidence": 0.2,
 "open": [
  "Acquisition source unknown: the Halloween-event consumable guess (first pass 'event') is consistent with the 'halloween_consumable' ability naming and sibling items, but no source names how players got it. Needs a Halloween event/holiday source or a wiki Halloween category check.",
  "Price unknown: no coin store price in the client definition or stores.json.",
  "Retirement status unknown: no source states whether it was retired after the Halloween event.",
  "'live: yes' from the first pass is unverified; it is a hint only. Client presence does not prove it was obtainable.",
  "The citem-packs.json entries in quest-lines are internal pack data, not sources; they only repeat the locale line and were not used as acquisition evidence."
 ]}
