<!-- fleet job=item-infer id=iwugachug-v1 status=nothing_found turns=2 usd=0.0026 tokens(read,write,in,out)=[3744, 12985, 6, 1959] model=claude-haiku-5-5 -->
# Wugachug

{"item": {"name": "Wugachug", "locale_id": 3505, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "'Wugachug' (locale 3505) is a place name in the client text table, tagged place | Wildwood, not an item name.", "source": "locale:3505"},
  {"claim": "The wiki page 'Wugachug' is a Locations page for the town (NE of Seaside, N of Merry Vale, home of the Chugawugs). It has an empty coin, Station Cash and IGD section and no acquisition text.", "source": "wiki page: Wugachug (rev 49978)"},
  {"claim": "Its categories are Locations, Sacred Grove and Wugachug. None is a sale or reward category (no SC Marketplace, Coin Shop, Prize Wheel, drop, or holiday category).", "source": "wiki page: Wugachug (categories)"},
  {"claim": "The only other client match, locale 422601, is a joke chat line flagged as nonsense, so it is not a real item.", "source": "locale:422601"},
  {"claim": "No coin vendor stocks anything named Wugachug, and no other answer mentions it as an item.", "source": "vendor_stock and mentioned_by_other_answers in the pack are empty"},
  {"claim": "Repo hits for 'Wugachug' are zone, collection, achievement, NPC and quest-text entries (zones.json, collections.json 'Wugachug' and 'Wugachug Rare Exploration', 'Wugachug Warpstone' node, and NPC spawns). None is an item sale or reward.", "source": "repo:prototype/osfr-tools/data/content/zones.json:230; repo:prototype/osfr-tools/data/content/collections.json:1356"}
 ],
 "confidence": 0.9,
 "open": [
  "The pack asks for the item 'Wugachug', but that name is the town (a location page), so it has no item sources. Nothing was sourced to it, and the town is not a purchasable or droppable item.",
  "Likely intended item: 'Wugachug Lot' (locale 69967 'Wugachug Lot'; description locale 69982 'An empty lot of land on the outskirts of Wugachug.'). It is a housing lot, so it is not the same thing as the town. If the brief meant this, re-run with that name. Known sources for it from the pack: SC Marketplace (wiki page 'Wugachug Lot', category SC Marketplace; the wiki price text is blank in this extract, so the regular and member prices are unverified). Membership bundles: 6 Month (articles 1964/1970), 12 Month and Lifetime (same articles), and the Snowhill Lodge bonus list (locale 432791-432793). Sale: 150 SC during a sale (article 2528). Locale 10479 also says it came with a free Wood Builders Pack, valued at SC 200, on purchase.",
  "The wiki's 'Wugachug' page mentions 'Wugachug Warpstone' and collections, but no item.",
  "Wugachug Lot is still a 'Lot' listed on the articles, so the 'retired' flag for it is not decided here. The membership bundles are older offers, so their current availability is unverified."
 ]}
