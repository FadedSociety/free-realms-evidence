<!-- fleet job=citem-infer id=camplifier-tempered-circle-shard-4527-v1 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[9349, 8538, 8, 2218] model=claude-haiku-5-5 -->
# Amplifier Tempered Circle Shard

{"item": {"name": "Amplifier Tempered Circle Shard", "locale_id": 4527, "kind": "other"},
 "sources": [
  {"type": "prize_wheel", "detail": "Daily Wheel, Shards wedge (flair shard drop from the wheel)", "where": null, "price": null, "currency": null, "source": "wiki page: Amplifier Tempered Circle Shard (\"It is acquired from the Daily Wheel, from the Shards wedge.\")"},
  {"type": "vendor", "detail": "Unidentified coin store (store category 124); the store row lists purchase 50 coins, member price 45 coins, sell-back 5 coins", "where": null, "price": "50 (member price 45)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:14606 (item_id 65818); client definition coin_store_prices [50]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name is locale 4527 'Amplifier Tempered Circle Shard'; its cluster siblings are the Crafty (4523) and Battle (4525) Tempered Circle Shards and Merk quest lines (4524, 4526, 4528), so it belongs to the Merk shard set.", "source": "locale:4527; locale:4523; locale:4525; locale:4524; locale:4528"},
  {"claim": "Wiki: level 1 flair shard usable in any job; acquired from the Daily Wheel, Shards wedge; increases stars earned from battles; Cannot Trade.", "source": "wiki page: Amplifier Tempered Circle Shard"},
  {"claim": "Tooltip: Resell Value 5, Power 5, Stats +13, Cannot Trade, Required Level 1 Any Job.", "source": "image:item_tooltip, File:Amplifier Tempered Circle Shard item.jpg (wiki)"},
  {"claim": "Store data lists item 65818 in coin store category 124 at 50 coins, 10% member discount to 45, sell price 5 coins (matches tooltip resell value).", "source": "repo:prototype/osfr-tools/data/content/stores.json:14606"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin store vendor that sells item 65818 is not identified: stores.json only gives category 124 and no NPC/vendor name, so the vendor detail and zone are unknown.",
  "Whether the 50-coin store listing is live or was a historical sale is unverified; no wiki price or date was found for it. Live status is therefore 'unsure'.",
  "The Daily Wheel wedge source is a single wiki statement with no article, video or drop-rate confirmation; the wiki page's category tags (Flair Shard, BrawlWiki) do not name a retirement date.",
  "Retirement status not found in any source; retired left null.",
  "No critiques were carried in the pack, so none needed fixing."
 ]}
