<!-- fleet job=citem-infer id=cfestival-pavilion-147988-v1 status=done turns=4 usd=0.0022 tokens(read,write,in,out)=[16830, 8295, 10, 2018] model=claude-haiku-5-5 -->
# Festival Pavilion

{"item": {"name": "Festival Pavilion", "locale_id": 147988, "kind": "furniture"},
 "sources": [{"type": "event", "detail": "Festival-themed update content (Festival Pavilion, festival stand, coin shop, festival tent, Kruglamp, malt-soda barrel/mug, Padres); the update's exact acquisition method for the pavilion is not stated in the sources", "where": null, "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=1792; http://www.freerealms.com:80/article/detail.action?articleId=1789"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client item name 'Festival Pavilion' is locale 147988, definition 18159, model hsg_tents_festival_01.adr, description 'Get the party started with this Festival Pavilion.' (locale:148064)", "source": "locale:147988; locale:148064"},
  {"claim": "Official article announces a new Festival Pavilion ('very large') added to the game, in the same update as a festival stand, coin shop, festival tent and other festival items", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1789"},
  {"claim": "Second official article describes the Festival Pavilion tent as very large, with French text", "source": "http://www.freerealms.com/article/detail.action?articleId=1799"},
  {"claim": "Store data lists item 18159 (category 57) with no coin purchase price, no member price, no sell price, and no_sale true, so it is not a coin vendor sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:4505"},
  {"claim": "Wiki Items index lists a '[Festival] [Pavilion]' page, but the page content was not retrievable, so no wiki price or acquisition detail was confirmed", "source": "lookup wiki page index: '[Festival] [Pavilion]'"}],
 "confidence": 0.3,
 "open": ["No coin price: the store row for 18159 has no price and no_sale=true, so no coin vendor sale is evidenced; do not record a coin price.",
  "Acquisition method unknown: the articles mention the pavilion only as a new item in a festival update; they do not say whether it was sold in the Coin Shop, the Station Cash Marketplace, a quest, or a prize. The festival stand and tent are also in the same cluster with no sourced price.",
  "Retirement status unknown: no source states whether it was retired or is still obtainable. The jev first-pass 'live: yes' is a hint only and is not confirmed.",
  "The wiki page '[Festival] [Pavilion]' is listed in the wiki index but its content was not returned; reading that page directly may resolve the source and price.",
  "No vendor stock, quest, drop, or video evidence found for this item."]}
