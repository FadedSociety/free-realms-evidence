<!-- fleet job=citem-infer id=csnowhill-doll-jacket-40587-v2 status=done turns=2 usd=0.0014 tokens(read,write,in,out)=[5391, 6359, 6, 1177] model=claude-haiku-5-5 -->
# Snowhill Doll Jacket

{"item": {"name": "Snowhill Doll Jacket", "locale_id": 40587, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Piece of the Snowhill Pixie Doll collection (also listed under the Snowhill Human Doll section of the collection list)", "where": null, "price": null, "currency": null, "source": "locale:132307; wiki page 'Toys (Collections)'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Snowhill Doll Jacket' is locale 40587, 3 definition ids (3371, 3419, 3507), slot 0, no model files, no coin store price", "source": "locale:40587; client definition pack"},
  {"claim": "Client description 'This item can be added to the Snowhill Pixie Doll Collection' is locale 132307 (corrected from the pack's nonexistent locale:169059737)", "source": "locale:132307"},
  {"claim": "Wiki Toys (Collections) lists '[Snowhill] [Doll] [Jacket]' under both the Snowhill Human Doll and Snowhill Pixie Doll sections", "source": "wiki page 'Toys (Collections)'"},
  {"claim": "The 10/22/13 weekly update 'Dolly [Doll]' mention is a different item and is not used as a source", "source": "wiki page 'User blog:Soe amnerys/Weekly Update - 10/22/13'"},
  {"claim": "No vendor stock, quest, drop, event, or video evidence found for this item; no coin store price in client or repo stores", "source": "repo search (stores.json, vendors.json) with no match; client definition coin_store_prices empty"}
 ],
 "confidence": 0.35,
 "open": [
  "Acquisition route beyond collection membership is not established. Snow Days/Toys prize wheel or Marketplace releases are plausible but no source names this jacket.",
  "Price unknown: no coin store price in client or repo, no wiki price.",
  "Retired status unknown: no source says when it was last available.",
  "Kind is 'collection' per the first pass and description, though the item is a doll outfit piece worn by the doll.",
  "Pack's locale:169059737 citation was wrong and is replaced by locale:132307."
 ],
 "critique_resolution": "Evidence critique (score 3): fixed the id citation to locale:132307 and verified it; verified the wiki Toys (Collections) listing. The critique's note that no price/source exists is accepted; item is wireable only as a collection-membership entry."}
