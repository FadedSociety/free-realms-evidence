<!-- fleet job=citem-infer id=cpet-dog-large-pointy-darkmark-brown-75124-v2 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[22052, 17133, 8, 2479] model=claude-haiku-5-5 -->
# Pet: Dog: Large Pointy: darkmark-brown

{"item": {"name": "Pet: Dog: Large Pointy: darkmark-brown", "locale_id": 75124, "kind": "pet"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing with no named vendor NPC. Store row lists purchase 540 coins, member price 486 (10% member discount), sell-back 54. No vendors.json entry links item 23974 to an NPC.", "where": null, "price": "540 coins (member 486 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23974 (line 6851); client coin_store_prices [540]"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client definition: definition 23974, name locale 75124, model dog_large_pointy.adr, one definition, slot 0, class 0; coin_store_prices [540].", "source": "client definition in evidence pack; locale:75124"},
  {"claim": "Coin store row for item 23974: purchase_price_coins 540, member_discount 10%, member_price 486, sell_price 54, no_sale false, source_tags L1,L2,L4,R2,T633,R1. The row has no price_provenance block.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23974 (line 6851)"},
  {"claim": "Sibling rows 23958-23979 share the same 540 / 486 / 54 values. Some rows (23961, 23966, 23978) carry provenance saying their 540 Legacy coin cost was cleared because no coin vendor stocks the item and they were reconstructed at 225 Station Cash. Row 23974 has no such provenance, so whether its 540 is a live price is unverified.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6835-6856"},
  {"claim": "The only repo hit for '23974' in vendors.json is a catalogue sha256 substring (line 46815), not an item reference. No vendor NPC links to item 23974.", "source": "repo search for '23974' (only stores.json matched as an item id)"},
  {"claim": "The 11-variant Large Pointy Dog set sits together in client text ids 75119-75129, with darkmark-tan (75153), solid-ivory (75152) and spots-ivory (75154) nearby.", "source": "locale:75119-75129; locale:75152-75154"},
  {"claim": "No wiki page, article, video frame or other answer names this pet. The wiki and article lookups returned nothing for it.", "source": "lookup on client/wiki/articles/video (no wiki or article match)"}
 ],
 "confidence": 0.3,
 "open": [
  "No vendor NPC or zone is confirmed. The 540-coin figure is a raw store-row value, not a verified live coin-vendor price.",
  "Sibling rows in the same run were reconstructed as legacy costs with no vendor. Row 23974 has no provenance block, so it is unclear whether its 540 is the same legacy value left in place.",
  "Live status is not confirmed by any dated or external source. no_sale=false in our data is the only support, and the source_tags are unexplained.",
  "No Station Cash Marketplace, quest, event, prize wheel or drop source is evidenced for this pet.",
  "Retirement status is unknown. Sibling tint variants were not priced individually."
 ]}
