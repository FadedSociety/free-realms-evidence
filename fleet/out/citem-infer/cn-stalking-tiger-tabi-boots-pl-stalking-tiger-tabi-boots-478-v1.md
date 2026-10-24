<!-- fleet job=citem-infer id=cn-stalking-tiger-tabi-boots-pl-stalking-tiger-tabi-boots-478-v1 status=nothing_found turns=6 usd=0.0047 tokens(read,write,in,out)=[53925, 19558, 14, 3515] model=claude-haiku-5-5 -->
# {n}Stalking Tiger Tabi Boots{pl="Stalking Tiger Tabi Boots"}

{"item": {"name": "Stalking Tiger Tabi Boots", "locale_id": 478, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 478 '{n}Stalking Tiger Tabi Boots', a ugdt item with 19 definitions sharing the name, slot 5 (feet), class 2, model ninja_<race>_<gender>_feet_wideguard.adr.", "source": "locale:478; client definition pack"},
  {"claim": "Sibling Stalking Tiger pieces exist in the client as named items: Gi (locale 473), Wristguards (483), Cowl (488), Hakama (493), Shoulderguard (498). Stalking Panther Tabi Boots (480) and Panther Gi (475) are the matching Panther set.", "source": "locale:473, 475, 480, 483, 488, 493, 498"},
  {"claim": "No wiki page, article fact, or video frame names Stalking Tiger Tabi Boots. The only wiki Stalking item is Stalking Panther Scythe (Level 12 Ninja weapon, Blacksmith recipe from Silverray at Quagmire Quarry, Blackspore). That is a different item and does not source the boots.", "source": "wiki: Stalking Panther Scythe; notes/Build Guides/Content/Jobs/Blacksmith.md:260"},
  {"claim": "repo:prototype/osfr-tools/data/content/stores.json has a purchase_price_coins of 291 (member price 261) on many item rows (e.g. item_id 109, 112, 113). The pack's 291 is a shared tier price, not a link to this item. No stores.json row for definition ids 168, 1075-1077, 19330-19345 was found, so no coin vendor sale is confirmed.", "source": "repo:prototype/osfr-tools/data/content/stores.json:86-89"},
  {"claim": "The pack's first-pass 'vendor / Potion Vendor' guess has no stock evidence behind it. Locale 479 'Potion Vendor' is an NPC name sitting in the cluster, not a link.", "source": "locale:479 (cluster only)"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found for how Stalking Tiger Tabi Boots is obtained. Vendor, Coin Shop, SC Marketplace, quest, drop, or crafting are all unconfirmed.",
  "Coin price 291 in the pack was not tied to a store row for this item. Find the stores.json item_id for definition 168 (or 1075-1077, 19330-19345) and check whether its category is a coin vendor.",
  "Check repo stores.json and the Potion Vendor's stock list for these definition ids.",
  "The 'Mysterious Merchant'/'Sci-Fi Mystery Chest' text (locale 481-482) is next to the cluster but is not tied to the Stalking Tiger set. Check whether Stalking pieces are Mystery Chest rewards.",
  "Live status is unconfirmed. The first-pass 'live: yes' is a hint only. The 'Potion Vendor' guess is unverified.",
  "Pack critiques: none were supplied."
 ]}
