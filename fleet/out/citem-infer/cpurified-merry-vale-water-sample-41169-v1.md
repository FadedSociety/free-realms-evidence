<!-- fleet job=citem-infer id=cpurified-merry-vale-water-sample-41169-v1 status=done turns=4 usd=0.0042 tokens(read,write,in,out)=[29335, 19451, 10, 2987] model=claude-haiku-5-5 -->
# Purified Merry Vale Water Sample

{"item": {"name": "Purified Merry Vale Water Sample", "locale_id": 41169, "kind": "collection"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, store vendor not named in repo data (stores.json row for item 41169, category 103, tint group 1)", "where": null, "price": "358 coins (member price 322 coins; sell-back 35 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:7951 (item_id 41169)"},
  {"type": "collection", "detail": "Item for the Merry Vale Water Samples collection (collection item definition 3953, name locale 41169, sits at index 3 of the Merry Vale set in the collection catalogue)", "where": "Merry Vale", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:10081-10084; repo:prototype/osfr-tools/data/content/collections.json:11270-11297 (wiki:8:223 'Merry Vale Water Samples', List of Collections, rev 27852, 2013-07-13); locale:41169 'This item can be added to the Merry Vale Water Samples Collection'"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name and description: 'Purified Merry Vale Water Sample', 'This item can be added to the Merry Vale Water Samples Collection' (definition id 3953, one variant)", "source": "locale:41169"},
  {"claim": "The Merry Vale water sample set has 8 sibling items (41167-41174: Toxic, Clean, Purified, Dirty, Boiling, Freezing, Magical, Mystical) and a matching Merry Vale Water Samples collection exists on the wiki List of Collections", "source": "locale:41167-41174; repo:prototype/osfr-tools/data/content/collections.json:11270-11297"},
  {"claim": "Coin store row for item 41169 at 358 coins, member price 322, sell price 35, no_sale false, same tag set as the other coin-store rows", "source": "repo:prototype/osfr-tools/data/content/stores.json:7951"},
  {"claim": "Video frame shows the Toxic Merry Vale Water Sample in the collections inventory view with 'This item can be added to ... Collection', so sample items are held as collection entries", "source": "video:pjvw6oAT-zQ/00084.jpg"}
 ],
 "confidence": 0.5,
 "open": [
  "The pack's client definition says coin_store_prices is empty, but repo stores.json has a row for item 41169 at 358 coins. I used the repo row, which is the stronger record; the pack's empty field should be checked against the store loader.",
  "The stores.json row does not name the vendor or store. Category 103 is shared by many coin-store items, so the exact coin vendor/shop for item 41169 is unknown.",
  "No wiki page, article, or quest/drop source names how a player obtains a Purified Merry Vale Water Sample (quest reward, gathering, or drop). Only the coin-store row and collection membership are evidenced.",
  "The 358-coin price is from repo store data only; no wiki price was found to confirm it or show a sale price.",
  "Retired status and any later removal are unknown; no source says whether the sample set was retired."
 ]}
