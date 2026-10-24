<!-- fleet job=citem-infer id=csanctuary-birthday-cake-9396-v5 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[6474, 12616, 6, 2010] model=claude-haiku-5-5 -->
# Sanctuary Birthday Cake

{"item": {"name": "Sanctuary Birthday Cake", "locale_id": 9396, "kind": "consumable"},
 "sources": [{"type": "marketplace", "detail": "One of eight zone-specific Birthday Bash cakes sold on the Marketplace (Birthday Bash party set). The Sanctuary-to-9396 link is inferred from locale cluster order and is not stated per cake by any source read.", "where": "Marketplace", "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=1261 (\"eight cakes ... sold in the Marketplace\" for the party); http://www.freerealms.com/article/detail.action?articleId=2107 (eight zone-specific birthday cakes plus a bonus Boss Cake for buying all eight, sold on the Marketplace)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Sanctuary Birthday Cake' is locale 9396, in the 'Birthday Cake Samples' cluster 9391-9399 (one name per party zone). Client definition 7970, class 168, slot 0.", "source": "locale:9396; locale:9391; locale:9392-9399"},
  {"claim": "No coin store price in the client definition, and repo data/content/stores.json has no item_id 7970 entry (only unrelated ids such as 29396 and 79396 match the digits). So no coin-vendor source.", "source": "client definition in pack; repo:prototype/osfr-tools/data/content/stores.json (search for 7970)"},
  {"claim": "Articles 1261 and 2107 say the zone birthday cakes were sold on the Marketplace. Neither article text read names a currency or a price for the individual cake.", "source": "http://www.freerealms.com/article/detail.action?articleId=1261; http://www.freerealms.com/article/detail.action?articleId=2107"},
  {"claim": "The wiki labels the Boss Cake (not the zone cakes) as a Birthday Bash Station Cash Marketplace item that grants a boss illusion. This supports Station Cash only for the Boss Cake, not for the Sanctuary cake.", "source": "wiki Pumpkin Prince (Boss Cake section); wiki Stone Heart (Boss Cake section)"}
 ],
 "confidence": 0.35,
 "open": [
  "Currency for the Sanctuary cake is unknown. The wiki's Station Cash label is on the Boss Cake only. The earlier 'station_cash' claim was removed.",
  "No price for the Sanctuary cake was found in any source.",
  "The 9396 and definition 7970 identity with the Sanctuary cake is inferred from locale order and is not confirmed by a per-cake article line or client link.",
  "Sale window and end date are unknown. No source read says when the cake left the Marketplace, so retired is null and live is unsure.",
  "Removed from the earlier answer: the 'Free Realms Anniversary Celebration' and 'second anniversary party' event sources. They cite only locale 9396 and article summaries that do not say the cake was an event reward. Also removed: the articleId 1268 and 2099 claims (not verified) and locale 14419 and 30109. Locale 17807 is a placeholder and is excluded.",
  "No quest, enemy, crafting, or prize-wheel source found. wireable is false: the only source has no price and no quest, enemy or event tie. Keep it out of the builder's acquisition set until a price or per-cake listing is found.",
  "The wiki Cake page was not retrievable, so no currency label was confirmed from it."
 ]}
