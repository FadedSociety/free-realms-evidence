<!-- fleet job=citem-infer id=cdragonscale-roofing-shingles-19585-v1 status=nothing_found turns=6 usd=0.0028 tokens(read,write,in,out)=[36293, 9389, 14, 2435] model=claude-haiku-5-5 -->
# Dragonscale Roofing Shingles

{"item": {"name": "Dragonscale Roofing Shingles", "locale_id": 19585, "kind": "furniture"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text defines the item name 'Dragonscale Roofing Shingles' at locale 19585, with description 'Almost like having dragon scales on your roof.' Definition id 76784, slot 0, class 0, no models, and no coin store price.", "source": "locale:19585; client definition pack"},
  {"claim": "The item appears in the wiki Items index under the 'Roofs' heading (as 'Dragonscale Roofing Shingles'), alongside 'Natural Wooden Roofing' and the Walls section wallpapers. The index is a bare list with no acquisition info and no dedicated item page was found.", "source": "wiki page:ns0 'Items' (index listing)"},
  {"claim": "Client cluster 19580-19590 (flooring, roofing, and wallpaper decor) sits together in the client text table, consistent with housing decor items, but no source names how these were obtained.", "source": "locale:19580-19590"},
  {"claim": "Repo stores.json has no coin store entry for definition 76784, so no coin vendor sale is evidenced.", "source": "client definition pack; repo:data/content/stores.json (no match)"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found: no vendor, marketplace, coin shop, quest, drop, event, or crafting evidence for this item in any source searched (client, wiki, articles, video, repo, refs).",
  "The wiki Items index lists it under Roofs, so a wiki item page may exist, but it was not retrievable by search; check the page directly for its source and price.",
  "Live status is unconfirmed. The first-pass 'live: yes' tag is a model guess, not evidence; the wiki index listing suggests it was in the game, but no retirement info was found.",
  "Kind is set to furniture from the housing-decor context of the cluster and the Roofs wiki heading, not from the client definition (which has no class or model data).",
  "Critique notes: none carried in the pack. Jev's first-pass source guess 'unknown' is not contradicted, but nothing supports a different source either."
 ]}
