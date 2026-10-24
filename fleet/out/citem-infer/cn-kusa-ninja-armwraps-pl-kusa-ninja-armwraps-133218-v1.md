<!-- fleet job=citem-infer id=cn-kusa-ninja-armwraps-pl-kusa-ninja-armwraps-133218-v1 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[11208, 10634, 8, 2849] model=claude-haiku-5-5 -->
# {n}Kusa Ninja Armwraps{pl="Kusa Ninja Armwraps"}

{"item": {"name": "Kusa Ninja Armwraps", "locale_id": 133218, "kind": "clothing"},
 "sources": [
  {"type": "prize_wheel", "detail": "Ninja [Prize] Wheel, a prize pool in the minigames Cursed Graveyard!, Hewey's Escape, King of the Ring!, Frostfang Snarlers! and Hot Springs Haven (listed on each wiki page under the Ninja wheel)", "where": "Minigame prize wheels (Cursed Graveyard!, Hewey's Escape, King of the Ring!, Frostfang Snarlers!, Hot Springs Haven)", "price": null, "currency": null, "source": "wiki pages 'Cursed Graveyard!', 'Hewey's Escape', 'King of the Ring!', 'Frostfang Snarlers!', 'Hot Springs Haven'; video:5Su_nfQZyHU/00010.jpg and video:5Su_nfQZyHU/00056.jpg (Cursed Graveyard prize list showing [Kusa] [Ninja] [Armwraps])"},
  {"type": "vendor", "detail": "Coin store sale; the store row does not name the vendor or NPC", "where": "Coin store (stores.json category 102)", "price": "375 coins (member price 337 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76210 (line 15901)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 133218 is 'Kusa Ninja Armwraps', slot 2, class 2, one definition (76210), model ninja_<race>_<gender>_hands_elbowpad.adr", "source": "locale:133218"},
  {"claim": "Store row for item 76210 with purchase price 375 coins, member price 337, sell price 37, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json item 76210"},
  {"claim": "Ninja prize wheel on several minigame pages lists Kusa Ninja Armwraps as a prize", "source": "wiki: Cursed Graveyard!, Hewey's Escape, King of the Ring!, Frostfang Snarlers!, Hot Springs Haven"},
  {"claim": "Video frame of the Cursed Graveyard minigame shows the [Kusa] [Ninja] [Armwraps] prize", "source": "video:5Su_nfQZyHU/00010.jpg, video:5Su_nfQZyHU/00056.jpg"},
  {"claim": "Name sits in a cluster of Genin/Kusa/Nokizaru ninja set items (133213-133223)", "source": "locale:133213 through locale:133223"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin store row (stores.json item 76210, 375 coins) is in the store data, but the vendor/NPC that sells it is not named in the repo or the wiki. Confirm the vendor before treating it as a vendor source.",
  "The wiki pages list 19, 36, 49 and 2 coins next to the prize lists. These look like minigame entry or play costs, not the item's price. Not confirmed; no price is attached to the prize-wheel source.",
  "The wiki gives no drop rate or prize-wheel odds for the Armwraps, and no retirement date. Retired and live status are unconfirmed beyond the store row having no_sale false.",
  "The 'Ninja' wheel job tie-in is inferred from the wiki headings. The Ninja job itself was not checked.",
  "Cited wiki pages were read from search snippets, not full pages."
 ]}
