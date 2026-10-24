<!-- fleet job=citem-infer id=cpink-rose-1238-v1 status=done turns=7 usd=0.0047 tokens(read,write,in,out)=[77604, 17948, 16, 3268] model=claude-haiku-5-5 -->
# Pink Rose

{"item": {"name": "Pink Rose", "locale_id": 1238, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 'Pink Rose' (locale 1238) with description 'This item can be added to the Roses Collection' (locale:132286 'Roses Collection' UI string); definition_id 3090, no coin store price.", "source": "locale:1238; locale:132286; repo:refs quest-lines/citem-packs.json cpink-rose-1238"},
  {"claim": "The wiki's List of Collections lists a 'Roses' collection (and a separate 'Snowhill Roses' collection), with no entries known and no reward or source recorded.", "source": "https://freerealms.fandom.com/wiki/List_of_Collections (rev 27852, 2013-07-13), via repo:prototype/osfr-tools/data/content/collections.json lines 5555-5582 (wiki:3:80) and 5779-5800 (wiki:3:88)"},
  {"claim": "The Roses Collection is the non-Snowhill rose set; its sibling 'Red Rose', 'White Rose', 'Yellow Rose', 'Blush Rose', 'Orange Rose' sit in the same client cluster (locales 1239-1243), but no source text names how any rose is obtained.", "source": "client cluster locale:1233-1243"},
  {"claim": "Video frame shows pink rose bushes as scenery by a garden gate in Snowhill during the Miner: Rush Order quest. This is scenery, not an item source.", "source": "video:ct2JrtOiO4g/00318.jpg"},
  {"claim": "No coin vendor, quest reward, drop, or event in the repo or wiki stocks or names Pink Rose; the lookup returned no wiki page or article for it.", "source": "lookup (wiki, articles, client) and repo search for 'Pink Rose' / 'Roses'"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition source unknown: the Roses collection is listed on the wiki with no entries or reward, so the collection itself is the only attested link. Whether roses drop, are harvested, or come from an event is not evidenced.",
  "The jev first pass tagged source_guess 'collection' and live 'yes'; the collection listing supports 'collection' as a category but not a specific source. Treated as a hint only.",
  "Retired status unknown; no source states whether the Roses collection was closed or made unobtainable.",
  "The video scenery frame (Miner: Rush Order, Snowhill) is a landmark only and does not show Pink Rose being obtained. Do not use it as a source.",
  "The Snowhill Roses collection (locale 132492) is a different collection; its items are not confirmed to overlap with the plain Roses collection.",
  "No coin store price exists in stores.json for definition 3090, so no coin vendor sale is evidenced."
 ]}
