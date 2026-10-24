<!-- fleet job=citem-infer id=cstone-roundtop-coffee-table-147697-v3 status=nothing_found turns=4 usd=0.0018 tokens(read,write,in,out)=[18666, 6788, 10, 1494] model=claude-haiku-5-5 -->
# Stone Roundtop Coffee Table

{"item": {"name": "Stone Roundtop Coffee Table", "locale_id": 147697, "kind": "furniture"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Stone Roundtop Coffee Table' as locale 147697, description 'Stone Age Style', definition 36498, model hsg_coffee_table_04.adr.", "source": "locale:147697"},
  {"claim": "Store data has one row for item 36498: category 53, purchase 50 coins, member 45 coins, sell_price_coins null, no_sale true, source_tags L1,L2,L4,R2,L3,L3. The row is flagged as not for sale, so it is not evidence of a coin vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11969"},
  {"claim": "Wiki Items index lists the item as '[Stone] [Roundtop] [Coffee] [Table]'. The index shows no price, source, or retirement text.", "source": "wiki page:ns0 | Items"},
  {"claim": "Client text for the item sits in a cluster of Stone Age-style tables, locale 147692-147702. No line in the cluster names a source.", "source": "locale:147692-147702"},
  {"claim": "No vendor stock, quest, drop, event, video, or article in the pack names this item.", "source": "evidence pack"}
 ],
 "confidence": 0.2,
 "open": [
  "The only price (50 coins, member 45) comes from a no_sale: true row in store category 53. Category 53 is unnamed in every source, so it cannot be called the Coin Shop. Under the rules it is not a sale source. It is kept out of sources and noted here instead.",
  "No wiki page, article, video, or other answer confirms any acquisition route, so the item has no evidenced source.",
  "Retirement status is unknown. The no_sale flag does not say whether the item was ever sold.",
  "Store source_tags (L1, L2, L4, R2, L3, T633, R1) are not decoded, so the meaning of L3 and no_sale cannot be confirmed here.",
  "A holiday, promotion, or set-related source is possible given the Stone Age cluster, but nothing in the pack supports one."
 ]}
