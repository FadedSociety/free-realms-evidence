<!-- fleet job=citem-infer id=cchaz-s-mystical-necklace-86700-v2 status=nothing_found turns=3 usd=0.0036 tokens(read,write,in,out)=[21510, 18467, 8, 2182] model=claude-haiku-5-5 -->
# Chaz's Mystical Necklace

{"item": {"name": "Chaz's Mystical Necklace", "locale_id": 86700, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale:86700 \"Chaz's Mystical Necklace\"; one definition (22709), slot 9, class 42, no models, empty description, no coin store price.", "source": "locale:86700; client definition in pack"},
  {"claim": "Part of an 11-item family of Chaz-named necklaces (locale 86697-86705 plus 86706 Chaz's Cosmic Necklace), each with its own definition ID (the Phantasmal one is 22710, so this one is probably 22709). Same name pattern as Gleaming and Mystical necklaces (for example Champion Mystical Necklace 86616, Prowler Mystical Necklace 86607, Magus Mystical Necklace 86625).", "source": "locale:86697-86706; locale:86607, 86616, 86625; refs quest-lines/citem-packs.json:63958-63994"},
  {"claim": "Chaz Strongarm is an NPC name in the client and is a pixie NPC in Lakeshore, a retired brawler who runs the fighter's club. The NPC name does not show that the necklace is sold or dropped.", "source": "locale:117044 (npc_name); wiki page 'Chaz Strongarm' (Category:NPC, Category:Lakeshore, Category:Brawler)"},
  {"claim": "Repeated lookups (client, wiki, articles, video) for 'Chaz Necklace' and the repo/refs searches for 22709 and the necklace name found no vendor, quest reward, drop, event, prize wheel, crafting, store, wiki, article, or video source for this item. The only hits were the client name cluster and sibling pack records.", "source": "lookup client/wiki/articles/video 'Chaz Necklace'; search repo '22709|Necklace|86700'; search refs 'Chaz...Necklace|22709'"},
  {"claim": "The earlier citation to locale:22811 was dropped because it belongs to a NOT LIVE quest. The Chaz Strongarm NPC claim now cites locale:117044 and the wiki page.", "source": "id_check flag on locale:22811; locale:117044"},
  {"claim": "The first-pass tag (live yes, source guess drop) is a model guess and is not supported by any source found.", "source": "jev_first_pass in evidence pack"}
 ],
 "confidence": 0.1,
 "open": [
  "No source for how this necklace is obtained. No vendor, quest, drop, event, prize wheel, crafting, Coin Shop, Station Cash Marketplace, or promotion entry was found.",
  "Whether it is a Chaz quest reward, Lakeshore Brawler Club reward, or a set/promotion item is unproven. The Chaz family naming suggests a shared source, but that source is not in the repo, refs, or wiki.",
  "Retired status is unknown. Live status is unsure: the client defines the item, but no source shows it was sold or dropped.",
  "Description is empty in the client definition, so no in-game text describes it.",
  "The necklace has no coin store price in stores data, so the coin shop route is closed by the pack, not confirmed absent from every store."
 ]}
