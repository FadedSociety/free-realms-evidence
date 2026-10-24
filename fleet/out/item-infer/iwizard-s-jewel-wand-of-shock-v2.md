<!-- fleet job=item-infer id=iwizard-s-jewel-wand-of-shock-v2 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[12971, 8446, 8, 2475] model=claude-haiku-5-5 -->
# Wizard's Jewel Wand of Shock

{"item": {"name": "Wizard's Jewel Wand of Shock", "locale_id": 132046, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Melninster (pixie NPC merchant, Wizard job items), Sells section", "where": "South of the Blackspore Swamp warpstone", "price": "1504 coins (member price 1353 coins; sell-back 752 coins). The 1504 figure is a stores.json reference price, not a captured NPC quote.", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:4540-4581 (item_id 75162, name_id 132046, stock_source wiki page 'Melninster' Sells section, rev 2025-03-16); repo:prototype/osfr-tools/data/content/stores.json:15173 (purchase_price_coins 1504); wiki https://freerealms.fandom.com/wiki/Melninster (Sells list and Merchants entry for Melninster south of the Blackspore Swamp Warpstone)"},
  {"type": "coin_shop", "detail": "Coin Shop listing (wiki category 'Coin Shop' / 'Coin Shop Weapons'). Likely the same 1504-coin listing as the Melninster stock row; no separate Coin Shop stock row is evidenced.", "where": "Coin Shop", "price": "1504 coins (wiki coins field only; rendered page text blanks the price)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Wizard's_Jewel_Wand_of_Shock (rev 34737: coins field 1504; categories 'Coin Shop', 'Coin Shop Weapons')"},
  {"type": "prize_wheel", "detail": "Prize wheels at Bandit Hideout! and Croaking Vale (no odds, wheel cost, or dates sourced)", "where": "Bandit Hideout!; Croaking Vale", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Wizard's_Jewel_Wand_of_Shock (page text 'acquired from the prize wheels at Bandit Hideout! and Croaking Vale'; category 'Prize Wheel Weapons')"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name is client text locale 132046 \"Wizard's Jewel Wand of Shock\"", "source": "locale:132046"},
  {"claim": "Melninster stock row lists the wand at 1504 coins purchase, 1353 member price, 752 sell price, sourced to the wiki Melninster Sells section (rev 2025-03-16)", "source": "repo:prototype/osfr-tools/data/content/vendors.json:4540-4581; https://freerealms.fandom.com/wiki/Melninster"},
  {"claim": "Wiki Melninster page: pixie NPC merchant south of the Blackspore Swamp Warpstone selling Wizard job items", "source": "https://freerealms.fandom.com/wiki/Melninster"},
  {"claim": "Wiki page lists wand as level 12 Wizard weapon, sold in Coin Shop (coins field 1504) and prize-wheel reward at Bandit Hideout! and Croaking Vale", "source": "https://freerealms.fandom.com/wiki/Wizard's_Jewel_Wand_of_Shock"},
  {"claim": "Tooltip Resell Value 150 is a resale value, not a purchase price; Power 4, Required Level 12 Wizard, Zap 1492 damage, Lightning Blast 6717 damage", "source": "image:item_tooltip on the wiki page"}
 ],
 "confidence": 0.6,
 "open": [
  "The Melninster Sells entry is confirmed only by the repo vendors.json row, which cites the wiki Sells section. The wiki snippet I could check was truncated before the wand, so the Melninster listing is not verified line-by-line on the wiki.",
  "The 1504 coin price for Melninster is a stores.json reference price (price_basis says no captured retail NPC quote). Verify with a dated NPC capture or screenshot.",
  "The 'Coin Shop' source and the Melninster source may be the same listing at the same 1504 price; not separately evidenced as two stock rows. Merge if confirmed.",
  "Prize-wheel source has no odds, wheel cost, or dates; only location names are sourced.",
  "No retirement or removal category or date was found, so live status is unsure and retired is null.",
  "The Resell Value 150 is not a purchase price and is not used as a source price.",
  "Station Cash: the 'Marketplace Items' category is not converted to a Station Cash source; no SC price is recorded."
 ]}
