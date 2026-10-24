<!-- fleet job=citem-infer id=cpet-dog-small-pointy-darkmark-tan-75091-v2 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[5327, 7200, 6, 1768] model=claude-haiku-5-5 -->
# Pet: Dog: Small Pointy: darkmark-tan

{"item": {"name": "Pet: Dog: Small Pointy: darkmark-tan", "locale_id": 75091, "kind": "pet"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing, item definition 23951 (legacy CoinShopItems Cost). Unverified starting price: the vendor NPC and shop page are not named, and the Coin Shop note says the Cost-to-buy mapping has not been checked against a real client transaction.", "where": null, "price": "540 coins (member price 486 coins, 10% member discount, derived rule R; sell-back 54 is a derived rule T633, not a source)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23951 (line 6828); client definition coin_store_prices 540; notes/Research/Coin Shop.md lines 33-34"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 75091 is 'Pet: Dog: Small Pointy: darkmark-tan', one of the Small Pointy dog colour variants (locale 75086-75096; locale 75085 'solid-gold' sits just before the cluster).", "source": "locale:75091; locale:75086-75096; lookup client results"},
  {"claim": "Item definition 23951 carries a legacy Cost of 540 coins (member price 486), i.e. a catalogue price in the coin store data.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23951; client definition coin_store_prices 540"},
  {"claim": "The Cost field is a starting price, not a verified transaction; the mapping has not been checked against a live client purchase.", "source": "notes/Research/Coin Shop.md lines 33-34"},
  {"claim": "No wiki page, image, article fact, video frame, quest reward, drop or other answer names this pet. The vendor claim in the first-pass tag is a hint only and is not used.", "source": "lookup wiki/articles/video/client searches for 'Small Pointy dog pet' (no wiki or article hits)"},
  {"claim": "Critique: Cost alone does not prove a sale, since the same file sets Cost to no_sale for some rows that no vendor stocks (stores.json 23941, 23943, 23957, 23961). Sibling rows 23938-23953 sharing 540 show a shared default, not a group sale, so that is not counted as support.", "source": "critique (evidence lens) on pack; repo:prototype/osfr-tools/data/content/stores.json rows 23938-23961"}
 ],
 "confidence": 0.3,
 "open": [
  "Coin price is an unverified legacy catalogue Cost (540), not a confirmed sale. Do not wire as a live vendor sale until a vendor, wiki page or client transaction names it.",
  "The vendor NPC and shop location are not identified. stores.json source_tags (L1, L2, L4, R2, T633, R1) are data-field tags, not vendor names.",
  "Live status and retirement are unknown. retired is null; the coin price may never have been live in 2009-2014.",
  "Jev's first-pass 'vendor' guess is unsupported by evidence and is not used."
 ]}
