<!-- fleet job=citem-infer id=csilent-screen-shorts-404385-v4 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6004, 8448, 6, 2045] model=claude-haiku-5-5 -->
# Silent Screen Shorts

{"item": {"name": "Silent Screen Shorts", "locale_id": 404385, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 404385 is 'Silent Screen Shorts'. Its Elite variants are locale 404390 ('Elite Pink Silent Screen Shorts') and 404391 ('Elite Black Silent Screen Shorts'). All three re-checked this pass via lookup.", "source": "locale:404385; locale:404390; locale:404391"},
  {"claim": "The Soccer Star note lists a 'Silent Screen' clothing set as families 19 (base), 20 (Elite Black) and 21 (Elite Pink), with a Shorts column of ids 2065132298, 2650199705, 2018882118. These note ids are a different key from the client locale ids 404385/404390/404391, and the mapping between them is unverified. The link of this set to Soccer Star is by slot name and set-name inference only (marked as such in the note, Soccer Star.md:193, :199-201), not a confirmed Soccer Star job item.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md:223-225, :193, :199-201, :316"},
  {"claim": "Fred Futbol (ucdt 4036414402) is the 'Soccer Star Gear' vendor at Snowhill Soccer Field (video title). His stock and prices are unknown: the notes and npcs/snowhill.json record no stock list. Not recorded as a source for this item.", "source": "notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:126, :240; repo:prototype/osfr-tools/data/content/npcs/snowhill.json:16192-16210"},
  {"claim": "The 'Soccer Star Gear' collection id 2614216159 appears only in the notes (Soccer Star.md:195). It is not a client locale id (no locale entry exists), so it is not cited as evidence.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md:42, :195"},
  {"claim": "No stores.json row exists for definition ids 61955-61968; nearby rows 61960 and 61961 are 9453-coin category 104 items and are not this item. The client coin prices 528 and 750 cannot be bound to this item and are not recorded as a price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:14528-14529; repo search for Silent Screen found no store row"},
  {"claim": "No wiki page, article, video frame or other answer names Silent Screen Shorts. Repo search for 'Silent Screen|Fred Futbol' returned only the Soccer Star and Snowhill notes and npc data above.", "source": "lookup (client, wiki, articles, video); repo search"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source is confirmed. Fred Futbol, 'Soccer Star Gear' vendor, is the only lead; his stock is unknown and nothing ties these shorts to his stock. Keep as an open lead, not a sourced vendor.",
  "Coin prices 528 and 750 come from the client definition but have no stores.json row by item id for definitions 61955-61968. They are unbound and must not be used as this item's price until a row is found.",
  "The pack lists 34 definitions but only 12 definition ids. The base, Elite Black and Elite Pink tiers and any tints are not all mapped to ids.",
  "Live status and retirement are unknown. No source gives an acquisition date or retirement; the first-pass 'live: yes' is not backed by evidence.",
  "Quest, enemy-drop, event, crafting and collection sources were not checked against this item beyond the Soccer Star notes.",
  "Critique fixes applied: removed the locale:2614216159 citation from evidence and from open (it is not a client locale id); stated that the Soccer Star note id column and the client locale ids are different keys; softened the 'Soccer Star family' claim to a slot-name and set-name inference per Soccer Star.md:193, :199-201; sources left empty."
 ]}
