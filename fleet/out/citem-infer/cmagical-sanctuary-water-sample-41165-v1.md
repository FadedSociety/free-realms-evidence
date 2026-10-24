<!-- fleet job=citem-infer id=cmagical-sanctuary-water-sample-41165-v1 status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[32249, 19687, 10, 3312] model=claude-haiku-5-5 -->
# Magical Sanctuary Water Sample

{"item": {"name": "Magical Sanctuary Water Sample", "locale_id": 41165, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 3949 is named 'Magical Sanctuary Water Sample' (locale 41165) and its description reads 'This item can be added to the Sanctuary Water Samples Collection', so it is a collection-card item, not a directly usable or sellable item.", "source": "locale:41165; client definition id 3949"},
  {"claim": "Sibling samples in the same locale block (41160 Clean, 41161 Purified, 41162 Dirty, 41163 Boiling, 41164 Freezing, 41166 Mystical, and 41159 Toxic Sanctuary) share the Sanctuary sample collection line; the Merry Vale samples (41167-41170) are a separate set.", "source": "locale:41159-41170 (client_cluster in pack; lookup client results)"},
  {"claim": "A video frame shows a sample item in the inventory tooltip under 'Stuff Extras > Collections', but the tooltip reads 'added to the Sacred Keys Collection', which does not match this item's own description; the frame is only weak evidence of the collection UI.", "source": "video:pjvw6oAT-zQ/00084.jpg"},
  {"claim": "stores.json has a row with item_id 41165 (category 105, tint group 3) priced 1027 coins, member price 924 coins, sell price 102 coins. Its item_id equals this locale id, not the definition id 3949, and the client definition carries no coin_store_prices, so this is not confirmed as this item's store price. Sibling rows 41160, 41161, 41166 are also 1027 coins.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 12572 (and 12570, 12571, 12573)"},
  {"claim": "Repo notes describe a Lakeshore water-sample collection (Embir Clearwell, Shrouded Glade) with 'Lakeshore Water Sample' items; no note links the Sanctuary sample collection to a vendor, quest, drop, or event.", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Lakeshore.md:132"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is proven. No wiki page, article, or video names how a player obtains a Magical Sanctuary Water Sample; no vendor stocks it in the pack; no quest, drop, or event is cited.",
  "Coin store price: stores.json row item_id 41165 (1027 coins, member 924, sell 102) matches this locale id, not definition id 3949. Confirm whether store item_id is a definition id or a locale id before recording it as a Coin Shop or vendor price. If it is the definition id, no store price exists.",
  "The Sanctuary water sample set (Clean, Purified, Dirty, Boiling, Freezing, Magical, Mystical, Toxic) needs one source trace for the whole set; the water-sample quest or collection source should be checked against the Sanctuary zone notes.",
  "Live status: first pass says live, but no wiki or article confirms it. Keep 'unsure' until the collection's source or a retirement note is found.",
  "The video frame's collection name (Sacred Keys) conflicts with this item's description; treat the frame as unreliable for the collection name."
 ]}
