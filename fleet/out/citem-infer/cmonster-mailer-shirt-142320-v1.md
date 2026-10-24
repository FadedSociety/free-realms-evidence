<!-- fleet job=citem-infer id=cmonster-mailer-shirt-142320-v1 status=done turns=7 usd=0.0058 tokens(read,write,in,out)=[84402, 25392, 16, 3527] model=claude-haiku-5-5 -->
# Monster Mailer Shirt

{"item": {"name": "Monster Mailer Shirt", "locale_id": 142320, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash bundle record 'Monster Mailer Shirt' (Store bundle Id 3732, MarketingItemId 76754, GameItemId 3379, tintable, launched 2009-12-06). The record has no usable price (Price 1 placeholder) and no wiki or article confirmation.", "where": "SC Marketplace (unconfirmed)", "price": null, "currency": null, "source": "refs:Sanctuary-PS3-20261009/src/Resources/StoreBundles.json:13748-13778"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 142320 'Monster Mailer Shirt'; description (locale 145053 per the bundle record) reads 'The shirt that growls back at unruly dogs.'", "source": "locale:142320; client definition pack"},
  {"claim": "Generic placeholder text locale 150515 'This is a Monster Mailer Shirt item.' is flagged placeholder, so it is not evidence of a live source.", "source": "locale:150515"},
  {"claim": "Three definitions (50438, 50450, 76754; tints 1, 2, 3 of one shirt) are in the coin store data at category 103 with purchase_price_coins 1761, member price 1584, no_sale true, and no price_provenance.", "source": "repo:prototype/osfr-tools/data/content/stores.json:8195, 8196, 16309"},
  {"claim": "The 1761 value is a legacy coin Cost that the repo itself cleared for other items: the entries for item 50363 and 50377 (Sgt. Stepper Jacket) note 'no coin vendor stocks the item, so the Legacy coin Cost of 1761 is cleared'. The same 1761 figure on the Monster Mailer Shirt is therefore not a verified vendor price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:8193-8194"},
  {"claim": "No vendor in the repo stocks definitions 50438, 50450 or 76754, and the pack lists no vendor stock or wiki page.", "source": "search of repo for 50438/50450/76754; vendor_stock empty in pack"}
 ],
 "confidence": 0.3,
 "open": [
  "Coin price: the 1761 coin figure is a legacy Cost not tied to a vendor. Treat it as unverified, not a coin vendor sale. The first-pass guess of 'vendor' is not supported.",
  "Source type: the only concrete source is a Station Cash bundle record (Id 3732) in the Sanctuary store data, with no price. Whether it was sold on the SC Marketplace, and at what price, needs a wiki page, article or video. Nothing found in lookup (wiki, articles, video returned no matches).",
  "Retirement: the bundle record has ExpireTime 2040-08-15, which is a placeholder and not a real retirement date. Retired status is unknown.",
  "Live status is unsure: the client carries the item, and a bundle record exists, but no confirmed sale or wiki page was found.",
  "No quest, drop, event, prize wheel or crafting source was found in the pack or repo."
 ]}
