<!-- fleet job=citem-infer id=csolid-cocoon-66742-v3 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[6158, 7278, 6, 1785] model=claude-haiku-5-5 -->
# Solid Cocoon

{"item": {"name": "Solid Cocoon", "locale_id": 66742, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Cocoons collection (wiki List of Collections category 5, 'Cocoons'). Membership rests on the item description only; the collection entry list is empty in our data, so no entry names this item.", "where": null, "price": null, "currency": null, "source": "locale:132399 ('This item can be added to the Cocoons Collection'); repo:prototype/osfr-tools/data/content/collections.json lines 9479-9487 (key wiki:5:159, name 'Cocoons', entries_known false); https://freerealms.fandom.com/wiki/List_of_Collections"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Solid Cocoon' (definition 23129, name locale 66742) with description pointing to the Cocoons Collection", "source": "locale:66742; locale:132399"},
  {"claim": "No coin store price in the client definition (coin_store_prices empty), so no coin vendor sale is recorded", "source": "client definition for definition_id 23129"},
  {"claim": "Cocoons collection exists as wiki category row wiki:5:159 with no entries listed", "source": "repo:prototype/osfr-tools/data/content/collections.json lines 9479-9487"},
  {"claim": "A collection-catalogue reward row lists item_definition_id 23129 x1 with coins 4, XP 50 (profile 12), collection_add [140], under a collection id 79 (name_id 7730) rather than the Cocoons collection", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 5978-5997"},
  {"claim": "Lookup of 'Solid Cocoon' returns only the client locale line; no wiki page, article fact or video frame names the item", "source": "lookup, sources client/wiki/articles/video"}
 ],
 "confidence": 0.3,
 "open": [
  "Collection-catalogue reward for item 23129 (coins 4, XP 50, collection_add 140) sits under collection id 79 (name_id 7730), not the Cocoons collection (name_id 67506). Unresolved whether collection 79 is a different collection or the Cocoons link is wrong. Not wired as a source.",
  "Cocoons collection entry list is empty in our data; the membership source is description-only until a wiki entry or entry list names Solid Cocoon.",
  "Grexan's Camp removed as a source: the articles and locale text (locale:139305) describe cocoons as traps and rescue targets, and name no drop of Solid Cocoon. Unverified lead only.",
  "Locale block neighbours (Perfect Timing 66737, Flawless Precision 66738, Immense Courage 66739) carry no text linking them to cocoons; the four-colour set grouping is inference from locale ordering, not a source.",
  "No coin price, vendor stock, marketplace, prize wheel, drop, event or crafting evidence found. Retirement and current obtainability unknown.",
  "wireable: false until the collection-79 reward or a Cocoons entry list is confirmed."
 ]}
