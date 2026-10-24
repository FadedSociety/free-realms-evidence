<!-- fleet job=citem-infer id=cgravel-kendama-hammer-139965-v1 status=done turns=5 usd=0.0038 tokens(read,write,in,out)=[39825, 15771, 12, 2953] model=claude-haiku-5-5 -->
# Gravel Kendama Hammer

{"item": {"name": "Gravel Kendama Hammer", "locale_id": 139965, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, item 48215 (category 207), purchase price 811 coins; member price 729 coins (10% member discount); sell-back 81 coins", "where": "Coin store / vendor stock (store data; the specific NPC vendor is not named in the evidence)", "price": "811 coins (member 729 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13264 (item_id 48215)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name is locale 139965 'Gravel Kendama Hammer', one definition (48215), slot 7, class 5, model hammer_ar_ag_weapon_kendama.adr", "source": "locale:139965"},
  {"claim": "Store data lists item 48215 at purchase_price_coins 811, member_price 729, sell 81, source_tags L1, L2, L4, R2, T633, R1", "source": "repo:prototype/osfr-tools/data/content/stores.json:13264"},
  {"claim": "Wiki 'Blue Text weapon' list includes '[Gravel] Kendama Hammer' in the Gravel set alongside Gravel Bow, Scalpel, Blade, Hammer, Wand", "source": "wiki page:ns0 Blue Text weapon"},
  {"claim": "Sibling Gravel weapons (Gravel Wand, Batty Bow) are Blue Text weapons described as 'can only be acquired through trade'; Gravel Wand resell value 81, Batty Bow resell 143", "source": "wiki page:ns0 Gravel Wand; wiki page:ns0 Batty Bow; wiki image:item_tooltip Gravel Wand item.jpg"},
  {"claim": "Gravel Wand is a level 5 Wizard weapon, Batty Bow level 13 Archer; the Gravel Kendama Hammer's level/class is not given in any source", "source": "wiki page:ns0 Gravel Wand; wiki page:ns0 Batty Bow"}
 ],
 "confidence": 0.5,
 "open": [
  "Conflict: the wiki Blue Text weapon family is described as 'can only be acquired through trade' (player trade), but the store data lists a 811-coin coin-store price for item 48215. The store row is the only price evidence; it may be a coin-store listing for an item that was also a trade-only Blue Text weapon. Needs confirmation.",
  "The specific coin vendor/NPC and zone for the 811-coin sale are not named in the repo or wiki; the stores.json row has category 207 but no vendor name.",
  "No wiki page for Gravel Kendama Hammer itself; no level, class, or resell value found. Only the Blue Text list names it.",
  "Retirement status unknown: no source states whether the coin sale ended."
 ]}
