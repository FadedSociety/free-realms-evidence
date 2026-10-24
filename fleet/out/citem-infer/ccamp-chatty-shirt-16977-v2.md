<!-- fleet job=citem-infer id=ccamp-chatty-shirt-16977-v2 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[16631, 10994, 8, 2024] model=claude-haiku-5-5 -->
# Camp Chatty Shirt

{"item": {"name": "Camp Chatty Shirt", "locale_id": 16977, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale (store data only; the shop and vendor are not named in any source for this item). Item 9050 sits in store category 103 with 9051 and 9092-9098 at the same price.", "where": "Coin Shop (shop name unconfirmed)", "price": "370 coins (member price 333 coins, 10% member discount; sell-back 37 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 9050 (line 6411, category 103, purchase_price_coins 370, member_price_coins 333, sell_price_coins 37)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Camp Chatty Shirt', definition 9050, chest slot 3, class 72", "source": "locale:16977; client definition 9050"},
  {"claim": "Client description 'Make Campmeister Chatty proud by sporting his camp's uniform.'", "source": "locale:16983"},
  {"claim": "Coin store price 370 coins for item 9050, member 333, sell 37", "source": "repo:prototype/osfr-tools/data/content/stores.json item 9050 (line 6411)"},
  {"claim": "The June 4, 2010 Summer Camp update added clothing, Marketplace and Coin Shop items tied to Summer Camp. The article names Camp Chatty and Camp Robbie banners, campfires, tents, totems and playgrounds as sold in the Summer Camp Coin Shop, but does not name this shirt.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1498"},
  {"claim": "Summer Camp Marketplace and Coin Shop items were announced for the 13-week camp season, with no item list in the summary.", "source": "http://www.tentonhammer.com:80/node/85170"},
  {"claim": "The Camp Chatty Shirt appears in 2011-era inventory and tooltip videos next to Camp Robbie Shirt, with Chest slot and Cannot Trade shown.", "source": "video:6mmERh2D8yc/00236.jpg; video:xC7asgOhJKc/00015.jpg; video:zNMmxK6l5jI/00090.jpg"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor not named: stores.json category 103 does not name the shop. The link to the Summer Camp Coin Shop is an inference from the 2010 camp event and the camp-banner article, not evidence for this shirt. The earlier 'camp-clothing set' wording was dropped.",
  "Article 1498 names the Summer Camp Coin Shop for banners, campfires, tents, totems and playgrounds only; clothing is not named there.",
  "Start and end dates of the coin sale are unknown. No source says when item 9050 left the store, so the 2010-only window is not stated.",
  "Quest, drop and prize-wheel sources are unconfirmed. The earlier Bigfoot prize-wheel claim had no cited row and was removed. The Camp Chatty Hat Bigfoot reward is a different item and does not extend to the shirt.",
  "The earlier citation locale:1204384885 does not exist and was replaced with locale:16983 for the description.",
  "Marketplace (SC) availability is not evidenced."
 ]}
