<!-- fleet job=item-infer id=iarcher-s-raptor-bow-of-explosions-v3 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6201, 8584, 6, 2315] model=claude-haiku-5-5 -->
# Archer's Raptor Bow of Explosions

{"item": {"name": "Archer's Raptor Bow of Explosions", "locale_id": 131906, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Will the Red (Briarwood NPC, npc_id 9500000233), 'Sells' section; item_id 75022. Also described on the wiki item page as 'acquired from the Coin Shop'; the two are merged here as one coin sale because the pack shows no separate Coin Shop NPC listing.", "where": "Briarwood", "price": "2152 coins (reference value from stores.json, not a captured NPC quote; member price 1936, sell price 1076 per the same reference). The wiki price sentence is blank.", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Will_the_Red (Sells, rev 2025-06-08); repo:prototype/osfr-tools/data/content/vendors.json:13954-13991; wiki page https://freerealms.fandom.com/wiki/Archer's_Raptor_Bow_of_Explosions (rev 32758, Coin Shop category and intro text)"},
  {"type": "prize_wheel", "detail": "Archer Prize Wheel at Haunted Mines. Odds and price unknown. Not wireable by ID yet.", "where": "Haunted Mines", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Archer's_Raptor_Bow_of_Explosions (intro text; category 'Prize Wheel Weapons'); https://freerealms.fandom.com/wiki/Haunted_Mines (Archer Prize Wheel list includes this item); repo:prototype/osfr-tools/data/content/dungeons/haunted_mines.json:2949-2951 (target_id null)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Level 16 Archer weapon, Power 5; Charged Shot 2372 damage, Explosive Shot 8302 damage", "source": "https://freerealms.fandom.com/wiki/Archer's_Raptor_Bow_of_Explosions"},
  {"claim": "Client English name maps to name_id 131906 (locale:131906 exact match)", "source": "locale:131906; repo:prototype/osfr-tools/data/content/vendors.json:13957"},
  {"claim": "Will the Red's wiki Sells section lists this weapon; reference price 2152 coins, member 1936, sell 1076, with basis noted as stores.json reference, no captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:13954-13991; https://freerealms.fandom.com/wiki/Will_the_Red"},
  {"claim": "Wiki item page says it is acquired from the Coin Shop and from the Haunted Mines prize wheel; categories include Coin Shop Weapons and Prize Wheel Weapons", "source": "https://freerealms.fandom.com/wiki/Archer's_Raptor_Bow_of_Explosions"},
  {"claim": "Haunted Mines wiki page lists this weapon in the Archer Prize Wheel", "source": "https://freerealms.fandom.com/wiki/Haunted_Mines"},
  {"claim": "No Station Cash price or SC Marketplace listing in the pack; 'Marketplace Items' category alone does not prove an SC Marketplace sale", "source": "https://freerealms.fandom.com/wiki/Archer's_Raptor_Bow_of_Explosions (categories)"}
 ],
 "confidence": 0.55,
 "open": [
  "The 2152 coin price is a stores.json reference value, not an observed Will the Red quote. Confirm with a live quote.",
  "Coin Shop and Will the Red are merged into one vendor source. If a separate Coin Shop NPC or storefront is confirmed, add it as its own source.",
  "Haunted Mines prize wheel: no odds, no price, and no item definition ID (haunted_mines.json target_id null). Needs an ID before wiring.",
  "No retirement or removal date in the pack; live status unverified.",
  "No quest, enemy drop, crafting, collection, or event source in the pack.",
  "Critiques applied: the duplicate Coin Shop row was merged into the vendor row, and the price is marked as a reference value. The wiki's Coin Shop mention is kept as a note, not a separate source."
 ]}
