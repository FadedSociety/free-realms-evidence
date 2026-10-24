<!-- fleet job=citem-infer id=cbodkin-archer-hoodie-132776-v1 status=done turns=4 usd=0.0035 tokens(read,write,in,out)=[24707, 14443, 10, 2870] model=claude-haiku-5-5 -->
# Bodkin Archer Hoodie

{"item": {"name": "Bodkin Archer Hoodie", "locale_id": 132776, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Cissie (NPC id 9500000105), sells the Bodkin Archer set (Quiver, Leggings, Cap, Gloves, Boots, Hoodie) and Archer's Recurve Bows of Stunning/Splintering", "where": "Briarwood (per repo npc file briarwood.json)", "price": "902 coins (member price 811 coins; sell price 90 coins)", "currency": "coins", "source": "wiki page Cissie (https://freerealms.fandom.com/wiki/Cissie, Sells section, rev 2021-12-05): lists [Bodkin] [Archer] [Hoodie]; repo:prototype/osfr-tools/data/content/vendors.json (Cissie block, item_id 75768); price repo:data/content/stores.json item 75768 (purchase_price_coins 902, member_price_coins 811). The 902 figure is the store reference price, not a captured NPC quote."}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item name 'Bodkin Archer Hoodie' is locale:132776, slot 3, class 16, one definition (id 75768).", "source": "client definition (locale:132776)"},
  {"claim": "Cissie sells the Bodkin Archer Hoodie; she sells exclusively Archer job items.", "source": "wiki page Cissie, Sells section (https://freerealms.fandom.com/wiki/Cissie)"},
  {"claim": "Cissie stock list maps item 75768 to Bodkin Archer Hoodie with reference price 902 coins / member 811 coins.", "source": "repo:prototype/osfr-tools/data/content/vendors.json (npc_id 9500000105, Cissie block, item 75768)"},
  {"claim": "Store price 902 coins for item 75768.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 8502"},
  {"claim": "Wiki pages for other zones/enemies list '[Bodkin] [Archer] [Hoodie]' next to Battle Item Mystery Pack and Archer Prize Wheel entries, with coin amounts (68 Coins, 60 Coins, 202 Coins, 209 Coins, 304 Coins).", "source": "wiki pages Moldy Shamblers!, Bandit Hideout!, Treeleaf's Retreat (lookup hits)"}
 ],
 "confidence": 0.7,
 "open": [
  "Retirement status unknown: no source in the pack says whether Cissie still sells the hoodie today. The Cissie wiki revision is from 2021-12-05; the repo sale record is a reference price, not a captured live quote.",
  "The wiki pages Moldy Shamblers!, Bandit Hideout! and Treeleaf's Retreat list the hoodie alongside Battle Item Mystery Pack and Archer Prize Wheel entries. The lookup excerpts do not show how the hoodie relates to those entries (drop, mystery pack contents, or prize wheel). Not counted as a source until the full pages are read.",
  "Cissie's Briarwood location comes from the repo npc file name (briarwood.json), not from a wiki location quote. Not checked against the wiki.",
  "Client definition shows an empty description and a single definition; no tint or race variants were reported beyond the model path archer_<race>_<gender>_chest_oneslvhoodie.adr."
 ]}
