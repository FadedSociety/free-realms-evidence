<!-- fleet job=item-infer id=imedic-s-megasaw-of-triage-v2 status=done turns=4 usd=0.0040 tokens(read,write,in,out)=[34547, 15546, 10, 3330] model=claude-haiku-5-5 -->
# Medic's Megasaw of Triage

{"item": {"name": "Medic's Megasaw of Triage", "locale_id": 131956, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Farnsworth, Medic Job merchant (pixie, NPC 9500000025), 'Sells' list", "where": "Blackspore Swamp, near the Blackspore warpstone", "price": "1504", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:2435-2470 (npc_id 9500000025, item 75072, purchase_price_coins 1504; price_basis is a stores.json reference price, not a captured NPC quote); https://freerealms.fandom.com/wiki/Farnsworth (Sells list includes Medic's Megasaw of Triage; quest-lines/npc-packs.json:2077)"},
  {"type": "coin_shop", "detail": "Coin Shop sale (Level 12 Medic weapon, Power 4)", "where": "Coin Shop", "price": "1504", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Medic's_Megasaw_of_Triage (categories 'Coin Shop' and 'Coin Shop Weapons'; coin field 1504). Same price as the Farnsworth row; may be the same stock listed twice, see open."},
  {"type": "prize_wheel", "detail": "Prize wheel at Bandit Hideout!", "where": "Bandit Hideout! (difficulty 4 dungeon, Greenwood Camp barrier, Wilds)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Medic's_Megasaw_of_Triage (page text and category 'Prize Wheel Weapons')"},
  {"type": "prize_wheel", "detail": "Prize wheel at Croaking Vale", "where": "Croaking Vale (difficulty 4 dungeon, Nettleseed barrier, Briarwood)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Medic's_Megasaw_of_Triage (page text and category 'Prize Wheel Weapons')"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client English name is \"Medic's Megasaw of Triage\", name id 131956.", "source": "locale:131956"},
  {"claim": "Level 12 Medic weapon, Power 4; effects Incision (deals 1492 damage) and Triage.", "source": "https://freerealms.fandom.com/wiki/Medic's_Megasaw_of_Triage (item tooltip image)"},
  {"claim": "Farnsworth, a pixie Medic merchant near the Blackspore warpstone, sells Medic's Megasaw of Triage; the wiki Farnsworth page says he sells exclusively Medic Job items.", "source": "https://freerealms.fandom.com/wiki/Farnsworth (quest-lines/npc-packs.json:2077); repo:prototype/osfr-tools/data/content/vendors.json:2435-2470"},
  {"claim": "Farnsworth's stock price for this item is 1504 coins (member price 1353, sell-to-vendor 752), taken from stores.json as a reference price, not a captured NPC quote.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:2469-2473; repo:prototype/osfr-tools/data/content/stores.json:15083"},
  {"claim": "Wiki says the item is acquired from the Coin Shop and from prize wheels at Bandit Hideout! and Croaking Vale; categories include Coin Shop Weapons and Prize Wheel Weapons.", "source": "https://freerealms.fandom.com/wiki/Medic's_Megasaw_of_Triage"},
  {"claim": "Wiki coin field lists 1504 for the Coin Shop price; the rendered body price is blank.", "source": "https://freerealms.fandom.com/wiki/Medic's_Megasaw_of_Triage (coins field)"},
  {"claim": "Tooltip Resell Value is 150; this is a resale figure, not a purchase price, so it is not used as a source price.", "source": "https://freerealms.fandom.com/wiki/Medic's_Megasaw_of_Triage (item tooltip image)"},
  {"claim": "Bandit Hideout! and Croaking Vale both list Medic's Megasaw of Triage in their repo dungeon data (Medic table), which is consistent with the wiki wheel claim but does not prove the wheel source.", "source": "notes/Build Guides/Content/Dungeons/Bandit Hideout.md:71; notes/Build Guides/Content/Dungeons/Croaking Vale.md:71"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin Shop and Farnsworth both show 1504 coins. Not verified whether these are two separate vendors or one stock listing; the repo's 1504 is a stores.json reference price with no captured NPC quote. Treat as one price until a live check.",
  "The raw wikitext claim 'sells for {{Coin|1504}}' from an earlier critique could not be found in the refs search, so the 1504 Coin Shop figure rests on the wiki coin field only.",
  "Prize wheel entries have no drop rate or wheel price anywhere in the pack or repo.",
  "Dungeon tables in the repo list the item for Bandit Hideout! and Croaking Vale; not checked whether those are wheel results or enemy drops, so the prize wheel source relies on the wiki category.",
  "No Station Cash price or SC Marketplace category found; 'Marketplace Items' category alone is not a marketplace source, so no marketplace row.",
  "No retirement evidence found. Farnsworth wiki page has a 2025-06-08 revision and no retirement note; current availability in the live game is unverified.",
  "Wiki Triage text 'Heals 1357 damage' is a wiki wording issue and was not used as data."
 ]}
