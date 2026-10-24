<!-- fleet job=citem-infer id=cgreen-ramp-block-134820-v1 status=done turns=4 usd=0.0028 tokens(read,write,in,out)=[17111, 11347, 10, 2358] model=claude-haiku-5-5 -->
# Green Ramp Block

{"item": {"name": "Green Ramp Block", "locale_id": 134820, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store, category 147 (store vendor not named in repo data), definition 77227: 50 coins, member price 45 coins, no_sale true (cannot be sold back)", "where": null, "price": "50 coins (member 45 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:16558 item 77227"},
  {"type": "vendor", "detail": "Coin store, category 147 (store vendor not named in repo data), definition 77276: 400 coins, member price 360 coins, sell-back 40 coins", "where": null, "price": "400 coins (member 360 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:16607 item 77276"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Green Ramp Block' as locale 134820 with two definitions (77227, 77276) and a single block model hsg_block_ramp_01.adr", "source": "locale:134820"},
  {"claim": "Both definitions carry coin store purchase prices (50 and 400 coins) in the store data", "source": "repo:prototype/osfr-tools/data/content/stores.json item 77227 and item 77276"},
  {"claim": "Name sits in a set of colored block/ramp items (Black, Blue, Orange, Pink, Purple, Red, Teal Ramp; Teal, White, Yellow Flat Square) with no wiki page for any of them", "source": "locale:134815-134825; lookup of 'Ramp Block' found no wiki article for the 134xxx set"},
  {"claim": "Wiki Items page lists block-style building items but does not name Green Ramp Block", "source": "wiki page Items (lookup result)"},
  {"claim": "Item is a housing/building block (description 'Great for stackability.'), so kind is furniture", "source": "locale:134820 description and client definition"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor name and location for category 147 are not stated in the repo data; the coin-store sale is confirmed by price data but the vendor (and zone) is unknown.",
  "The two definitions carry different prices (50 coins no-sale vs 400 coins with sell-back 40). Which one is the player-facing Green Ramp Block, or whether they are tint/variant copies, is not established.",
  "No wiki, article, or video evidence names this item, so release dates, retirement, and any later availability (SC Marketplace, Coin Shop, event) are unverified.",
  "The jev_first_pass 'live: yes' is a hint only; the store data shows a sale price but does not show that the item is currently sold.",
  "No quest, drop, prize wheel, crafting, or collection source found."
 ]}
