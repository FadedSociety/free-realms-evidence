<!-- fleet job=citem-infer id=ccurved-wooden-walkway-29556-v1 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3558, 6585, 6, 1757] model=claude-haiku-5-5 -->
# Curved Wooden Walkway

{"item": {"name": "Curved Wooden Walkway", "locale_id": 29556, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale (housing build item, store category 56); the vendor NPC is not identified in the store data", "where": null, "price": "50 coins (member price 45 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 15507 (line 3966: purchase_price_coins 50, member_price_coins 45, no_sale true)"},
  {"type": "membership", "detail": "June membership package (included one curved wooden walkway, alongside a soccer pet, 10,000 coins, three wooden walkways and one wooden walkway ramp)", "where": null, "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=1570"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Store record exists for item 15507 at 50 coins, member price 45 coins, marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:3966"},
  {"claim": "The June membership package included one curved wooden walkway", "source": "http://www.freerealms.com/article/detail.action?articleId=1570"},
  {"claim": "Client name and description match: 'Curved Wooden Walkway', 'Raised walkways imported from Lakeshore.' (housing build item, not quest text)", "source": "locale:29556; locale:29560"},
  {"claim": "The wiki Items page lists Curved Wooden Walkway under Platforming, and a 'Wood Builders Pack' section appears on the same page", "source": "wiki page: Items (Wood Builders Pack section)"},
  {"claim": "Wiki quest page 'Quest:Rob Robbie Daily' lists one Curved Wooden Walkway as a reward-style entry in a list with other housing items", "source": "wiki page: Quest:Rob Robbie Daily"}
 ],
 "confidence": 0.7,
 "open": [
  "The coin vendor NPC/zone for store category 56 is not named in the pack; the store record gives price but not location.",
  "Possible Wood Builders Pack source appears on the wiki Items page, but the pack's contents and sale channel for this walkway are not confirmed.",
  "The Quest:Rob Robbie Daily wiki entry is a list of housing items; it does not clearly say this walkway is a quest reward, so no quest_reward source is claimed.",
  "The June membership package year is not stated in the article fact, so the date is unknown.",
  "Retirement status is unknown: the store record shows no_sale true, but no wiki or article source states when it was removed."
 ]}
