<!-- fleet job=citem-infer id=cemergency-medic-backpack-133109-v2 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[12493, 7926, 8, 2137] model=claude-haiku-5-5 -->
# Emergency Medic Backpack

{"item": {"name": "Emergency Medic Backpack", "locale_id": 133109, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Spratt (Medic job-item merchant; wiki Sells list: [Emergency] [Medic] [Backpack])", "where": "Snowhill (per repo NPC row and 2013 build guide; wiki Spratt page does not give a zone in the text checked)", "price": null, "currency": null, "source": "wiki page 'Spratt' (Sells section, https://freerealms.fandom.com/wiki/Spratt); repo:prototype/osfr-tools/data/content/vendors.json:36102-36125 (stock_source wiki Spratt, price_basis not captured NPC quote)"},
  {"type": "coin_shop", "detail": "Coin store reference price for item 76101 (category 106, tint group 1); not a quoted Spratt price", "where": "coin store / stores table", "price": "528 coins (member price 475 coins, 10% member discount; sell price 52 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 76101 (line 15812); repo:data/content/vendors.json:36111 labels this '(R) stores.json reference price; no captured retail NPC quote'"},
  {"type": "prize_wheel", "detail": "[Medic] Prize Wheel (Bristlewood Glade reward list, Medic job)", "where": "Bristlewood Glade", "price": null, "currency": null, "source": "wiki page 'Bristlewood Glade' ([Medic] Prize Wheel list includes [Emergency] [Medic] [Backpack]). Repo bristlewood_glade.json:2285 is an unresolved reward (target_id null) and is not independent proof."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client defines Emergency Medic Backpack, locale 133109, slot 6, class 7, one variant", "source": "locale:133109"},
  {"claim": "Spratt sells exclusively Medic job items, including [Emergency] [Medic] [Backpack]", "source": "wiki page 'Spratt'"},
  {"claim": "[Medic] Prize Wheel on the Bristlewood Glade page lists [Emergency] [Medic] [Backpack]", "source": "wiki page 'Bristlewood Glade'"},
  {"claim": "Coin store row for item 76101: purchase 528 coins, member 475, sell 52", "source": "repo:data/content/stores.json item 76101"},
  {"claim": "Same Medic set (Emergency Medic Shirt/Boots/Gloves/Cap/Fatigues) appears on the Spratt Sells list, so the backpack is part of a set sold together", "source": "wiki page 'Spratt'; locale:133104-133109"},
  {"claim": "The critique's correction is applied: the 528/475 price is kept off the Spratt vendor source and reported as a coin-store reference price", "source": "repo:data/content/vendors.json:36111, 36140"}
 ],
 "confidence": 0.6,
 "open": [
  "No wiki or article source gives a Spratt sale price for the backpack; the 528-coin figure is a stores.json reference price, not a quoted NPC price. Whether Spratt charges it, and at what price, is unverified.",
  "Spratt's zone (Snowhill) comes from the repo NPC row and the 2013 build guide (notes/Build Guides/Content/NPCs/NPCs - Snowhill.md row 110); the wiki text checked does not state the zone.",
  "Bristlewood Glade prize wheel: no drop rate or wheel price from the wiki. Medic prize-wheel listing is a wiki source; the repo JSON line is unresolved.",
  "Retirement status is not confirmed by any source; live is 'unsure' (the first-pass 'yes' is only supported by the store row and the Spratt listing).",
  "Client description is empty; no text evidence beyond the name and the Emergency Medic set cluster."
 ]}
