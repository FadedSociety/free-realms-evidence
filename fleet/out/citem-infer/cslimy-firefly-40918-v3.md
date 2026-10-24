<!-- fleet job=citem-infer id=cslimy-firefly-40918-v3 status=nothing_found turns=5 usd=0.0031 tokens(read,write,in,out)=[29492, 13186, 12, 2277] model=claude-haiku-5-5 -->
# Slimy Firefly

{"item": {"name": "Slimy Firefly", "locale_id": 40918, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item definition 3702 is named 'Slimy Firefly' (locale 40918). Its client description reads 'This item can be added to the Fireflies Collection'.", "source": "locale:40918; client definition definition_ids 3702"},
  {"claim": "Slimy Firefly is entry index 5 (entry id 634, name_id 40918, item_definition_id 3702) of collection id 89, name_id 7740 ('fireflies'), description_id 7816 ('A collection of fireflies found dancing in the night').", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:6926-6978; locale:7816"},
  {"claim": "Collection 89 entries carry item_link 'sanctuary'. This is a link field in the catalogue, not a named acquisition source, so it is not recorded as a source.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:6977-6978"},
  {"claim": "The reward block at lines 6905-6924 (3 coins, item 23085, xp 50, collection_add 133) sits before collection 89's opening brace at line 6926. It belongs to the preceding collection (whose last entry is item 3697, name_id 40913 'Queen Striped Snail'), not to the fireflies set. It is therefore not cited as Slimy Firefly's or collection 89's reward.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:6895-6926"},
  {"claim": "The wiki Collections page mentions firefly sparks in its general text but does not name Slimy Firefly.", "source": "wiki: Collections"},
  {"claim": "Related client strings exist for sibling items: Slimy Orange Firefly (locale:66703), Slimy Red Firefly (locale:66711), and Slimy Green Firefly (locale:66719, tagged npc_name). These do not establish how 3702 is obtained.", "source": "locale:66703; locale:66711; locale:66719"},
  {"claim": "No coin store price (stores.json), vendor stock, quest reward, enemy drop, event, or video frame names item 3702 or Slimy Firefly. The client definition has no coin_store_prices. Repo search for 3702 hits only the catalogue row and unrelated IDs.", "source": "repo search for 3702 / Slimy Firefly; client definition; lookup wiki/articles/video/client"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is evidenced for definition 3702. The jev first-pass 'drop' guess is unsupported and was not used. Needs an in-game pickup, drop, or reward record.",
  "Live status is unsure and retired is null. The item and its collection row exist, but no wiki, article, or video source says it was obtainable or removed.",
  "The previous answer's collection-complete reward (3 coins + item 23085) was removed: the reward block precedes collection 89 and belongs to the prior collection. Collection 89 has no reward block in the pack, so its completion reward is unknown.",
  "Collection 89 'fireflies' membership is recorded as data, not as an acquisition source. Whether the 'sanctuary' item_link means the firefly is found in Sanctuary is unverified and needs a source.",
  "The Slimy Orange, Red and Green Firefly siblings (locale 66703, 66711, 66719) could be checked for a shared source, but no evidence links them to 3702."
 ]}
