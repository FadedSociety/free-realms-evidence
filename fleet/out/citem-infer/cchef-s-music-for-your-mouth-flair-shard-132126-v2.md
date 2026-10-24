<!-- fleet job=citem-infer id=cchef-s-music-for-your-mouth-flair-shard-132126-v2 status=done turns=4 usd=0.0030 tokens(read,write,in,out)=[19734, 11672, 10, 2617] model=claude-haiku-5-5 -->
# Chef's Music for your Mouth Flair Shard

{"item": {"name": "Chef's Music for your Mouth Flair Shard", "locale_id": 132126, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Rachael (NPC 9500000058 per pack), Sells section; listed alongside the Blended Chef Pants, Hat, Shoes and Shirt", "where": "Blackspore Swamp (repo NPC file repo:prototype/osfr-tools/data/content/npcs/blackspore_swamp.json line 27541; zone not confirmed by wiki or video)", "price": "1504 coins purchase (repo reference price, not a captured NPC or wiki quote); member price 1353 coins (10% discount); sell-back 150 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Rachael (Sells, revision 2013-10-09, lists \"Chef's Music for your Mouth Flair Shard\"); repo:prototype/osfr-tools/data/content/vendors.json lines 6083-6124 (stock_source wiki Rachael; price_basis says reference only); repo:prototype/osfr-tools/data/content/stores.json line 15478 (item_id 75680, category_id 124, purchase 1504, member 1353, sell 150)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name locale 132126 is exact text \"Chef's Music for your Mouth Flair Shard\"; definition 75680, slot 13, class 21", "source": "locale:132126; client definition in pack"},
  {"claim": "Wiki page Rachael ('sells Chef job related items', introduced in game with the 1 Oct 2013 update) lists \"Chef's Music for your Mouth Flair Shard\" in its Sells section", "source": "lookup wiki: page:ns0 Rachael; https://freerealms.fandom.com/wiki/Rachael"},
  {"claim": "vendors.json records item 75680 under Rachael with stock_source wiki Rachael 'Sells' and price_basis 'stores.json reference price; no captured retail NPC quote'", "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 6083-6124"},
  {"claim": "stores.json has a row for item 75680 with purchase 1504, member 1353, sell 150, category_id 124. The critique's claim that this is a shared category-207 default was checked and does not match this row (it is category 124)", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15478"},
  {"claim": "Rachael's NPC record sits in the Blackspore Swamp NPC file, with Legacy reference Npcs.json Id=1526 and a Chef merchant model", "source": "repo:prototype/osfr-tools/data/content/npcs/blackspore_swamp.json lines 27541-27681"}
 ],
 "confidence": 0.6,
 "open": [
  "Price 1504 coins is a repo reference from stores.json (category 124 row), not a captured NPC or wiki quote. Treat it as unverified against the live store. Member price 1353 is the same reference figure with a 10% discount.",
  "Zone Blackspore Swamp comes from the repo NPC file. No wiki page or video frame confirmed Rachael's location.",
  "Wiki evidence is a single Sells listing from a 2013-10-09 revision. It fits both live and retired status, so live stays 'unsure' and retired stays null. No later source was found.",
  "Only the vendor source was found. No quest reward, enemy drop, event, prize wheel or crafting source is evidenced for this item.",
  "Critique fix not fully applied: the critique asked to mark the price as unknown. I kept the coin figure, labelled as a repo reference, because stores.json does carry an item-75680 row. Whether that row is item-specific or a category default remains unresolved."
 ]}
