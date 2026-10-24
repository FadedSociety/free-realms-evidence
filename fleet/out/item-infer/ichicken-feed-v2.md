<!-- fleet job=item-infer id=ichicken-feed-v2 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[12673, 8517, 8, 1914] model=claude-haiku-5-5 -->
# Chicken Feed

{"item": {"name": "Chicken Feed", "locale_id": 1930, "kind": "consumable"},
 "sources": [{"type": "promotion", "detail": "Redeem the Physical Trading Card Game Virtual Reward loot card 'Chicken Feed' (card ID 1L14) by entering its code; one Chicken Feed is delivered to the redeeming player's communicator. The physical card comes randomly from Series 1 Topps Physical booster packs.", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Chicken_Feed (rev 47547); image 1L14 chicken feed card.png"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Chicken Feed is a consumable usable by any job, obtained by redeeming the TCG Virtual Reward loot card of the same name; one item per code, delivered via communicator; card ID 1L14", "source": "https://freerealms.fandom.com/wiki/Chicken_Feed"},
  {"claim": "The physical loot card comes randomly from Series 1 Topps Physical booster packs", "source": "https://freerealms.fandom.com/wiki/Chicken_Feed"},
  {"claim": "Card image text: 'Creates the illusion that you are a baby chick for 15 minutes.'", "source": "https://freerealms.fandom.com/wiki/Chicken_Feed (image 1L14 chicken feed card.png)"},
  {"claim": "Client item name 'Chicken Feed' is locale:1930", "source": "locale:1930"},
  {"claim": "Client item definition: Comment 'Chicken Feed', Id 2581, Type 1, NameId 1930, DescriptionId 1953, MaxStackSize 20, NoTrade true, SingleUse true, Cost 180", "source": "repo:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:47708-47720 (also Lxzxrus-Free-Realms-Server and Sanctuary copies at the same NameId 1930)"},
  {"claim": "locale:1953 is 'Chicken Feed Brand Soup... It'll make you feel younger!' and is this item's DescriptionId, not a separate item", "source": "locale:1953; repo:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:47712"},
  {"claim": "Wiki categories: Consumable, Trading Card Game, Virtual Rewards", "source": "https://freerealms.fandom.com/wiki/Chicken_Feed"}
 ],
 "confidence": 0.6,
 "open": [
  "Description conflict: the wiki card text says it makes you a baby chick for 15 minutes, but the client DescriptionId 1953 reads 'Brand Soup... feel younger!'. Both are recorded; the builder must pick one. The earlier note that 1953 is a different item was wrong.",
  "Client Cost 180 in the item definition is not a wiki price and no coin, Station Cash, or Coin Shop price is recorded; treat as unknown price. Not a sale or vendor source.",
  "No retirement or end date for the TCG code is recorded; whether the code is still redeemable is unknown, so live is unsure.",
  "locale:150015 ('This is Chicken Feed.') was mentioned earlier but was not confirmed in this pass; not used.",
  "The redemption mechanism (code entry giving one item) rests on wiki text only; no repo code table was found for card 1L14. Wireable is false: there is no quest, enemy, event, or price to wire, only a code redemption."
 ]}
