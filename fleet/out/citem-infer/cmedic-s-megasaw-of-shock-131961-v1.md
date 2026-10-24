<!-- fleet job=citem-infer id=cmedic-s-megasaw-of-shock-131961-v1 status=done turns=6 usd=0.0040 tokens(read,write,in,out)=[49376, 14284, 14, 3451] model=claude-haiku-5-5 -->
# Medic's Megasaw of Shock

{"item": {"name": "Medic's Megasaw of Shock", "locale_id": 131961, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop weapon sale (wiki category 'Coin Shop Weapons'; store-data item 75077, category 207)", "where": "Coin Shop", "price": "1504 coins (store reference price); member price 1353 coins (10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75077 (line 15093); wiki page 'Medic's Megasaw of Shock' (Coin Shop, Category:Coin Shop Weapons)"},
  {"type": "vendor", "detail": "River (NPC, wilds.json), Medic gear 'Pressure Wave Medic set' stock list", "where": "wilds (River's zone per vendor file)", "price": "1504 coins (stores.json reference price, not a captured NPC quote); member 1353 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/River (Sells section, revision 2025-08-04); repo:prototype/osfr-tools/data/content/vendors.json lines 42674-42715"},
  {"type": "prize_wheel", "detail": "Prize wheels at Grexan's Camp and Shady Smugglers", "where": "Grexan's Camp; Shady Smugglers", "price": null, "currency": null, "source": "wiki page 'Medic's Megasaw of Shock' (text: 'acquired from the prize wheels at Grexan's Camp and Shady Smugglers'; Category:Prize Wheel Weapons)"},
  {"type": "marketplace", "detail": "Station Cash Marketplace listing", "where": "SC Marketplace", "price": null, "currency": null, "source": "wiki page 'Medic's Megasaw of Shock' (Category:Marketplace Items) - no price or date given; treat as unverified"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client defines the item as name locale 131961 \"Medic's Megasaw of Shock\", definition 75077, slot 7, class 7, model sword_ar_ag_weapon_megasaw.adr", "source": "locale:131961; client definition in pack"},
  {"claim": "Store data prices item 75077 at 1504 coins purchase, 1353 member, 150 sell", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75077 (line 15093)"},
  {"claim": "Wiki: level 12 Medic weapon, acquired from Coin Shop and from prize wheels at Grexan's Camp and Shady Smugglers; Power 4; Clear! 1357 damage; Shock Paddles 4750 damage", "source": "wiki page 'Medic's Megasaw of Shock'"},
  {"claim": "Wiki River page lists the item in its Sells section (Medic set, same family as Megasaw of Vitals/Vitae/Alarm)", "source": "https://freerealms.fandom.com/wiki/River"},
  {"claim": "Tooltip shows Resell Value 150 (this is the sell-back value, not a purchase price)", "source": "image:item_tooltip 'Medic's Megasaw of Shock item.jpg' (wiki file)"},
  {"claim": "Wiki price sentence is blank ('sells for  and'), so no wiki-stated purchase price exists; the 1504 figure comes only from store data", "source": "wiki page 'Medic's Megasaw of Shock'"}
 ],
 "confidence": 0.7,
 "open": [
  "Wiki page's Coin Shop price is blank; 1504 coins is from repo stores.json and vendors.json reference prices, not a captured in-game quote. Confirm before publishing.",
  "River vendor source rests on the wiki River page only; the vendor file marks prices as reference, not NPC-captured. The River listing's zone is labelled 'wilds' in the repo, but no direct location was confirmed.",
  "Prize wheel and Station Cash Marketplace sources are wiki-category claims with no dates, rates or revision evidence; the marketplace entry has no price.",
  "No quest reward, enemy drop, event or crafting source found. No video or article evidence for this item.",
  "Retired status not found in any source; the item is still defined in the client and in current store data, but I did not verify it is currently sold."
 ]}
