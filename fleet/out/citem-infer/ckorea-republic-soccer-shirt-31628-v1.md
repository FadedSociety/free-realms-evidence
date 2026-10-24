<!-- fleet job=citem-infer id=ckorea-republic-soccer-shirt-31628-v1 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[13082, 13614, 8, 3087] model=claude-haiku-5-5 -->
# Korea Republic Soccer Shirt

{"item": {"name": "Korea Republic Soccer Shirt", "locale_id": 31628, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for item 16311 (category 103, tint group 1), 50 coins, member price 45 coins (10% member discount); no_sale flag set, so it is not resold to players", "where": "coin store (stores.json category 103)", "price": "50 coins (member price 45 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:6623"},
  {"type": "marketplace", "detail": "2010 FIFA World Cup national-team soccer shirt set, sold through the Station Cash Marketplace. Sibling wiki pages for the same set (Brazil, Spain, Italy, Mexico, Korea DPR, New Zealand) each say this. No wiki page for Korea Republic itself.", "where": "Station Cash Marketplace", "price": null, "currency": null, "source": "wiki: Korea DPR Soccer Shirt; wiki: Mexico Soccer Shirt; wiki: Italy Soccer Shirt (sibling pages); locale:31627 and locale:31628 sit in the same client cluster"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client name 'Korea Republic Soccer Shirt' is locale 31628, description 'Show support of your favorite country's team!', chest slot (3), class 143, definition 16311, one variant", "source": "locale:31628; client definition"},
  {"claim": "Item 16311 is in the coin store data at 50 coins, member price 45 coins, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json:6623"},
  {"claim": "The sibling national-shirt pages (Brazil, Spain, Italy, Mexico, Korea DPR, New Zealand) say each was an unobtainable chest clothing item from the 2010 FIFA World Cup, acquired through the Station Cash Marketplace", "source": "wiki: Brazil Soccer Shirt; wiki: Spain Soccer Shirt; wiki: Italy Soccer Shirt; wiki: Mexico Soccer Shirt; wiki: Korea DPR Soccer Shirt; wiki: New Zealand Soccer Shirt"},
  {"claim": "Ref Ruby's World Cup video guide (June 2010) previewed new World Cup items; the post names no items or prices", "source": "articles/articles.json: Free Realms - What is New?: Ref Ruby's Video Guide to the World Cup"},
  {"claim": "Client cluster of 11 national shirts (locale 31623-31633) shares one naming pattern and sits in the same locale block", "source": "locale:31623 through locale:31633"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict on price and channel: the store data lists 50 coins (a coin-store price), but the wiki sibling pages say Station Cash Marketplace with no price. The 50 may be an internal coin-equivalent value or an error. Verify whether the 2010 shirts sold for Station Cash or coins before setting a price.",
  "No wiki page or direct source names Korea Republic Soccer Shirt. The marketplace source is inferred from the set siblings, not from a direct citation for this item.",
  "Retired status comes from the sibling pages ('unobtainable'), not from a direct source for this item. Live 'no' is an inference, so it contradicts the first-pass 'live: yes' tag, which is only a hint.",
  "Store data has 50 coins as the purchase price, but this is no_sale, so there is no sell price. Confirm whether the shirt was ever on sale in the coin store or only appears in the data.",
  "The 2010 World Cup event dates were not found in the sources; the set is only tied to the 2010 FIFA World Cup by the sibling pages."
 ]}
