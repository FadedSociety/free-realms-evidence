<!-- fleet job=citem-infer id=cbrawler-doll-gloves-40655-v1 status=done turns=9 usd=0.0050 tokens(read,write,in,out)=[105768, 17565, 20, 3421] model=claude-haiku-5-5 -->
# Brawler Doll Gloves

{"item": {"name": "Brawler Doll Gloves", "locale_id": 40655, "kind": "collection"},
 "sources": [
  {"type": "drop", "detail": "Robgoblin (enemy spawn type recorded for the Brawler Human Doll collection; the piece itself is not tied to a named enemy on the wiki)", "where": "Northern Wilds", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collections.json:6430-6510 (collection wiki:4:105, entries include 'Brawler Doll Gloves'; spawn_type Robgoblin, area Northern Wilds, quality Common; source wiki page 'Toys (Collections)' https://freerealms.fandom.com/wiki/Toys_(Collections))"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Brawler Doll Gloves (locale 40655) is one of the 8 pieces of the 'Brawler Human Doll' collection; client text says it 'can be added to the Brawler Human Doll Collection'.", "source": "locale:40655; locale:45816; repo:prototype/osfr-tools/data/content/collections.json:6433-6487"},
  {"claim": "The wiki 'Toys (Collections)' page lists Brawler Doll Gloves in the Brawler Human Doll collection (Cap, Jacket, Shirt, Pants, Gear, Gloves, Shoes, Shorts).", "source": "wiki page 'Toys (Collections)' (lookup wiki page:ns0 Toys (Collections)); https://freerealms.fandom.com/wiki/Toys_(Collections)"},
  {"claim": "The collection is listed on the wiki 'List of Collections' page and in a video frame showing 'Brawler Human Doll (Collected: 8 / 8)'.", "source": "wiki page 'List of Collections'; video:5apg6w6ZZeU/00024"},
  {"claim": "Collection-level wiki reward: 21 coins, recorded as 'Human Brawler Doll 21'. This is the collection reward, not a price or source for the gloves alone.", "source": "repo:prototype/osfr-tools/data/content/collections.json:6492-6501"},
  {"claim": "No coin store price, vendor stock, or quest reward exists for the gloves in the repo data or the evidence pack.", "source": "client definition coin_store_prices: []; vendor_stock: []"}
 ],
 "confidence": 0.4,
 "open": [
  "The per-piece source is not confirmed. The only source is the collection record's spawn_type 'Robgoblin' in Northern Wilds, which may describe the whole collection rather than this glove. Needs a wiki page or player report that says the gloves drop from Robgoblins.",
  "Price is unknown. The 21 coins is the collection reward, not a price for the gloves.",
  "Retired status is unknown. No source states whether the Brawler Human Doll collection is still obtainable.",
  "The first-pass tag said source 'drop'. That matches the Robgoblin record but is unconfirmed, so it is treated only as a hint.",
  "The wiki page text for the Toys (Collections) pieces was not read in full, so the spawn detail could not be cross-checked against the page."
 ]}
