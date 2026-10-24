<!-- fleet job=citem-infer id=cn-trauma-care-medic-gloves-pl-trauma-care-medic-gloves-133112-v1 status=done turns=4 usd=0.0037 tokens(read,write,in,out)=[28693, 14904, 10, 3103] model=claude-haiku-5-5 -->
# {n}Trauma Care Medic Gloves{pl="Trauma Care Medic Gloves"}

{"item": {"name": "Trauma Care Medic Gloves", "locale_id": 133112, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Kimble (human male merchant, sells exclusively Medic job items)", "where": "Stillwater Crossing, near the warpstone", "price": "63 coins (reference price, not a captured NPC quote); member price 56 coins (10% member discount); resale 6 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Kimble (Sells list, revision 2023-11-18, CC BY-SA); repo:data/content/stores.json item 76104 (purchase_price_coins 63, member_price_coins 56, provenance kind 'reconstructed'); repo:prototype/osfr-tools/data/content/vendors.json (item_id 76104, stock_source kind wiki, page Kimble)"},
  {"type": "prize_wheel", "detail": "Medic job prize wheel in dungeon-bonus wheels (one of five items per Medic wheel, alongside Battle Item Mystery Pack, Medic's Bonesaw, Medic's Necklace of Bark Skin III, Medic's Power Shard of Regeneration III)", "where": "Misty Mountain (dungeon prize wheel by job; the Medic table is the wiki-derived list)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Misty Mountain.md:81 (wiki-tagged prize wheel by job table)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name for locale 133112 is '{n}Trauma Care Medic Gloves{pl=\"Trauma Care Medic Gloves\"}'; defined as definition 76104, slot 2, class 7, model military_<race>_<gender>_hands_glove.adr", "source": "locale:133112; client definition in the evidence pack"},
  {"claim": "Kimble's wiki Sells list includes [Trauma] [Care] [Medic] [Gloves] alongside the rest of the Trauma Care Medic set and Medic's power shards, rings, necklaces and bonesaws; Kimble sells exclusively Medic job items", "source": "https://freerealms.fandom.com/wiki/Kimble"},
  {"claim": "Repo store data prices the gloves at 63 coins, member 56 coins, sell 6 coins, but the price provenance says it is a reconstructed reference from the legacy client, with no captured retail NPC quote", "source": "repo:data/content/stores.json item 76104 (line 17420)"},
  {"claim": "The Trauma Care Medic set (Backpack, Fatigues, Cap, Gloves, Boots, Shirt) is stocked by Kimble", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Stillwater Crossing.md:66 and repo:prototype/osfr-tools/data/content/npcs/stillwater_crossing.json vendor_stock"},
  {"claim": "Gloves appear in the Medic prize wheel for Misty Mountain (one of five items), and the dungeon page also lists the Trauma Care set for other dungeons' Medic wheels", "source": "repo:notes/Build Guides/Content/Dungeons/Misty Mountain.md:81"},
  {"claim": "Client cluster: the Trauma Care Medic set and Emergency Medic set (locale 133107-133117) sit together as one job set", "source": "locale:133107 to locale:133117"}
 ],
 "confidence": 0.7,
 "open": [
  "The 63-coin price is a reconstructed reference (legacy client cost and a 10% member discount), not a captured Kimble quote. Verify the live price before the rebuild uses it.",
  "No wiki price was found for the gloves on the Kimble page; the Kimble listing has no prices in the snippet returned.",
  "The Misty Mountain prize-wheel row is a repo note built from wiki-tagged data; the wiki page was not checked directly for this item, and no wheel price or drop rate is known.",
  "Kimble's introduction date (27 August 2013 per the Stillwater Crossing note) is the only date found; no retirement date or later-removal source was found, so retired is null.",
  "Gloves are not in the 'Trauma Care' dungeon-bonus table for Medic on other dungeons' pages as an exact item in every case; the Howling Hills and Forgotten Caves rows list other Trauma Care pieces, so the wheel rotation may differ by dungeon.",
  "No video frames, article facts, or quest rewards found for this item."
 ]}
