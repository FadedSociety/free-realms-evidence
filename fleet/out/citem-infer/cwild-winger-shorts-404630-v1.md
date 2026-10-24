<!-- fleet job=citem-infer id=cwild-winger-shorts-404630-v1 status=nothing_found turns=6 usd=0.0057 tokens(read,write,in,out)=[68330, 25996, 14, 3454] model=claude-haiku-5-5 -->
# Wild Winger Shorts

{"item": {"name": "Wild Winger Shorts", "locale_id": 404630, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Wild Winger Shorts' is locale 404630; the Elite Pink and Elite Black variants are 404635 and 404636.", "source": "locale:404630, locale:404635, locale:404636"},
  {"claim": "Wild Winger is one of the Soccer Star gear sets (base, Elite Black, Elite Pink tiers) with Shorts as a slot; the set is client-only, with no item-to-vendor table decoded.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md:193-228 (rows 22-24, [client])"},
  {"claim": "The Soccer Star gear vendor is Fred Futbol at Snowhill Soccer Field, but his stock and prices were not seen.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md:42 (video and title string 2614216159)"},
  {"claim": "The pack's 'coin_store_prices' [750, 752] do not tie to this item. In repo stores.json, 750 and 752 are price values, not item ids. Definition ids 62200-62213 are absent from stores.json except 62205 and 62206, which list 9453 coins (category 104, same as other unnamed 62xxx items). No mapping ties those ids to the Wild Winger definitions.", "source": "prototype/osfr-tools/data/content/stores.json:14556-14557; repo search for 6220x/6221x"},
  {"claim": "No vendor in vendors.json stocks Wild Winger Shorts; the search for the name returned no hit. The wiki and articles have no page or fact for the name.", "source": "repo search 'Winger'; lookup wiki/articles 'Wild Winger Shorts' (no matches)"}
 ],
 "confidence": 0.15,
 "open": [
  "No verified acquisition source. The likely source by set name is the Snowhill 'Soccer Star Gear' vendor (Fred Futbol), but its stock and prices are unseen, so this is not listed as a source.",
  "The pack's coin_store_prices [750, 752] are prices, not item ids. Coin price for this item is unknown. Store items 62205/62206 (9453 coins) are unmapped to this item.",
  "Mapping of definition ids 62200-62213 to store/vendor item ids is missing; the set's clothing vendor row needs a catalogue join.",
  "Whether the item is live or retired is unknown (no wiki or article source). The first-pass 'live: yes' is a hint only.",
  "Elite Black and Elite Pink variants (404635/404636) are not separately sourced."
 ]}
