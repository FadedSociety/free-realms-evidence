<!-- fleet job=citem-infer id=cisland-shirt-143565-v1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[17354, 8603, 10, 3220] model=claude-haiku-5-5 -->
# Island Shirt

{"item": {"name": "Island Shirt", "locale_id": 143565, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Palm Tree Island Shirt, added for the Seaside Summer Splash celebration (one of the 71 definitions under this name)", "where": "SC Marketplace", "price": null, "currency": "station_cash", "source": "article: http://www.freerealms.com:80/article/detail.action?articleId=137"},
  {"type": "marketplace", "detail": "Dark Flower Island Shirt (boys and girls, multiple colors), summer item", "where": "SC Marketplace", "price": null, "currency": "station_cash", "source": "wiki: Dark Flower Island Shirt; article: http://www.freerealms.com:80/article/detail.action?articleId=1521"},
  {"type": "membership", "detail": "Summer Membership Pass 2013 bonus: free Dark Flower Island Shirt with a 3-month pass (available June 4 to June 25, 2013; bonus item Star Lawn Chair)", "where": null, "price": "$9.99 for the 3-month pass (the shirt itself has no separate price)", "currency": null, "source": "wiki: Summer Pass; locale:813; locale:834"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "locale 143565 is the generic name 'Island Shirt'; the 71 definitions cover several named shirts (Palm Tree, Dark Flower, Doggy, Kitty, Festive Flower, Swirly Flower), each with its own source", "source": "locale:143565; locale:5239; locale:5241; locale:11654; locale:79207; locale:400145; locale:400180"},
  {"claim": "Palm Tree Island Shirt was added to the Marketplace for Seaside Summer Splash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=137"},
  {"claim": "Dark Flower Island Shirt is an All Jobs chest clothing item sold in the SC Marketplace during the Summer event and given to Members; wiki categories Membership and Station Cash", "source": "wiki: Dark Flower Island Shirt; wiki: Summer Pass"},
  {"claim": "Summer Pass 2013 gave a bonus Dark Flower Island Shirt", "source": "locale:813; locale:834"},
  {"claim": "Dark Flower Island Shirt was also listed as casual wear alongside Rubber Ducky Float and Palm Tree Hat", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1532"},
  {"claim": "A 270-coin store price exists in stores.json for many other item ids, but none of the 12 definition ids listed in the pack (51683-51694) appear in stores.json, so the 270 coin price is not tied to this item", "source": "repo:prototype/osfr-tools/data/content/stores.json (purchase_price_coins 270 on item_ids such as 47, 76, 82)"},
  {"claim": "Video frame shows a 'Doggy Island Shirt' item in a Trade Lobby, confirming variants are still in circulation as tradeable items; it does not give a source", "source": "video:UFsVcZ3X5iA/00048.jpg"}
 ],
 "confidence": 0.35,
 "open": [
  "The pack's 'coin_store_prices: [270]' is not linked to any definition id; no stores.json entry for 51683-51694. Do not treat 270 coins as this item's price until the item id is found.",
  "The first-pass 'vendor' source guess has no support: vendor_stock is empty and no coin vendor is evidenced for any Island Shirt variant.",
  "Prices for the SC Marketplace Palm Tree and Dark Flower shirts are not in the sources we have (the wiki price text is blank in the lookup). Need the wiki page or the Marketplace listing for the price in Station Cash.",
  "Retirement: the Summer Pass sale window ended June 25, 2013; the Marketplace end dates for the shirts are not in the pack.",
  "The 71 definitions are not split by variant. Each named shirt (Palm Tree, Dark Flower, Doggy, Kitty, Festive Flower, Swirly Flower) needs its own item id and source sheet. The pack's name-level sources cannot be applied to all 71.",
  "Doggy, Kitty, Festive Flower and Swirly Flower shirts have no source evidence in this pack. The Festive and Swirly variants may be holiday or event items; not checked.",
  "The pack carries no critiques. The item-level kind is clothing (slot 3, chest) which is supported by the client definition."
 ]}
