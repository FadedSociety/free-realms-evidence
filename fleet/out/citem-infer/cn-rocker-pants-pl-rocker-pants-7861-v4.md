<!-- fleet job=citem-infer id=cn-rocker-pants-pl-rocker-pants-7861-v4 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[6120, 6861, 6, 1507] model=claude-haiku-5-5 -->
# {n}Rocker Pants{pl="Rocker Pants"}

{"item": {"name": "Rocker Pants", "locale_id": 7861, "kind": "clothing"},
 "sources": [
  {"type": "other", "detail": "TCG Virtual Reward: unobtainable (trade only). Found only in physical Trading Card Game packs, which the wiki says are no longer produced. Not in normal in-game packs.", "where": null, "price": null, "currency": null, "source": "wiki page 'Rocker Pants' (Category:Virtual Rewards)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name '{n}Rocker Pants{pl=\"Rocker Pants\"}' (locale 7861), description 'Dresses you up in rock and roll pants!', client definition 2615, slot 4, class 1, model freestyle_<race>_<gender>_legs_skinnylegpants.adr", "source": "locale:7861; client definition id 2615"},
  {"claim": "Wiki: Rocker Pants are unobtainable (trade only) TCG Virtual Rewards; not in normal in-game packs; in physical TCG packs, which are no longer produced", "source": "wiki page 'Rocker Pants'"},
  {"claim": "Packaging art 'Rocker pant.jpg' carries the same name and description line, labelled TOYWIZ", "source": "wiki image 'Rocker pant.jpg'"},
  {"claim": "Client definition 2615 carries coin_store_prices [270]; a stores.json row for item 2615 shows 270 coins / 243 member / 27 sell. No vendor, zone or dated sale was found, so this is an unresolved conflict with the trade-only wiki wording, not a sourced sale.", "source": "client definition id 2615; repo:data/content/stores.json item 2615 (line 690)"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin store price 270 (client coin_store_prices and stores.json:690) conflicts with the wiki's trade-only status. No vendor, zone or dated listing confirms a sale, so it is not listed as a source. Needs a store-page or vendor check before it is treated as a coin sale.",
  "Retired is null. The wiki's 'unobtainable' wording and 'packs no longer produced' describe the packs; no dated retirement notice for the item was found.",
  "No Station Cash price found.",
  "The 'one item for one character' redemption detail from the earlier answer is not in the wiki text and was dropped.",
  "Repo file read of data/content/stores.json failed ('not a file') when re-checking lines 686-696, so the row was not re-read in this pass; the store row claim rests on the earlier answer's citation.",
  "Hipster Pants variant claim from the earlier answer was not re-checked and is not used here."
 ]}
