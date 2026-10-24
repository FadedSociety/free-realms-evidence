<!-- fleet job=item-infer id=ininja-s-jagged-scythe-of-solar-flare-v3 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[6918, 7744, 6, 2645] model=claude-haiku-5-5 -->
# Ninja's Jagged Scythe of Solar Flare

{"item": {"name": "Ninja's Jagged Scythe of Solar Flare", "locale_id": 131991, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop listing for the Ninja job weapon (wiki categories 'Coin Shop' and 'Coin Shop Weapons'). The wiki Shivering Shark page lists the scythe in his Sells list; he is the Ninja job merchant who sells exclusively Ninja Job Items. Price 1504 is the wiki infobox coins value only; the wiki text price field is blank, and the source of the figure is not stated. Treat as unverified.", "where": "Coin Shop; sold by Shivering Shark", "price": "1504 (unverified; list vs sale price not stated)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Ninja's_Jagged_Scythe_of_Solar_Flare (infobox coins 1504; categories Coin Shop, Coin Shop Weapons); https://freerealms.fandom.com/wiki/Shivering_Shark (Sells list; NPC behind Blackspore Swamp Pet Adoption Center; sells exclusively Ninja Job Items)"},
  {"type": "prize_wheel", "detail": "Ninja Prize Wheel", "where": "Grexan's Camp", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Grexan's_Camp (Ninja Prize Wheel list includes the scythe; a '162 Coins' figure appears beside the list but its spin-cost mapping is unconfirmed); item page 'acquired from the prize wheels at Grexan's Camp and Shady Smugglers'"},
  {"type": "prize_wheel", "detail": "Ninja Prize Wheel", "where": "Shady Smugglers!", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Shady_Smugglers! (Ninja Prize Wheel list includes the scythe; a '16 Coins' figure appears beside the list but its spin-cost mapping is unconfirmed); item page 'acquired from the prize wheels at Grexan's Camp and Shady Smugglers'"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Level 12 Ninja weapon, Power 4; Ashen Strike 1641 damage; Flaming Uppercut 4750 damage", "source": "https://freerealms.fandom.com/wiki/Ninja's_Jagged_Scythe_of_Solar_Flare"},
  {"claim": "Client English name for locale 131991 is \"Ninja's Jagged Scythe of Solar Flare\"", "source": "locale:131991"},
  {"claim": "Item tooltip shows Resell Value 150 (wiki tooltip). The repo sell-back figure of 752 is an unverified reference and is not used.", "source": "wiki image:item_tooltip, File:Ninja's Jagged Scythe of Solar Flare item.jpg"},
  {"claim": "Shivering Shark is a Pixie NPC merchant behind the Blackspore Swamp Pet Adoption Center, introduced August 27, 2013, selling Ninja Job Items; the scythe is in his Sells list", "source": "https://freerealms.fandom.com/wiki/Shivering_Shark"},
  {"claim": "Wiki categories Coin Shop, Coin Shop Weapons, Prize Wheel Weapons, Marketplace Items are present; no SC Marketplace category", "source": "https://freerealms.fandom.com/wiki/Ninja's_Jagged_Scythe_of_Solar_Flare"}
 ],
 "confidence": 0.5,
 "open": [
  "The 1504 coin price has no wiki text price (blank 'sells for'). It matches the repo stores.json reference figure (vendors.json:6408-6449, labelled reference, not a captured NPC quote), so it is not independently confirmed. Confirm in-game.",
  "Sale vs list price for 1504 is not stated anywhere.",
  "Resell value: wiki tooltip 150 is used; the repo 752 figure is dropped as unverified.",
  "Prize wheel spin cost and drop rate are unknown. The 162 Coins (Grexan's Camp) and 16 Coins (Shady Smugglers) figures appear near the wheel lists but are not assigned to the spin.",
  "Repo dungeon notes place the scythe in a Ninja Battle Item Mystery Pack at Grexan's Camp and Shady Smugglers. No drop-rate or enemy evidence exists, so no drop source is listed.",
  "No Station Cash source: no SC Marketplace category or SC price was found. 'Marketplace Items' is a category only.",
  "No retirement or removal date found; the wiki uses present tense. Live status unverified."
 ]}
