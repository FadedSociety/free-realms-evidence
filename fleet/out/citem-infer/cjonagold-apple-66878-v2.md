<!-- fleet job=citem-infer id=cjonagold-apple-66878-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5654, 7146, 6, 2183] model=claude-haiku-5-5 -->
# Jonagold Apple

{"item": {"name": "Jonagold Apple", "locale_id": 66878, "kind": "collection"},
 "sources": [{"type": "collection", "detail": "Entry of the 'Red Apples' collection (catalogue collection id 157, name_id 67523, entry id 1140, item_definition_id 23265). Entries: Robgoblin, Gala, Braeburn, Pixiewood, Honeycrisp, Jonagold, Sweet Apple (locale 66873-66879). The individual apple's acquisition method is not evidenced.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:12116 (name_id 67523) and :12183 (item_definition_id 23265); locale:132416 ('Red Apples Collection', 'This item can be added to the Red Apples Collection'); wiki \"List of Collections\" (https://freerealms.fandom.com/wiki/List_of_Collections) lists '[Red] [Apples]' under Flora / Common, with no entry list or reward given"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Jonagold Apple' is locale 66878 and sits in a block of apple names 66864-66879 (Granny Smith through Sweet Apple).", "source": "locale:66878; locale:66873-66879"},
  {"claim": "Client description for item definition 23265 reads 'This item can be added to the Red Apples Collection'. The matching collection-name line is locale:132416 'Red Apples Collection'.", "source": "client_definition; locale:132416"},
  {"claim": "The repo catalogue lists item_definition_id 23265 as an entry of collection name_id 67523 'Red Apples'.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:12116, 12183; repo:prototype/osfr-tools/data/content/collections.json:5531, 5552"},
  {"claim": "The wiki 'List of Collections' has a 'Red Apples' collection (shown as '[Red] [Apples]') under the Flora / Common group, alongside Roses, Daisies, Green [Apples] and other harvested plants. This suggests the set is gathered from flora, but the wiki page gives no entries or reward, so it does not confirm the Jonagold entry or any Sanctuary source.", "source": "lookup wiki:page:ns0 'List of Collections'; repo:prototype/osfr-tools/data/content/collections.json:5528-5554"},
  {"claim": "No coin store price (stores.json has no entry for item 23265 and coin_store_prices is empty) and no vendor stock. No quest, drop or event source was found.", "source": "client_definition; repo:data/content/stores.json"},
  {"claim": "The pack's previous answer placed the apple in 'Sanctuary' only because every catalogue entry carries item_link 'sanctuary'. That tag does not give an acquisition location, so the Sanctuary location is removed here.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:12114-12209 (item_link only)"},
  {"claim": "The 4-coin + 50-XP reward for completing Red Apples appears only in the repo catalogue. It is not confirmed by wiki or client, and it is a reward for the whole set, not a source of the single apple. It is left out of the sources.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:12196-12205 (catalogue only)"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition method for the individual Jonagold Apple is unknown. It is likely a harvest from a Flora node, based on the wiki's Flora grouping, but no source confirms this. Do not wire it until a harvest node, drop or reward is evidenced.",
  "Sanctuary as a location is unsupported; the catalogue item_link 'sanctuary' is not a location source.",
  "Wiki 'List of Collections' (rev 27852, 2013) gives no entry list or reward for Red Apples, so the collection membership of Jonagold rests on the repo catalogue alone.",
  "Collection completion reward (4 coins, 50 XP) is catalogue-only and unverified. It is not listed as an item source.",
  "Retired and live status unknown: no retirement notice found. The first-pass 'live=yes' is a hint only; the wiki's 2013 date is the latest evidence.",
  "The critique's 'wireable' flag is set to false: no evidenced acquisition exists yet."
 ]}
