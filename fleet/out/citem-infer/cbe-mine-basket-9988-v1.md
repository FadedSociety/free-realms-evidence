<!-- fleet job=citem-infer id=cbe-mine-basket-9988-v1 status=done turns=5 usd=0.0031 tokens(read,write,in,out)=[23413, 9688, 12, 3375] model=claude-haiku-5-5 -->
# Be-Mine Basket

{"item": {"name": "Be-Mine Basket", "locale_id": 9988, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for item 76822 (purchase 2000 coins, member price 1800 coins with 10% member discount, sell price 200 coins); category 54; the listing's source tags are L1, L2, L4, R2, T633, R1. The store data alone does not name a vendor, and the wiki does not corroborate a coin sale.", "where": "Coin store (stores.json category 54)", "price": "2000 coins (member 1800 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76822 (line 16334)"},
  {"type": "promotion", "detail": "Prize/gift item from the Gifting Basket, a housing item sold in the Station Cash Marketplace during the 2011 Festival of Hearts event. The wiki lists the Be-Mine Basket among the Gifting Basket's items, in Amethyst, Bubblegum, Rubyburst and Stonesurf colours. The Gifting Basket gives daily gifts for 30 days.", "where": "Player housing (Gifting Basket)", "price": null, "currency": null, "source": "wiki: Gifting Basket (https://freerealms.fandom.com/wiki/Gifting_Basket); wiki: Festival of Hearts; video:fktAs_GRrjM/00604.jpg"},
  {"type": "event", "detail": "2011 Festival of Hearts event (Be-Mine item set: Be-Mine Basket, Balloon, Large and Small Floral Arrangements, Bouquet)", "where": null, "price": null, "currency": null, "source": "wiki: Festival of Hearts (lists [Be-Mine] Bouquet as available only through the Gifting Basket); locale:9996 'Great for giving to that special someone.'"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client name 'Be-Mine Basket' is locale 9988, with description 'Great for giving to that special someone.' (locale:9996 is the Be-Mine items group line).", "source": "locale:9988; locale:9996"},
  {"claim": "The Gifting Basket was a housing item sold through the Station Cash Marketplace during the 2011 Festival of Hearts and can no longer be acquired.", "source": "wiki: Gifting Basket"},
  {"claim": "The Gifting Basket page lists Be-Mine Basket, Be-Mine Balloon, and Be-Mine Large/Small Floral Arrangements, each in Amethyst, Bubblegum, Rubyburst and Stonesurf.", "source": "wiki: Gifting Basket (search excerpt)"},
  {"claim": "Festival of Hearts wiki page says the Be-Mine Bouquet, Gifting Basket and Lovely T-Shirt were 2011-only items available through the Gifting Basket.", "source": "wiki: Festival of Hearts"},
  {"claim": "Coin store listing for item 76822 at 2000 coins (member 1800).", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76822"},
  {"claim": "Client text cluster 9985-9990 (Stone Heart's Bear, Hearts Wall Sticker, Be-Mine Balloon, Basket, Large/Small Floral Arrangement) is one Be-Mine set.", "source": "locale:9985-9990"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the wiki says the Gifting Basket group was sold only through the Station Cash Marketplace, while the coin store data lists the Be-Mine Basket at 2000 coins. The wiki page does not name the Be-Mine Basket as a standalone purchase, and no coin vendor is named, so the coin price is unverified as a sale. The coin price is kept as a listed price, not confirmed as a sale.",
  "The wiki does not give a station-cash price for the Be-Mine Basket itself. Only the Gifting Basket housing item has a Marketplace listing.",
  "Whether the Be-Mine Basket was a prize from the Gifting Basket or a separate Marketplace item is not clear from the excerpts. The full Gifting Basket page was not read.",
  "Live status: the wiki says the Gifting Basket cannot be acquired now, so the Be-Mine Basket is presumed retired. The source for that is the Gifting Basket page, not a page for this item."
 ]}
