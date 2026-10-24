<!-- fleet job=citem-infer id=cfelt-beret-4415-v1 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[4186, 11141, 6, 2628] model=claude-haiku-5-5 -->
# Felt Beret

{"item": {"name": "Felt Beret", "locale_id": 4415, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, base item 210 (tint group 2), with tint variants 79421 (tint group 1) and 79422 (tint group 3) at the same price; the vendor NPC is not named in our data", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 210 (line 129), item 79421 (line 17170), item 79422 (line 17171)"},
  {"type": "prize_wheel", "detail": "Level 17 members-only Farming wheel, reward from Sal Monella's Shopping List and Terrence's Shopping List (wiki); video frames show the Felt Beret as a wheel win on Lucca De'Flor's and Lumlot's Shopping List wheels", "where": "Farming wheel (Freestyle Jobs)", "price": null, "currency": null, "source": "wiki page 'Felt Beret'; video:ljDRabG8Akk/00422.jpg; video:ljDRabG8Akk/00450.jpg"},
  {"type": "membership", "detail": "White Snowfall Felt Beret introduced as part of the November 2009 Monthly Member Bonus / Member's Pack (with Trendy Sunglasses and Sport Shades)", "where": null, "price": null, "currency": null, "source": "wiki page 'Felt Beret'; wiki page 'Trendy Sunglasses' and 'Sport Shades' (November 2009 Member's Pack)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Felt Beret' is locale 4415, description 'Snug to the fit.' (locale 4416)", "source": "locale:4415; locale:4416"},
  {"claim": "Item 210 and tint variants 79421 and 79422 are sold in the coin store at 270 coins, member price 243, sell price 27, with source tags including R1/R2/T633", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 129, 17170, 17171"},
  {"claim": "Felt Beret is a members-only Freestyle Jobs head clothing item, a reward from the level 17 Farming wheel for Sal Monella's and Terrence's Shopping Lists", "source": "wiki page 'Felt Beret'"},
  {"claim": "Felt Beret appeared as a wheel win on the Shopping List wheels", "source": "video:ljDRabG8Akk/00422.jpg; video:ljDRabG8Akk/00450.jpg; video:pjvw6oAT-zQ/00060.jpg"},
  {"claim": "Felt Beret is in the Adventurer and Farmer wiki context as a head item and a spin-wheel item", "source": "wiki pages 'Adventurer', 'Farmer'"},
  {"claim": "Wiki 'Trendy Sunglasses' / 'Sport Shades' pages list the white Felt Beret in the November 2009 Member's Pack and carry Category:Unobtainable (for those pages, not confirmed for Felt Beret itself)", "source": "wiki pages 'Trendy Sunglasses', 'Sport Shades'"}
 ],
 "confidence": 0.7,
 "open": [
  "Coin vendor NPC and zone for the 270-coin sale are not named in the pack; vendor_stock is empty. stores.json category_id 101 should be mapped to a vendor before this source is finalized.",
  "Whether the Snowfall Felt Beret from the November 2009 pack is still obtainable is not stated on the Felt Beret page; the Unobtainable category sits on the sibling pages, so the retired status is unconfirmed.",
  "Wheel drop rate and whether the Farming wheel is still live are not in the pack.",
  "Wiki price on the Felt Beret page is absent; the 270-coin price is from our store data only, with the member price 243 coins. No sale-price history was found."
 ]}
