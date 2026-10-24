<!-- fleet job=citem-infer id=cbeaming-celestial-square-shard-86266-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5533, 7330, 6, 2097] model=claude-haiku-5-5 -->
# Beaming Celestial Square Shard

{"item": {"name": "Beaming Celestial Square Shard", "locale_id": 86266, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Reference coin-store catalogue row, store item 22275 (category 121, source tags L1, L2, L4, R2, T633, R1). Shop/vendor name for category 121 not resolved in repo.", "where": "coin store (category 121; shop name unresolved)", "price": "1780 coins (member price 1602 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:6690 (item 22275); the catalogue is derived from Legacy CoinStoreItems and is unverified against a real client transaction (notes/Research/Coin Shop.md lines 29-33)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is locale 86266 'Beaming Celestial Square Shard'; it sits in a cluster of 11 Square Shard names (Shimmering/Beaming/Blinding x Infernal/Eternal/Celestial/Ethereal, plus Brittle/Heavy/Solid/Burning/Glowing/Pulsing/Shining Celestial).", "source": "locale:86266; client cluster locale:86261-86271"},
  {"claim": "stores.json lists item 22275 in category 121 with purchase_price_coins 1780, member_discount 10%, member_price 1602, sell_price 178.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6690"},
  {"claim": "The 1780 price is a single row value, not a shared tier: category 121 rows carry mixed prices (3600, no-sale, 540, 866, 1780, 3600).", "source": "repo:prototype/osfr-tools/data/content/stores.json item 22260-22280 range"},
  {"claim": "Sell-back 178 is the server's policy value (max(1, Cost//10)), not an observed client value.", "source": "notes/Research/Coin Shop.md lines 36-41"},
  {"claim": "A sibling Square Shard, Briarheart Bandage Square Shard, is documented on the wiki as acquired by redeeming a Trading Card Game virtual reward (series 2). This is sibling evidence only; nothing ties it to the Beaming Celestial variant.", "source": "wiki page: Briarheart Bandage Square Shard; wiki file page File:Briarheart bandage square shard tcg.png"},
  {"claim": "Briarheart tooltip: resell value 50, Cannot Sell, Cannot Trade (sibling only, not confirmed for this variant).", "source": "wiki image:item_tooltip Briarheart bandage square shard.jpg"},
  {"claim": "No wiki page, article, or video frame names 'Beaming Celestial Square Shard' directly.", "source": "lookup over wiki, articles, video, client (no exact-name hits)"}
 ],
 "confidence": 0.3,
 "open": [
  "Store category 121 is not named in the repo, so the shop it belongs to is unresolved. The 1780 coin price rests on a reference catalogue row, not a wiki page or a client transaction.",
  "Conflict: sibling Square Shards are documented as TCG virtual reward redemptions, while this variant has a coin-store row. Which source applies to this variant is unresolved. Check the wiki or a TCG card list for 'Beaming Celestial Square Shard' before accepting either.",
  "Earlier answer's claim that 1780 is the 'same price tier as other items in that category' is false and has been dropped; category 121 prices are mixed.",
  "Earlier claim that the Legacy ClientItemDefinitions Cost matches 1780 was not re-verified in this pass; treat as unconfirmed.",
  "The client definition has an empty description and no model files, so the item's class/power (which job, which element) is not confirmed.",
  "Retired status and any later removal of store category 121 sales are unknown; no source found.",
  "First-pass tag said kind 'card'; classed as 'other' (a Square Shard power item, not a trading card). The first-pass 'live: yes' is not confirmed beyond the store row."
 ]}
