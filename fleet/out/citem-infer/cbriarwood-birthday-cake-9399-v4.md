<!-- fleet job=citem-infer id=cbriarwood-birthday-cake-9399-v4 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6806, 8665, 6, 1912] model=claude-haiku-5-5 -->
# Briarwood Birthday Cake

{"item": {"name": "Briarwood Birthday Cake", "locale_id": 9399, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "One of eight zone-specific birthday cakes sold on the Marketplace for the Free Realms second-anniversary party (2011). Membership of Briarwood in the set is inferred from the client name cluster (locale 9392-9399) and the eight party zones; no source names this cake individually. Collecting all eight cakes grants a free Boss Birthday Cake (locale 30109), which is a different item.", "where": "Marketplace (second-anniversary party)", "price": null, "currency": null, "source": "refs:articles/facts.json:30878-30885 (article-2107 fact: 'Eight zone-specific birthday cakes are sold on the Marketplace'); refs:articles/facts.json:15088 (Briarwood is a party zone); locale:9399; locale:14419"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Briarwood Birthday Cake' is locale 9399 (definition 7973, class 168), one of eight zone cakes locale 9392-9399 (Shrouded Glade, Seaside, Snowhill, Merry Vale, Sanctuary, Wugachug, Blackspore Swamp, Briarwood).", "source": "locale:9392-9399; client definition 7973"},
  {"claim": "Article 2107 fact: eight zone-specific birthday cakes are sold on the Marketplace, can be placed anywhere, and each has a different effect when eaten. The fact row is a generic 'Birthday Cake' entry (locale 9391) with a Portuguese quote; it does not name individual cakes.", "source": "refs:articles/facts.json:30878-30885"},
  {"claim": "The party was held in eight zones including Briarwood.", "source": "refs:articles/facts.json:15085-15093 (article-2107)"},
  {"claim": "Collecting all eight area-themed birthday cakes gives the Boss Birthday Cake free.", "source": "locale:14419; locale:30109"},
  {"claim": "The party ended May 18, 2011 per the article summary, which suggests the cake is no longer sold; this is inference only.", "source": "refs:articles/articles.json:17120 (article-2107 summary)"}
 ],
 "confidence": 0.35,
 "open": [
  "Price is unsourced. No Marketplace listing or price for this specific cake was found.",
  "Currency is unsourced. Article 2107 says only 'Marketplace'. Station Cash is not evidenced for this cake; the wiki's Birthday Bash Station Cash line names only the Boss item.",
  "Briarwood's membership in the eight-cake Marketplace set is inferred, not named in any source.",
  "Retirement is inferred from the party end date (May 18, 2011); no source states this cake was retired. retired is null.",
  "Placeholder locale 17810 ('Briarwood Birthday Cake Sample') was dropped as evidence. Locale 9391 is a generic row, not this cake's name.",
  "Consumables.json transform/BossCake details and the transform ability were dropped as unverified in refs.",
  "No quest, enemy drop, crafting, vendor, or coin-shop source is evidenced. Not wireable until a per-cake listing or price is sourced."
 ]}
