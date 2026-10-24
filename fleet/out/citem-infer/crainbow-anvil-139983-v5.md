<!-- fleet job=citem-infer id=crainbow-anvil-139983-v5 status=done turns=4 usd=0.0039 tokens(read,write,in,out)=[40538, 17938, 10, 2437] model=claude-haiku-5-5 -->
# Rainbow Anvil

{"item": {"name": "Rainbow Anvil", "locale_id": 139983, "kind": "weapon"},
 "sources": [
  {"type": "drop", "detail": "Category-level only: Blue Text weapons (incl. the Rainbow list: Bow, Anvil, Bonesaw, Scythe, Hammer, Wand) were 'acquired in dungeons where they were dropped at random by certain \"boss\" enemies'. No specific boss or dungeon is named for the Anvil.", "where": "dungeons (unnamed)", "price": null, "currency": null, "source": "wiki page 'Blue Text weapon' and Category:Blue Text Weapons (general statement; Rainbow Anvil appears in the Rainbow list, level 13)"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client name is locale 139983 'Rainbow Anvil', in an 11-item cluster of Winged, Rainbow and Spectrum weapon names (139978-139988).", "source": "locale:139983"},
  {"claim": "Wiki 'Blue Text weapon' lists '[Rainbow] [Anvil]' in its Rainbow list at level 13.", "source": "wiki page 'Blue Text weapon'"},
  {"claim": "Blue Text weapons were members-only, acquired in dungeons by random drops from certain boss enemies.", "source": "wiki page 'Blue Text weapon'; Category:Blue Text Weapons"},
  {"claim": "On December 14, 2009, Blue Text weapons were retired: names changed to white font, membership requirement dropped, and they are 'currently only acquired through trade'. This is a category-wide statement; no Anvil-specific date is given.", "source": "wiki page 'Blue Text weapon'"},
  {"claim": "Store row for item 48233 (the Anvil's definition id): purchase 1431 coins, member 1287, sell 143, no_sale false. It sits in a block of identical rows 48220-48243 with no vendor, NPC or store named; rows 48216-48219 are 811 and 48245-48246 are 540. Treated as an unattributed block value, not a vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 13269-13292 (item 48233 at line 13282)"},
  {"claim": "No wiki page exists for Rainbow Anvil itself; no vendor, enemy or dungeon names it in any source read.", "source": "lookup of wiki and client for 'Rainbow Anvil' (only the Blue Text list hit and the client locale line)"}
 ],
 "confidence": 0.45,
 "open": [
  "Coin price conflict: the 1431-coin store row (stores.json item 48233) is not used as a sale source. It has no vendor and sits in a block of identical rows, and Blue Text weapons were retired in 2009 and are trade-only per the wiki. Needs a client or vendor check before any coin price is wired.",
  "Drop is category-level only: no boss enemy or dungeon is named for the Anvil. Needs a per-item source before wiring.",
  "Retirement date (Dec 14, 2009) is from the category statement on the Blue Text weapon page, not an Anvil-specific source. Current availability is trade-only per the same page; trade is not a source type here.",
  "wireable: false. No source names both a specific vendor or enemy and a price."
 ]}
