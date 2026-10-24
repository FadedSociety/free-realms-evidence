<!-- fleet job=citem-infer id=csmokey-bow-72354-v3 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6558, 9261, 6, 1999] model=claude-haiku-5-5 -->
# Smokey Bow

{"item": {"name": "Smokey Bow", "locale_id": 72354, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Unplaced coin-store data row for item 48116 (Smokey Bow, client definition 48116). No vendor, store page or date is named in any source; row sits in shared category 207 with items 48110-48124, which share the same price points. Not confirmed as a currently offered listing.", "where": null, "price": "2204 coins (member price 1983 coins, 10% member discount; sell price 220 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13172 (re-read: item_id 48116, category_id 207, purchase 2204, member 1983, sell 220, no_sale false); client coin_store_prices [2204] matches"},
  {"type": "other", "detail": "Player-to-player trade only, per wiki note. Not an NPC, shop, quest or drop source; conflicts with the coin row above.", "where": null, "price": null, "currency": null, "source": "wiki ns0 'Smokey Bow' ('can only be acquired through trade')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Wiki: Smokey Bow is a level 16 Archer weapon, Blue Text, Power 5, listed in Category:Retired Weapons (undated)", "source": "wiki ns0 'Smokey Bow'"},
  {"claim": "Wiki: the weapon 'can only be acquired through trade'", "source": "wiki ns0 'Smokey Bow'"},
  {"claim": "Blue Text weapon page lists the Smokey family (Bow, Hammer, Shockrod, Shadowblade, Axe, Wand) alongside Rocky and Soapy sets", "source": "wiki ns0 'Blue Text weapon'"},
  {"claim": "Client name locale 72354 is 'Smokey Bow'; wearable line 72360 reads 'Wearable by a level 5 or higher Archer' with a bonus-damage proc (PH)", "source": "locale:72354; locale:72360"},
  {"claim": "Coin store row for item 48116 at 2204 coins, member 1983, no_sale false", "source": "repo:prototype/osfr-tools/data/content/stores.json:13172"},
  {"claim": "Level conflict: wiki says Required Level 16; client line 72360 says level 5 or higher", "source": "wiki ns0 'Smokey Bow'; locale:72360"},
  {"claim": "Wiki image files File:Smokey Bow item.jpg and File:Smokey Bow held.jpg exist but their transcribed text was not read; no video frames name the item", "source": "wiki ns6 file list"}
 ],
 "confidence": 0.3,
 "open": [
  "Conflict: wiki says trade-only; store row stores.json:13172 gives a 2204-coin price with no_sale false. Unresolved. The coin row is an unvendored data entry, not a confirmed live listing, so no vendor is named.",
  "Retired status is not settled. The wiki's undated Category:Retired Weapons says retired, but store row 48116 is not marked no_sale, and no dated removal source was found. Left null.",
  "Level conflict unresolved: wiki Level 16 vs client line 72360 'level 5 or higher'.",
  "No quest, enemy, event, prize wheel, crafting or collection source was found.",
  "Client definition 23024 has no store row; the name is shared by two definitions. Whether 23024 is a separate tint or a different sourced item was not checked."
 ]}
