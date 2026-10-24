<!-- fleet job=citem-infer id=cninja-s-necklace-of-vitality-iii-131131-v4 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6511, 11197, 6, 2140] model=claude-haiku-5-5 -->
# Ninja's Necklace of Vitality III

{"item": {"name": "Ninja's Necklace of Vitality III", "locale_id": 131131, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Dizzy Toad (Pixie NPC Merchant, npc 9500000742). Repo-only link: item 75387 is in his item_ids, but the row's stock_completeness is 'partial_evidence_reference' and the wiki Sells list (visible part only: 'Nusumi Ninja Shoulderguard..') does not name this necklace. Not wiki-confirmed.", "where": "Perry's Pastures, south of Snowhill", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 33059-33070 (item 75387 at line 33070; description 'Nusumi Ninja set; ... Power Shard, Necklace, Ring ... Added 27 Aug 2013'); wiki page Dizzy Toad (https://freerealms.fandom.com/wiki/Dizzy_Toad: Perry's Pastures south of Snowhill, introduced August 27, 2013, sells exclusively Ninja Job Items)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131131 is exactly \"Ninja's Necklace of Vitality III\"; it sits in a set with Vitality I-V, Bark Skin III-V and Ring of Energy I-III.", "source": "locale:131131; client cluster locale:131126-131136"},
  {"claim": "Dizzy Toad is a Pixie NPC Merchant at Perry's Pastures, south of Snowhill, introduced August 27, 2013, and sells exclusively Ninja Job Items.", "source": "wiki page Dizzy Toad (https://freerealms.fandom.com/wiki/Dizzy_Toad)"},
  {"claim": "The repo vendor row for Dizzy Toad includes item 75387 in item_ids. The row's description ('Power Shard, Necklace, Ring') is a multi-item category string, so it does not single out this necklace.", "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 33059-33070"},
  {"claim": "The 'Added 27 Aug 2013' date describes the vendor's stock list, not this item's current availability.", "source": "repo:prototype/osfr-tools/data/content/vendors.json line 33063"},
  {"claim": "Reference price 106 coins (member 95, sell 10) exists only as a reconstructed value from Legacy reference Cost with a 10% member discount; no observed quote. The client definition's coin_store_prices [106] is a client field and does not confirm a Coin Shop listing or a Dizzy Toad price.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 17353 (price_provenance kind 'reconstructed'); client definition 75387"}
 ],
 "confidence": 0.35,
 "open": [
  "Dizzy Toad vendor link is repo-only (stock_completeness 'partial_evidence_reference'). No wiki sell list shows this necklace; the visible wiki Sells list is cut off. Needs an observed Dizzy Toad sell list or an in-game check.",
  "No observed price. The 106 coins (member 95) figure is reconstructed from Legacy reference Cost, not a captured quote. Do not use it as the vendor price until observed.",
  "Coin Shop, Station Cash Marketplace, and prize wheel: no source found. The client coin_store_prices field alone does not establish a Coin Shop listing.",
  "Live status is 'unsure'. No source dates this item's current stock or removal. Retired is null.",
  "No wiki page for the necklace; no quest, drop, crafting, or event source found.",
  "Kind is 'other' because the schema has no jewelry category. Slot 8 suggests a worn accessory; 'clothing' is the alternative."
 ]}
