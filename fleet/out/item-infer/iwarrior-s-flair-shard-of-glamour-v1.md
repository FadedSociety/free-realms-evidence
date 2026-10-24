<!-- fleet job=item-infer id=iwarrior-s-flair-shard-of-glamour-v1 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[12160, 10644, 8, 2271] model=claude-haiku-5-5 -->
# Warrior's Flair Shard of Glamour

{"item": {"name": "Warrior's Flair Shard of Glamour", "locale_id": 131248, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop purchase (wiki: 'acquired from the Coin Shop'; category Coin Shop)", "where": "Coin Shop", "price": "1504 coins (wiki infobox coin value; the page text's price is blank)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Warrior's_Flair_Shard_of_Glamour (rev 32703)"},
  {"type": "vendor", "detail": "Hannibal, Warrior Job merchant (introduced 1 October 2013)", "where": "Blackspore Swamp, Mire's Edge", "price": "1504 coins (stores.json reference price; member price 1353 coins; sell price 752 coins)", "currency": "coins", "source": "wiki page Hannibal, section Sells (https://freerealms.fandom.com/wiki/Hannibal) as recorded in repo:prototype/osfr-tools/data/content/vendors.json:3378-3419; NPC note repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:87"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item is a level 12 Warrior flair shard that duplicates the particle effect of Star Flow Chopper; sold from the Coin Shop for 1504 coins.", "source": "https://freerealms.fandom.com/wiki/Warrior's_Flair_Shard_of_Glamour"},
  {"claim": "Client English name for locale 131248 is Warrior's Flair Shard of Glamour.", "source": "locale:131248"},
  {"claim": "Hannibal (Warrior Job merchant, Mire's Edge, Blackspore Swamp, introduced 1 Oct 2013) sells Warrior's Flair Shard of Glamour; item_id 75504, purchase 1504 coins.", "source": "https://freerealms.fandom.com/wiki/Hannibal ; repo:prototype/osfr-tools/data/content/vendors.json:3378-3419"},
  {"claim": "Hannibal's stock list in the NPC notes includes the Warrior's Flair Shard of Glamour.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:87"},
  {"claim": "No retirement or unobtainable note was found for this item in the wiki page or the sources checked.", "source": "https://freerealms.fandom.com/wiki/Warrior's_Flair_Shard_of_Glamour"}
 ],
 "confidence": 0.7,
 "open": [
  "The wiki page says Coin Shop, but the repo's vendor data says Hannibal sells it. Both are listed; the Coin Shop vs. Hannibal distinction is unresolved. Possibly the same 1504-coin item is sold in both places.",
  "The member price (1353 coins) and sell price (752 coins) come from repo stores.json reference prices, not from a wiki or in-game quote. Treat them as unverified.",
  "The wiki page carries the 'Marketplace Items' category, but no Station Cash price or SC Marketplace listing was found, so no marketplace source is listed.",
  "The page text's price is blank; the 1504 figure comes from the wiki coin field and the repo, not the visible page text.",
  "Live status is unsure: the sources show when the item was sold, not whether it is still sold today."
 ]}
