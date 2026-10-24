<!-- fleet job=citem-infer id=celite-explorer-backpack-of-seaside-419892-v1 status=done turns=7 usd=0.0039 tokens(read,write,in,out)=[54061, 12413, 16, 3644] model=claude-haiku-5-5 -->
# Elite Explorer Backpack of Seaside

{"item": {"name": "Elite Explorer Backpack of Seaside", "locale_id": 419892, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (vendor not named in our data; stores.json lists the item with purchase price 270 coins, member price 243, sell price 27)", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:14930 (item_id 70346, category 106)"},
  {"type": "collection", "detail": "Reward for the Elite Explorer collection (collection_add 309, name_id 419914 'Elite Explorer'); the reward block grants 1 Elite Explorer Backpack of Seaside plus token 525", "where": "Seaside (zone of this variant's collection, per video frame and name)", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:21861 (reward block); locale:419914; video:QPhBoJrHSDI/00660.jpg (\"Collection Started: Elite Explorer ... You receive 1 Elite Explorer Backpack of Seaside\"); video:4kAFL0X0KkA/00888.jpg"},
  {"type": "other", "detail": "Video shows the item received in the Seaside zone from an NPC named Kendall, with an 'Elite Exploration Coin' prompt (exploration-coin reward chain; the exact quest/turn-in is not confirmed)", "where": "Seaside", "price": null, "currency": null, "source": "video:1gt4j8_A5Hc/00050.jpg; video:1gt4j8_A5Hc/00052.jpg"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name is 'Elite Explorer Backpack of Seaside', locale 419892; one of nine per-zone variants (Snowhill, Wugachug, Shrouded Glade, Briarwood, Blackspore, Merry Vale, Sanctuary, Sacred Grove) with consecutive ids 419887-419895", "source": "locale:419892; client cluster locales 419887-419895"},
  {"claim": "Coin store entry exists for item 70346 at 270 coins, member price 243, not no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:14930"},
  {"claim": "Item is the reward of an Elite Explorer collection (collection 309 'Elite Explorer', name_id 419914)", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:21861 and :23218; locale:419914"},
  {"claim": "Players receive the item from the Elite Exploration Coin / Kendall in Seaside, and get 'Collection Started: Elite Explorer' messages when it drops", "source": "video:1gt4j8_A5Hc/00050.jpg; video:QPhBoJrHSDI/00660.jpg"},
  {"claim": "Wiki Collections page describes [Elite] collections for every realm, with Seaside explorer collections listed", "source": "wiki: Collections; wiki: List of Collections"},
  {"claim": "Sibling backpacks (Explorer's, Pathfinder's, Seeker's, Traveler's) appear in the same inventory captures", "source": "video:22IH8XFo6R4/00024.jpg; video:MzxfUBdIIGU/00032.jpg"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin vendor that sells item 70346 is not named in stores.json; the vendor and zone need confirming in-client or on the wiki (no wiki page for this item).",
  "Collection-reward block at collection_catalogue.json:21857 is not tied to its parent collection id in my read; the reward may belong to a different collection than 309. Confirm the parent before relying on the collection source.",
  "Kendall / Elite Exploration Coin turn-in in Seaside is seen in video only; the exact quest or exchange and its cost are unconfirmed.",
  "No wiki article, article facts, or retirement info found; retired status unknown.",
  "Jev's first pass said 'live: yes, vendor' - the vendor claim is supported only by the 270-coin store row, not by a named vendor."
 ]}
