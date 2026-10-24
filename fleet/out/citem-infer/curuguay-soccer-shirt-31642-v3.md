<!-- fleet job=citem-infer id=curuguay-soccer-shirt-31642-v3 status=nothing_found turns=2 usd=0.0021 tokens(read,write,in,out)=[6015, 9173, 6, 1758] model=claude-haiku-5-5 -->
# Uruguay Soccer Shirt

{"item": {"name": "Uruguay Soccer Shirt", "locale_id": 31642, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 16325: chest slot (slot 3), class 143, one definition, model freestyle_<race>_<gender>_chest_shortslvshirt.adr", "source": "locale:31642 client definition in evidence pack"},
  {"claim": "Name and description: 'Uruguay Soccer Shirt' / \"Show support of your favorite country's team!\"", "source": "locale:31642; locale:31643"},
  {"claim": "Store-table row exists: item 16325, category 103, tint group 1, purchase 50 coins, member 45 coins, sell_price_coins null, no_sale true. No vendor or shop is named in the row.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6637 (re-read and confirmed)"},
  {"claim": "Neighbouring category-103 rows 16308-16325 share the same 50-coin no_sale pattern, so the row is a block of non-sold entries, not a vendor stock listing.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6630-6637"},
  {"claim": "Sibling 2010 FIFA World Cup shirts (Brazil, Spain, Italy, Mexico, Korea DPR, New Zealand Soccer Shirt) are wiki pages describing them as unobtainable chest items acquired through the Station Cash Marketplace during the 2010 FIFA World Cup. They are not evidence for Uruguay.", "source": "wiki: Brazil Soccer Shirt; Spain Soccer Shirt; Italy Soccer Shirt; Mexico Soccer Shirt; Korea DPR Soccer Shirt; New Zealand Soccer Shirt"},
  {"claim": "No wiki page, article, or video mentions Uruguay Soccer Shirt (lookup returned no matches).", "source": "lookup, wiki/articles/video, query 'Uruguay Soccer Shirt'"},
  {"claim": "The first-pass tag (live yes, event guess) is a hint only and was not used.", "source": "evidence pack first-pass tag"}
 ],
 "confidence": 0.15,
 "open": [
  "No evidenced acquisition source. The 50-coin store row (stores.json:6637) is marked no_sale: true with no vendor, so it is not a sale source and was dropped from sources.",
  "Station Cash Marketplace origin is a sibling-pattern hypothesis only (other 2010 World Cup shirts on the wiki). Needs a Uruguay-specific source (wiki page, Station Cash listing, or client/store data) before it can be listed.",
  "Retired status unknown. Siblings are Category:Unobtainable, which suggests the group is retired, but no source states it for Uruguay.",
  "Live status unknown; the pack's live:yes is unsupported.",
  "Wireable: false. The builder cannot set an acquisition from current evidence.",
  "Only one definition and one model template; race/gender variants not checked beyond the template."
 ]}
