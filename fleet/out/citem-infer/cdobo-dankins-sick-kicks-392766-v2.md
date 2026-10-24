<!-- fleet job=citem-infer id=cdobo-dankins-sick-kicks-392766-v2 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[17598, 13125, 8, 2726] model=claude-haiku-5-5 -->
# Dobo Dankins' Sick Kicks

{"item": {"name": "Dobo Dankins' Sick Kicks", "locale_id": 392766, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin vendor. The client definition carries a coin store price (Cost 270, MemberDiscount 10%), which the rules count as a coin vendor sale. No stores.json row matches definition ids 56482-56493, so no vendor is named.", "where": null, "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "refs: Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:1071973-1071992 (Id 56482, NameId 392766, Cost 270, MemberDiscount 10, Slot 5, Class 1, CategoryId 105, Rarity 3); repo search for 56482 in data/content/stores.json found no row"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition Id 56482 (Comment and NameId 392766) is named Dobo Dankins' Sick Kicks, with Cost 270 and MemberDiscount 10, Slot 5 (feet), ModelName freestyle_<race>_<gender>_feet_sneakersthick.adr", "source": "refs: Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json:1071973-1071992; same comment on FreeRealms-Legacy ClientItemDefinitions.json from line 1071973 onward"},
  {"claim": "The name is held by locale 392766 (ucdt/item), with the same text also under locale 369, and in the locale table as 724550010 (ugdt), 1838026739 (ucdt) and 3597049432 (ucdt)", "source": "locale:392766; locale:369; FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat lines 19016, 48483, 95335"},
  {"claim": "Item is shown worn (equipped tooltip) and in a feet/shoes list beside student and starter boots, so it existed in game; this shows it was worn, not how it was acquired", "source": "video:98uNKkDRvQU/00290.jpg; video:DSt1CTHpDWM/00020.jpg"},
  {"claim": "Wiki harvest list has an entry with the name but no price or source", "source": "freerealms-wiki/harvest/lists/items.json:11037"},
  {"claim": "No wiki article, quest, drop, event or promotion names this item; the only price is the client Cost field", "source": "lookup/search of repo and refs; no other answer mentions it"}
 ],
 "confidence": 0.3,
 "open": [
  "The vendor source rests only on the client Cost field (270). No stores.json row matches definition 56482-56493, so the vendor, zone and shop are unknown. If the Cost is not a live store listing, this source should be dropped and the item recorded as price-known with no source.",
  "Only definition 56482 was checked for Cost and MemberDiscount. The pack reports 35 definitions across 12 listed ids; the other variant ids (and the Legacy copies with the same comment) were not checked for different prices or slots.",
  "Name-bearing locale ids are 369, 392766, 724550010, 1838026739 and 3597049432. Which one the shipped store uses is unknown.",
  "Retired status is unknown; no source says whether it left any vendor or became unobtainable.",
  "Live status is unsure: the video frames show it worn in game, but no source dates its last sale.",
  "The pack's first-pass tag 'live: yes, source guess: vendor' is a hint only and was not used as evidence."
 ]}
