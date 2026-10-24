<!-- fleet job=citem-infer id=cclump-of-troll-hair-2184-v1 status=nothing_found turns=4 usd=0.0020 tokens(read,write,in,out)=[17690, 8796, 10, 1537] model=claude-haiku-5-5 -->
# Clump of troll hair

{"item": {"name": "Clump of troll hair", "locale_id": 2184, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Clump of troll hair' (locale:2184); description 'Some hair from a troll that vendors will buy' (locale:2185). The description says it is a vendor-sell junk item, not a vendor sale or coin-store item.", "source": "locale:2184; locale:2185"},
  {"claim": "Client definition has definition_id 894, one variant, no coin store price, no models.", "source": "client definition pack"},
  {"claim": "No wiki page, article fact, or video frame names this item. The lookup for 'troll hair' returned only client text and unrelated wiki news ('Ice [Troll] Scout' costumes).", "source": "lookup 'troll hair'"},
  {"claim": "Repo search for 'clump' / 'troll hair' in JSON content finds no item record or loot table for definition 894. The only '2184' hits are icon_id 2184 in collection_catalogue.json (collection id 200 entry 1478, item_definition_id 23603), which is a different item and not this one.", "source": "prototype/osfr-tools/data/content/collection_catalogue.json:16254"},
  {"claim": "Repo stores have no coin store price for definition 894 (client lists none).", "source": "repo:data/content/stores.json (no matching item)"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found. The first-pass guess of 'drop' from trolls is unsupported: no enemy drop table, quest reward, or wiki page names this item. Trolls in the game (Ice Trolls in Snowhill, Forest Troll Fort) are the likely origin, but this needs a loot table or a player report to confirm.",
  "Vendor sale: the description says vendors will buy it, so it is probably a sell-only junk item, not a store item. The sell price is unknown; no buy-from-vendor source exists.",
  "Retired/live status is unknown. The client still defines it (definition 894), but no evidence shows it is obtainable in any era.",
  "Icon id 2184 shared with collection entry 1478 is a coincidence of icon ids, not evidence of a link."
 ]}
