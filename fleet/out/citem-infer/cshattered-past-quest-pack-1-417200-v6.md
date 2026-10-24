<!-- fleet job=citem-infer id=cshattered-past-quest-pack-1-417200-v6 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[16131, 9792, 8, 2348] model=claude-haiku-5-5 -->
# Shattered Past - Quest Pack 1

{"item": {"name": "Shattered Past - Quest Pack 1", "locale_id": 417200, "kind": "other"},
 "sources": [
  {"type": "quest_reward", "detail": "Sir Wellington and friends: card duel quest that wins Shattered Past card-set cards (the Pack 1 quest content, the pack being the quest's entry item)", "where": "Bristlewood, outside the Vale of the Ancients", "price": null, "currency": null, "source": "locale:417203; locale:156877"},
  {"type": "marketplace", "detail": "Sold individually as a purchasable Trading Card Game quest pack in the Station Cash store (historical). No standalone Pack 1 price is evidenced; the only SC price is the three-pack Shattered Past - Quest Bundle, which is not a Pack 1 price.", "where": "Station Cash store", "price": null, "currency": "station_cash", "source": "http://www.freerealms.com/article/detail.action?articleId=2739; http://www.freerealms.com/article/detail.action?articleId=2746; locale:156876; locale:156877 (bundle: 650 SC for all three packs, 100 SC saving)"}
 ],
 "retired": false,
 "live": "unsure",
 "evidence": [
  {"claim": "Pack 1 is the Shattered Past quest pack; Sir Wellington, found outside the Vale of the Ancients in Bristlewood, lets card duelists win Shattered Past cards.", "source": "locale:417203 (unflagged); locale:417200 (name, unflagged)"},
  {"claim": "Pack 2's text requires the player to have 'purchased and completed Shattered Past Quest Pack 1', so Pack 1 is the first step of the chain.", "source": "locale:417204"},
  {"claim": "The three Shattered Past Quest Packs were sold together as the Shattered Past - Quest Bundle for 650 SC, a 100 SC saving. This is a bundle price, not Pack 1's price.", "source": "locale:156876; locale:156877"},
  {"claim": "Articles say the Trading Card Game quest packs from the first two expansion sets, previously sold for purchase, are now free to all players. Article 2746 names them as the Shattered Past and Baron quest packs.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2734; http://www.freerealms.com/article/detail.action?articleId=2739; http://www.freerealms.com/article/detail.action?articleId=2746"},
  {"claim": "The client definition 62539 has no coin store price, so there is no coin vendor sale.", "source": "client definition in pack"}
 ],
 "confidence": 0.45,
 "open": [
  "No standalone Station Cash price for Pack 1 is evidenced; only the 650 SC three-pack bundle (locale:156877).",
  "The paid sale has ended and the articles say the packs are now free to all players. Whether the quest is still playable on the live server is not confirmed, so live is 'unsure'. retired is false because the quest itself is not described as removed; the paid source is historical.",
  "Location conflict: article 2745 places Sir Wellington outside Ancestor Valley in Borstenwald, and article 2739 starts the series with Professor Altamiro in Spiky Woods. The client text (locale:417203) and locale:156877 say the Vale of the Ancients in Bristlewood; that is used here and the conflict is unresolved.",
  "Whether Pack 1 is consumed on completion or stays in inventory is not shown in the evidence.",
  "No quest_dialog or quest_objective line names the NPC for Pack 1; the location comes only from the description rows.",
  "Kind: the enum has no quest-item value, so 'other' is used. Client class 1, slot 0, no model: a TCG quest pack, not a physical item.",
  "Critique fixes: removed the citation to locale:417201 (flagged placeholder). Restated the 'sold separately' claim as articles-level wording with no Pack 1 price. Dropped retired: true and added the quest source. Marketplace price stays null."
 ]}
