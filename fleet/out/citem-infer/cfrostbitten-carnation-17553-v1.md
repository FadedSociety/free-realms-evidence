<!-- fleet job=citem-infer id=cfrostbitten-carnation-17553-v1 status=done turns=4 usd=0.0037 tokens(read,write,in,out)=[23161, 17271, 10, 2669] model=claude-haiku-5-5 -->
# Frostbitten Carnation

{"item": {"name": "Frostbitten Carnation", "locale_id": 17553, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: item_definition_id 9185 is named locale:17553 'Frostbitten Carnation' with description locale:132498 'This item can be added to the Snowhill Carnations Collection'. No coin store price, no models, one definition.", "source": "pack client_definition; locale:132498"},
  {"claim": "The item is entry index 6 (id 1814, icon_tint_id 105) of a Carnations set in the collection catalogue, with the same item_link 'sanctuary' as its set-mates (9183 Frosty, 9184 Frozen, 9186 Glacial Carnation).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:18419-18427"},
  {"claim": "The collection 'Snowhill Carnations' (wiki key wiki:3:82, name_id 17579) is listed on the wiki's List of Collections page as '[Snowhill] [Carnations]' with no entry list, so the set exists, but the page gives no acquisition method for its items.", "source": "https://freerealms.fandom.com/wiki/List_of_Collections (repo:prototype/osfr-tools/data/content/collections.json:5611-5638)"},
  {"claim": "No coin vendor, Station Cash, quest, drop, event or crafting source names this carnation. The pack had no vendor stock, wiki page, image, article or video for it.", "source": "pack (vendor_stock, mentioned_by_other_answers empty); lookup of client, wiki, articles, video for 'Frostbitten Carnation' and 'Snowhill Carnations' found only the collection list"},
  {"claim": "The client text sits in a set of eight Carnation names (locale 17548-17555: Icy, Wintery, Snowy, Frosty, Frozen, Frostbitten, Chilled, Glacial). Only the Chilled Carnation name also appears in the client search results.", "source": "pack client_cluster; locale:17554"}
 ],
 "confidence": 0.35,
 "open": [
  "No acquisition source found. The item is a Snowhill Carnations collection piece, but how players got it (drop, quest, event, or Snowhill gathering/fishing) is not documented in any source here. Do not assign a source without evidence.",
  "Live status is unsure. The collection list and the catalogue entry show the item is defined, but no source shows it is still obtainable. The first-pass 'live: yes' is only a hint.",
  "The catalogue's item_link 'sanctuary' is the only hint about where this item came from. It may refer to Sanctuary-server data, which is not evidence of a live source for Bryce's server.",
  "Wiki collection pages for 'Snowhill Carnations' (and the other 'Snowhill' flower sets, e.g. Snowhill Daisies, Roses) were not fetched in full. Check the collection's own wiki page for the item list and any sources, and check whether these are gathered or drops.",
  "No coin price for the item, so no coin vendor sale is recorded."
 ]}
