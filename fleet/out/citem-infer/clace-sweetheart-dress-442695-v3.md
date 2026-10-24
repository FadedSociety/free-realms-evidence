<!-- fleet job=citem-infer id=clace-sweetheart-dress-442695-v3 status=nothing_found turns=3 usd=0.0027 tokens(read,write,in,out)=[18682, 12555, 8, 1830] model=claude-haiku-5-5 -->
# Lace Sweetheart Dress

{"item": {"name": "Lace Sweetheart Dress", "locale_id": 442695, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name text 'Lace Sweetheart Dress' is locale 442695; description 'This dazzling dress is perfect for a night on the town!' (locale 442697); definition id 78401, slot 3 (chest), class 173.", "source": "locale:442695; locale:442697; client definition in evidence pack"},
  {"claim": "stores.json item 78401 record: category_id 103, tint_group_id 1, purchase_price_coins 100, member_price_coins 90, sell_price_coins null, no_sale true, source_tags [L1, L2, L4, R2, L3, L3]. The record names no vendor, store, zone or stock row and has no price_provenance block (unlike neighbouring rows, which carry a reconstructed price basis).", "source": "repo:prototype/osfr-tools/data/content/stores.json:16826"},
  {"claim": "The 100-coin figure equals the client coin_store_prices [100]. That is a price value, not a stock row, so it does not show who sold the item.", "source": "repo:prototype/osfr-tools/data/content/stores.json:16826; client definition in evidence pack"},
  {"claim": "no_sale: true on the store row argues against a current coin sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:16826"},
  {"claim": "Lookup of the client text found only the locale line itself. No wiki page, article or video names this dress.", "source": "lookup: client locale:442695"},
  {"claim": "Sibling texts (locale 442694 Rhinestone Halter Top Dress, 442696 Dotty One Sleeve Dress, 442700 'New Party Dresses and Earrings!') suggest a shared dress batch. They are context only and do not name a source.", "source": "locale:442694, locale:442696, locale:442700"}
 ],
 "confidence": 0.15,
 "open": [
  "No evidenced acquisition source. The prior 'vendor' source is withdrawn: stores.json:16826 is a bare price record with no vendor, store or stock row, and it is flagged no_sale: true. It cannot be cited as a coin vendor sale.",
  "Live status is unsure. The no_sale flag argues against current availability. The first-pass live: yes is not supported.",
  "Retired is null: nothing dates the removal.",
  "wireable: false. A builder cannot place acquisition without a vendor/store id, wiki, video or article naming where the dress was sold.",
  "Locale 442700 'New Party Dresses and Earrings!' and the ad image 'Adventure With Style! Get a NEW [Party] [Dress]!!' are unverified context. Neither is cited as a source.",
  "Locales 442698 and 442699 duplicate the text of 442697 and are not separate items.",
  "Next steps: find a coin-store stock row for definition 78401 (or its tint variants), or a wiki/video/forum mention of a party dress sale. Check whether the store row's L1/L2/L4/R2/L3 source tags resolve to a vendor table."
 ],
 "critiques_addressed": "Evidence and world critiques accepted: vendor source removed; no_sale conflict stated; live not set to yes; where left null; wireable false; sibling and ad references kept as context only."}
