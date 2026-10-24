<!-- fleet job=citem-infer id=cn-pin-hole-archer-boots-pl-pin-hole-archer-boots-132789-v5 status=no_submit turns=2 usd=0.0024 tokens(read,write,in,out)=[6805, 9246, 6, 2445] model=claude-haiku-5-5 -->
# {n}Pin Hole Archer Boots{pl="Pin Hole Archer Boots"}

```json
{"item": {"name": "Pin Hole Archer Boots", "locale_id": 132789, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Elinor (human NPC merchant near the Shrouded Glade Pet Park), who sells exclusively Archer job items; the Sells list includes Pin Hole Archer Boots", "where": "Shrouded Glade Pet Park area", "price": "1276 coins (store reference price, member price 1148; the Elinor NPC quote is not confirmed)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Elinor (ns0 Sells list); repo:prototype/osfr-tools/data/content/stores.json item 75781 (line 15559, purchase_price_coins 1276, category 105)"},
  {"type": "other", "detail": "Random job-matched armor reward in Cray Caves and Briarheart Caverns. The armor is random and matches the receiving player's current job; the Archer set is Bull's-Eye, Pin Hole, Upshot. Boots is not confirmed as a per-piece roll.", "where": "Cray Caves; Briarheart Caverns", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Cray_Caves (ns0 lookup text); https://freerealms.fandom.com/wiki/Briarheart_Caverns (ns0 lookup text)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client defines the item as locale 132789 '{n}Pin Hole Archer Boots', definition 75781, slot 5, class 16", "source": "locale:132789; client definition in pack"},
  {"claim": "Elinor's wiki Sells list includes Pin Hole Archer Boots, and the page says she sells exclusively Archer job items", "source": "https://freerealms.fandom.com/wiki/Elinor (ns0 lookup)"},
  {"claim": "Store data lists item 75781 at 1276 coins purchase, 1148 member price, in category 105", "source": "repo:prototype/osfr-tools/data/content/stores.json:15559"},
  {"claim": "Cray Caves and Briarheart Caverns pages say the armor is random, matches the receiving player's job, and list Archer: Bull's-Eye, Pin Hole, Upshot", "source": "https://freerealms.fandom.com/wiki/Cray_Caves ; https://freerealms.fandom.com/wiki/Briarheart_Caverns (ns0 lookup, verified this run)"},
  {"claim": "The Elinor page has no retirement note in the lookup text", "source": "https://freerealms.fandom.com/wiki/Elinor (ns0 lookup)"}
 ],
 "confidence": 0.6,
 "open": [
  "The 1276 coin figure is a stores.json purchase price, and the link from that store row to the Elinor NPC is not confirmed. The Elinor NPC's own quote is not captured, so treat 1276 coins as the store price, not a verified Elinor quote. The member price is 1148 coins (10% member discount), and the wiki sale price is not captured.",
  "Whether Boots specifically drop from the Cray Caves and Briarheart Caverns job-armor reward, and the chance and difficulty requirement, are not confirmed. The source lists the Archer set, not the Boots piece.",
  "The Bull's-Eye Archer Boots sibling page mentions a prize wheel and bonus-goal drops. No source confirms those for the Pin Hole Boots, so they are left out.",
  "The Job Starter Outfits research note (slot 5 = 75781) is an unsourced lead, and it is left out.",
  "The wiki page carries no date, so live is 'yes' from the current listing only. Retirement is not stated by any source.",
  "Wireable is false until the Elinor price is confirmed on the live NPC or the wiki."
 ]}
```
