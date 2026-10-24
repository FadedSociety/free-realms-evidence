<!-- fleet job=citem-infer id=c16oz-steak-4139-v1 status=done turns=5 usd=0.0049 tokens(read,write,in,out)=[47265, 18597, 12, 4145] model=claude-haiku-5-5 -->
# 16oz Steak

{"item": {"name": "16oz Steak", "locale_id": 4139, "kind": "consumable"},
 "sources": [
  {"type": "vendor", "detail": "Guppie, lure vendor (client: \"Buy a lure (name) from Guppie in Sacred Grove Shallows.\" 1920656359; \"purchase a lure from Guppie\" 2184478761). Stock and prices for Guppie were not seen in the client, so it is not confirmed that Guppie sells this lure specifically.", "where": "Sacred Grove Shallows", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Jobs/Fisherman.md:40 and :64 (client lines 1920656359, 2184478761); wiki Fisherman page is the only wiki text naming the lure"},
  {"type": "coin_shop", "detail": "Lures are sold in the Coin Shop under supplies (per the wiki, as recorded in our notes). Not reproduced in my own lookup, so treat as unverified.", "where": "Coin Shop", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Jobs/Fisherman.md:262 (cites [wiki]); no wiki page found by direct lookup"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "The item name '16oz Steak' is locale 4139, a bare item name; the lure's own name string is '16oz Steak - Lure' (locale 412633) and '16oz Steak- Lure' (locale 412920, 415412580 in the data file).", "source": "locale:4139; locale:412633; locale:412920; locale/en_us_data.dat:10983"},
  {"claim": "The lure's own description is 'This lure grants you 10% higher chance of catching Winter Pirahna, Toothy Tetra and Blind Swurglefish.' (locale 412634). The pack's description string is locale 4141, which sits in the Flyfisher 3000 block and describes the Flyfisher lure's fish sibling set, so the pack's description attribution is wrong.", "source": "locale:412634; locale:4141 (listed under Flyfisher 3000 in the client cluster)"},
  {"claim": "fishing.json lists the 16oz Steak lure with 10% bonus, but the fish group it pairs (talking_bass, cheery_salmon, bitter_betta) does not match the description text (Winter Piranha, Toothy Tetra, Blind Swurglefish). Its name pairing is from the wiki and is in conflict with the client line.", "source": "repo:prototype/osfr-tools/data/content/fishing.json:1383-1394"},
  {"claim": "Wiki Fisherman page lists '16oz Steak' with the description 'This lure gives a 10% better chance of catching Winter Piranha, Toothy Tetra and Blind Swurglefish.'", "source": "wiki page: Fisherman"},
  {"claim": "Client Fisherman lines for the fish: 'The Blind Swurglefish likes the savory 16oz Steak!', 'The Toothy Tetra likes the savory 16oz Steak!', 'The Winter Piranha likes the savory 16oz Steak!'", "source": "locale:29756; locale:29764; locale:29778"},
  {"claim": "No store price for this item in the client definition (coin_store_prices empty) and no station cash or prize wheel listing found.", "source": "client definition 68152; repo search of stores found no lure entries"}
 ],
 "confidence": 0.5,
 "open": [
  "Client definition 68152 description text is the Flyfisher 3000 line (4141); the correct description for 16oz Steak is locale 412634. Confirm which string the definition really carries before the rebuild uses it.",
  "Name conflict: locale 4139 '16oz Steak' vs lure name '16oz Steak - Lure' (412633). Confirm whether definition 68152 is the lure (likely) or a separate consumable named 16oz Steak.",
  "Lure fish pairing in fishing.json (talking_bass, cheery_salmon, bitter_betta) conflicts with the client text (Winter Piranha, Toothy Tetra, Blind Swurglefish). Fix the fishing.json row.",
  "No coin price in stores.json for definition 68152: the Coin Shop claim rests only on the Fisherman notes citing the wiki; I could not reproduce it.",
  "Guppie's stock and prices are not seen; the vendor link is inferred from the quest lines that say to buy a lure from Guppie.",
  "Wiki spelling 'Piranha' vs client 'Pirahna' (locale 412634 / 4141) is a typo in the client; the wiki spelling is used here.",
  "Sale price, currency and retired status are unknown; no source states them."
 ]
}
