<!-- fleet job=citem-infer id=cbrawler-doll-gear-40654-v1 status=done turns=4 usd=0.0033 tokens(read,write,in,out)=[24637, 14879, 10, 2344] model=claude-haiku-5-5 -->
# Brawler Doll Gear

{"item": {"name": "Brawler Doll Gear", "locale_id": 40654, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text for 40654 is 'Brawler Doll Gear', and its description (locale:132315, ui) reads 'This item can be added to the Brawler Human Doll Collection', so it is a piece of the Brawler Human Doll collection, not a standalone purchasable.", "source": "locale:40654; locale:132315"},
  {"claim": "The Brawler Human Doll collection exists on the wiki with its pieces listed (Cap, Jacket, Shirt, Pants, Gear, Gloves, Shoes, and Shorts in the client cluster); the wiki page gives no acquisition method for them.", "source": "wiki: Toys (Collections); wiki: List of Collections"},
  {"claim": "A video frame shows a collection tracker entry '[Brawler] Human [Doll] (Collected: 8 / 8)', so the collection is tracked in-game with pieces collected. This does not say how the pieces are obtained.", "source": "video:5apg6w6ZZeU/00024.jpg"},
  {"claim": "The client definition has no coin store price (coin_store_prices empty), so there is no coin vendor sale evidence for this item.", "source": "pack client_definition; repo:data/content/stores.json has no entry for item 3438"},
  {"claim": "The repo has no vendor, quest, or drop record for definition 3438 or the Brawler Doll names.", "source": "search repo for 'Brawler|3438|40654' (only unrelated MODLOG/notes hits)"}
 ],
 "confidence": 0.2,
 "open": [
  "No source for how the Brawler Doll pieces are obtained. The first-pass guess of 'drop' has no evidence behind it and is not used. Needs a wiki page or player report on the Brawler Human Doll collection's acquisition (drop, collection reward, event, or vendor).",
  "Whether the piece is live or retired is unknown. The wiki collection list shows the collection with no retired note, but it gives no date, so 'live' is left as unsure.",
  "The wiki lists the collection as '[Brawler] Human [Doll]'. The pack says the collection name is 'Brawler Human Doll Collection' (from the description). The name matches; the wiki's own piece list is the only evidence the other eight pieces belong to it.",
  "Slots [0] and class [0] do not show clothing or a collection kind directly. Kind 'collection' follows the item description and the collection tracker, not a slot check.",
  "Pack critique: none was carried in the pack, so none to fix."
 ]}
