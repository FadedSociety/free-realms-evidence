<!-- fleet job=item-infer id=isal-monella-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6289, 7841, 6, 1967] model=claude-haiku-5-5 -->
# Sal Monella

{"item": {"name": "Sal Monella's Special", "locale_id": 3967, "kind": "consumable"},
 "sources": [
  {"type": "other", "detail": "Quest-delivery food in the 'Sal Monella Special' chain: Sal Monella hands out bowls of his Special to be delivered to Darci Flitterstride and Bart Purpleton (quest 'Deliver the Sal Monella Special'). Quest text says 'Grab these bowls of stew and hand them out before they get cold!' and 'Deliver Sal Monella's food before time runs out!'. This is a quest handout, not a purchase; the item's delivery to the quest NPCs is supported, the exact item-to-bowl link is inferred from the matching name.", "where": "Mire's Edge, Blackspore Swamp", "price": null, "currency": null, "source": "locale:77281; locale:91855; locale:91859; locale:77084; locale:3967; locale:45300"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Sal Monella's Special' is locale 3967 (item). The NPC name Sal Monella is locale 45300.", "source": "locale:3967; locale:45300"},
  {"claim": "Quest text: Sal wants his fresh samples out there; grab the bowls of stew and hand them out before they get cold.", "source": "locale:77281; locale:91855"},
  {"claim": "Delivery quest title 'Deliver the Sal Monella Special'; objective 'Deliver Sal Monella's food before time runs out!'.", "source": "locale:77084; locale:91859"},
  {"claim": "Sal offers a taste of his Sal Monella Special in dialog; NPCs respond 'Say, have you ever tried Sal Monella's Special?'.", "source": "locale:390253; locale:6343"},
  {"claim": "Sal Monella is a robgoblin chef NPC in Mire's Edge, Blackspore Swamp, giving the Sal Monella Special quest chain.", "source": "https://freerealms.fandom.com/wiki/Sal_Monella"},
  {"claim": "A wiki item render 'Sal Monella's Special' exists; a user blog page is categorized Category:Food.", "source": "wiki image:item_render Bandicam 2013-04-01 14-54-00-696.jpg; wiki: User blog:Amber Kindpaws :)/Sal Monella's Special"},
  {"claim": "No coin vendor, Station Cash, Coin Shop, drop or prize-wheel listing for the item was found in the pack or client; no price found.", "source": "lookup client/wiki/articles for \"Sal Monella's Special\""}
 ],
 "confidence": 0.35,
 "open": [
  "Fresh Ingredients reward (quest_reward) dropped from sources: the only support is a user blog ('You Will Receive 5 [Sal Monella's Special] As A Reward'), which is user-written and does not name a verified quest. Needs an official reward check on the Fresh Ingredients quest.",
  "No wiki item page, price, or vendor for Sal Monella's Special was found; no Station Cash or Coin Shop source exists in the evidence.",
  "Whether the item is still obtainable live is unknown; the evidence is from the shipped client quest text only.",
  "Kind 'consumable' is inferred from food text and the Category:Food blog tag, not from an item-data record.",
  "Pack critique said the 'Birthday Bash' link was unverified; not used as a source here.",
  "The pack's 'not purchasable or rewarded' claim was removed; it overreached, since absence of a vendor in the pack is not proof."
 ]}
