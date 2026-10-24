<!-- fleet job=citem-infer id=chuman-brawler-doll-66662-v1 status=done turns=5 usd=0.0032 tokens(read,write,in,out)=[35164, 11895, 12, 2781] model=claude-haiku-5-5 -->
# Human Brawler Doll

{"item": {"name": "Human Brawler Doll", "locale_id": 66662, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Member of the Brawler Human Doll Collection (the Human Brawler Doll is one of the doll pieces that completes that collection; the in-game tracker shows 'Brawler Human [Doll] (Collected: 8 / 8)')", "where": null, "price": null, "currency": null, "source": "wiki: List of Collections (lists 'Brawler Human Doll' under the Doll collections); locale:132315 'This item can be added to the Brawler Human Doll Collection'; video:5apg6w6ZZeU/00024.jpg"},
  {"type": "other", "detail": "Unknown acquisition method. The pack has no vendor, quest, drop, event or coin-store source for this specific doll, and the client definition has no coin store price (coin_store_prices is empty).", "where": null, "price": null, "currency": null, "source": "client definition (definition_ids 23049, coin_store_prices []); no wiki or article source found"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 66662 is named 'Human Brawler Doll' with the description 'This item can be added to the Human Dolls Collection'", "source": "locale:66662"},
  {"claim": "Client item 7707 'Brawler Human Doll' is a separate string; locale:7783 describes 'Brawler wear for the Human doll', so the Brawler doll set has related clothing items", "source": "locale:7707, locale:7783"},
  {"claim": "A Brawler Human Doll Collection exists in the client UI and in the wiki collection list", "source": "locale:132315; wiki List of Collections"},
  {"claim": "In-game 'My Collections' screen shows 'Brawler Human [Doll] (Collected: 8 / 8)', so the collection is live and has 8 entries", "source": "video:5apg6w6ZZeU/00024.jpg"},
  {"claim": "Its neighbours in the client (66657-66667) are other doll items: Pixie Casual/Rockstar, Human Seaside/Snowhill/Lakeshore/Casual/Rockstar, and Ninja Outfit dolls; they sit in the same collection family", "source": "client_cluster in pack, locale:66657-66667"},
  {"claim": "First-pass tag (live yes, kind collection) agrees with the evidence; it is a hint only", "source": "jev_first_pass"}
 ],
 "confidence": 0.35,
 "open": [
  "No source for how a player obtains the Human Brawler Doll itself (vendor, drop, quest, event, prize wheel, or Station Cash). The wiki List of Collections names the doll but gives no acquisition detail, and no article, video frame or vendor stock names it.",
  "No coin store price in the client definition or repo stores, so no coin or Station Cash price can be stated.",
  "Retirement status is unknown. Live status is supported only by the in-game collection screen.",
  "The wiki page 'Toys (Collections)' lists Brawler doll clothing pieces (Cap, Jacket, Shirt, Pants, Gear, Gloves, Shoes) under '[Brawler] [Doll]'. These are separate outfit pieces, not this doll, and they were not verified against this item.",
  "Next step: check the wiki page for 'Brawler Human Doll Collection' or the Human Dolls Collection page directly (not indexed in this pack), and the Player Studio / event weeklies for doll releases (the 10/22/13 weekly lists Dolly [Doll] at 49 Station Cash, which is a different item)."
 ]}
