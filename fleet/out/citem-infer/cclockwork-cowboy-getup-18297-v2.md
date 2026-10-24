<!-- fleet job=citem-infer id=cclockwork-cowboy-getup-18297-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6143, 8596, 6, 1741] model=claude-haiku-5-5 -->
# Clockwork Cowboy Getup

{"item": {"name": "Clockwork Cowboy Getup", "locale_id": 18297, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, category 103 (vendor NPC and zone not identified in any source)", "where": null, "price": "500 coins (member price 450 coins, 10% member discount; sell price 50 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:17041 (item_id 79283, purchase_price_coins 500, member_price_coins 450)"},
  {"type": "quest_reward", "detail": "Reward for completing a Sanctuary campaign about a plot against the queen, after 'Campaign 6: Tanglewood Fort' is purchased and completed. The campaign number is not named in the text; the 'Campaign 7: Queen's Last Hope' link in the earlier answer is unconfirmed and dropped.", "where": "Sanctuary", "price": null, "currency": null, "source": "locale:39527 (quest_objective: 'Earn the Clockwork Cowboy Getup when you complete this campaign... already purchased and completed \u201cCampaign 6: Tanglewood Fort\u201d')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 79283 named 'Clockwork Cowboy Getup' (locale 18297), chest slot 3, class 173, model freestyle_<race>_<gender>_chest_clockworkcowboy.adr", "source": "client definition in pack; locale:18297"},
  {"claim": "Coin store row for item 79283: category 103, 500 coins, 10% member discount to 450, sell price 50, not marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:17041"},
  {"claim": "Quest objective text says the getup is earned by completing a Sanctuary plot-against-the-queen campaign after Campaign 6: Tanglewood Fort", "source": "locale:39527"},
  {"claim": "Sibling items 18298-18302 (Boots, Gloves, Bowler, Backpack, description line) share the set name in the client text", "source": "locale:18298-18302 (client cluster in pack)"}
 ],
 "confidence": 0.5,
 "open": [
  "Vendor NPC and zone for the 500-coin store sale are not named. The stores.json row sits in a bulk block with many items at the same 500/450/50 values, so it is a store row, not a named vendor sale.",
  "Campaign number for the Sanctuary quest reward is unconfirmed. No wiki page or client text found ties the getup to Campaign 7 or the Queen's Last Hope chapter; the Royal Guard Tabard pattern is an analogy, not evidence.",
  "Retired status is unknown. Neither the store row nor the campaign is dated in any source. Live 'unsure' rather than 'yes' because the store row exists in repo data but its current status is not confirmed.",
  "No wiki article exists for the item; no sale-price history or second wiki price was found."
 ]}
