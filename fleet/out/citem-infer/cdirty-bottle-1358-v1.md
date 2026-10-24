<!-- fleet job=citem-infer id=cdirty-bottle-1358-v1 status=done turns=5 usd=0.0038 tokens(read,write,in,out)=[42993, 15397, 12, 2828] model=claude-haiku-5-5 -->
# Dirty Bottle

{"item": {"name": "Dirty Bottle", "locale_id": 1358, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client text: locale 1358 is 'Dirty Bottle', with the description 'This item can be added to the Bottles Collection' (locale:132299 is the Bottles Collection UI line).", "source": "locale:1358; locale:132299; client_definition in quest-lines/citem-packs.json (cdirty-bottle-1358)"},
  {"claim": "Dirty Bottle is one of 11 items in the Bottles cluster (locale 1353-1363: Army Men, Dirty/Perfume/Water Bottle, Bottle of Sand, Baby Bottle, Message in a Bottle).", "source": "client_cluster in the evidence pack; locale:1353-1363"},
  {"claim": "The wiki's List of Collections lists a '[Bottles]' collection, and a My Collections video frame shows '[Bottles] (Collected: 8 / 8)', so the Bottles collection was live in the game client UI.", "source": "wiki: List of Collections; video:5apg6w6ZZeU/00024.jpg"},
  {"claim": "Client definition IDs 3210 (Dirty Bottle, NameId 1358, DescriptionId 132299) and 48250 share the name.", "source": "TCG-Files/Emulator/Resources/ClientItemDefinitions.json lines 67185-67195 (Id 3210, Comment 'Dirty Bottle')"}
 ],
 "confidence": 0.5,
 "open": [
  "No acquisition source found. The wiki, articles, video frames and repo have no page or answer saying how Dirty Bottle is obtained (no vendor stock, quest reward, drop, prize wheel or store listing). The pack's vendor_stock and mentioned_by_other_answers are empty, so no source is listed.",
  "The Bottles collection page (wiki 'List of Collections' '[Bottles]') was seen only as a title in the video frame; its member list (which bottles it contains, and where each one comes from) was not found. Check the collection's member list and the Bottles items' sources before adding any source.",
  "ClientItemDefinitions.json carries a 'Cost': 10 field on definition 3210. It is not a coin store price (coin_store_prices is empty and no stores.json entry was found), so it is not used as a vendor price. Confirm what the field means before treating it as a price.",
  "Definition 48250 is a second variant of the name, with no source data found. Two definitions share the name; it is unknown whether both are collectible.",
  "Live status is inferred from the collection being shown in a video frame and the first-pass tag, not from a dated source. Retired status is unknown."
 ]}
