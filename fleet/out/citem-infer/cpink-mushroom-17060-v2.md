<!-- fleet job=citem-infer id=cpink-mushroom-17060-v2 status=nothing_found turns=2 usd=0.0017 tokens(read,write,in,out)=[5927, 7044, 6, 1581] model=claude-haiku-5-5 -->
# Pink Mushroom

{"item": {"name": "Pink Mushroom", "locale_id": 17060, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Pink Mushroom' is locale 17060, tagged Briarwood, in the Briarwood Mushrooms cluster (17055 Briarwood Mushrooms collection description, 17056 to 17063 mushroom names).", "source": "locale:17060; locale:17055"},
  {"claim": "Item definition 11085 is entry 'Pink Mushroom' in the Briarwood Mushrooms collection (collection key wiki:3:69, client id 17054).", "source": "repo:prototype/osfr-tools/data/content/collections.json:5152-5155; repo:prototype/osfr-tools/data/content/collection_catalogue.json:70"},
  {"claim": "The wiki's List of Collections page lists a Briarwood Mushrooms set; the page snippet confirms the set name, not the Pink Mushroom entry itself.", "source": "wiki: List of Collections (per pack)"},
  {"claim": "Item 11085 also appears in the Rare Mushrooms harvest node pool, but those repo rows are tagged legacy reference data and no live wiki, article or video confirms that node yields it. Dropped as a source.", "source": "repo:prototype/osfr-tools/data/content/harvest_nodes.json:95-111, 105"},
  {"claim": "Video frames show Briarwood pink mushroom scenery only, not a pickup. The 'Pink Mushroom Cap' Virtual Reward card (video:4pioItLqlU8/00134.jpg) and 'Pink Mushroom Hat' (locale 392660) are different items. 'Pink Spotted Mushroom' (locale 1428) is also different.", "source": "video:P1aMSRArMDw/00100.jpg; video:98uNKkDRvQU/00384.jpg; video:4pioItLqlU8/00134.jpg; locale:392660; locale:1428"},
  {"claim": "No coin store price exists (coin_store_prices empty), and no vendor stock, quest reward, or event names the item.", "source": "client definition; vendor_stock empty"}
 ],
 "confidence": 0.3,
 "open": [
  "No verified acquisition source. Collection membership (Briarwood Mushrooms, entry 45) is a progress slot, not a source, so it is not listed.",
  "The Rare Mushrooms harvest-node drop is legacy reference data with no live confirmation; excluded per critique. Needs a live client check or wiki confirmation before it can be added back as a 'drop' (zone Briarwood).",
  "Collection set rewards for completing Briarwood Mushrooms were not found; if the set has a reward, it is unknown here.",
  "Retirement status unknown; no evidence either way.",
  "Kind is 'collection' as the pack has it; the item has no model, slot, or icon data in the client definition, so this is a guess from the collection link."
 ]}
