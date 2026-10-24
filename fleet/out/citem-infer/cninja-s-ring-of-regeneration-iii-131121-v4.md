<!-- fleet job=citem-infer id=cninja-s-ring-of-regeneration-iii-131121-v4 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[7146, 14000, 6, 2204] model=claude-haiku-5-5 -->
# Ninja's Ring of Regeneration III

{"item": {"name": "Ninja's Ring of Regeneration III", "locale_id": 131121, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Dizzy Toad (Ninja gear merchant, ucdt 1820886519). Wiki says Dizzy Toad is a Pixie NPC merchant who sells exclusively Ninja Job Items; the Sells list on the wiki is only partly visible in lookup, so this ring's presence there is taken from the Snowhill notes (which list Dizzy Toad's Ring) and should be re-checked on the live page.", "where": "Perry's Pastures, south of Snowhill (wiki-only placement; client does not place the merchant)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Dizzy_Toad; repo:notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:116"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Ninja's Ring of Regeneration III' is locale 131121; client definition 75377; slot 8; class 2.", "source": "locale:131121"},
  {"claim": "Wiki Dizzy Toad page: Pixie NPC Merchant found at Perry's Pastures south of Snowhill, introduced August 27, 2013, sells exclusively Ninja Job Items.", "source": "https://freerealms.fandom.com/wiki/Dizzy_Toad"},
  {"claim": "Snowhill NPC notes list Dizzy Toad (ucdt 1820886519) as Ninja gear merchant, Perry's Pastures, added 27 Aug 2013, with a Ring among its items, and no known quest.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:116"},
  {"claim": "Same-name ring appears in Ninja rows of dungeon tables beside Battle Item Mystery Pack (Snarling Hedges, Mushroom Gigas, Snatching Snappers, Seaside Swoopers, Nettleseed Nibblers table rows use the Ninja Ring III line too). These are guide tables, not wiki or client confirmations of a drop or wheel slot.", "source": "repo:notes/Build Guides/Content/Dungeons/The Snarling Hedges.md:73; The Mushroom Gigas.md:67; Snatching Snappers.md:69; Seaside Swoopers.md:69"},
  {"claim": "The 1055 coin store reference (stores.json item 75377) is a reconstructed reference, not a captured NPC or wiki price, so no coin price is attributed to a source.", "source": "critique of previous answer; repo:prototype/osfr-tools/data/content/vendors.json lines 33222, 33251"}
 ],
 "confidence": 0.35,
 "open": [
  "Dizzy Toad coin price not evidenced; price left null. The 1055-coin figure in stores.json is a reconstructed reference only. A captured Dizzy Toad price is needed.",
  "Prize-wheel / mystery-pack / dungeon reward source dropped from the sources list: it rests only on build-guide tables citing the wiki generically (Floren Forest.md:62-71 'Prize wheel by job' heading). Needs a wiki page or client table naming this ring for the wheel or mystery pack.",
  "Perry's Pastures location is wiki-only; the client does not place Dizzy Toad, so the location is unconfirmed.",
  "The lookup excerpt of the wiki Dizzy Toad Sells list was truncated before the ring entry; re-confirm on the live page.",
  "Live status unsure: newest evidence is the Oct 2013 wiki revision; no retirement evidence found.",
  "Wireable: false. The only source has no evidenced price."
 ]}
