<!-- fleet job=item-infer id=ibrawler-s-hammer-of-pummeling-v2 status=done turns=3 usd=0.0039 tokens(read,write,in,out)=[18777, 14159, 8, 3861] model=claude-haiku-5-5 -->
# Brawler's Hammer of Pummeling

{"item": {"name": "Brawler's Hammer of Pummeling", "locale_id": 131918, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Lingan (Brawler job merchant), Sells section; stock row lists Brawler's Hammer of Pummeling", "where": "Seaside, near the Seaside warpstone (per repo NPC notes)", "price": "850 coins (reference price from stores.json, not a captured NPC quote; member price 765, sell price 425)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:26697-26738 (item_id 75034, stock_source wiki page Lingan, section Sells, revision 2025-08-04, https://freerealms.fandom.com/wiki/Lingan); repo:prototype/osfr-tools/data/content/stores.json:15045; repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:125"},
  {"type": "coin_shop", "detail": "Coin Shop (wiki category label only; the page body leaves the price blank, and no separate Coin Shop listing was found in the repo)", "where": "Coin Shop", "price": "850 (wiki infobox coins field; same value as the Lingan reference price)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Pummeling (Category:Coin Shop Weapons, Category:Coin Shop; infobox coins 850)"},
  {"type": "prize_wheel", "detail": "Prize wheel (Brawler), Arachnia's Lair", "where": "Arachnia's Lair", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Pummeling (page text, Category:Prize Wheel Weapons); repo:prototype/osfr-tools/data/content/dungeons/arachnia_s_lair.json:2202; repo:notes/Build Guides/Content/Dungeons/Arachnia's Lair.md:68"},
  {"type": "prize_wheel", "detail": "Prize wheel (Brawler), Highroad Hijinx", "where": "Highroad Hijinx", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Pummeling (page text); repo:prototype/osfr-tools/data/content/dungeons/highroad_hijinx.json:2224; repo:notes/Build Guides/Content/Dungeons/Highroad Hijinx.md:69"},
  {"type": "prize_wheel", "detail": "Prize wheel (Brawler), Petty Yetis!", "where": "Petty Yetis!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Pummeling (page text); repo:prototype/osfr-tools/data/content/dungeons/petty_yetis.json:2148; repo:notes/Build Guides/Content/Dungeons/Petty Yetis.md:66"},
  {"type": "prize_wheel", "detail": "Prize wheel (Brawler), Robgoblin Adept Trouble!", "where": "Robgoblin Adept Trouble!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Pummeling (page text, Category:Prize Wheel Weapons); no repo dungeon file confirmed for this zone"},
  {"type": "prize_wheel", "detail": "Prize wheel (Brawler), Robgoblin Creek", "where": "Robgoblin Creek", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Pummeling (page text); repo:prototype/osfr-tools/data/content/dungeons/robgoblin_creek.json:1996; repo:notes/Build Guides/Content/Dungeons/Robgoblin Creek.md:63"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Level 4 Brawler weapon, Power 2; Pound deals 488 damage, Pummel deals 659 damage; categories include Coin Shop Weapons and Prize Wheel Weapons", "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Pummeling"},
  {"claim": "Client name string is locale:131918 'Brawler's Hammer of Pummeling'", "source": "locale:131918"},
  {"claim": "Lingan's Sells stock lists Brawler's Hammer of Pummeling (item_id 75034, name_id 131918), wiki revision 2025-08-04", "source": "repo:prototype/osfr-tools/data/content/vendors.json:26697-26738; https://freerealms.fandom.com/wiki/Lingan"},
  {"claim": "Lingan is a Brawler job merchant near the Seaside warpstone, stock includes hammers", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:125"},
  {"claim": "Price 850 coins, member 765, sell 425 come from stores.json reference prices, explicitly not a captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:26702-26706, 26735; repo:prototype/osfr-tools/data/content/stores.json:15045"},
  {"claim": "Item tooltip shows Resell Value 85, which conflicts with stores.json sell_price_coins 425; unresolved", "source": "https://freerealms.fandom.com/wiki/Brawler's_Hammer_of_Pummeling (image:item_tooltip); repo:stores.json:15045"}
 ],
 "confidence": 0.6,
 "open": [
  "Price conflict: wiki tooltip Resell Value 85 vs stores.json sell_price_coins 425 (and the 850 purchase value is a reference, not a captured NPC quote). Unresolved.",
  "Coin Shop row is wiki-category-based; the 850 value matches the Lingan reference price, so it may be the same vendor. No separate Coin Shop listing was found in the repo. Treat as unverified.",
  "Robgoblin Adept Trouble! prize wheel is wiki-only; no repo dungeon file was confirmed for it.",
  "repo dungeons/feisty_floren.json (line 2253) also contains a Brawler's Hammer of Pummeling reward entry, but the wiki page does not list Feisty Floren, so it is not included as a source. Verify before adding.",
  "No Station Cash marketplace source: the wiki has 'Marketplace Items' but no SC Marketplace category or station_cash price.",
  "Retirement status not evidenced in the pack; retired left null. Prize wheel odds and per-spin prices are unknown.",
  "Critique 'world' asked for Lingan vendor row to be added: done above. Critique 'evidence' asked for Lingan where field and the price-basis note: done."
 ]}
