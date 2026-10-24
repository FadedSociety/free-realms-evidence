<!-- fleet job=citem-infer id=cunbreakable-bow-strings-67353-v2 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[6705, 12585, 6, 2984] model=claude-haiku-5-5 -->
# Unbreakable Bow Strings

{"item": {"name": "Unbreakable Bow Strings", "locale_id": 67353, "kind": "collection"},
 "sources": [
  {"type": "vendor", "detail": "Nirvi (Steelbloom's apprentice smith; client quest line says 'Nirvi over there can sell you one, but they aren't cheap'), for Archer quest 'Archer: Building a Better Bow' (Bullseye's quest)", "where": "Sanctuary Royal Smithy per NPC notes (the 'over there' line does not itself fix a zone; the earlier 'Blackspore entrance' placement is unverified)", "price": null, "currency": null, "source": "locale:115396; notes/Build Guides/Content/Jobs/Archer.md:57; notes/Build Guides/Content/NPCs/NPCs - Sanctuary.md:64"},
  {"type": "vendor", "detail": "Bullseye (conflicting seller: quest objective text says to buy bow strings from Bullseye); unresolved against Nirvi", "where": "Greenwood Forest / Blackspore entrance area (Bullseye)", "price": null, "currency": null, "source": "quest objective text locale 130873 and 115370 (cited in quest-lines/quests.json); notes/Build Guides/Content/Jobs/Archer.md:130 and :210"},
  {"type": "collection", "detail": "Archer Bow Materials collection (Archer job collection; wiki says the string can come randomly from Archer Materials, no drop rate given)", "where": null, "price": null, "currency": null, "source": "wiki image:collection 'Archer Bow Materials.png'; wiki page 'Archer Magical Bow Essences' (collection of eight items); wiki page 'Job Specific (Collections)'; repo:prototype/osfr-tools/data/content/collections.json:2464-2481; notes/Build Guides/Content/Jobs/Archer.md:210"},
  {"type": "coin_shop", "detail": "Wiki-stated Coin Shop source, quoted second-hand in Archer.md; no Coin Shop listing found in the pack or repo stores. Not confirmed.", "where": "Coin Shop", "price": null, "currency": null, "source": "notes/Build Guides/Content/Jobs/Archer.md:210 (second-hand wiki statement only)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 'Unbreakable Bow Strings' is locale 67353 with definition ids 23740 and 48324; its description says it can be added to the Archer Bow Materials Collection and requires quest 'Archer: Building a Better Bow'.", "source": "locale:67353; description locale:132474"},
  {"claim": "The Archer Bow Materials collection is composed of eight items, including Unbreakable Bow Strings.", "source": "wiki page 'Archer Magical Bow Essences'; wiki image 'Archer Bow Materials.png'; repo:prototype/osfr-tools/data/content/collections.json:2464-2481"},
  {"claim": "Nirvi is named as the seller of an unbreakable bow string in the Bullseye quest line; the NPC says 'they aren't cheap'. No price is given.", "source": "locale:115396; locale:115373; locale:115376; notes/Build Guides/Content/Jobs/Archer.md:57"},
  {"claim": "Bullseye's quest objective text says to buy bow strings from Bullseye, which conflicts with the Nirvi line.", "source": "locale 130873, 115370; notes/Build Guides/Content/Jobs/Archer.md:130, :210"},
  {"claim": "The quest 'Archer: Building a Better Bow' is Bullseye's quest that uses the string to repair his bow.", "source": "locale:115376; locale:78468 (quest title); notes/Build Guides/Content/Jobs/Archer.md:130"},
  {"claim": "Archer.md gives the wiki's Coin Shop and random Archer Materials sources for this string, and notes the wiki line describes a later retired state.", "source": "notes/Build Guides/Content/Jobs/Archer.md:210"}
 ],
 "confidence": 0.4,
 "open": [
  "No coin store price: the client definitions 23740 and 48324 have no coin_store_prices entry, and no source gives Nirvi's or Bullseye's price or currency.",
  "Seller conflict: the Nirvi line (locale 115396) and the Bullseye objective text (locale 130873/115370) name different sellers. Unresolved.",
  "Quest level conflict: Archer.md row 30 says 'After 28'; archer.json in quest-lines says level 20. The level is not stated in this answer.",
  "The Coin Shop source is second-hand (Archer.md:210) and unconfirmed by any Coin Shop listing.",
  "Collection drop detail: the wiki says the string can come randomly from Archer Materials, but the rate, the dungeons, and whether it drops from enemies are not given in the pack. The earlier 'dungeons' claim is removed as unsupported.",
  "Nirvi's location: the Royal Smithy in Sanctuary per NPC notes; the earlier 'Blackspore Swamp entrance' placement is not supported.",
  "Two definition ids (23740 and 48324) with no notes; whether they are variants or tints is unknown.",
  "Retirement: Archer.md says the wiki line describes a later retired state, but no source states the item is retired; retired is left null.",
  "Locale ids corrected per critique: 4015355435 and 3538808478 and 1716889141 do not exist; the working ids are 115396, 132474 and 78468."
 ]}
