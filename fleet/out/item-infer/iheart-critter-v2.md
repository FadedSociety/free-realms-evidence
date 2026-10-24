<!-- fleet job=item-infer id=iheart-critter-v2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5753, 6559, 6, 1647] model=claude-haiku-5-5 -->
# Heart Critter

{"item": {"name": "Heart Critter", "locale_id": 10822, "kind": "pet"},
 "sources": [
  {"type": "event", "detail": "Random prize from the Gifting Basket (housing item) during the 2011 Festival of Hearts. The purchaser clicks the basket once every 24 hours within its 30-day window for a Festival of Hearts themed reward.", "where": "Gifting Basket (housing item), 2011 Festival of Hearts", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Heart_Critter (rev 50239); https://freerealms.fandom.com/wiki/Pet_Pals (Heart Critter row: 'Only available during 2011 Festival of Hearts as a random prize from the Gifting Basket'); https://freerealms.fandom.com/wiki/Gifting_Basket (Rewards section)"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Heart Critter is a pet pal available as a prize from the Gifting Basket, which was available during 2011 Festival of Hearts and can no longer be acquired.", "source": "https://freerealms.fandom.com/wiki/Heart_Critter (rev 50239)"},
  {"claim": "Pet Pals table, Heart Critter row: 'Only available during 2011 Festival of Hearts as a random prize from the Gifting Basket.'", "source": "https://freerealms.fandom.com/wiki/Pet_Pals"},
  {"claim": "Gifting Basket: the player who purchased it can click it every 24 hours within the thirty days for a Festival of Hearts themed reward; the Festival of Hearts page says the Gifting Basket was the only source of some 2011 items.", "source": "https://freerealms.fandom.com/wiki/Gifting_Basket ; https://freerealms.fandom.com/wiki/Festival_of_Hearts"},
  {"claim": "Wiki categories on Heart Critter: Festival of Hearts, Pet Pal, Seasonal. Infobox category: Heart creature.", "source": "https://freerealms.fandom.com/wiki/Heart_Critter"},
  {"claim": "Client name string 10822 is 'Heart Critter'.", "source": "locale:10822"}
 ],
 "confidence": 0.6,
 "open": [
  "No Station Cash Marketplace or Coin Shop link is evidenced for the Gifting Basket or the pet. The earlier 'marketplace' typing was removed: the pack's Gifting Basket record has an empty station_cash field, so the sale channel is unconfirmed.",
  "The Gifting Basket's purchase price and currency are not in the pack, so the price is null.",
  "Random-prize odds for Heart Critter within the basket are not stated.",
  "The 'No longer available' phrase was not used: it does not appear on the Heart Critter row of the Pet Pals table. Retired status rests on the Heart Critter and Gifting Basket pages.",
  "The 'Broken Hearted' image variant has no separate source.",
  "The repo NPC spawn named Heart Critter (npc_spawns_extra.json) is a world NPC, not item evidence. The repo stores.json entry with item_id 10822 is unverified and not used.",
  "The 'Festival of Hearts' event rows from other answers (currency 'reward') are the same Gifting Basket source and are not independent evidence."
 ]}
