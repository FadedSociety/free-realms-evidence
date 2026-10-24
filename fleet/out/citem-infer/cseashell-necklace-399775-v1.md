<!-- fleet job=citem-infer id=cseashell-necklace-399775-v1 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[9542, 8293, 8, 2249] model=claude-haiku-5-5 -->
# Seashell Necklace

{"item": {"name": "Seashell Necklace", "locale_id": 399775, "kind": "clothing"},
 "sources": [
  {"type": "event", "detail": "Seaside Postman's weekly Merry Vale contest prize: 'The prize this week is a seashell necklace made by Enaine in Seaside!' Player sorts the mail entries and picks a winner; the winner receives the necklace, and Enaine's dialog says it arrives broken and must be returned for a new one.", "where": "Merry Vale / Seaside", "price": null, "currency": null, "source": "locale:117168 (Seaside Postman: And the Winner Is...); locale:117186 (Seaside Enaine)"},
  {"type": "vendor", "detail": "Coin store sale listed in the client definition (store item id not resolved; no matching entry found in repo stores.json for definition ids 15721/16030/59895)", "where": "coin store (unresolved)", "price": "270", "currency": "coins", "source": "client definition coin_store_prices [270]; repo:prototype/osfr-tools/data/content/stores.json (no matching item id found)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Seashell Necklace' is locale 399775, flavor text locale 399950; slot 6 (shoulders), 37 definitions across 12 definition ids, model freestyle_<race>_<gender>_shoulders_shellnecklace.adr", "source": "client definition; locale:399775; locale:399950"},
  {"claim": "Necklace is a weekly contest prize made by Enaine in Seaside, awarded through Merry Vale mail contests", "source": "locale:117168; locale:117186"},
  {"claim": "Client has a coin store price of 270 for one definition", "source": "client definition coin_store_prices [270]"},
  {"claim": "Earlier client line locale:151329 'Seashell necklace' is a non-tagged duplicate name string", "source": "locale:151329"}
 ],
 "confidence": 0.4,
 "open": [
  "No wiki page, images, article facts or video cover this item; no retired/live date found.",
  "The 270-coin store price is not tied to a store item id: the pack gives no stores.json item id and none of the definition ids matched stores.json. Verify which store item carries this necklace before keeping the coin_shop/vendor line.",
  "Weekly contest prize: the contest's run dates, whether it is still running, and whether the necklace was also sold in a shop are unknown. Check Merry Vale mail contest records.",
  "Enaine's 'broken necklace' dialog (locale:117186) suggests a repair/replacement step; not verified as a separate source.",
  "The first-pass tag 'vendor' is only a hint; the contest-prize source is the better-supported one."
 ]}
