<!-- fleet job=citem-infer id=cfaintly-glowing-purple-flair-shard-386230-v1 status=done turns=3 usd=0.0039 tokens(read,write,in,out)=[11588, 18228, 8, 2974] model=claude-haiku-5-5 -->
# Faintly Glowing Purple Flair Shard

{"item": {"name": "Faintly Glowing Purple Flair Shard", "locale_id": 386230, "kind": "other"},
 "sources": [
  {"type": "quest_reward", "detail": "Science Experiment (Mugwort's Hollow quest; the wiki says the shard is acquired by completing it)", "where": "Mugwort's Hollow", "price": null, "currency": null, "source": "wiki page 'Faintly Glowing Purple Flair Shard' (acquisition text); quest title locale:51078 ('Science Experiment', ucdt); turn-in line locale:90476 [quest_dialog | Mugwort's Hollow | Science Experiment]; objective locale:90468 'Speak with Funnel Bindweed'"},
  {"type": "vendor", "detail": "unidentified coin vendor (no NPC in the repo's vendor data stocks item 55358; the vendor_stock field in the pack is empty)", "where": null, "price": "890 coins (member price 801 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 55358 (purchase_price_coins 890, member_price_coins 801, sell_price_coins 89); the item tooltip image shows Resell Value 89, which matches"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item name and description: 'Faintly Glowing Purple Flair Shard', 'This shard places a purple glow effect on your weapon.' Level 1, any job, Cannot Trade.", "source": "locale:386230; wiki page 'Faintly Glowing Purple Flair Shard'; image:item_tooltip"},
  {"claim": "Wiki says the shard is acquired by completing the quest Science Experiment", "source": "wiki page 'Faintly Glowing Purple Flair Shard'; freerealms-wiki/wikitext/4560-15516-34012585ccce.wiki"},
  {"claim": "Store data lists a coin purchase of 890 coins (801 for members), resell 89, for item 55358; the sibling items 55354-55359 carry the same price, the same six-color set", "source": "repo:prototype/osfr-tools/data/content/stores.json:13847 (item 55358) and lines 13843-13848"},
  {"claim": "The client's Science Experiment line 'These samples look great! ... Thanks for your help!' is a turn-in thank-you, placing the reward at the end of this quest", "source": "locale:90476"},
  {"claim": "The Sweetwater Climb lines in the cluster (locale:386232, 386235) belong to a different quest and do not name this item", "source": "locale:386232; locale:386235"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin vendor for item 55358 is not identified. stores.json has the 890-coin price, but no NPC stock list in the repo includes it, so the vendor name and zone are unknown.",
  "The wiki lists no coin price. The 890 price comes only from our store data, so the coin sale is not confirmed by a second source.",
  "The Science Experiment quest's reward is not confirmed in the repo's quest data. The source is the wiki text alone. The speaker of locale:90473/90476 is unnamed.",
  "Retired status is unknown: no wiki or article says when the coin sale or the quest reward ended.",
  "The pack's client cluster includes Sweetwater Climb lines (locale:386232, 386235). They are unrelated to this shard, so they are not used as sources.",
  "The wiki's Cannot Trade note fits a quest reward, but does not rule out the coin sale; both are listed as sources."
 ]}
