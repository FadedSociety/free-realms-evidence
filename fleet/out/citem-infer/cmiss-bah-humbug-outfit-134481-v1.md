<!-- fleet job=citem-infer id=cmiss-bah-humbug-outfit-134481-v1 status=done turns=5 usd=0.0025 tokens(read,write,in,out)=[16721, 8196, 12, 2571] model=claude-haiku-5-5 -->
# Miss Bah Humbug Outfit

{"item": {"name": "Miss Bah Humbug Outfit", "locale_id": 134481, "kind": "clothing"},
 "sources": [
  {"type": "event", "detail": "Snow Days holiday event (the female sibling of the Bah Humbug Outfit; the wiki page for the male version says it was sold for Snow Days events)", "where": null, "price": null, "currency": null, "source": "wiki page 'Bah Humbug Outfit' (male version, Snow Days wording); locale:134476"},
  {"type": "marketplace", "detail": "Station Cash Marketplace, Snow Days event listing (inferred from the male sibling; no wiki page for the female version)", "where": "SC Marketplace", "price": "not stated (wiki price text is truncated in the source)", "currency": "station_cash", "source": "wiki page 'Bah Humbug Outfit' (male version); female-specific listing unverified"},
  {"type": "coin_shop", "detail": "coin store listing, store category 201, item 76564; vendor not identified in the pack", "where": null, "price": "750 coins (member price 675 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 16192 (item 76564)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client defines Miss Bah Humbug Outfit as definition 76564, costume slot 17, class 1, with a female chest model (freestyle_<race>_f_chest_girlysanta.adr)", "source": "client definition in the evidence pack; locale:134481"},
  {"claim": "Client text 'Miss Bah Humbug Outfit - female' (locale:156904) marks it as the female variant of the Bah Humbug Outfit (locale:134476)", "source": "locale:156904; locale:134476"},
  {"claim": "The male Bah Humbug Outfit was sold through the Station Cash Marketplace during Snow Days events; the page says 'available exclusively to male avatars'", "source": "wiki page 'Bah Humbug Outfit'"},
  {"claim": "Store data lists item 76564 at 750 coins, member price 675 coins, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json:16192"},
  {"claim": "The Snow Days holiday set includes Candy Cane, Gingerbread, Reindeer, Snowman, Toy Soldier and other outfits, all in the same client name cluster", "source": "client_cluster locale:134476-134486"}
 ],
 "confidence": 0.5,
 "open": [
  "The coin store vendor for item 76564 (750 coins) is not identified; stores.json gives only category 201 and no vendor name. Confirm the vendor and whether the coin listing was a Snow Days-only sale.",
  "The Station Cash price of the female outfit is unknown. The wiki price text for the male outfit is truncated ('at the regular price of , and to..'), so the SC price and sale price must be recovered from the full page.",
  "The female outfit has no wiki page of its own. The Snow Days SC Marketplace source is inferred from the male sibling and should be checked against an SC listing for the female item.",
  "The retirement status is not stated in any source. The store data shows no_sale true, which suggests the coin listing is no longer sold, but this needs confirmation.",
  "The wiki's 'Snow Days' category is not confirmed for the female item, and no event dates are given in the pack."
 ]}
