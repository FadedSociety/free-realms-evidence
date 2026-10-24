<!-- fleet job=citem-infer id=cmystical-snowhill-liquid-concoction-66759-v1 status=done turns=6 usd=0.0039 tokens(read,write,in,out)=[55404, 15330, 14, 2877] model=claude-haiku-5-5 -->
# Mystical Snowhill Liquid Concoction

{"item": {"name": "Mystical Snowhill Liquid Concoction", "locale_id": 66759, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text for locale 66759 is 'Mystical Snowhill Liquid Concoction', and its description (locale 132401) reads 'This item can be added to the Snowhill Liquid Concoction Collection', so it is a collection-feeding item, not a usable consumable or gear.", "source": "locale:66759; locale:132401; lookup client"},
  {"claim": "Description id 23146 appears in the research coverage file as a description_id, tying the definition to this collection text.", "source": "repo:notes/Research/original-activity-coverage.json:2828"},
  {"claim": "The Snowhill tier cluster is locale 66752 (Toxic) through 66759 (Mystical), beside the Nettleseed concoction cluster (66760-66764). Snowhill also has a base item 'Snowhill Liquid Concoction' at locale 67508.", "source": "lookup client; locale:67508"},
  {"claim": "The wiki 'List of Collections' page lists concoction collections for Lakeshore, Merry Vale, Nettleseed, Sanctuary and Seaside, but no Snowhill concoction entry; the repo's collections.json has matching entries for those five and none for Snowhill.", "source": "wiki:List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections); repo:prototype/osfr-tools/data/content/collections.json:11442-11465"},
  {"claim": "No coin store price, vendor stock, wiki page, article fact or video frame names this item, so no coin vendor sale is established.", "source": "client definition coin_store_prices: []; vendor_stock: []; lookup wiki/articles/video: no match"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source found. The first-pass guess 'drop' is a hint only and is not backed by any evidence in the pack; sources are left empty rather than guessed.",
  "Unknown whether the Snowhill concoction collection exists on the live wiki: the List of Collections concoction section omits Snowhill, though the client has the full tier set and the Snowhill collection text. Live status is therefore 'unsure'.",
  "Need the Snowhill concoction collection's reward and how the concoctions are produced (the sibling Lakeshore, Merry Vale, Nettleseed, Sanctuary and Seaside concoctions have no source data in the repo either). Check the original server/item-source tables or the Snowhill collection reward before assigning drop, crafting or vendor sources.",
  "Retired status unknown: no source states retirement or later unobtainability.",
  "Quest, drop, crafting and event sources to check: none located. Tiered concoction names (Toxic, Clean, Purified, Dirty, Boiling, Freezing, Magical, Mystical) suggest a refinement chain from a base item (locale 67508), which may be the real acquisition path."
 ]}
