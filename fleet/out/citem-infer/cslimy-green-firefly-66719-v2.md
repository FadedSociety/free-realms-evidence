<!-- fleet job=citem-infer id=cslimy-green-firefly-66719-v2 status=done turns=2 usd=0.0015 tokens(read,write,in,out)=[5501, 6665, 6, 1265] model=claude-haiku-5-5 -->
# Slimy Green Firefly

{"item": {"name": "Slimy Green Firefly", "locale_id": 66719, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 23106 is named 'Slimy Green Firefly' (name locale 66719; typed npc_name in the client) with description 'This item can be added to the Green Fireflies Collection'.", "source": "locale:66719; locale:132395"},
  {"claim": "Item 23106 is entry of collection 'Green Fireflies' (collection id 136, catalogue entry id 981, item_definition_id 23106 at line 10580).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:10580"},
  {"claim": "'Green Fireflies' is a named collection in the collection data (name at line 8922), listed on the wiki's List of Collections under Insects > Fireflies; that wiki listing is a 2013-dated secondary cite and does not establish current status.", "source": "repo:prototype/osfr-tools/data/content/collections.json:8922; https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "The sibling green firefly names (locale 66715-66722) are all typed item or npc_name, so the client types are inconsistent for this set; the name alone does not establish inventory-item status.", "source": "locale:66715-66722"},
  {"claim": "No coin store price (coin_store_prices empty), no wiki page, no video frame, no vendor stock, and no quest or drop answer names this item.", "source": "client definition in pack; lookup on 'Green Firefly' (client, wiki, video) returned only client name lines"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition method is unknown. No evidenced source (vendor, drop, quest, event, crafting, prize wheel) was found. The earlier 'drop' guess and the article fact about 'bugs found along the journey' are not specific to this item and were removed from sources.",
  "Only evidenced relation is membership in the Green Fireflies collection (collection 136, entry 981). This is a collection membership, not an acquisition source.",
  "The client types the name as npc_name, so the item may be a spawned creature collected in-world rather than an inventory drop. Needs an in-client check.",
  "Catalogue item_link is 'sanctuary' for the green firefly entries, suggesting a Sanctuary-area source, but no area, spawn or quest is named.",
  "Retired status unknown. The wiki list is dated 2013 and does not confirm whether the set is still obtainable. Live status is 'unsure': the definition exists in the shipped client, but no current source is confirmed."
 ]}
