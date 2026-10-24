<!-- fleet job=citem-infer id=cn-medic-s-shockrod-of-vitamins-pl-medic-s-shockrod-of-vitami-131968-v1 status=done turns=4 usd=0.0020 tokens(read,write,in,out)=[16217, 6728, 10, 2066] model=claude-haiku-5-5 -->
# {n}Medic's Shockrod of Vitamins{pl="Medic's Shockrod of Vitamins"}

{"item": {"name": "Medic's Shockrod of Vitamins", "locale_id": 131968, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale of the level 16 Medic weapon (item 75084, category 207, tint group 1)", "where": "Coin Shop", "price": "2152 coins (purchase); 1936 coins member price (10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 75084 (line 15100); wiki page 'Medic's Shockrod of Vitamins' (says it is acquired from the Coin Shop, sale price left blank on the wiki)"},
  {"type": "prize_wheel", "detail": "Prize wheel at Trail of Betrayal (Medic prize wheel listing)", "where": "Trail of Betrayal", "price": null, "currency": null, "source": "wiki page 'Medic's Shockrod of Vitamins' (prize wheel at Trail of Betrayal); wiki 'Medic Prize Wheel' listing"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name locale 131968 is Medic's Shockrod of Vitamins; item definition 75084, slot 7, class 20, model club_ar_ag_weapon_shockrod.adr", "source": "locale:131968; client definition"},
  {"claim": "Level 16 Medic weapon, Power 5, 'Wound' effect; resell value 215 coins (matches store sell_price_coins 215)", "source": "wiki File:Medic's Shockrod of Vitamins item.jpg tooltip transcription"},
  {"claim": "Acquired from the Coin Shop and from the prize wheel at Trail of Betrayal", "source": "wiki page Medic's Shockrod of Vitamins"},
  {"claim": "Coin store purchase price 2152, member price 1936, sell price 215", "source": "repo:data/content/stores.json item 75084"},
  {"claim": "Sits in a 10-item Medic shockrod/megasaw set (locales 131963-131973) listed together on the Medic prize wheel and Medic vendor/wiki pages", "source": "client_cluster; wiki page Medic"}
 ],
 "confidence": 0.7,
 "open": [
  "Wiki sale price is blank; the 2152 coin figure is from our store data only and is unverified against a live price. The stray '307 Coins' text on the wiki sits near the Trail of Betrayal entry and is not clearly tied to this item; not used.",
  "Prize wheel entry has no odds or drop rate; the source is the wiki only, no video or article confirmation.",
  "Retired status unknown: no wiki or client text says it was removed from the Coin Shop.",
  "Client definition has an empty description, so no in-game text beyond the tooltip confirms the wound effect detail.",
  "Trail of Betrayal is named as the prize wheel location; the zone's own page was not checked for the wheel's current status."
 ]}
