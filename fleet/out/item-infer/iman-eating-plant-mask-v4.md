<!-- fleet job=item-infer id=iman-eating-plant-mask-v4 status=done turns=3 usd=0.0020 tokens(read,write,in,out)=[13459, 7405, 8, 1915] model=claude-haiku-5-5 -->
# Man-Eating Plant Mask

{"item": {"name": "Man-Eating Plant Mask", "locale_id": 1944, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "Random Virtual Reward loot card (card 1L76, 11/76) pulled from a Trading Card Game Series 1 booster pack; redeemed via communicator for one mask. Pull rate within the pack is undocumented.", "where": "SC Marketplace (Trading Card Game Series 1 booster packs, if still sold; current availability unverified)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Man-Eating_Plant_Mask ; wiki 'Category:Virtual Rewards' (\"With each booster pack, you receive 1 Virtual Reward\"); articles: http://www.freerealms.com:80/article/detail.action?articleId=314 (fact:economy, loot cards in packs)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item name matches client text.", "source": "locale:1944"},
  {"claim": "Client use text: 'Using this mask will temporarily turn the player into a man-eating plant for a long time.' Supports a usable consumable effect. Unlimited use and 'any job' are not in client text.", "source": "locale:11568"},
  {"claim": "Card art reads 'Allows you to disguise yourself as a man-eating plant', 11/76; wiki image filename is '1L76 man-eating plant mask card.png', which supports card ID 1L76 (ID not confirmed in client data).", "source": "image:art_or_promo and wiki File:1L76 man-eating plant mask card.png on https://freerealms.fandom.com/wiki/Man-Eating_Plant_Mask"},
  {"claim": "Mask is redeemed from the Series 1 Virtual Reward loot card of the same name; categories Consumable, Unlimited Consumable, Virtual Rewards, Trading Card Game.", "source": "https://freerealms.fandom.com/wiki/Man-Eating_Plant_Mask"},
  {"claim": "Series 1-3 weekend sale was 199 SC, stated as 50 SC off the individual pack price. This was a past promotion (1-4 September), not a current price.", "source": "articles: http://www.freerealms.com/article/detail.action?articleId=2757"}
 ],
 "confidence": 0.4,
 "open": [
  "No individual Series 1 pack price is stated in any source. The earlier 249 SC figure was arithmetic (199 + 50) and is withdrawn; the only direct 249 SC figure (articleId=2415) is for the Baron von Darkcheat set. No price is recorded for the mask.",
  "The mask is not sold directly. Its only route is a random loot-card pull inside a Series 1 pack; the pull rate is undocumented.",
  "Whether Series 1 packs are still sold on the SC Marketplace is unverified. retired is null and live is unsure; do not treat as live until confirmed.",
  "'Unlimited use' and 'usable by any job' are wiki-only (Unlimited Consumable category), not confirmed in client text.",
  "Card ID 1L76 and number 11/76 come from the wiki and card art only; not confirmed in client data.",
  "The 'planned to contain' wording in tradingCardGame.vm means pack contents (10 cards + 1 loot card) are only partly confirmed; the wiki Virtual Rewards text is the stronger support.",
  "No vendor, Coin Shop, prize wheel, event, quest, or drop source found for this item."
 ]}
