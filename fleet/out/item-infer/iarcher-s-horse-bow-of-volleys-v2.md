<!-- fleet job=item-infer id=iarcher-s-horse-bow-of-volleys-v2 status=done turns=3 usd=0.0040 tokens(read,write,in,out)=[21913, 17921, 8, 3112] model=claude-haiku-5-5 -->
# Archer's Horse Bow of Volleys

{"item": {"name": "Archer's Horse Bow of Volleys", "locale_id": 131886, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop, sold to everyone", "where": "Coin Shop", "price": "850 coins (everyone)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys (wiki text 'sells to everyone for the price of {{Coin|850}}'; coins field [850, 765]; category Coin Shop Weapons)"},
  {"type": "coin_shop", "detail": "Coin Shop, Members price (10% discount)", "where": "Coin Shop", "price": "765 coins (Members; 10% discount price, a sale price relative to 850)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys (wiki text 'to Members at the %10 discount price of {{Coin|765}}')"},
  {"type": "prize_wheel", "detail": "Archer prize wheel at Call of the Wildest!", "where": "Call of the Wildest! (wheel); drop chance not stated", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys (wiki text; category Prize Wheel Weapons)"},
  {"type": "prize_wheel", "detail": "Archer prize wheel at Eight-Legged Monstrosities!", "where": "Eight-Legged Monstrosities! (wheel); drop chance not stated", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys (wiki text)"},
  {"type": "prize_wheel", "detail": "Archer prize wheel at Robgoblin Treasure Trove", "where": "Robgoblin Treasure Trove (wheel); drop chance not stated", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys (wiki text); repo:notes/Build Guides/Content/Dungeons/Robgoblin Treasure Trove.md:87"},
  {"type": "prize_wheel", "detail": "Archer prize wheel at The Bat Cave!", "where": "The Bat Cave! (wheel); drop chance not stated", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys (wiki text); repo:notes/Build Guides/Content/Dungeons/The Bat Cave.md:69"},
  {"type": "prize_wheel", "detail": "Archer prize wheel at Thugawug Thug!", "where": "Thugawug Thug! (wheel); drop chance not stated", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys (wiki text)"},
  {"type": "vendor", "detail": "Marian, Pixie Archer merchant (sells exclusively Archer job items)", "where": "Seaside, near the Seaside Information Center", "price": null, "currency": null, "source": "wiki page 'Marian' (refs freerealms-wiki/wikitext/10139-32541-2be767db52ae.wiki, '==Sells==' list line 25: [[Archer's Horse Bow of Volleys]]); no price stated"},
  {"type": "vendor", "detail": "Vere, human Archer merchant (sells exclusively Archer job items)", "where": "Wugachug, near the Wugachug Cooking Table", "price": null, "currency": null, "source": "quest-lines/npcs.json vendor_sells ('Archer's Horse Bow of Explosions and Archer's Horse Bow of Volleys'); repo:notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:78; no price stated"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Level 4 Archer weapon, Power 2; Barrage 488 damage, Volley 885 damage", "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys"},
  {"claim": "Client name string is locale 131886 'Archer's Horse Bow of Volleys'", "source": "locale:131886"},
  {"claim": "Coin Shop price 850 coins for everyone; 765 coins for Members at 10% discount", "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys"},
  {"claim": "Prize wheels at Call of the Wildest!, Eight-Legged Monstrosities!, Robgoblin Treasure Trove, The Bat Cave!, Thugawug Thug!", "source": "https://freerealms.fandom.com/wiki/Archer's_Horse_Bow_of_Volleys"},
  {"claim": "Marian (Seaside) sells the bow; no price listed", "source": "freerealms-wiki/wikitext/10139-32541-2be767db52ae.wiki line 25"},
  {"claim": "Vere (Wugachug) sells the bow; no price listed", "source": "quest-lines/npcs.json vendor_sells; repo:notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:78"},
  {"claim": "Item tooltip shows Resell Value 85", "source": "image:item_tooltip (wiki image transcription)"}
 ],
 "confidence": 0.7,
 "open": [
  "No Station Cash price or 'SC Marketplace' category; the 'Marketplace Items' category is unexplained, so no marketplace source is recorded.",
  "Wiki revision 32536 is old; no retirement date or current-availability evidence. Whether the Coin Shop still stocks it is unverified, so live is 'unsure'.",
  "Prize-wheel drop rates and wheel costs are not stated anywhere in the pack.",
  "Marian's and Vere's sale prices are not recorded in any source; the NPC vendor entries carry price null.",
  "Marian's wiki page is revision 32541 (2013-era), and Vere's entry is from the repo's npcs.json; the NPC sales lists may have changed since."
 ]}
