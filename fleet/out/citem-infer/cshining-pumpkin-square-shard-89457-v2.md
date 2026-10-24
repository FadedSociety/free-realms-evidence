<!-- fleet job=citem-infer id=cshining-pumpkin-square-shard-89457-v2 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[4836, 15790, 6, 2026] model=claude-haiku-5-5 -->
# Shining Pumpkin Square Shard

{"item": {"name": "Shining Pumpkin Square Shard", "locale_id": 89457, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin store vendor; stores.json category 121 has no vendor key, so the NPC and shop are not named in our data", "where": null, "price": "1236 coins (member price 1112 coins with 10% member discount; sell value 123 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 10448 (line 3075); locale:89457"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Shining Pumpkin Square Shard', definition id 10448, slot 12, class 67, no description text", "source": "locale:89457; client definition 10448"},
  {"claim": "Coin store row for item 10448 (category 121): purchase 1236 coins, member discount 10%, member price 1112, sell price 123, not no-sale. Source tags listed in the row are L1/L2/L4/R2/T633/R1; the row does not say what those tags mean or which store they came from.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 3075"},
  {"claim": "Sibling rows in category 121 at 1236 coins (member 1112, sell 123): items 10435, 10436, 10437 (lines 3064-3066) and others in the 10435-10448 run. Items 10425-10430 and 10442-10444 in the same category are 640 coins (member 576, sell 64), so the 1236 price is not shared by the whole block.", "source": "repo:stores.json lines 3058-3066, 3070-3075"},
  {"claim": "Client text places this shard next to Pulsing Pumpkin, Shining Honey, Shining Ocean Square Shards and Faded Ocean Ring, which share the same naming pattern", "source": "locale:89452, locale:89453, locale:89455, locale:89456, locale:89462"},
  {"claim": "No wiki page, article, image or video names this item; no other answer names it", "source": "lookup over client, wiki and articles returned only the client line locale:89457"}
 ],
 "confidence": 0.4,
 "open": [
  "The coin vendor is not identified. Need the Legacy CoinStoreItems or Stores source (or an NPC/shop link for category 121) to name the seller and location.",
  "Only the legacy store row supports the 1236-coin price. No wiki or article price confirms it, so there is no second price to compare for a sale.",
  "Live status is unsure: the store row exists, but no source confirms the item was sold in a live period or when it stopped.",
  "The item's theme (the 'Pumpkin' family) is not tied to any event or holiday by any source; the Super Spooktacular link is not evidenced.",
  "The item is a Square Shard with class 67; its exact function (power/shard type) is not stated by any source, so no kind beyond 'other' is claimed.",
  "The critique's 'Power-type' label and the 'carried from the Legacy coin store' gloss were removed as unsupported. The critique's correction on sibling prices is applied in evidence item 3."
 ]}
