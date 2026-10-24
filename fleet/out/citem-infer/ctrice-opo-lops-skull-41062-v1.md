<!-- fleet job=citem-infer id=ctrice-opo-lops-skull-41062-v1 status=done turns=6 usd=0.0055 tokens(read,write,in,out)=[66999, 23806, 14, 3762] model=claude-haiku-5-5 -->
# Trice-opo-lops Skull

{"item": {"name": "Trice-opo-lops Skull", "locale_id": 41062, "kind": "collection"},
 "sources": [{"type": "other", "detail": "Rare Item-collection spawn (sparkling 'Pile of Fossils' spawn, rare variant) in the Blackspore region; the spawn yields one piece of a collection, and this skull is a piece of the Skull Fossils (Rare, Archaic) collection", "where": "Blackspore (Blackspore Swamp region, Sacred Grove)", "price": null, "currency": null, "source": "wiki: Collections (freerealms-wiki 1991-45236 'Item Collections' section); wiki: Spawn Types 'Pile of Fossils' (freerealms-wiki 2145-20376); wiki: List of Collections, Archaic > Rare > Skull Fossils (freerealms-wiki 2038-27852 line 262)"}],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client defines 'Trice-opo-lops Skull' as locale 41062, description 'This item can be added to the Skull Fossils Collection', one definition (id 3846), no tints/races, no coin store price", "source": "locale:41062; locale:132366 / 'Skull Fossils' locale 3809470774 and 4128465665; repo: quest-lines/citem-packs.json (same description string on several items)"},
  {"claim": "The Skull Fossils collection is a Rare collection in the Archaic category of the wiki's List of Collections", "source": "wiki: List of Collections (freerealms-wiki/wikitext/2038-27852-f0e36d086ea8.wiki lines 246-262)"},
  {"claim": "Item-collection pieces come from sparkling spawn objects; Rare pieces appear less often and show '<Rare Collection>' in the spawn name", "source": "wiki: Collections (freerealms-wiki/wikitext/1991-45236-52bebd9576a3.wiki lines 14-17)"},
  {"claim": "Pile of Fossils spawns are found only in the Blackspore region, with a Common and a Rare variant", "source": "wiki: Spawn Types (freerealms-wiki/wikitext/2145-20376-d0e62216cc0b.wiki lines 53-58)"},
  {"claim": "Sibling skull pieces in the same client cluster (Tri-celopter, Tricera-topsy, Tricera-turvey, Tricera-tips, Trici-teratops) share the same description, so this is one of six pieces of the set", "source": "locale:41057-41061"}
 ],
 "confidence": 0.5,
 "open": [
  "No wiki page or video names this specific skull or says which spawn type yields Skull Fossils pieces; the Pile of Fossils link is inferred from the collection being in the Archaic/fossil family, not confirmed by a source.",
  "Not verified that the Skull Fossils collection still has spawns in the live game; the wiki list has no dates, so 'live: yes' rests on the client definition and the wiki list only.",
  "No completion reward for the Skull Fossils collection was found, so no collection-reward source is listed.",
  "No coin vendor, Station Cash, or prize-wheel source found; no vendor stock or prices given.",
  "Jev's first pass said 'drop'; the evidence points to a gathered spawn, not an enemy drop, so it is recorded as 'other'."
 ]}
