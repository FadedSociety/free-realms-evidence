<!-- fleet job=citem-infer id=cninja-s-ring-of-regeneration-iii-131121-v3 status=done turns=2 usd=0.0036 tokens(read,write,in,out)=[7388, 15060, 6, 3231] model=claude-haiku-5-5 -->
# Ninja's Ring of Regeneration III

{"item": {"name": "Ninja's Ring of Regeneration III", "locale_id": 131121, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Dizzy Toad (Ninja gear merchant, ucdt 1820886519). Wiki Sells list includes this ring; wiki stock entry dated 27 Aug 2013 (introduction date).", "where": "Perry's Pastures, south of Snowhill (wiki-only location; the client could not place this merchant, so the location is unconfirmed)", "price": null, "currency": null, "source": "wiki page https://freerealms.fandom.com/wiki/Dizzy_Toad (Sells section, revision 2013-10-03); repo:prototype/osfr-tools/data/content/vendors.json lines 33213-33237; repo:notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:116 and :240"},
  {"type": "prize_wheel", "detail": "Ninja row of the Floren Forest 'Prize wheel by job' table (guide citation only; not checked against a wiki page or client source). The same item also appears in Ninja rows of the Snarling Hedges, Mushroom Gigas, Snatching Snappers and Seaside Swoopers dungeon tables beside Battle Item Mystery Pack, so it may be a mystery-pack content line or a dungeon reward rather than a direct wheel slot.", "where": "Floren Forest (dungeon reward wheel); also the other dungeons listed", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Floren Forest.md:62-71; repo:notes/Build Guides/Content/Dungeons/The Snarling Hedges.md:73; repo:notes/Build Guides/Content/Dungeons/The Mushroom Gigas.md:67; repo:notes/Build Guides/Content/Dungeons/Snatching Snappers.md:69; repo:notes/Build Guides/Content/Dungeons/Seaside Swoopers.md:69"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Ninja's Ring of Regeneration III' is locale 131121; client definition 75377; slot 8; class 2.", "source": "locale:131121; repo:prototype/osfr-tools/data/content/vendors.json lines 33213-33217"},
  {"claim": "Dizzy Toad's wiki Sells list includes this ring (wiki stock only, no prices on the wiki page).", "source": "https://freerealms.fandom.com/wiki/Dizzy_Toad; repo:prototype/osfr-tools/data/content/vendors.json lines 33229-33237"},
  {"claim": "Snowhill NPC notes list Dizzy Toad as a Ninja gear merchant added 27 Aug 2013 with Nusumi Ninja set, Power Shard, Necklace, Ring; gear merchants are wiki-only and the client could not place them.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:116 and :240"},
  {"claim": "Floren Forest guide lists this ring in the Ninja prize-wheel row, beside Battle Item Mystery Pack. The guide cites the wiki generically; no page-level citation.", "source": "repo:notes/Build Guides/Content/Dungeons/Floren Forest.md:62-73"},
  {"claim": "Same ring appears in Ninja rows of four other dungeon reward tables.", "source": "repo:notes/Build Guides/Content/Dungeons/The Snarling Hedges.md:73; The Mushroom Gigas.md:67; Snatching Snappers.md:69; Seaside Swoopers.md:69"},
  {"claim": "The 1055-coin store reference (member 949, sell 105) is a reconstructed Legacy reference, not a captured NPC or wiki price.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75377 (price_provenance reference); vendors.json line 33222; critique of previous answer"},
  {"claim": "A differently named 'Ring of Regeneration III' (no Ninja prefix) is sold by a Cross Wind Archer vendor and is a different item.", "source": "repo: lakeshore.json:5752 (per previous answer; not re-checked)"}
 ],
 "confidence": 0.4,
 "open": [
  "Dizzy Toad's price is not evidenced. The 1055 coin figure is a reconstructed reference (stores.json item 75377), not a wiki or in-game quote. Price left null. A captured Dizzy Toad price is needed.",
  "Perry's Pastures location is wiki-only; the client could not place Dizzy Toad, so the location is unconfirmed.",
  "The prize-wheel / mystery-pack / dungeon-reward entries rest only on build-guide tables that cite the wiki generically. Not confirmed against a wiki page or client source. Unclear whether it is a direct wheel slot, Battle Item Mystery Pack content, or a drop.",
  "Live status unsure: newest dated evidence is the Oct 2013 wiki revision. No retirement evidence found, and no current check was done.",
  "wireable: false. No source has an evidenced price, and the prize-wheel source is unverified."
 ]
}
