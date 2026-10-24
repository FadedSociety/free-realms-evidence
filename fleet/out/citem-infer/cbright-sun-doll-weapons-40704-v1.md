<!-- fleet job=citem-infer id=cbright-sun-doll-weapons-40704-v1 status=done turns=7 usd=0.0043 tokens(read,write,in,out)=[67248, 14985, 16, 3468] model=claude-haiku-5-5 -->
# Bright Sun Doll Weapons

{"item": {"name": "Bright Sun Doll Weapons", "locale_id": 40704, "kind": "collection"},
 "sources": [{"type": "drop", "detail": "Robgoblin enemies (spawn type recorded for the whole Bright Yellow Sun Ninja Doll collection; no per-item drop row)", "where": "Northern Wilds", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json:6515-6600 (key wiki:4:106, entries include 'Bright Sun Doll Weapons'; spawn_type Robgoblin, area Northern Wilds); wiki page 'Toys (Collections)' https://freerealms.fandom.com/wiki/Toys_(Collections) revision 31048 (2013-08-21)"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Bright Sun Doll Weapons' as locale 40704, description 'This item can be added to the Bright Yellow Sun Ninja Doll Collection' (locale:132321 is the collection-membership line), definition id 3488, no coin store price.", "source": "locale:40704; locale:132321; client definition pack (definition_ids [3488])"},
  {"claim": "The item is one of eight parts of the 'Bright Yellow Sun Ninja Doll' collection (Mask, Chest, Pauldrons, Arms, Legs, Pants, Weapons, Potions), listed on the wiki 'Toys (Collections)' page.", "source": "wiki page Toys (Collections); repo:prototype/osfr-tools/data/content/collections.json:6515-6573 (entry_count 8)"},
  {"claim": "Collection record gives quality Common, spawn_type Robgoblin, area Northern Wilds; this is the only source-type data in the record and is not stated per item.", "source": "repo:prototype/osfr-tools/data/content/collections.json:6576-6577"},
  {"claim": "Catalogue row links name_id 40704 to item definition 3488 (legacy-unique-name).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:4186-4192"},
  {"claim": "Wiki gives a collection reward of 21 coins with the reward line 'Blue Ninja Outfit Doll'; this is the collection-completion reward, not a price for this item.", "source": "repo:prototype/osfr-tools/data/content/collections.json:6578-6587"}
 ],
 "confidence": 0.4,
 "open": [
  "No wiki article for this item; the only wiki material is the 'Toys (Collections)' list page (rev 2013-08-21). It does not give a per-piece source or price.",
  "Robgoblin/Northern Wilds is a collection-level spawn record. Confirm the piece actually drops from Robgoblin enemies before relying on it. The area name 'Northern Wilds' also needs checking against zone data.",
  "The 21-coin figure belongs to the collection reward ('Blue Ninja Outfit Doll'), not to the weapon piece. No coin store price exists for item 3488 in stores.json.",
  "Retirement and later availability are unknown. Live status is 'unsure' because the first-pass 'live: yes' is only a hint and no source shows the piece still obtainable.",
  "Jev's first-pass 'source_guess: collection' describes how the piece is used (collection membership), not how it is obtained. It is not a source."
 ]}
