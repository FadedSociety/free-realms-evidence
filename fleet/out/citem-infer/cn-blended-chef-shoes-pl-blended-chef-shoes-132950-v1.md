<!-- fleet job=citem-infer id=cn-blended-chef-shoes-pl-blended-chef-shoes-132950-v1 status=done turns=8 usd=0.0062 tokens(read,write,in,out)=[106189, 27633, 18, 3462] model=claude-haiku-5-5 -->
# {n}Blended Chef Shoes{pl="Blended Chef Shoes"}

{"item": {"name": "Blended Chef Shoes", "locale_id": 132950, "kind": "clothing"},
 "sources": [{"type": "vendor", "detail": "Rachael (NPC 9500000058, Chef job merchant; wiki 'Sells' section lists Blended Chef Pants, Hat, Shoes, Shirt)", "where": "Blackspore Swamp, Blackspore Cooking Table", "price": "902 coins (member price 811 coins; sell-back 90 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 75942 (purchase_price_coins 902, member_price_coins 811); repo:prototype/osfr-tools/data/content/vendors.json:6167-6182 (item_id 75942 under Rachael npc_id 9500000058); wiki page Rachael (https://freerealms.fandom.com/wiki/Rachael, Sells section, rev 2013-10-09)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Blended Chef Shoes' is locale:132950, one definition (definition_id 75942), slot 5, class 21, model freestyle_<race>_<gender>_feet_dressshoes.adr", "source": "locale:132950; client definition pack"},
  {"claim": "Item 75942 is stocked by Rachael and priced at 902 coins (member 811, sell 90) in the store reference data", "source": "repo:data/content/stores.json item 75942; repo:prototype/osfr-tools/data/content/vendors.json:6167-6182"},
  {"claim": "Wiki page Rachael lists Blended Chef Pants, Hat, Shoes and Shirt under 'Sells'; she was introduced in the 1 October 2013 update and sells Chef job items", "source": "lookup wiki page Rachael; freerealms-wiki wikitext list of Blended Chef pages"},
  {"claim": "Rachael is at the Blackspore Cooking Table in Blackspore Swamp (legacy placement, NPC id 9500000058, NameId 5102508)", "source": "quest-lines/npcs.json (Rachael record); repo:prototype/osfr-tools/data/content/npcs/blackspore_swamp.json:27538"},
  {"claim": "Blended Chef set sits with Deep Fried and Simmering Chef clothing in client text (locale 132945-132955), consistent with one Chef-job clothing set", "source": "locale:132945-132955"},
  {"claim": "Chef rank 15+ could buy Rachael's recipes per Game Update 120 (11/19/2013)", "source": "wiki Template:News (cited in quest-lines/npcs.json Rachael record)"}
 ],
 "confidence": 0.6,
 "open": [
  "Live status unsure: the only sale evidence is the 2013 wiki Sells list and the reference store price; no video, article, or client-tagged dialog confirms Rachael or this item still sold after 2013. No retirement source found either.",
  "The 902-coin price comes from repo stores.json reference data ('no captured retail NPC quote'), not a wiki or in-game price quote. No wiki price for the shoes was found, so treat 902 as unverified.",
  "Pack said vendor_stock was empty; the stock list is from the wiki Rachael page via repo vendors.json, not the pack.",
  "NPC name id conflict: repo notes give 2147809857 for Rachael, client has 5102508; client value used.",
  "No Blended Chef set bonus, promotion, or drop evidence found; no quest reward or enemy drop sources identified.",
  "Pack's client_definition gave a single definition and no description; no wiki page titled 'Blended Chef Shoes' exists in the cache (only list membership)."
 ]}
