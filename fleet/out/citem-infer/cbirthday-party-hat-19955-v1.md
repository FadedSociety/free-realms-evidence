<!-- fleet job=citem-infer id=cbirthday-party-hat-19955-v1 status=done turns=4 usd=0.0032 tokens(read,write,in,out)=[24935, 12135, 10, 2831] model=claude-haiku-5-5 -->
# Birthday Party Hat

{"item": {"name": "Birthday Party Hat", "locale_id": 19955, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing (Legacy CoinStoreItems, category 101), item 9091; purchase price 370 coins, member price 333 coins (10% member discount), sell-back 37 coins", "where": "Coin store", "price": "370 coins (member 333 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:2699 (item_id 9091, purchase_price_coins 370, member_price_coins 333, sell_price_coins 37)"},
  {"type": "event", "detail": "Birthday Bash (annual April event celebrating Free Realms launch day); party hats were event items, each party hat with its own Birthday T-Shirt. The sources do not name this specific hat as an event reward, so this is a category-level link.", "where": "Free Realms, April event", "price": null, "currency": null, "source": "wiki page 'Birthday Bash'; wiki page 'Events'; http://www.freerealms.com:80/article/detail.action?articleId=2099 ; http://www.freerealms.com:80/article/detail.action?articleId=1268"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Birthday Party Hat' is locale 19955; its description is 'It's not a party without a party hat.' (locale 19963). Definition 9091, head slot, one variant, model freestyle_<race>_<gender>_head_partyhat.adr.", "source": "locale:19955; locale:19963; client definition in pack"},
  {"claim": "Coin store record exists for item 9091 at 370 coins, member price 333 coins, sell-back 37 coins.", "source": "repo:prototype/osfr-tools/data/content/stores.json:2699"},
  {"claim": "Video frame shows the Birthday Party Hat in the inventory with Resell Value 37, Cannot Trade, Head slot, Adventurer job, as part of a set with Birthday Cake Hat and Balloon Bunny Ears Baseball Cap.", "source": "video:Qg7_4br2H80/00138.jpg"},
  {"claim": "Wiki Animated page names the '[Birthday] [Party] [Hat]' as a guild outfit item, consistent with it being a known party-era item.", "source": "wiki page 'Animated'"},
  {"claim": "Birthday Bash is an annual April event (launch day April 29, 2009) featuring party items and Cakenstein; party rewards included balloon weapons and a T-shirt for each party hat.", "source": "wiki page 'Birthday Bash'; articleId=2099; articleId=1268"}
 ],
 "confidence": 0.6,
 "open": [
  "The first-pass tag said source 'vendor'; no coin vendor stock list names this item (vendor_stock empty), so the coin store listing is treated as a Coin Shop sale instead of a coin vendor. The jev tag is not evidence.",
  "The Birthday Bash event link is category-level. No source confirms that this specific hat was a Birthday Bash event reward or which Birthday Bash quest or vendor gave it.",
  "The store record's category 101 is not mapped to a named shop in the repo, so the exact shop and whether it was sold in the Coin Shop vs a Legacy-only store is unconfirmed.",
  "Retired status and live availability are unverified. Nothing in the pack shows when the coin store listing was removed or if the hat returned in later Birthday Bash events.",
  "Cannot-trade flag and the 370/333 prices are from the Legacy store data and not confirmed against a live-era wiki page.",
  "No wiki article covers this item directly; the wiki Birthday Bash and Events pages mention party items but not the hat by name."
 ]}
