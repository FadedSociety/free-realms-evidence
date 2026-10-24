<!-- fleet job=item-infer id=ibaron-von-darkcheat-character-v1 status=blocked turns=2 usd=0.0024 tokens(read,write,in,out)=[3659, 11145, 6, 1984] model=claude-haiku-5-5 -->
# Baron von Darkcheat (character)

{"item": {"name": "Unidentified: the evidence pack is for the NPC 'Baron von Darkcheat (character)', not an item", "locale_id": null, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "The pack's subject is an NPC card duelist (infobox: Dwarf, Snowhill/Seaside, occupation Card duelist), not a purchasable or obtainable item.", "source": "wiki: Baron von Darkcheat (character), rev 50125"},
  {"claim": "Leads for items tied to the Baron, none yet attributed to a specific item in this pack: the Gloamstone Hoverboard ride is obtained by completing the Heroes TCG questline; the Rides page says it is one of the rides available outside the SC Marketplace.", "source": "wiki: Rides; wiki: The Gloamstone; client locale:387 'item - Gloamstone Hoverboard'"},
  {"claim": "The Baron's outfit, Baron trophies (décor) come from opening Heroes TCG booster packs, per the character page.", "source": "wiki: Baron von Darkcheat (character), 'Similar to the Realmkeepers... opening a Heroes TCG pack'"},
  {"claim": "An SOE preview names four virtual rewards tied to the Baron von Darkcheat TCG expansion (launched Nov 17, 2011): a Zamboni Ride, a Clockwork Beetle pet, a Shuffle Shooter weapon, and a Baron von Darkcheat Costume.", "source": "articles/articles.json:18464 (SOE news post summary)"},
  {"claim": "The Gloamstone Hoverboard's link to the quest reward is inferred, not stated: the quest text only says 'Say hello to your new hoverboard!' and the item name is a guess in the quest critique.", "source": "quest-lines/quests.json:41598, 41651, 41668"}
 ],
 "confidence": 0.0,
 "open": [
  "The job asks for one item's sources, but the supplied pack contains only the NPC page. No item name was given, so no item sources can be assigned from this pack.",
  "If the intended item is the Gloamstone Hoverboard (locale:387), the likely source is the Card Duelist: Baron von Darkcheat questline reward, but the reward item identity is still unconfirmed in the quest text (quest-lines/quests.json critiques). Needs a fresh pack for that item with price and category evidence.",
  "If the intended item is the Baron von Darkcheat Costume, Trophy, Zamboni Ride, Clockwork Beetle, or Shuffle Shooter, the TCG booster-pack and expansion-reward sources are in the pack, but no prices or Station Cash/coin vendor data were supplied. Needs a re-run with that item named.",
  "Wiki infobox has no coin, Station Cash, or IGD prices, and the page has no pricing for the NPC (none expected).",
  "Retired status is not determinable from this pack."
 ]}
