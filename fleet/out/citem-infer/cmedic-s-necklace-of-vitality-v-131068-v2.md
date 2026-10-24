<!-- fleet job=citem-infer id=cmedic-s-necklace-of-vitality-v-131068-v2 status=done turns=5 usd=0.0035 tokens(read,write,in,out)=[32604, 13159, 12, 2963] model=claude-haiku-5-5 -->
# Medic's Necklace of Vitality V

{"item": {"name": "Medic's Necklace of Vitality V", "locale_id": 131068, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Zaan (pixie merchant, sells exclusively Medic Job items; wiki Sells list)", "where": "Shrouded Glade (near the Cooking Table)", "price": "2152 coins (reference price; member 1936 coins, 10% member discount)", "currency": "coins", "source": "wiki:Zaan (page lists Medic job gear on its Sells list; the item line was not visible in my snippet, so confirm); repo:data/content/stores.json item 75324 (purchase_price_coins 2152, category 108) and prototype/osfr-tools/data/content/vendors.json line 32086 (stock_source wiki Zaan). The price is a repo reference value, not a captured NPC or wiki price."},
  {"type": "prize_wheel", "detail": "Medic Prize Wheel (spin)", "where": "Mushroom Mania! (wiki page lists the Medic wheel with \"Medic's [Necklace] of Vitality V\")", "price": "77 Coins shown on the page, next to the wheel block; the exact spin cost for this wheel is not confirmed", "currency": "coins", "source": "wiki:Mushroom Mania! (Medic Prize Wheel block, line for Medic's [Necklace] of Vitality V)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131068 is \"Medic's Necklace of Vitality V\"; definition 75324, slot 8, class 7", "source": "locale:131068"},
  {"claim": "Wiki Zaan page: Zaan is a pixie NPC merchant near the Shrouded Glade Cooking Table who sells exclusively Medic Job items", "source": "wiki:Zaan"},
  {"claim": "Medic Prize Wheel block on the wiki Mushroom Mania! page lists \"Medic's [Necklace] of Vitality V\" among its prizes", "source": "wiki:Mushroom Mania!"},
  {"claim": "Sibling wiki pages (Archer's Necklace of Vitality I, Brawler's Necklace of Vitality III) say these necklaces are sold in the Coin Shop at the standard price with a 10% member discount; this is a pattern only, not evidence for the Medic V item", "source": "wiki:Archer's Necklace of Vitality I; wiki:Brawler's Necklace of Vitality III"},
  {"claim": "Store reference price 2152 coins for item 75324", "source": "repo:data/content/stores.json item 75324"}
 ],
 "confidence": 0.55,
 "open": [
  "Vendor source rests on the Zaan wiki page's Sells list; the snippet I read did not show the necklace line itself, so the Zaan entry needs a direct page check.",
  "The 2152 / 1936 coin prices come from the repo's reconstructed stores.json reference (vendors.json marks it '(R)', no captured NPC quote). They are not wiki prices. The wiki page gives no prices for Zaan.",
  "The Medic Prize Wheel at Mushroom Mania! is a second source, but the 77 Coins figure on that page is not confirmed as this wheel's spin cost. The wheel's prize-to-spin mapping is also unverified.",
  "The 2021-12-14 revision date from the earlier answer could not be checked and was dropped.",
  "Live status and retirement are unknown. The wiki listings may be from an older snapshot, and no source states the item was retired or still sold.",
  "The client description is empty and there is no dedicated wiki article for this item."
 ]},
 "submit_note": null}
