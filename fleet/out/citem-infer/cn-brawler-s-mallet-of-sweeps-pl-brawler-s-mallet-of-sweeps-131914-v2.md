<!-- fleet job=citem-infer id=cn-brawler-s-mallet-of-sweeps-pl-brawler-s-mallet-of-sweeps-131914-v2 status=done turns=3 usd=0.0038 tokens(read,write,in,out)=[20875, 14989, 8, 3381] model=claude-haiku-5-5 -->
# {n}Brawler's Mallet of Sweeps{pl="Brawler's Mallet of Sweeps"}

{"item": {"name": "Brawler's Mallet of Sweeps", "locale_id": 131914, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop (wiki: 'acquired from the Coin Shop where it sells for' with the price field blank in the prose; page categories include Coin Shop and Coin Shop Weapons)", "where": "Coin Shop", "price": "750 coins (client coin store price for definition 75030; member price 675 coins is a derived 10% member rule, not a captured quote)", "currency": "coins", "source": "wiki page 'Brawler's Mallet of Sweeps' (text and categories, refs quest-lines/item-packs.json line 17239); repo:prototype/osfr-tools/data/content/stores.json line 15046 (item_id 75030, purchase_price_coins 750, member_price_coins 675); client definition coin_store_prices [750]"},
  {"type": "vendor", "detail": "Roosey (NPC 9500000255), pixie merchant who sells Brawler job items", "where": "Cobblestone Village (near the Cooking Table)", "price": "unknown (repo reference 750 coins, member 675; no captured NPC quote; a harness-run note in notes/Reviews/Native Checklist 2026-10-16.md:306 also lists 750/375 but is not a captured quote)", "currency": "coins", "source": "wiki page 'Roosey' Sells list naming Brawler's Mallet of Sweeps (refs quest-lines/npc-packs.json line 21497 and 21551); repo:prototype/osfr-tools/data/content/vendors.json lines 14648-14711 (price_basis: stores.json reference, no captured NPC quote)"},
  {"type": "other", "detail": "Free starter weapon: in inventory for every character created between 2009-12-14 and 2013-03-15 (starter grant, not a purchase; ended for later characters)", "where": null, "price": null, "currency": null, "source": "wiki page 'Brawler's Mallet of Sweeps' (text: 'All characters created between December 14, 2009 and March 15, 2013 began the game with this item in their inventory'); repo:notes/Research/Job Starter Outfits.md line 77"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131914 is \"Brawler's Mallet of Sweeps\"; one definition 75030, slot 7, class 71 (client pack)", "source": "locale:131914"},
  {"claim": "Repo coin store row: purchase 750 coins, 10% member discount to 675 coins, sell price 0 (F228 rule)", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15046"},
  {"claim": "Wiki page says the mallet is 'acquired from the Coin Shop where it sells for' with the number missing; categories list Coin Shop, Coin Shop Weapons and Marketplace Items", "source": "wiki page 'Brawler's Mallet of Sweeps' via refs quest-lines/item-packs.json line 17239"},
  {"claim": "Wiki Roosey Sells list includes Brawler's Mallet of Sweeps", "source": "refs quest-lines/npc-packs.json lines 21497, 21507; repo:prototype/osfr-tools/data/content/vendors.json lines 14648-14711"},
  {"claim": "Starter grant to characters created 2009-12-14 to 2013-03-15", "source": "wiki page 'Brawler's Mallet of Sweeps'"},
  {"claim": "Wiki tooltip shows Resell Value 75, Power 1, Required Brawler, abilities Glancing Blow (254 damage) and Leg Sweep (889 damage)", "source": "wiki image item_tooltip via refs quest-lines/item-packs.json line 17243"}
 ],
 "confidence": 0.5,
 "open": [
  "The wiki Coin Shop sentence has its price blank, so the 750-coin price rests on the repo stores.json row and the client coin_store_prices field, not on wiki prose. Treat as reconstructed until a captured Coin Shop listing is found.",
  "Roosey's price is unverified: vendors.json says price_basis is a stores.json reference with no captured NPC quote. Do not state 750 as a Roosey price as fact. Whether Roosey and the Coin Shop are the same sale or two separate routes is not established.",
  "Resell Value 75 (wiki tooltip) conflicts with the repo sell price of 0 (F228 starter rule). The F228 value is a repo rule, not a live game value. Unresolved.",
  "Class disagreement: client/stores data gives class 71; the pinned Legacy table and piece_014 notes give class 25 (repo:notes/Research/Pieces/014 Forging recipes/content.md). Unresolved.",
  "Retired status unknown: the starter grant closed for characters created after 2013-03-15, and no source gives an end date for the Coin Shop or Roosey sale.",
  "Repo scripts use 75030 as an opening substitute hammer (prepare-opening-content.py, prepare-forging-campaign.py); that is a reconstruction and is not counted as a source.",
  "No drop, quest reward, event or collection source found in the evidence."
 ]}
