<!-- fleet job=citem-infer id=cbrawler-s-ring-of-regeneration-i-130989-v3 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[6081, 12579, 6, 2172] model=claude-haiku-5-5 -->
# Brawler's Ring of Regeneration I

{"item": {"name": "Brawler's Ring of Regeneration I", "locale_id": 130989, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Miesha (NPC 9500000408), Sells list; wiki stock description lists 'Ring of Regeneration I' among her Sells items", "where": "Merry Vale (merry_vale.json)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Miesha (Sells, rev 2023-05-28T15:31:36Z) as mirrored in repo:prototype/osfr-tools/data/content/vendors.json:22645-22749 (item_id 75245, listed_as \"Brawler's Ring of Regeneration I\", stock_completeness \"partial_evidence_reference\")"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines Brawler's Ring of Regeneration I with name locale 130989 (item 75245, slot 8, class 25, one definition).", "source": "locale:130989; client definition"},
  {"claim": "Miesha's wiki Sells list (rev 2023-05-28) is recorded in the repo mirror with item 75245 under this exact name; the wiki stock description names 'Ring of Regeneration I'. The live wiki page was not re-fetched; the mirror is the only direct check.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:22645-22749"},
  {"claim": "The 750 / 675 member / 75 sell figures are reconstructed reference prices from our store data, labelled 'reference price, not captured NPC quote'. They are not a price shown on the wiki or quoted from Miesha, so no coin price is sourced for this vendor sale.", "source": "repo:data/content/stores.json item 75245 (line 17306, price_provenance reconstructed); vendors.json:22713-22717 price_basis"},
  {"claim": "The 'coin_store_prices [750]' field in the evidence pack is derived from our store data, not an independent client read, so it does not corroborate the price.", "source": "evidence pack client definition; brief says coin price comes from our store data"},
  {"claim": "Sibling Brawler's Ring of Regeneration V has a wiki tooltip showing Required: Level 16, Brawler. This is a sibling item and does not establish this item's requirements.", "source": "wiki image:item_tooltip \"Brawler's ring of regeneration v.jpg\""},
  {"claim": "No Brawler Prize Wheel, Coin Shop, quest, or drop source naming this item was found. Archer ring prize-wheel and Coin Shop entries refer to sibling items.", "source": "wiki snippets noted in pack; not re-verified"}
 ],
 "confidence": 0.35,
 "open": [
  "Price unverified: the 750 / 675 / 75 coin figures are reconstructed reference values in repo stores.json, not a captured Miesha quote or a live wiki price. The vendor source therefore has price null. Needs a captured Miesha price or live wiki check.",
  "Live status rests on the wiki Miesha Sells revision dated 2023-05-28 via the repo mirror. The live wiki was not re-fetched, so live is 'unsure' and retired is unknown.",
  "The stock listing is a partial_evidence_reference in the repo mirror; the item name appears only in that mirrored row and the wiki description's abbreviated 'Ring of Regeneration I'.",
  "The pack's vendors_unresolved.json citation (line 4379) was not checked in this pass.",
  "wireable: false until a captured or live price is found."
 ],
 "wireable": false}
