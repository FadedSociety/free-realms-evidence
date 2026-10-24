<!-- fleet job=citem-infer id=cbutterfly-bow-139910-v3 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[6447, 15362, 6, 1985] model=claude-haiku-5-5 -->
# Butterfly Bow

{"item": {"name": "Butterfly Bow", "locale_id": 139910, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store listing, stores.json category 207 (the same category holds about 90 other weapons, so it is a listing group, not a named NPC; vendor/NPC not identified in the repo). Disputed: the wiki says the bow can only be acquired through trade.", "where": "coin store (stores.json category 207); zone unknown", "price": "640 coins (member price 576 coins, 10% member discount; sell-back 64 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48160 (line 13210)"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client item name 'Butterfly Bow' is locale 139910, item definition 48160, Archer weapon slot 7, class 18, one variant", "source": "locale:139910; client definition in pack"},
  {"claim": "Level 1 Archer Blue Text weapon with Barrage (2609 dmg) and Volley (4732 dmg); wiki Category:Retired Weapons", "source": "https://freerealms.fandom.com/wiki/Butterfly_Bow"},
  {"claim": "Wiki says the bow 'can only be acquired through trade' (player-to-player); no NPC sale is stated on the page", "source": "https://freerealms.fandom.com/wiki/Butterfly_Bow"},
  {"claim": "Store row for item 48160: category 207, purchase 640, member 576, sell 64, no_sale false; neighbouring rows 48161-48171 share the same 640 price", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13185-13230"},
  {"claim": "Blue Text weapon page lists '[Butterfly] [Bow]' with the other Butterfly items (Log Hammer, Scalpel, Blade, Club, Wand)", "source": "wiki Blue_Text_weapon (lookup snippet); locale:139911-139915"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict: the 640-coin store row and the wiki's 'can only be acquired through trade' disagree. The vendor source is kept only because the store row exists; the NPC, zone and whether the row is live are unconfirmed.",
  "Category 207 is a generic weapon-listing group with no named vendor in the repo, so the vendor type rests on the price row alone.",
  "Retirement date and last sale date are not in the sources; 'retired' rests on the wiki Retired Weapons category.",
  "The critique's claim that Blue Text weapons were members-only dungeon drops could not be confirmed, so no drop source is listed.",
  "The sibling-bow trade-only claims (Soapy Bow, Toxic Sting, Winged Bow) were not checked and are not relied on.",
  "Player trade is a wiki statement only, not a wireable source.",
  "No quest reward, crafting, collection, event, membership, promotion or prize wheel source found.",
  "Wiki file images (File:Butterfly Bow item.jpg, File:Butterfly Bow held.jpg) were not reviewed."
 ]}
