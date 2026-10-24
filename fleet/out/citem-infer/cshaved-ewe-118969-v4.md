<!-- fleet job=citem-infer id=cshaved-ewe-118969-v4 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6055, 9765, 6, 2381] model=claude-haiku-5-5 -->
# Shaved Ewe

{"item": {"name": "Shaved Ewe", "locale_id": 118969, "kind": "pet"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, vendor not identified. No vendor stock row names definition 17541. Treat as a price candidate, not a confirmed vendor stock entry.", "where": null, "price": "10000 coins (member price 9000 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:4332 (item_id 17541, category 200, tint_group_id 2, purchase 10000, member 9000, no_sale true); client definition 17541 coin_store_prices [10000]"},
  {"type": "collection", "detail": "Sanctuary collection entry id 1802 (index 2), name_id 17541, which maps to item_definition_id 9173, not 17541. Unconfirmed whether this grants the Shaved Ewe pet or a different item.", "where": "Sanctuary", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:18281-18288"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 17541 is the pet 'Shaved Ewe' (name locale 118969, description 'This simple pet will only follow you around and keep you company.', model ewe_shaved.adr, one definition) with coin_store_prices [10000].", "source": "client definition (pack); locale:118969"},
  {"claim": "stores.json item 17541 is priced 10000 coins, member 9000, no_sale true, sell_price null. It sits in a run of 28 rows (17529-17554) with the same price and source tags. Its tint_group_id is 2, so it reads as a tinted variant in a pet family block, not a standalone vendor row.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4320-4345"},
  {"claim": "collection_catalogue entry id 1802 has name_id 17541 and item_definition_id 9173 (item_link sanctuary). The key 17541 is used as a name id here, which leaves the store key ambiguous.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:18281-18288"},
  {"claim": "Locale 3132, 150098 and 150838 describe a 30-minute Shaved Ewe food that transforms the player; locale 147594 is 'Illusion: Ewe Shaved - 30 minutes'. These are separate items, not the pet.", "source": "locale:3132; locale:150098; locale:150838; locale:147594"},
  {"claim": "Wiki, articles and video lookups for 'Shaved Ewe' returned no matches, so no wiki page, article or video frame names the pet.", "source": "lookup wiki/articles/client 'Shaved Ewe pet' (no matches)"}
 ],
 "confidence": 0.3,
 "open": [
  "Vendor identity is unresolved. No vendor stock row names definition 17541, so the coin-store price cannot be wired to a specific vendor.",
  "Store key ambiguity: stores.json 17541 (tint group 2, 10000 coins) versus collection name_id 17541 -> definition 9173. Confirm whether store item_ids are definition ids or name ids. If they are name ids, the price may belong to a different tinted variant.",
  "Retired status is unknown. no_sale true and null sell price are store-flag hints only; no source confirms the pet is no longer sold.",
  "The Sanctuary collection entry (id 1802) is a candidate only. It points at definition 9173, so it may not grant this pet.",
  "The first-pass 'live: yes' has no source and was not used.",
  "Baby Black Widow (locale 118964), a pet in the same cluster, is reported on the wiki Pet Pals list as a Coin Shop item sold only during a holiday. A similar seasonal pattern for Shaved Ewe is plausible but unverified.",
  "The 30-minute Shaved Ewe food and the Illusion item need their own entries and are not sources for the pet."
 ]}
