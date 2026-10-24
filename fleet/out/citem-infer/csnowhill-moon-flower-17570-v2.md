<!-- fleet job=citem-infer id=csnowhill-moon-flower-17570-v2 status=done turns=3 usd=0.0030 tokens(read,write,in,out)=[18394, 13857, 8, 2184] model=claude-haiku-5-5 -->
# Snowhill Moon Flower

{"item": {"name": "Snowhill Moon Flower", "locale_id": 17570, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name is locale 17570 'Snowhill Moon Flower'; client definition 9202 has no coin store price, model, or vendor stock.", "source": "locale:17570; client definition (coin_store_prices empty)"},
  {"claim": "Its description says it can be added to the Exotic Snowhill Flowers Collection; the collection is locale 17581 'Exotic Snowhill Flowers', with description 'A collection of rare Snowhill flowers. Legend says only 1 out of every 9 flowers found is this rare.' (locale 17590). Locale 132500 binds the item to this Exotic collection.", "source": "locale:17570, 17581, 17590, 132500"},
  {"claim": "The wiki's List of Collections page has an Exotic [Snowhill] [Flowers] section listing Exotic Snowhill Tulips/Orchids/Carnations/Roses/Daisies/Lilies/Sunflowers/Daffodils and an 'Exotic [Snowhill] [Flower]' entry, plus a 'Rare [Snowhill] Flowers' section. This corrects the critique: the snippet does show the Exotic Snowhill entry. The Moon Flower is not named individually on that page.", "source": "wiki page: List of Collections (lookup snippet)"},
  {"claim": "Rare Snowhill Flowers is a sibling collection (locale 16965; 132280 'This item can be added to the Rare Snowhill Flowers Collection').", "source": "locale:16965, 132280"},
  {"claim": "Snowhill flowers are picked in the field: quest objective 'Pluck a flower from Snowhill' and 'Use the launch pads to jump your way to the flower in Snowhill' (quest 'A Bundle of Love'). This shows the flower-picking mechanic exists, but nothing ties this specific flower to that quest or to a drop.", "source": "locale:427060, 427061"},
  {"claim": "An 'Exotic Snowhill Flower' item also exists (locale 387767), which may be the actual pickup form, but its source is not evidenced.", "source": "locale:387767"}
 ],
 "confidence": 0.25,
 "open": [
  "No acquisition source is evidenced for Snowhill Moon Flower. Snowhill flower picking (quest 'A Bundle of Love', locale 427060) and the Exotic Snowhill Flower item (387767) suggest a field-gathering mechanism, but no node, drop table or reward was found in repo, wiki or video. Needs a wiki page for the Exotic Snowhill Flowers collection or gathering-node data.",
  "The collection's completion reward and price are not in the evidence.",
  "Retired or live status is unconfirmed. The first-pass 'live: yes' is a hint only and is not supported by a source.",
  "The wiki's List of Collections page lists the Exotic Snowhill flowers but does not name the Moon Flower individually; the pack's 'Snowhill Orchids' parallel line (132497) and sibling cluster (17565-17575) were not traced to sources.",
  "Repo search for 'snowhill', '9202' and '17570' found no store, drop or vendor data for this item."
 ]}
