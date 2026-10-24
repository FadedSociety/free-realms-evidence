<!-- fleet job=citem-infer id=cpoofy-blouse-vest-2510-v1 status=done turns=4 usd=0.0023 tokens(read,write,in,out)=[18415, 8113, 10, 2150] model=claude-haiku-5-5 -->
# Poofy Blouse Vest

{"item": {"name": "Poofy Blouse Vest", "locale_id": 2510, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Coin store sale (stock listing; vendor NPC not named in store data)", "where": "coin store, store category 103", "price": "225 coins (member price 202 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 216 (line 134: purchase_price_coins 225, member_price_coins 202, sell_price_coins 22, tint_group 1)"}],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name is 'Poofy Blouse Vest', locale id 2510, item class 11, slot 3, definition id 216.", "source": "locale:2510"},
  {"claim": "Store data lists definition/item 216 as a coin store item at 225 coins, member price 202, with source tags L1, L2, L4, R2, T633, R1 (the same tag set as many standard coin-store clothing items).", "source": "repo:prototype/osfr-tools/data/content/stores.json item 216"},
  {"claim": "Wiki image render file titled with the item name exists (Bandicam 2014-01-12 screenshot), confirming the item was seen in-game in the 2014 era.", "source": "image:item_render 'Bandicam 2014-01-12 19-17-01-985.jpg'"},
  {"claim": "Wiki Farmer and Adventurer job-outfit pages list 'Poofy Blouse Vest' alongside Freestyle job clothing (Outback Hat, Gold Buckled Knee High Boots, Designer Gloves), indicating it belongs to the Freestyle job clothing set; these pages give no price or vendor.", "source": "wiki page: Farmer; wiki page: Adventurer"},
  {"claim": "Client cluster of neighbouring locale ids 2505-2515 (Treasure Hunter, Postman, Outback Hat, Freestyle Jobs, Designer Gloves) shows the same job-clothing grouping; no separate quest or event tag was found.", "source": "locale:2505-2515"}],
 "confidence": 0.6,
 "open": [
  "The store data gives the 225-coin price but not the vendor NPC or zone; the vendor name and location need confirmation from a coin-store page or client data.",
  "The wiki job pages show the item but do not say whether it was sold as a single item or as part of a job-outfit bundle; the sale is taken from the store row only.",
  "No retirement date was found in the sources, so retired is left null.",
  "The first-pass tag said 'vendor' and its evidence was the store row, not a wiki category; the Farmer/Adventurer pages are not a price source.",
  "The client description is blank, so no further description evidence is available."
 ]}
