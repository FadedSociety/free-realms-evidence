<!-- fleet job=item-infer id=imedic-s-shockrod-of-reflexes-v2 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[5391, 12405, 6, 2709] model=claude-haiku-5-5 -->
# Medic's Shockrod of Reflexes

{"item": {"name": "Medic's Shockrod of Reflexes", "locale_id": 131970, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Bishop, Sells list (Energy Transfer Medic set stock, added 27 Aug 2013)", "where": "Briarwood, near the Briarheart warpstone", "price": "2152 coins (reference price from stores.json, not a captured NPC quote); member price 1936 coins; resell 1076 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:8110-8151 (item_id 75086, stock_source wiki page Bishop, section Sells, listed_as this item); repo:prototype/osfr-tools/data/content/npcs/briarwood.json:4634 and notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:210 (Bishop stock list includes Reflexes)"},
  {"type": "coin_shop", "detail": "Coin Shop weapon listing (wiki category and page text; the page's price text is blank, only the coins field gives 2152)", "where": "Coin Shop", "price": "2152 coins", "currency": "coins", "source": "wiki page \"Medic's Shockrod of Reflexes\" (rev 32842): acquired from the Coin Shop; categories Coin Shop, Coin Shop Weapons. The 2152 figure matches the Bishop reference price above, so the Coin Shop listing and the Bishop vendor may be the same price point; unresolved which one is live."},
  {"type": "prize_wheel", "detail": "Prize wheel at Forest Troll Fort (no odds, no price, no date given)", "where": "Forest Troll Fort", "price": null, "currency": null, "source": "wiki page \"Medic's Shockrod of Reflexes\": 'it is also acquired from the prize wheel at Forest Troll Fort'; category Prize Wheel Weapons"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Level 16 Medic weapon, Power 5; Traumatize (2372 damage) and Reflex Test (10674 damage)", "source": "wiki page Medic's Shockrod of Reflexes; image:item_tooltip"},
  {"claim": "Client name string is Medic's Shockrod of Reflexes", "source": "locale:131970"},
  {"claim": "Sold by Bishop (Briarwood) in the Sells list, 2152 coins reference price, member 1936, resell 1076; price basis is stores.json reference, not a captured quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:8110-8151"},
  {"claim": "Bishop's Energy Transfer Medic set stock includes Shockrod of Reflexes, added 27 Aug 2013", "source": "repo:prototype/osfr-tools/data/content/npcs/briarwood.json:4634; notes/Build Guides/Content/NPCs/NPCs - Briarwood.md:210"},
  {"claim": "Wiki categories include Coin Shop, Coin Shop Weapons, Prize Wheel Weapons, Marketplace Items; no Retired category", "source": "wiki page Medic's Shockrod of Reflexes categories"},
  {"claim": "Tooltip resell value 215 is a different number from the 1076 resell in vendors.json and is not a purchase price", "source": "wiki image:item_tooltip Medic's Shockrod of Reflexes"}
 ],
 "confidence": 0.7,
 "open": [
  "Bishop (Briarwood) vendor source rests on the repo vendor data and the Briarwood NPC note, which are repo-compiled, not a captured in-game quote. The critique's claim is verified: vendors.json:8110-8151 exists with these values.",
  "The 2152 price is a reference price (stores.json), not a captured NPC quote. The wiki coin field also says 2152. Treat as unconfirmed against live play.",
  "Member price 1936 coins is a membership discount on the vendor price, not a separate membership pack source.",
  "Forest Troll Fort dungeon loot table (notes/Build Guides/Content/Dungeons/Forest Troll Fort.md:73, Medic row with Battle Item Mystery Pack) lists the item, and dungeons_unresolved.json:9778 has a Reflexes target. Not recorded as a drop source: no resolved wiki or client evidence of the drop mechanism. Note the '214 Coins' figure on that page is unidentified.",
  "The wiki Coin Shop listing and the Bishop Sells listing both carry 2152 coins; whether they are two separate vendors or one listing is unresolved.",
  "No Station Cash Marketplace evidence. 'Marketplace Items' is a wiki category, not an SC Marketplace listing; not recorded as a source.",
  "Prize wheel source has no odds, price, or date; only the wiki sentence supports it.",
  "Live status unknown: no Retired category, but no evidence it is still sold. Bishop's stock note says 'Added 27 Aug 2013' only; no removal date found."
 ]}
