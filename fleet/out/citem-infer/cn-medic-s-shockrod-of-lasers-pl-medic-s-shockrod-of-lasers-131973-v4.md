<!-- fleet job=citem-infer id=cn-medic-s-shockrod-of-lasers-pl-medic-s-shockrod-of-lasers-131973-v4 status=done turns=3 usd=0.0031 tokens(read,write,in,out)=[18107, 12255, 8, 2803] model=claude-haiku-5-5 -->
# {n}Medic's Shockrod of Lasers{pl="Medic's Shockrod of Lasers"}

{"item": {"name": "Medic's Shockrod of Lasers", "locale_id": 131973, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Zaan (pixie merchant; wiki Zaan page 'Sells' section lists \"Medic's Shockrod of Lasers\"; Zaan's Medic-job stock)", "where": "Shrouded Glade, near the Cooking Table (wiki Merchants page: 'Zaan found near the Shrouded Glade Cooking Table')", "price": "2152 coins (stores.json reference price, not a captured NPC quote or wiki price); member price 1936 coins (10% member discount); resell 215 coins", "currency": "coins", "source": "wiki page Zaan (https://freerealms.fandom.com/wiki/Zaan, Sells, rev 2021-12-14); repo:prototype/osfr-tools/data/content/vendors.json:32002-32025; repo:prototype/osfr-tools/data/content/stores.json:15105; wiki Merchants page"},
  {"type": "coin_shop", "detail": "Coin Shop, per wiki item page sentence 'acquired from the Coin Shop where it sells for' (price blank in wiki text). Probably the same coin-store sale as the Zaan row; not counted as a separate price", "where": "Coin Shop", "price": null, "currency": null, "source": "wiki page ns0 \"Medic's Shockrod of Lasers\" (lookup text); client coin_store_prices [2152] for item 75089 as reference"},
  {"type": "prize_wheel", "detail": "Prize wheel at Bergram Stumpfinger's Ghost; odds and wheel table not checked", "where": "Bergram Stumpfinger's Ghost", "price": null, "currency": null, "source": "wiki page ns0 \"Medic's Shockrod of Lasers\" ('also acquired from the prize wheel at Bergram Stumpfinger's Ghost'); wiki page ns0 Bergram Stumpfinger's Ghost lists the item"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131973 is \"Medic's Shockrod of Lasers\"; wiki tooltip: level 16 Medic weapon, resell 215", "source": "locale:131973; wiki image:item_tooltip 'Medic's Shockrod of Lasers item.jpg'"},
  {"claim": "Wiki Zaan page lists the item under Sells", "source": "vendors.json:32017-32025 stock_source wiki, page Zaan, section Sells, listed_as \"Medic's Shockrod of Lasers\" (the Zaan page text in lookup shows the name in its list; no price shown there)"},
  {"claim": "Zaan is found near the Shrouded Glade Cooking Table", "source": "wiki page ns0 Merchants"},
  {"claim": "stores.json row for item 75089: category 207, purchase 2152, member 1936, sell 215", "source": "repo:prototype/osfr-tools/data/content/stores.json:15105"},
  {"claim": "Wiki item page: acquired from the Coin Shop (price blank) and from the Bergram Stumpfinger's Ghost prize wheel", "source": "wiki page ns0 \"Medic's Shockrod of Lasers\""},
  {"claim": "Wiki Bergram Stumpfinger's Ghost page lists the item", "source": "wiki page ns0 Bergram Stumpfinger's Ghost"}
 ],
 "confidence": 0.55,
 "open": [
  "All prices (2152 purchase, 1936 member, 215 resell) are stores.json reference values, not captured NPC quotes or wiki prices. The wiki Coin Shop price is blank and the Zaan Sells entry shows no price.",
  "Coin Shop and Zaan may be the same sale; kept as one priced source (Zaan) plus a price-null Coin Shop mention. Confirm in-game.",
  "The wiki item sentence was checked only in the lookup excerpt. The critique's claim of a second prize wheel at Explosive Robgoblins was NOT found in the excerpt I saw, so it is not listed. Re-check the full wiki page before adding it.",
  "Prize-wheel source rests on one wiki sentence; odds and wheel table not checked.",
  "Zaan's exact position inside Shrouded Glade is unknown; zone comes from the Merchants page.",
  "Retirement status unknown; no dated availability source. 'live: unsure' because the only current-tense evidence is wiki wording and stores.json row.",
  "The Job Starter Outfits loadout (job 11, slot 7) is a loadout, not an acquisition source, and was not used as a source."
 ]}
