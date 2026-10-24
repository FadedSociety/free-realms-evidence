<!-- fleet job=citem-infer id=cn-bermuda-shorts-pl-bermuda-shorts-8620-v2 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[5817, 9185, 6, 2276] model=claude-haiku-5-5 -->
# {n}Bermuda Shorts{pl="Bermuda Shorts"}

{"item": {"name": "Bermuda Shorts", "locale_id": 8620, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop vendor sale, Freestyle legs-slot clothing, sold to everyone at the regular price (wiki text 'available to everyone in the Coin Shop'; the wiki price fields were blank in the text lookup). Regular price 270 coins comes from the client definition coin_store_prices [270]; the stores.json rows with 270/243 (item_ids 47, 76, 82, 106, 108) are value matches, not confirmed to be this item.", "where": "Coin Shop", "price": "270 coins (regular)", "currency": "coins", "source": "client definition coin_store_prices 270 (definition pack); wiki page 'Bermuda Shorts' (ns0); repo:prototype/osfr-tools/data/content/stores.json:76-79 (value match only)"},
  {"type": "coin_shop", "detail": "Members' discount on the same Coin Shop item. 243 is the member price in the value-matched stores.json rows (270 less 10%), not a wiki-sourced member price.", "where": "Coin Shop", "price": "243 coins (members, 10% off, derived)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:76,78,79 (member_discount_percent 10, member_price_coins 243; value match)"},
  {"type": "other", "detail": "Level-3 level-up reward of Bermuda shorts reported by one player in a Ten Ton Hammer article. Anecdote, not a documented reward table.", "where": null, "price": null, "currency": null, "source": "http://www.tentonhammer.com:80/node/69806"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 8620 '{n}Bermuda Shorts{pl=\"Bermuda Shorts\"}'; 2901 is plain 'Bermuda Shorts'", "source": "locale:8620; locale:2901"},
  {"claim": "Locale 385536 reads 'This is a pair of Bermuda Shorts' (text exists; link to definition 427 etc. not verified; definition pack shows empty description)", "source": "locale:385536"},
  {"claim": "Client coin_store_prices lists 270 for this item", "source": "client definition pack"},
  {"claim": "Wiki item tooltip shows Resell Value 27, Cannot Sell, Cannot Trade, Required: All Jobs, You Own: 1", "source": "wiki image:item_tooltip 'Bermuda shorts code.jpg'"},
  {"claim": "Ten Ton Hammer article says a player got Bermuda shorts at level 3", "source": "http://www.tentonhammer.com:80/node/69806"},
  {"claim": "Charcoal Bermuda Shorts (locale 151297) is a separate item", "source": "locale:151297"}
 ],
 "confidence": 0.5,
 "open": [
  "Full wiki page 'Bermuda Shorts' text was not re-read in this pass; the blank regular/member price fields and the 'Promotional Ad' section were not verified. Prior answer's claims about them are not confirmed.",
  "The 270/243 store prices are value matches on stores.json rows keyed to other item_ids (47, 76, 82, 106, 108). Nothing links those rows to this item's 68 definition ids (427, 979-983, 2184, 15722, 17988-17991). Confirm the store row before trusting the price.",
  "Promotion source removed: the pack gave no price, date or distribution evidence for a darkmatter promo pair. Re-add only if the full wiki Promotional Ad section names the promotion and how the pair was obtained.",
  "Which of the 68 tints/races were sold in the Coin Shop is unknown; the darkmatter (black) tint and a Guild Outfit dark blue variant are mentioned in the prior answer but not verified here.",
  "Retirement not evidenced. 'Cannot Sell' is a per-item trade rule, not a retirement signal. Wiki present tense suggests live as of the wiki, but no date or closure evidence was found, so live is left as unsure.",
  "Locale 385536 description link to the definition is unverified.",
  "'Mystery Reward' lines (8615, 8617) are flagged duplicates and were not used."
 ]}
