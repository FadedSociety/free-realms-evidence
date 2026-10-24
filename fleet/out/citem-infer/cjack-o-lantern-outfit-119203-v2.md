<!-- fleet job=citem-infer id=cjack-o-lantern-outfit-119203-v2 status=done turns=3 usd=0.0033 tokens(read,write,in,out)=[17235, 15100, 8, 2406] model=claude-haiku-5-5 -->
# Jack-O-Lantern Outfit

{"item": {"name": "Jack-O-Lantern Outfit", "locale_id": 119203, "kind": "clothing"},
 "sources": [
  {"type": "quest_reward", "detail": "Special TCG Halloween quest (Rose in Pixiewood Hills, won in a TCG game), unlocked by buying a TCG Quest Pack; the other quest reward from the same pack is the Chiller Boombox", "where": "Super Spooktacular (Halloween event), Pixiewood Hills", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=476; http://www.freerealms.com:80/article/detail.action?articleId=1854; http://www.freerealms.com:80/article/detail.action?articleId=2304 (Rose quest: 'win her jack-o-lantern costume'); wiki page Jack-O-Lantern Outfit; wiki page Super Spooktacular"},
  {"type": "marketplace", "detail": "The TCG Halloween quest that awards the costume is itself sold in the Marketplace (article 2304 says 'Purchase this quest from the Marketplace'); the TCG Quest Pack's own price was not found", "where": "Marketplace", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304; http://www.freerealms.com:80/article/detail.action?articleId=476"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Buying a TCG Quest Pack unlocks one of two special TCG Halloween quests; completing it rewards either the glow-in-the-dark Jack O' Lantern costume or the Chiller Boombox", "source": "http://www.freerealms.com:80/article/detail.action?articleId=476; http://www.freerealms.com:80/article/detail.action?articleId=1854"},
  {"claim": "Article 1857 (French-language) names the alternate reward 'Scary Transistor' rather than the Chiller Boombox; conflicts with 476/1854 and is unresolved", "source": "http://www.freerealms.com/article/detail.action?articleId=1857"},
  {"claim": "Article 2304 lists the Rose quest, purchased from the Marketplace, where a player challenges Rose in Pixiewood in a TCG game to win her jack-o-lantern costume", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"},
  {"claim": "Wiki page: the outfit is earned from purchasing the TCG Quest Pack in Spooktacular and completing the quest", "source": "wiki page Jack-O-Lantern Outfit"},
  {"claim": "Client name 'Jack-O-Lantern Outfit' is locale 119203 with one definition (id 69832), chest slot 17", "source": "locale:119203; client definition"},
  {"claim": "stores.json item 69832 has a 50-coin purchase price in category 201 with no_sale true, sell_price null and no price_provenance block. Unlike its neighbours (69824, 69833-69838), it was not reconciled to a Station Cash price and no coin vendor or Coin Shop page confirms it, so it is not used as a coin_shop source", "source": "repo:prototype/osfr-tools/data/content/stores.json line 14918"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin store price 50 coins (stores.json item 69832) is an unresolved legacy cost, not a confirmed sale; dropped as a source. Needs a Coin Shop or vendor check.",
  "TCG Quest Pack price and Marketplace listing were not found; add a price if a source is found.",
  "Alternate reward conflict: Chiller Boombox (articles 476, 1854, wiki) vs 'Scary Transistor' (article 1857). Verify the Boombox client name before wiring.",
  "Article 2306 (Halloween outfit set) was not checked; it is background only and not used as a source.",
  "Retirement not confirmed. Super Spooktacular is seasonal, but no source states the outfit was retired, so live status is unsure.",
  "No coin vendor, client cluster, or video evidence found for this item."
 ]}
