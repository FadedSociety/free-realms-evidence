<!-- fleet job=citem-infer id=cbirthday-gift-14420-v1 status=done turns=4 usd=0.0019 tokens(read,write,in,out)=[13426, 6758, 10, 1929] model=claude-haiku-5-5 -->
# Birthday Gift

{"item": {"name": "Birthday Gift", "locale_id": 14420, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, item 77451 (vendor/store not identified in our data; store category 54)", "where": null, "price": "100 coins (member price 90 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 77451 (purchase_price_coins 100); client definition coin_store_prices 100"},
  {"type": "event", "detail": "Likely a Birthday event (anniversary) gift item, seen in a Birthday-event video frame; the event link is unconfirmed", "where": "Birthday event zones", "price": null, "currency": null, "source": "video:a1p2wZhNao0/00014.jpg (shows 'Birthday Gift' with Birthday T-Shirts during the Cake-Eating Cakelings minigame); wiki page Birthday Bash (event held each April for launch day)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name 'Birthday Gift' (locale 14420) with description 'Decorate your house with this wrapped birthday gift.' (locale 14425); it is a furniture-style house decoration (slot 0, class 0, model hsg_present_freerealms_02.adr)", "source": "locale:14420; locale:14425; client definition"},
  {"claim": "Store data lists item 77451 in category 54 at 100 coins, 90 coins for members; the sell price is 10 coins", "source": "repo:data/content/stores.json item 77451 (line 16675)"},
  {"claim": "Store source tags include L1, L2, L4, R2, T633, R1, which suggests a live store listing in the later data set", "source": "repo:data/content/stores.json item 77451"},
  {"claim": "Birthday Bash is an annual April event celebrating Free Realms launch day, with party items; the anniversary gift rewards included party t-shirts per zone and a Gifting Pinata", "source": "wiki Birthday Bash; articles http://www.freerealms.com/article/detail.action?articleId=2107"},
  {"claim": "Video frame shows 'Birthday Gift' alongside Birthday T-Shirts during the birthday event", "source": "video:a1p2wZhNao0/00014.jpg"}
 ],
 "confidence": 0.55,
 "open": [
  "The vendor that sells item 77451 for 100 coins is not identified: vendor_stock is empty and the store data has no vendor name or zone for category 54. Need the category-54 vendor mapping.",
  "The event link is weak: no article or wiki page names 'Birthday Gift' as an event reward. The video frame only shows it beside event shirts. Confirm whether the coin-store gift is the same as an anniversary gift reward.",
  "Retirement status is unknown. No source says whether the coin sale ended."
 ]}
