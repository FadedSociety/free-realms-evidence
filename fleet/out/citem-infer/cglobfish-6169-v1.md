<!-- fleet job=citem-infer id=cglobfish-6169-v1 status=done turns=4 usd=0.0035 tokens(read,write,in,out)=[25594, 14675, 10, 2768] model=claude-haiku-5-5 -->
# Globfish

{"item": {"name": "Globfish", "locale_id": 6169, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale of item 2147 (store category 107), vendor not identified in the store data", "where": null, "price": "10 coins (member price 9 coins, 10% member discount; resell 1 coin)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2147 (line 616)"},
  {"type": "other", "detail": "Caught by fishing at Brambleback's Bayou, catchable at level 1 (wiki lists it as a fish type; Perch Pinpointer lure raises its catch chance by 10%). Size variants Medium/Large/Extra Large Globfish also exist as catches.", "where": "Brambleback's Bayou, Briarwood", "price": null, "currency": null, "source": "wiki page Brambleback's Bayou (Types of Fish: Globfish, catchable at level 1); wiki page Fisherman; locale:409559; locale:412933; locale:407677-407679; repo:notes/Build Guides/Content/Jobs/Fisherman.md:190"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Globfish' is locale 6169, description 'Your very own wieldable fish!' (locale 6172 flavor: 'Show those fish who's the boss.')", "source": "locale:6169; locale:6172"},
  {"claim": "Item is a coin store entry: item 2147, purchase 10 coins, member price 9 coins, sell 1 coin", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2147"},
  {"claim": "In-game tooltip shows 'Weapon', 'Your very own wieldable fish!', 'Resell Value: 1', 'You Own: 1', matching the store sell price of 1 coin", "source": "video:Qg7_4br2H80/00432.jpg"},
  {"claim": "Item appears in a video item list alongside Calico Catfish and Defender Baton; a second frame shows it on screen in-game", "source": "video:D5spNSvquDQ/00078.jpg"},
  {"claim": "Globfish is a catchable fish at Brambleback's Bayou from level 1", "source": "wiki page Brambleback's Bayou; repo:notes/Build Guides/Content/Jobs/Fisherman.md:190"},
  {"claim": "Quest objective 'Reel in an extra large Globfish' and 'Globfish can be found at Brambleback's Bayou' exist, so a fishing quest uses it", "source": "locale:410480; locale:410481"}
 ],
 "confidence": 0.7,
 "open": [
  "The store row (item 2147, category 107) does not name the coin vendor. The vendor_stock list in the pack is empty, so the vendor and town for the 10-coin sale are unconfirmed.",
  "Definition 2866 (second of two definitions sharing the name) is not explained in any source. It may be a tint or a size variant; the pack does not say.",
  "Whether the 10-coin sale is still offered, and the retirement date, are not stated by any source.",
  "The fish catch is an identified source, but whether Globfish is also a quest reward or a drop is not evidenced.",
  "The 'Medium/Large/Extra Large Globfish' catches (locale 407677-407679) are separate items or sizes; they are not covered by this item."
 ]}
