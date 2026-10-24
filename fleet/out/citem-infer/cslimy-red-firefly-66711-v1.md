<!-- fleet job=citem-infer id=cslimy-red-firefly-66711-v1 status=done turns=11 usd=0.0080 tokens(read,write,in,out)=[197194, 30187, 24, 4585] model=claude-haiku-5-5 -->
# Slimy Red Firefly

{"item": {"name": "Slimy Red Firefly", "locale_id": 66711, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 5 of the Red Fireflies collection (collection id 135, name_id 67501, Insects category 5); the entry is a collectible added to the set via the 'This item can be added to the Red Fireflies Collection' line (locale:132394)", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:10474-10478 (entry id 973, item_definition_id 23098, item_link sanctuary); wiki List of Collections https://freerealms.fandom.com/wiki/List_of_Collections lists [Red] [Fireflies] under Insects"},
  {"type": "other", "detail": "Set-completion reward for Red Fireflies collection (not this item itself): 10 coins, item definition 23111 x1, 50 XP (profile 52), adds collection 137", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:10405-10424 (community-server data, sanctuary)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Slimy Red Firefly' is locale 66711, item definition 23098, with description 'This item can be added to the Red Fireflies Collection'", "source": "locale:66711; locale:132394"},
  {"claim": "Red Fireflies is a wiki collection in the Insects category of List of Collections", "source": "https://freerealms.fandom.com/wiki/List_of_Collections; repo:prototype/osfr-tools/data/content/collections.json:8978-8999 (wiki:5:141, name_id 67501)"},
  {"claim": "Sanctuary community catalogue lists the Red Fireflies set with eight firefly entries (Queen Orange range 66706 area to Red entries 66707-66714, item defs 23094-23100 etc.), with Slimy Red Firefly at index 5, item definition 23098", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:10426-10500"},
  {"claim": "No coin store price, no wiki article, no vendor stock, no quest or drop answer names this item; the client's coin_store_prices is empty", "source": "pack client_definition; repo search for 23098/66711 (only collection_catalogue.json)"}
 ],
 "confidence": 0.5,
 "open": [
  "How an individual Slimy Red Firefly is obtained (world catch/spawn, enemy drop, or other) is not evidenced anywhere in the repo, wiki or articles; the 'drop' guess in the first pass is unsupported. Need a wiki per-set page for Red Fireflies or a video/capture.",
  "No coin store price or Station Cash listing for item 23098 in stores.json; no marketplace, prize wheel, or event source found.",
  "Live status is unverified: the item is in the Sanctuary community catalogue and the wiki set list, but no wiki article or dated source confirms it was live or retired.",
  "Item 23111 (set reward) was not resolved to a name; not checked here.",
  "Wiki List of Collections (rev 2013) gives no entry lists or acquisition details for Insects sets; the per-set page for Red Fireflies is absent from the corpus."
 ]}
