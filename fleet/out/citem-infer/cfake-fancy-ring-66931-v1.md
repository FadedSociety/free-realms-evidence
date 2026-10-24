<!-- fleet job=citem-infer id=cfake-fancy-ring-66931-v1 status=done turns=27 usd=0.0182 tokens(read,write,in,out)=[722052, 40971, 56, 11674] model=claude-haiku-5-5 -->
# Fake Fancy Ring

{"item": {"name": "Fake Fancy Ring", "locale_id": 66931, "kind": "collection"},
 "sources": [
  {"type": "other", "detail": "Gathered from the Stillwater 'robgoblin-junk' (junk node) common drop pool, one of 100-weight entries alongside other Fancy Rings entries (23317, 23319, 23320)", "where": "Stillwater", "price": null, "currency": null, "source": "refs:Sanctuary-main-20261019/src/Resources/CollectionNodePools.json:1470 (pool key 'stillwater-robgoblin-junk', lines 875-1868)"},
  {"type": "other", "detail": "Gathered from the Sanctuary Central 'robgoblin-junk' (junk node) common drop pool, weight 100", "where": "Sanctuary Central", "price": null, "currency": null, "source": "refs:Sanctuary-main-20261019/src/Resources/CollectionNodePools.json:4702 (pool key 'sanctuary-central-robgoblin-junk', lines 4059-5100)"},
  {"type": "other", "detail": "Gathered from the Southern Wilds 'robgoblin-junk' (junk node) common drop pool, weight 100", "where": "Southern Wilds", "price": null, "currency": null, "source": "refs:Sanctuary-main-20261019/src/Resources/CollectionNodePools.json:7132 (pool key 'southern-wilds-robgoblin-junk', lines 6512-7532)"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name locale 66931 is 'Fake Fancy Ring'; description 'This item can be added to the Fancy Rings Collection'; item definition 23318, no coin store price, no models, slot 0, class 0", "source": "locale:66931; client definition in pack (ClientItemDefinitions via refs Sanctuary/Lxzxrus Resources)"},
  {"claim": "Item 23318 is entry 4 of collection 'Fancy Rings' (collection id 164, name_id 67530, entries 1190-1194 and onward), listed on the wiki 'List of Collections' page as '[Fancy] [Rings]'", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:12825 (id 1193, name_id 66931, item_definition_id 23318); repo:prototype/osfr-tools/data/content/collections.json:9930; wiki page 'List of Collections' (revision 27852, 2013-07-13)"},
  {"claim": "Item 23318 appears in three robgoblin-junk node drop pools (Stillwater, Sanctuary Central, Southern Wilds) at weight 100; it is not in any rare pool", "source": "refs:Sanctuary-main-20261019/src/Resources/CollectionNodePools.json lines 1470, 4702, 7132"},
  {"claim": "Fancy Rings collection reward is 2 coins and 50 XP on completion; this is the collection reward, not a source for the ring", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json (collection id 164 reward block, ~line 12772)"},
  {"claim": "Marriage Proposal quest (locale 23583, 23586, 24932, 77482) mentions buying a fancy ring but is flagged NOT LIVE and names no Fake Fancy Ring; not a source", "source": "locale:23583; locale:23586; locale:24932; locale:77482"},
  {"claim": "Collection entries use item_link 'sanctuary' only as a join label in the rebuild data, not as a vendor or shop source", "source": "notes/Autopilot/T447.md:60-99"},
  {"claim": "No coin vendor stocks 23318; no wiki article, article fact, or video frame names it; no quest reward names it", "source": "lookup of client/wiki/articles/video for 'Fancy Ring', 'Fake Fancy', 'Jagged Ring'; repo search for 23318 and stores.json"}
 ],
 "confidence": 0.55,
 "open": [
  "The three pool sources are gathering-node drops from junk nodes, not enemy drops. The schema has no node type, so they are filed as 'other'. Confirm whether the rebuild treats node pools as drops.",
  "Pool weights are 100 each and the drop chance per node is not in the data; the rate is unknown.",
  "The pool file is community-sourced (Sanctuary repo) and has no wiki or player-facing confirmation for these three zones. Nothing in the wiki or video covers Fancy Rings sources.",
  "The zone names come from the pool keys; ZoneDefinitionId is 1 for all of these pools, so zone mapping is by key name only.",
  "No wiki price, Station Cash price, or Coin Shop listing exists for this item. Coin price: none.",
  "Retirement status is unknown: no source states that the ring was retired or removed, and no source confirms it is still obtainable. live is 'yes' on the strength of the catalogue and pool data and the first-pass tag, not a dated source.",
  "Locale 23318 is a different string ('Junk', a UI fragment); it is not this item and was not used.",
  "The three zone pools (Stillwater, Sanctuary Central, Southern Wilds) are community data; check them against a live node or a player report before relying on them."
 ]}
