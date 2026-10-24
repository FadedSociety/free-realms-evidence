<!-- fleet job=citem-infer id=cgrow-food-iv-36363-v2 status=nothing_found turns=3 usd=0.0028 tokens(read,write,in,out)=[16416, 12955, 8, 1985] model=claude-haiku-5-5 -->
# Grow Food IV

{"item": {"name": "Grow Food IV", "locale_id": 36363, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: definition_id 2991, class 9, slot 0, description 'Eating this food will increase the size of the player.', no models, no coin_store_prices in the client definition.", "source": "client definition in pack; locale:36363"},
  {"claim": "Client text tags the name 'quest_reward' (type tag only); no quest, NPC, vendor, drop or event text in the client, wiki or refs names this item.", "source": "lookup client locale:36363; lookup wiki 'Grow Food' (no article hit)"},
  {"claim": "Client tags of the family: Grow Food I (36360) item; II (36361), III (36362), IV (36363), V (36364) quest_reward; Shrink Food IV (36358), Tiny Tincture (36359), Invisibility Food I-IV (36365-36368) item.", "source": "locale:36358-36368 via lookup client"},
  {"claim": "repo:prototype/osfr-tools/data/content/stores.json lines 11909-11913 contain rows item_id 36360, 36361, 36362, 36363, 36364, each category_id 4, purchase_price_coins 40, member_price_coins 36, sell_price_coins 4, no_sale false. The row for 36363 is the only store row keyed to this item's locale id. The row is NOT tied to this item: the store's item_id space is not confirmed to be the client locale id or the definition id (2991), so it cannot be attached as a source for Grow Food IV.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11912 (item_id 36363)"},
  {"claim": "No vendors.json, quest, recipe or drop entry references 36363 or definition 2991 in the repo.", "source": "repo search for '36363|2991' and 'Grow Food' (no vendor/quest hits)"}
 ],
 "confidence": 0.15,
 "open": [
  "Unresolved: stores.json item_id 36363 (40 coins, member 36, sell 4, category 4) may be the store price for this item, but only if store item_id equals the client locale id, which is unverified. Confirm the item-catalogue mapping from store item_id to definition id (2991) before recording a coin_shop source. If confirmed, the price would be 40 coins (member price 36 coins, 10% member discount), and the same row pattern covers the whole 36360-36364 block.",
  "Quest_reward source is unnamed: the client tag suggests a quest reward but no quest is found. Find the quest whose reward list includes definition 2991 (or the locale 36363) in repo quest data.",
  "Enemy drop, event, prize wheel, crafting and membership sources: none found.",
  "Live status and retirement unknown; no wiki, article or video source confirms availability. The first-pass 'live: yes' is a hint only.",
  "The previous answer's claim that stores.json has no price was incorrect in the sense that a row exists under 36363; that row is recorded above as an unverified candidate, not a confirmed source."
 ]}
