<!-- fleet job=citem-infer id=ctoxic-lakeshore-mixture-66832-v1 status=done turns=5 usd=0.0046 tokens(read,write,in,out)=[53110, 21971, 12, 2569] model=claude-haiku-5-5 -->
# Toxic Lakeshore Mixture

{"item": {"name": "Toxic Lakeshore Mixture", "locale_id": 66832, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item text 'Toxic Lakeshore Mixture' is locale 66832, with description 'This item can be added to the Lakeshore Mixture Collection' (locale 132411 / 1779281785 in the data file), so it is a collection-fill item, not a vendor or quest item.", "source": "locale:66832; locale:132411"},
  {"claim": "The client defines 'Lakeshore Mixture' as a collection name (locale 67518), and the Lakeshore Mixture set has eleven variants: Toxic, Clean, Purified, Dirty, Boiling, Freezing, Magical, Mystical (locales 66832-66839 plus 66833-66837 cluster).", "source": "locale:67518; locale:66832..66839"},
  {"claim": "The wiki 'List of Collections' page lists a '[Lakeshore] [Mixture]' collection, which supports the collection being a live, named collection. The page does not say how members are obtained.", "source": "wiki: List of Collections"},
  {"claim": "Sibling 'Seaside Mixture' items (Dirty, Boiling, Freezing, Magical, Mystical, Toxic, Clean, Purified) share the same description pattern and the same collection structure, so this set is a parallel collection family.", "source": "locale:66827-66831; refs: FreeRealmsLocaleTools en_us_data.dat 'This item can be added to the Seaside Mixture Collection'"},
  {"claim": "The client definition has no coin store price, and no vendor stocks this item in our data, so no coin vendor source is supported.", "source": "client definition (coin_store_prices: []; vendor_stock: [])"}
 ],
 "confidence": 0.3,
 "open": [
  "No source found. The item is a member of the Lakeshore Mixture collection, but no page, article, video, quest, drop, or vendor in the pack says where a Toxic Lakeshore Mixture comes from (picked up while fishing or from a water-sampling activity, or crafted, is a guess only and is not evidenced).",
  "The client has a related 'Toxic Lakeshore Water Sample' (locale 1711713891 / 940329751) and 'Lakeshore Water Samples' collection text, which suggests the mixtures may come from the same water-sample activity, but this is unverified and needs a source check before it is recorded.",
  "The 'Lakeshore Mixture' collection reward (what the player gets for completing the set) is not in the pack. It is not known whether the collection is still live or was retired; the collection is listed on the wiki, so live status is unsure rather than no.",
  "Price, currency and retirement are unknown; no coin store entry and no marketplace or prize-wheel source is listed for this item.",
  "Next checks: the wiki 'Lakeshore Mixture' or 'Seaside Mixture' pages (if they exist), the fishing and water-sample quest text for 'mixture', and the crafting recipes for mixture items in the repo."
 ]}
