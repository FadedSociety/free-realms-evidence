<!-- fleet job=citem-infer id=cmystical-nettleseed-water-sample-41134-v1 status=done turns=9 usd=0.0079 tokens(read,write,in,out)=[174801, 29365, 20, 5011] model=claude-haiku-5-5 -->
# Mystical Nettleseed Water Sample

{"item": {"name": "Mystical Nettleseed Water Sample", "locale_id": 41134, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 8 (index 8, item definition 3918) of the 'Nettleseed Water Samples' collection (collection id 116, name_id 7767; the 8 entries are 41127 to 41134, item defs 3911 to 3918). The collection is a set of water samples, not a way to obtain the sample itself. Completing it gives 2 coins, 50 XP and item 23153.", "where": "Briarwood - Nettleseed", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 9640-9740 (collection 116, entry index 8, item_definition_id 3918); repo:prototype/osfr-tools/data/content/collections.json line 11302 (wiki:8:224 'Nettleseed Water Samples', from wiki List of Collections); locale:7843 'Samples of water that came from the village of Nettleseed.'; client definition 'This item can be added to the Nettleseed Water Samples Collection' (locale 305796500)"},
  {"type": "drop", "detail": "Unconfirmed for this item. Sibling samples were received from the Shady Smuggler marker in Nettleseed: 'You receive 1 Dirty Nettleseed Water Sample' and 'You receive 1 Magical Nettleseed Water Sample'. The first pass guessed drop, but no frame shows the Mystical sample, and nothing ties it to a specific enemy.", "where": "Briarwood - Nettleseed", "price": null, "currency": null, "source": "video:piWfe7lXZ9I/00399.jpg; video:piWfe7lXZ9I/00393.jpg (sibling items, not Mystical)"},
  {"type": "quest_reward", "detail": "Unconfirmed. The Nettleseed water quest 'You Can Lead a Tortoise to Water' has objectives to sample water at the waterfalls ('Sample the water at the base of the lower/upper waterfall in eastern Nettleseed'). These may hand out samples, but no repo or client line ties a sample item to them.", "where": "Briarwood - Nettleseed (eastern waterfalls)", "price": null, "currency": null, "source": "locale:39925; locale:41477; locale:41479"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Mystical Nettleseed Water Sample', locale 41134, item definition 3918; one definition, no coin store price.", "source": "locale:41134; client definition 3918"},
  {"claim": "It is entry 8 of the 'Nettleseed Water Samples' collection, next to the other Nettleseed samples (41127 to 41133).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 9640-9740; repo:prototype/osfr-tools/data/content/collections.json line 11302"},
  {"claim": "The collection's wiki entry is 'Nettleseed Water Samples' from List of Collections (rev 27852, 2013-07-13).", "source": "repo:prototype/osfr-tools/data/content/collections.json line 11302-11321 (wiki source https://freerealms.fandom.com/wiki/List_of_Collections)"},
  {"claim": "Sibling samples Dirty and Magical were received as drops near the Shady Smuggler marker in Nettleseed, so the family is live in the videos.", "source": "video:piWfe7lXZ9I/00399.jpg; video:piWfe7lXZ9I/00393.jpg"},
  {"claim": "No wiki page, article, vendor stock or coin store price covers the Mystical sample. A search of the client text, wiki, articles and video found no other mention.", "source": "lookup client/wiki/articles/video for 'Nettleseed Water Sample' (no wiki or article hits)"}
 ],
 "confidence": 0.35,
 "open": [
  "The actual acquisition of the Mystical sample is unknown. Only the collection membership is proven. Sibling samples were seen as Shady Smuggler-marker drops, but no video frame shows Mystical being received, so 'drop' is unproven for it.",
  "Check whether the eastern waterfall quest ('You Can Lead a Tortoise to Water', locale 39925) or the sample-collection flow gives the tiers, and which tier each step gives.",
  "The collection's completion reward (2 coins, 50 XP, item 23153) is from the repo. Item 23153 was not identified and may need its own check.",
  "Prices and retirement status are not given by any source. No coin store price exists for item 3918 (client definition shows none).",
  "The repo marks entries 'item_link: sanctuary' for this collection. That link type was not interpreted and may mean a Sanctuary-side source, which was not verified.",
  "The 'Shady Smuggler' marker in the video may be a nearby enemy label, not the item's source. The source attribution for the sibling samples should be checked in another frame."
 ]}
