<!-- fleet job=citem-infer id=cwand-of-spectral-fire-382830-v2 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[14767, 8546, 8, 2282] model=claude-haiku-5-5 -->
# Wand of Spectral Fire

{"item": {"name": "Wand of Spectral Fire", "locale_id": 382830, "kind": "weapon"},
 "sources": [
  {"type": "quest_reward", "detail": "Wizard: Parts and Labor (Osgood, Sanctuary). Player brings the wand parts and an Orb of Spectral Fire to Osgood, who builds the wand. The Orb is bought from Osgood's assistant Lavarius Sparksizzle (a coin purchase; price not in this pack).", "where": "Sanctuary", "price": null, "currency": null, "source": "https://wiki.freerealms.wiki/wiki/Wand_of_Spectral_Fire (\"acquired by completion of the quest Wizard: Parts and Labor\"); locale:103656, locale:103657, locale:103658; locale:116591 and locale:384723 (Orb bought from Lavarius Sparksizzle); locale:116363 (reward text 'wields The Wand of Spectral Fire'); repo:prototype/osfr-tools/data/content/npcs/sanctuary.json:41660 and :41718"},
  {"type": "coin_shop", "detail": "Unnamed coin-store listing for item 48319 (category 207). No vendor or NPC is named in the store data, and the wiki gives quest-only acquisition, so treat as unverified sale channel.", "where": null, "price": "1656 coins purchase; 1490 coins with membership (10% discount); sell-back 165 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13296 (item_id 48319, purchase_price_coins 1656, member_price_coins 1490, sell_price_coins 165, no_sale false); wiki item tooltip 'Resell Value 165'"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Level 20 Wizard weapon acquired by completing Wizard: Parts and Labor; Cannot Trade; Burn 2372 and Firestorm 4732 damage; Category:Quest Weapons", "source": "https://wiki.freerealms.wiki/wiki/Wand_of_Spectral_Fire"},
  {"claim": "Client name locale 382830 is 'Wand of Spectral Fire'; quest reward text locale 116363 and Orb purchase text locale 116591 / 384723 confirmed", "source": "locale:382830, locale:116363, locale:116591, locale:384723"},
  {"claim": "stores.json row for item 48319 exists with 1656 purchase, 10% member discount (1490), 165 sell, no_sale false; no vendor named", "source": "repo:prototype/osfr-tools/data/content/stores.json:13296"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin-store listing (item 48319, 1656 coins) has no named vendor in repo data; the wiki names only the quest. Whether any NPC sells the finished wand is unverified; the store row may be legacy or unlisted.",
  "Retirement not stated by any source; no date for the store listing or quest availability.",
  "Live status conflicts: wiki says quest-only/Cannot Trade, while stores.json row says listed with no_sale false. Left as unsure.",
  "Orb of Spectral Fire (required for the quest) is sold by Lavarius Sparksizzle per locale:116591 and locale:384723; its coin price and vendor stock row were not checked in this pack.",
  "The earlier claim that this is the 'final' wand of the Wizard line is unsupported and dropped."
 ]}
