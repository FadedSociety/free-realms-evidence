<!-- fleet job=citem-infer id=cflame-spike-helmet-30520-v1 status=done turns=4 usd=0.0035 tokens(read,write,in,out)=[19804, 13496, 10, 3264] model=claude-haiku-5-5 -->
# Flame Spike Helmet

{"item": {"name": "Flame Spike Helmet", "locale_id": 30520, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "coin store listing for the helmet's tint variants (store item ids 9281 and 10888); the store file gives no vendor or NPC id for these rows, so the seller is unknown", "where": null, "price": "9453 coins (member price 8507 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 9281 (line 2706, tint 1) and item 10888 (line 3194, tint 2); both rows are flagged no_sale:true"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is 'Flame Spike Helmet' (locale 30520; also 42264), with a placeholder description line at 150506 and the standard description 'This armor will level up with you, increasing your stat bonuses in combat.'", "source": "locale:30520, locale:42264, locale:150506"},
  {"claim": "Definition ids 9281, 10888, 10929; slot 1 (head); armor class 25; model freestyle_<race>_<gender>_head_bikerhelmet.adr", "source": "client definition (pack)"},
  {"claim": "Store rows for the helmet's variants carry a 9453-coin price, and both are marked no_sale:true, which suggests they are no longer sold in the coin store", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 2706 and 3194"},
  {"claim": "The 1761-coin price in the pack does not match any store row for definition 9281, 10888 or 10929; the matching 1761 rows (e.g. item 9284, 10879, 10911) are other items", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 2708, 3190, 3203"},
  {"claim": "Sibling items in the same client cluster (Skull Strike Hoodie 30519, Neon Blue Tiger Pauldrons 30521, Horned Mask 30524, Oni Shoulderguard 30525) have no wiki article, vendor rows, or quest text in the pack", "source": "locale:30519-30525 (pack client_cluster)"},
  {"claim": "No wiki page, article, or video frame names the Flame Spike Helmet; searches returned only an unrelated user page mentioning a horned mask", "source": "lookup wiki/articles/video, no matches for 'Flame Spike Helmet'"}
 ],
 "confidence": 0.35,
 "open": [
  "The seller is not identified: the store rows have no vendor or NPC id, so the coin shop entry is a price record, not a confirmed vendor. Need the store-to-vendor mapping for category 101 to name the vendor and zone.",
  "Live status conflicts: the first-pass tag says live 'yes', but both store rows are no_sale:true. I marked it 'unsure'. Need a wiki or forum date for when the helmet was last sold.",
  "The 1761-coin price in the client definition is unexplained: no store row for definition 10929 or 9281/10888 carries it. Needs a check of how the client's store price list was built.",
  "No evidence for the set or promotion the helmet belongs to (the cluster of 30519-30525 looks like one biker/street set). Could be a Station Cash, event, or prize-wheel item; no source found.",
  "Tint variants: 9281 is tint group 1 and 10888 is tint group 2. Whether both colours were sold separately, or the helmet has a third variant (10929 has no store row), is not established.",
  "The placeholder description at 150506 is generic and should not be used as the real description."
 ]}
