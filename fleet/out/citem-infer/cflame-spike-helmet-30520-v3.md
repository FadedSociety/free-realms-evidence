<!-- fleet job=citem-infer id=cflame-spike-helmet-30520-v3 status=nothing_found turns=3 usd=0.0040 tokens(read,write,in,out)=[19557, 17869, 8, 3236] model=claude-haiku-5-5 -->
# Flame Spike Helmet

{"item": {"name": "Flame Spike Helmet", "locale_id": 30520, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store price 9453 coins (member 8507) on store rows for definitions 9281 (tint group 1) and 10888 (tint group 2); no vendor or NPC id on the row", "where": null, "price": "9453 coins (member price 8507 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 9281 (line 2706); repo:prototype/osfr-tools/data/content/stores.json item 10888 (line 3194); client definition coin_store_prices"},
  {"type": "coin_shop", "detail": "Coin store price 1761 coins (member 1584) on store row for definition 10929 (tint group 3); no vendor or NPC id on the row", "where": null, "price": "1761 coins (member price 1584 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 10929 (line 3215); client definition coin_store_prices"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Flame Spike Helmet' is locale 30520, also locale 42264; head armor (slot 1, class 25, model freestyle_<race>_<gender>_head_bikerhelmet.adr), three definitions 9281, 10888, 10929.", "source": "locale:30520; locale:42264; client definition (pack)"},
  {"claim": "Client description: 'This armor will level up with you, increasing your stat bonuses in combat.'", "source": "client definition (pack)"},
  {"claim": "Store rows for 9281 and 10888 list purchase_price_coins 9453 (member 8507); row 10929 lists 1761 (member 1584). All three are flagged no_sale:true, sell_price_coins null, and have no vendor or NPC id.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 2706, 3194, 3215"},
  {"claim": "The 9453 and 1761 store prices are not an explained sale: the rows have no price_provenance block (unlike item 10874 at line 3188, whose 9453 was reconstructed as a legacy coin cost and cleared because no coin vendor stocks it). Whether 9281/10888/10929 are legacy costs is unverified.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 2706, 3188, 3194, 3215"},
  {"claim": "Lookup of wiki, articles, video and client text finds no wiki page, article, or video naming the helmet; the only hits are client strings (locale:30520, 42264). Sibling cluster items (30519 Skull Strike Hoodie, 30521 Neon Blue Tiger Pauldrons, 30525 Oni Shoulderguard) also have no wiki or article sources.", "source": "lookup client/wiki/articles/video 'Flame Spike Helmet' OR cluster names"},
  {"claim": "No quest, drop, event, or vendor row in the repo names item ids 9281, 10888 or 10929 (search of the repo content for these ids found nothing outside the store file).", "source": "repo search (data/content)"},
  {"claim": "locale:150506 is a FLAG placeholder ('This is a ... item.') and is rejected as evidence.", "source": "locale:150506 (FLAG placeholder)"}
 ],
 "confidence": 0.2,
 "open": [
  "Both coin_shop entries rest only on store-row prices. Every row is no_sale:true with no vendor or NPC id, and no wiki, article, or video confirms a coin sale. The critiques asked to drop the coin_shop source; I kept it because the rule treats a client coin price as coin-vendor evidence, but it is weak and should be cleared if the store-row prices are shown to be legacy costs.",
  "The 9453 vs 1761 price split across tint groups is unexplained, and 10929 (tint group 3) is a different price tier from 9281/10888.",
  "Live status unsure: no retirement date is sourced. The first-pass 'live: yes' is a hint only. no_sale:true is not treated as a retirement signal.",
  "No drop, quest reward, event, prize-wheel, collection, or promotion source is evidenced. The biker/street cluster (30519-30525) has no sources, so a shared set or promotion origin is unconfirmed.",
  "Next steps: find the mapping from store category 101 to vendors; search quest, event and drop tables for ids 9281, 10888, 10929; check wiki history or forum for a biker-set promotion date."
 ]}
