<!-- fleet job=citem-infer id=cformal-doll-shirt-40604-v1 status=done turns=7 usd=0.0039 tokens(read,write,in,out)=[60023, 15544, 16, 2695] model=claude-haiku-5-5 -->
# Formal Doll Shirt

{"item": {"name": "Formal Doll Shirt", "locale_id": 40604, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Formal Doll Shirt' is locale 40604; its description reads 'This item can be added to the Formal Pixie Doll Collection' (locale 294372632 / 132309 in the client text table).", "source": "locale:40604; locale:132309"},
  {"claim": "The wiki's Toys (Collections) page lists 'Formal Doll Shirt' as a piece of the Formal Pixie Doll collection (Formal Doll Cap, Jacket, Shirt, Dress, Accessories, Gloves, Shoes, Boots), and the same piece also appears under the Formal Queen Doll set.", "source": "wiki: Toys (Collections); wiki: List of Collections (lists 'Formal Pixie Doll' and 'Formal Queen Doll')"},
  {"claim": "The wiki says the reward for completing the Formal Pixie Doll collection is the 'Pixie Formal Doll' item, not the shirt.", "source": "wiki: Toys (Collections)"},
  {"claim": "The client has two definitions of the shirt (ids 3388 and 3524), both slot 0 and class 0, with no models and no coin store price, so no coin vendor sale is evidenced.", "source": "client definition in the evidence pack; repo:data/content/stores.json has no entry for these ids"},
  {"claim": "Client text 'Formal Doll Shirt' appears in both ugdt and ucdt string tables, consistent with a single named item with variants.", "source": "client locale data (en_us_data.dat)"}
 ],
 "confidence": 0.5,
 "open": [
  "No acquisition source found for the Formal Doll Shirt itself. The wiki lists it only as a collection member; the completion reward is the 'Pixie Formal Doll', and no vendor, quest, drop, or promotion names the shirt.",
  "No wiki article, video frame, article fact, or other answer names this shirt, and no coin vendor stocks it. Do not assign a vendor, coin price, or drop without new evidence.",
  "The pack lists 'Formal Pixie Doll Collection' as the collection; the wiki names it 'Formal Pixie Doll'. The item is probably a collection-only piece, but that is inferred from the description and the wiki list, not from a source saying how it is obtained.",
  "Live status is inferred from the first-pass tag and wiki listing; no retirement or unobtainability date is recorded in the sources."
 ]}
