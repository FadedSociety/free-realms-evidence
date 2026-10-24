<!-- fleet job=item-infer id=iassistant-chief-edward-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[4484, 11264, 6, 2058] model=claude-haiku-5-5 -->
# Assistant Chief Edward

{"item": {"name": "Assistant Chef Edward (NPC; recipe vendor, not an item)", "locale_id": 1206955417, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Assistant Chef Edward sells the Sizzling Snowberry Saute Recipe (chef level 10 recipe)", "where": "Snowhill, Lucca's Cafe", "price": null, "currency": null, "source": "locale:1521; locale:1548 (Requires chef level 10); locale:414512-414514; notes/Build Guides/Content/Jobs/Chef.md:228, 255; notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:79"},
  {"type": "vendor", "detail": "Assistant Chef Edward sells the Stainberry Chocolate Gumdrop Recipe", "where": "Snowhill, Lucca's Cafe", "price": null, "currency": null, "source": "locale:1524; locale:414515; notes/Build Guides/Content/Jobs/Chef.md:229, 255"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Wiki page is an NPC page: pixie in Snowhill, 'sells Chef Supplies'; no prices, no coin or Station Cash data.", "source": "https://freerealms.fandom.com/wiki/Assistant_Chief_Edward (rev 44920)"},
  {"claim": "Client spells the NPC 'Assistant Chef Edward' (ucdt 1206955417); wiki's 'Chief' is a misspelling.", "source": "notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:79, :214"},
  {"claim": "Client text says he sells recipes: 'Purchase recipes from Assistant Chef Edward in Snowhill.'", "source": "locale:414512"},
  {"claim": "Sizzling Snowberry Saute Recipe is sold by Assistant Chef Edward at Lucca's Cafe.", "source": "locale:414514; notes/Build Guides/Content/Jobs/Chef.md:228, 255"},
  {"claim": "Stainberry Chocolate Gumdrop Recipe is sold by Assistant Chef Edward at Lucca's Cafe.", "source": "locale:414515; notes/Build Guides/Content/Jobs/Chef.md:229, 255"},
  {"claim": "The '10' in the Chef.md recipe tables is the chef level gate ('Requires chef level 10', locale:1548), not a coin or Station Cash price, so no price is given.", "source": "locale:1548; notes/Build Guides/Content/Jobs/Chef.md:228-229"},
  {"claim": "Lorraine (Lakeshore) also sells both recipes, added 1 Oct 2013; this is a second vendor, not Edward.", "source": "notes/Build Guides/Content/NPCs/NPCs - Lakeshore.md:79; notes/Build Guides/Content/Jobs/Chef.md:262"}
 ],
 "confidence": 0.5,
 "open": [
  "The input is an NPC page, not an item. The sources above are the recipes he sells, which is the best-evidenced item-level tie. Confirm which item the builder wants and resubmit with its pack.",
  "No coin or Station Cash price for either recipe is in the pack or the repo notes. Price left null, not guessed.",
  "Edward's sale dates and whether the recipes are still sold are not evidenced; live is 'unsure'.",
  "Wiki says 'Chef Supplies'; the client and repo say recipes. The wiki line gives no item or price, so it is not used as a source.",
  "Vendor stock for Edward is not in vendor_stock (empty); the recipe links come from client text and Chef.md notes."
 ]}
