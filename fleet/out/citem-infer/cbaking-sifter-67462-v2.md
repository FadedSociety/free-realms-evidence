<!-- fleet job=citem-infer id=cbaking-sifter-67462-v2 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[14688, 10039, 8, 2142] model=claude-haiku-5-5 -->
# Baking Sifter

{"item": {"name": "Baking Sifter", "locale_id": 67462, "kind": "collection"},
 "sources": [{"type": "collection", "detail": "Member piece of the Chef's Cake Baking Utensils collection (Cake Baking Whisk, Big Baking Spoon, Baking Pan, Baking Oven Mitt, Baking Mixer, Glass Bowl, Baking Sifter, Baking Rack). Completing the collection gives the Mystery Cake reward. How the individual piece itself is obtained (drop, gather, craft, or turn-in) is not documented.", "where": null, "price": null, "currency": null, "source": "locale:67462 (client description: 'can be added to the Chef's Cake Baking Utensils Collection'); wiki image File:Chef's baking utensils.png (collection image lists Baking Sifter; 'Rewards' heading); repo:prototype/osfr-tools/data/content/collections.json:3291 (Baking Sifter listed in the cascading collection, reward 'Mystery Cake' at line 3309); video:0IaICGnTWWQ/00110.jpg (in-game collection window); wiki ns0 'Mystery Cake' (reward)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Baking Sifter is defined as client item 23849 with name locale 67462 and a description tying it to the Chef's Cake Baking Utensils collection", "source": "locale:67462; client definition definition_ids 23849"},
  {"claim": "The collection image lists Baking Sifter among its eight pieces", "source": "wiki image:collection File:Chef's baking utensils.png"},
  {"claim": "The in-game collection window shows Baking Sifter as a collection item", "source": "video:0IaICGnTWWQ/00110.jpg"},
  {"claim": "The collection's reward is Mystery Cake (a reusable placed cake that gives Slice of Mystery Cake); the reward is not the piece", "source": "repo:prototype/osfr-tools/data/content/collections.json:3307-3309; wiki ns0 'Mystery Cake'; locale:139646"},
  {"claim": "Client definition has no coin store price and no vendor stock row for this item", "source": "client definition coin_store_prices empty; vendor_stock empty in pack"},
  {"claim": "The collection is typed Cascading with spawn_type 'Job Material'; this hints the pieces are job-material drops/gathers, but no source ties that to the Sifter", "source": "repo:prototype/osfr-tools/data/content/collections.json:3303-3305 (unverified hint)"}
 ],
 "confidence": 0.5,
 "open": [
  "The Sifter's own acquisition is unverified: no vendor, price, drop, quest, or event names it. The collection entry's 'Job Material' spawn type suggests gathered or dropped pieces, but this is unsourced for the piece; check the wiki Chef page or a player source before wiring.",
  "The pack's previous answer cited the Chef and List of Collections wiki pages without their text; they were not re-verified here and were dropped.",
  "The pack's previous answer cited the collection image as proof the Mystery Cake is the piece's source. It is the collection's reward only, not the piece's source.",
  "Retired/live status is unknown for both the piece and the collection; no shutdown or retirement source was found.",
  "No price, currency, or vendor for the piece. wireable is false."
 ]}
