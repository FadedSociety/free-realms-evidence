<!-- fleet job=citem-infer id=cshiny-air-necklace-96544-v2 status=nothing_found turns=2 usd=0.0015 tokens(read,write,in,out)=[4510, 6533, 6, 1181] model=claude-haiku-5-5 -->
# Shiny Air Necklace

{"item": {"name": "Shiny Air Necklace", "locale_id": 96544, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is 'Shiny Air Necklace' (locale 96544); the client definition is 31138, item class 68, equip slot 8 (raw client values, no slot-name table cited), one definition, no description text, no model files, no coin store price.", "source": "locale:96544"},
  {"claim": "Sibling names in the same block: Shiny Wind Necklace (96545), Shiny Void Necklace (96546), Gleaming Fire Necklace (96547). These show name pattern only; nothing in the pack shows release status.", "source": "locale:96545; locale:96546; locale:96547"},
  {"claim": "Repo search for definition 31138 and locale 96544 found no store, vendor, recipe, quest or drop entry (vendors.json hits are unrelated IDs such as 131138).", "source": "repo:prototype/osfr-tools/data/content (search for 31138|96544)"},
  {"claim": "Lookup of 'Shiny Air Necklace' across client, wiki, articles and video returns only the client locale entry 96544; no wiki page, article fact or video frame names it.", "source": "lookup (client, wiki, articles, video)"}
 ],
 "confidence": 0.1,
 "open": [
  "No acquisition source is evidenced: no coin store price, no vendor stock, no wiki page, no quest, drop, event, crafting, collection, membership, promotion or prize-wheel link.",
  "Release status unknown. The earlier draft's use of locale:150453 (a placeholder 'This is a ... item' stub for Gleaming Fire Necklace) was dropped as evidence because it is flagged placeholder text and not live.",
  "The 'neck-type accessory' gloss for slot 8 was removed; only the raw slot value is cited.",
  "To resolve: check the original server's item, vendor and loot tables for definition 31138 and the 96544-96547 necklace family, and any Shiny/Gleaming necklace release notes. Until then live should stay 'unsure' and the first-pass tag 'live: yes, source: unknown' is unsupported."
 ]}
