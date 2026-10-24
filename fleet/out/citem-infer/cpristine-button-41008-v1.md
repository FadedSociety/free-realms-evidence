<!-- fleet job=citem-infer id=cpristine-button-41008-v1 status=done turns=5 usd=0.0038 tokens(read,write,in,out)=[36331, 16412, 12, 2698] model=claude-haiku-5-5 -->
# Pristine Button

{"item": {"name": "Pristine Button", "locale_id": 41008, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Awesome Buttons collection (wiki collection name; catalogue collection id 101, entry 724 = item_definition_id 3792, icon tint 125). Pristine Button is one of 11 button entries (41003-41013) that make up the set; it is a collection entry, not a sold item.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8141 (name_id 41008, item_definition_id 3792); repo:prototype/osfr-tools/data/content/collections.json:9678 (Awesome Buttons, wiki:6:166); wiki page List of Collections, https://freerealms.fandom.com/wiki/List_of_Collections (revision 27852, 2013-07-13), section 'Awesome Buttons'"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client text for locale 41008 is 'Pristine Button', with description 'This item can be added to the Awesome Buttons Collection' (ucdt 1136976005).", "source": "locale:41008; opening-native-lobby-20261009T163603Z/locale/en_us_data.dat:30136"},
  {"claim": "Item definition 3792 is entry 724 of collection id 101 (Awesome Buttons), name_id 41008.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:8141-8145"},
  {"claim": "The wiki lists Awesome Buttons as a collection with the flavour text 'Be on the lookout for every imaginable button...'.", "source": "wiki page List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections); freerealms-wiki/wikitext/1991-45236-52bebd9576a3.wiki:49-50"},
  {"claim": "No coin store price exists for item 3792 in the client definition or repo stores.json; it is not sold in a coin vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json (no item_id 3792 match)"},
  {"claim": "Community server definition carries the same 'Pristine Button' name for this item.", "source": "refs:Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:69416"}
 ],
 "confidence": 0.5,
 "open": [
  "How a player obtains an individual Pristine Button (drop, quest reward, crafting, or collection-completion reward) is not documented in any source here. The collection catalogue row for collection 101 gives no reward rows for 3792 in the excerpt read; check the collection reward and quest tables for the Awesome Buttons collection.",
  "No wiki article, video, or article fact names this specific button; the wiki only lists the Awesome Buttons collection as a whole.",
  "The 11-button set (41003-41013) is one collection; its per-button sources and any set-completion reward were not checked individually.",
  "Retired status and any later unobtainability are unknown."
 ]}
