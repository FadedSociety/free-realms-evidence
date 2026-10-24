<!-- fleet job=citem-infer id=cbig-cake-baking-book-67441-v1 status=done turns=4 usd=0.0030 tokens(read,write,in,out)=[21580, 11546, 10, 2739] model=claude-haiku-5-5 -->
# Big Cake Baking Book

{"item": {"name": "Big Cake Baking Book", "locale_id": 67441, "kind": "collection"},
 "sources": [
  {"type": "other", "detail": "Collection entry: the book is one of 8 entries in the 'Chef's Cake Baking Books' collection (Fancy, Big, Small, Kosher, Vegan, Sugar Free, Quick, Low Fat Cake Baking Book). Collection reward per wiki: 'Party Sized Platter'. Collection items are a Chef 'Job Material' spawn, Common quality, cascading wiki type. How an individual book is acquired (gathered/dropped/bought) is not documented in any source I checked.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json (key wiki:2:45, name_id 67594, entries 8); wiki page 'Job Specific (Collections)' https://freerealms.fandom.com/wiki/Job_Specific_(Collections) (revision 27853, 2013-07-13); lookup wiki hit listing the eight '[Cake] [Baking] [Book]' names under Chef's collection; video:0IaICGnTWWQ/00098.jpg (collection window 'Chef's Cake Baking Books', 'Rewards', reward tiles)"},
  {"type": "other", "detail": "Collection reward for completing the Chef's Cake Baking Books set: Party Sized Platter (a Chef/cooking item). Not the book itself.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json wiki:2:45 reward.wiki_lines; wiki 'Job Specific (Collections)'"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Big Cake Baking Book is locale 67441 and is listed in the Chef's Cake Baking Books collection with seven sibling books.", "source": "locale:67441; repo:prototype/osfr-tools/data/content/collections.json line 3163-3217"},
  {"claim": "The client definition (definition 23828) has no coin store price, no models, and the description says it can be added to the Chef's Cake Baking Books Collection.", "source": "client definition pack; locale:67441"},
  {"claim": "The Chef's Cake Baking Books collection appears in the live collection UI with a reward view (video frame shows 'Click Here to Select a Collection Chef's Cake Baking Books... Rewards').", "source": "video:0IaICGnTWWQ/00098.jpg"},
  {"claim": "The collection's wiki reward is Party Sized Platter, from the 2013 wiki page 'Job Specific (Collections)'.", "source": "repo:prototype/osfr-tools/data/content/collections.json wiki:2:45; https://freerealms.fandom.com/wiki/Job_Specific_(Collections)"},
  {"claim": "Chef notes record collection reward tiles of 20 coins with cake or whisk icons in the same video range.", "source": "repo:notes/Build Guides/Content/Jobs/Chef.md line 333; video:0IaICGnTWWQ/00098 to 00110"}
 ],
 "confidence": 0.45,
 "open": [
  "No source says how a single Big Cake Baking Book is obtained (job-material gather, enemy drop, quest, vendor, or Station Cash). The collection is marked spawn_type 'Job Material', which suggests Chef gathering, but that is an inference, not a confirmed source.",
  "No coin store price in client definition (coin_store_prices empty) and no vendor stock; no coin vendor or marketplace sale is evidenced.",
  "No wiki article for the individual book; the only wiki reference is the collection page.",
  "Retired status unknown; the 2013 wiki revision is the newest dated evidence.",
  "Cascading collection rewards and the exact 20-coin tile amounts still need a live-play check."
 ]}
