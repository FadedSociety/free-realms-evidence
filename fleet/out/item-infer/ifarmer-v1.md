<!-- fleet job=item-infer id=ifarmer-v1 status=nothing_found turns=2 usd=0.0015 tokens(read,write,in,out)=[3801, 5407, 6, 1486] model=claude-haiku-5-5 -->
# Farmer

{"item": {"name": "Farmer", "locale_id": null, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "The wiki page 'Farmer' describes a job, not an item: 'Farmer is a job that is available since May 2011, unlike other jobs, it is not in the rotation.'", "source": "wiki page Farmer (https://freerealms.fandom.com/wiki/Farmer, rev 45266)"},
  {"claim": "Category:Farming is defined as 'Everything relating to the [farmer] job.'", "source": "wiki Category:Farming"},
  {"claim": "The client text 'Farmer' appears only as a prefix in item names such as Farmer Hat, Farmer Shirt, Farmer Pants, Farmer Boots, Farmer Gloves (locale:436267, 436270, 436256, 436254, 436263); no client string named exactly 'Farmer' exists.", "source": "locale:436254, locale:436256, locale:436263, locale:436267, locale:436270; locale query ^Farmer$ returned no matches"},
  {"claim": "The wiki's 10000 coins value is attached to the job page and is not a price for any item; the wiki Farming vending machine lists separate priced items (e.g. Farmer Hat 16000 coins, Wilds Tractor 250000 coins, which must be bought at a Rank 15 / Rank 20 farm).", "source": "wiki image Farming vending machine.png (Merchant Store); wiki image Farmer Hat/Wilds Tractor text"},
  {"claim": "Farming gives coins and items, including Vaultberry items sold as Station Cash, and farm vendors like Muglap (Seaside) and Farmer's Market trades; these are sources for individual farm items, not for the job itself.", "source": "wiki page Farmer; wiki page Muglap; wiki page Farms"}
 ],
 "confidence": 0.8,
 "open": [
  "The evidence pack is for a job (Farmer), not a purchasable or obtainable item, so no item sources were assigned. Likely the job page was routed here by mistake; the individual items (Farmer Hat, Farmer Shirt, Farmer Pants, Farmer Boots, Farmer Gloves, Wilds Tractor, Seed Bag, etc.) each need their own evidence pack.",
  "The 10000 coin figure in the pack is unexplained for the job page; it was not treated as an item price.",
  "Vaultberry item lists on the Farmer page are unpriced and unsourced to a specific vendor; not assigned here.",
  "Farmer Chug (locale:359) and Farmer Wug/Muglap are NPCs; no item sourcing is established from the pack alone."
 ]}
