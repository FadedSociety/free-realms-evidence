<!-- fleet job=citem-infer id=csuper-spooky-flair-shard-16643-v1 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[3956, 5841, 6, 1826] model=claude-haiku-5-5 -->
# Super Spooky Flair Shard

{"item": {"name": "Super Spooky Flair Shard", "locale_id": 16643, "kind": "weapon"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace (SC Shop) during the annual Super Spooktacular event; wiki says it sells for 150 SC; article 2304 calls the Halloween flair shards 'sold in the Marketplace'", "where": "SC Shop / Station Cash Marketplace", "price": "150", "currency": "station_cash", "source": "wiki page 'Super Spooky Flair Shard'; wiki page 'Super Spooktacular'; http://www.freerealms.com:80/article/detail.action?articleId=2304"},
  {"type": "coin_shop", "detail": "Unverified coin store listing for item 2100 in our store data (purchase 900 coins, member price 810). The wiki does not name a coin shop for this item, and the store data does not say which store it belongs to, so this may be a data artifact.", "where": null, "price": "900 (member 810)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2100 (line 595)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Named 'Super Spooky Flair Shard', level 1 flair shard usable by any job, Cannot Trade, from the SC Shop during the annual Super Spooktacular at 150 SC", "source": "wiki page 'Super Spooky Flair Shard'"},
  {"claim": "Halloween flair shards Creepy Crawly and Super Spooky are sold in the Marketplace", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"},
  {"claim": "Super Spooktacular event introduced items in the Station Cash Marketplace (week 3, 10/15/13)", "source": "wiki page 'Super Spooktacular'"},
  {"claim": "Client item definition 2100 (locale 16643) has a store price of 900 coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 2100"},
  {"claim": "Client description 'Decorate your weapon with the spirit of Halloween.'", "source": "locale:16656"}
 ],
 "confidence": 0.6,
 "open": [
  "Price conflict: the wiki gives 150 SC (Station Cash), while our store data gives 900 coins. The wiki gives no coin-shop source, so the 900-coin price is unconfirmed. Treat it as a possible coin-shop listing until someone checks which store category 124 belongs to.",
  "Retirement is not stated anywhere. It was an annual event item, so it is probably no longer sold. Confirm the current status before relying on it.",
  "The wiki gives no exact sale dates for this shard. The Super Spooktacular week-3 introduction is for other items, so this shard's start date is not confirmed.",
  "The 'SC Marketplace' category tag and the 'SC Shop' phrase both point to Station Cash, but the wiki page lists no category tag for the Marketplace.",
  "Client shows a flair-slot item (slot 13), with no model files in the pack, so the visual was not checked."
 ]}
