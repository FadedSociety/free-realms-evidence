<!-- fleet job=citem-infer id=cstriped-sunglasses-6979-v3 status=nothing_found turns=2 usd=0.0020 tokens(read,write,in,out)=[5936, 9351, 6, 1601] model=claude-haiku-5-5 -->
# Striped Sunglasses

{"item": {"name": "Striped Sunglasses", "locale_id": 6979, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 2923 'Striped Sunglasses' exists: name locale 6979, description locale 6986 \"Zebras won't have nothing on you when you sport these.\", head slot 17, clothing class 1, model freestyle_<race>_<gender>_head_sunglasses.adr", "source": "locale:6979; locale:6986; client definition"},
  {"claim": "Store row for item 2923 carries purchase_price_coins 270, member_price_coins 243, no_sale true, sell_price_coins null, tint_group_id 2, and no price_provenance. A row with no_sale true and no vendor named is not evidence of a coin vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:769"},
  {"claim": "Lookup of 'Striped Sunglasses' across client, wiki, articles and video returns only the two locale lines above. No wiki page, article, or video names the item. Wiki hits for 'Striped' are unrelated Striped T-shirt and Striped Sandals.", "source": "lookup client/wiki/articles/video 'Striped Sunglasses'"},
  {"claim": "Repo search for item id 2923 in data/content finds only the stores.json row; no vendor, quest, drop, or recipe references it.", "source": "search repo prototype/osfr-tools/data/content '2923'"},
  {"claim": "The earlier vendor answer (Cragara, 270 coins, and a 99 SC Marketplace path) is withdrawn. Cragara comes only from sibling wiki pages Polkadot and Tiger Sunglasses, which give no price here and do not name Striped. The 99 SC price belongs to siblings 2922 and 2924, not 2923, and the row lacks the T638 tag.", "source": "critiques evidence and world lenses; stores.json:768-770"}
 ],
 "confidence": 0.2,
 "open": [
  "No evidenced acquisition source. The 270/243 coin figure is an unprovenanced store cost on a no_sale row, not a sale record. It should not be presented as a vendor price until a vendor is named.",
  "Vendor identity is unknown. Cragara is only inferred from sibling wiki pages and must be verified before it is listed.",
  "Station Cash Marketplace: no evidence for 2923. Siblings 2922 and 2924 carry the 99 SC price; 2923 does not.",
  "Retirement and live status are unknown. No source states either, and the row is no_sale true.",
  "Whether 2923 is a separate item or one tint of a shared Sunglasses model (tint_group_id 2) is not verified.",
  "Needs a direct check in the live client or a wiki page for Striped Sunglasses before any source is added."
 ]}
