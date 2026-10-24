<!-- fleet job=citem-infer id=cgravel-axe-139968-v1 status=done turns=13 usd=0.0102 tokens(read,write,in,out)=[238214, 38901, 28, 5950] model=claude-haiku-5-5 -->
# Gravel Axe

{"item": {"name": "Gravel Axe", "locale_id": 139968, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for definition 48218 (Gravel Axe); store vendor/NPC not identified in our data", "where": null, "price": "811 coins (member price 729 coins; sell-back 81 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48218 (category 207, purchase_price_coins 811); client definition coin_store_prices [811]"},
  {"type": "drop", "detail": "Blue Text weapon: dropped at random by certain boss enemies in dungeons (members only, before retirement). Specific boss for Gravel Axe not found.", "where": "dungeons (unnamed)", "price": null, "currency": null, "source": "wiki Category:Blue Text Weapons; wiki Blue Text weapon (family-level, not item-specific)"},
  {"type": "other", "detail": "Trade only after retirement (Blue Text weapons were retired 14 Dec 2009, names changed to white, membership requirement dropped; 'currently only acquired through trade')", "where": null, "price": null, "currency": null, "source": "wiki Blue Text weapon (family-level; Gravel Axe page not found, Gravel Blade/Gravel Wand pages carry the same wording)"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 139968 'Gravel Axe', item kind weapon (slot 7, class 17, model axe_ar_ag_weapon_battleaxe.adr), definition 48218, single definition", "source": "locale:139968; quest-lines/citem-packs.json cgravel-axe-139968 client_definition"},
  {"claim": "Store data lists definition 48218 at 811 coins purchase, 729 member price, 81 sell price, category 207", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48218"},
  {"claim": "Sibling Gravel Blade (48217) has the same 811-coin store price and wiki says Blue Text weapons were members-only dungeon boss drops, retired 14 Dec 2009, trade-only since", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48217; wiki Category:Blue Text Weapons; wiki Blue Text weapon; quest-lines/citem-packs.json cgravel-blade-139967"},
  {"claim": "Gravel Axe is in the Blue Text weapon table (Gravel family, level 5 power tier, alongside Gravel Wand 12/5 row)", "source": "wiki Blue Text weapon table (freerealms-wiki/harvest/lists/tables.json page 'Blue Text weapon')"},
  {"claim": "Gravel Wand wiki item tooltip shows Resell Value 81, matching store sell price 81", "source": "wiki File:Gravel Wand item.jpg (image:item_tooltip)"},
  {"claim": "Cluster of 11 Gravel/Rocky/Batty weapons share the same family; no article or video names the Gravel Axe specifically", "source": "client_cluster locale:139963-139973"}
 ],
 "confidence": 0.35,
 "open": [
  "Conflict: the store row says 811 coins (a current coin-store price), but the wiki says Blue Text weapons were retired in Dec 2009 and are trade-only. Unclear whether 811 is a live vendor sale or a stale client/store price; needs an in-game check or a vendor source.",
  "Vendor/NPC and zone for the 811-coin sale are not identified in the repo (no vendor record for item 48218 found).",
  "No wiki page for Gravel Axe itself; the family wording is from Blue Text weapon and sibling pages. The specific boss that dropped the Gravel Axe is not named.",
  "Live status is unsure: the first-pass 'live: yes' is a hint only and conflicts with the retirement statement.",
  "No critiques were attached to this pack."
 ]}
