<!-- fleet job=citem-infer id=chydrostatic-medic-jacket-133116-v1 status=done turns=5 usd=0.0045 tokens(read,write,in,out)=[46460, 18486, 12, 3463] model=claude-haiku-5-5 -->
# Hydrostatic Medic Jacket

{"item": {"name": "Hydrostatic Medic Jacket", "locale_id": 133116, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Farnsworth, Medic Job merchant (sells exclusively Medic Job items; introduced 27 August 2013)", "where": "North-east of the Blackspore Warpstone, Blackspore Swamp", "price": "752 coins (purchase price; member price 676 coins, 10% member discount)", "currency": "coins", "source": "wiki page 'Farnsworth' (Sells list includes [Hydrostatic] [Medic] Jacket); repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:92; repo:data/content/stores.json item 76108 (purchase_price_coins 752, member_price_coins 676)"},
  {"type": "prize_wheel", "detail": "Medic prize wheel for the Treeleaf's Retreat dungeon (one of five items plus the 202 Coins slot; the wheel's item list includes Hydrostatic Medic Jacket)", "where": "Treeleaf's Retreat (dungeon, Briarwood)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Treeleaf's Retreat.md:74 (wiki-sourced wheel table)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 'Hydrostatic Medic Jacket' is locale 133116, one of the Hydrostatic Medic set (Boots, Gloves, Helmet, Fatigues, Backpack).", "source": "locale:133116; locale:133117-133121"},
  {"claim": "Store item 76108 is sold for 752 coins (member price 676, sell price 75), category 103.", "source": "repo:data/content/stores.json item 76108 (line 8566)"},
  {"claim": "Farnsworth sells the Hydrostatic Medic Jacket; he sells exclusively Medic Job items.", "source": "wiki page Farnsworth; repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:92"},
  {"claim": "Hydrostatic Medic Jacket appears on the Medic prize wheel for Treeleaf's Retreat.", "source": "repo:notes/Build Guides/Content/Dungeons/Treeleaf's Retreat.md:74"},
  {"claim": "Dungeon bonus-goal clothing rolls pick a random piece from the set for the player's job, and the Hydrostatic set is the Medic bonus set in several dungeons (Croaking Vale, Vale of the Ancients, Treeleaf's Retreat, Grexan's Camp, Bandit Hideout, Frostfang Caverns, Darvon's Descent, Briar Patch, Mugwort's Hollow).", "source": "wiki pages (Dungeon bonus lines, e.g. Treeleaf's Retreat); repo:notes/Build Guides/Content/Dungeons/Treeleaf's Retreat.md:79"}
 ],
 "confidence": 0.8,
 "open": [
  "Retirement status not verified: no wiki or article says whether Farnsworth still sells the Hydrostatic set; the NPC was introduced 27 August 2013 and no end date was found.",
  "The Treeleaf's Retreat wheel and the dungeon bonus-clothing rolls are listed by the wiki without drop rates, so the wheel is recorded as a source but its odds are unknown.",
  "The wiki's Farnsworth page gives no price; the 752 coins figure comes from our store data (stores.json), not a wiki quote, so the wiki-vs-store price comparison is unavailable.",
  "The jacket is not in the Prince of Low Tide, Stealthy Despoilers, Croaking Vale or Vale of the Ancients wheel lists (those list gloves, fatigues, backpack and helmet), so it is not claimed for them.",
  "Wiki 'Farnsworth' says 'Sells' but no separate wiki price for this item was found in the evidence; the store data is the only price source."
 ]}
