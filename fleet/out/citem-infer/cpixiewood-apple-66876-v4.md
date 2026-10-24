<!-- fleet job=citem-infer id=cpixiewood-apple-66876-v4 status=nothing_found turns=2 usd=0.0023 tokens(read,write,in,out)=[5590, 11826, 6, 1608] model=claude-haiku-5-5 -->
# Pixiewood Apple

{"item": {"name": "Pixiewood Apple", "locale_id": 66876, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Pixiewood Apple' is locale 66876 (re-checked via lookup)", "source": "locale:66876"},
  {"claim": "Client description reads 'This item can be added to the Red Apples Collection' (re-checked via locale tool)", "source": "locale:132416"},
  {"claim": "Item 23263 is listed as a member of the Red Apples collection (collection 157, name_id 67523) in the repo catalogue. This is set membership, not an acquisition source.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json lines 12159-12167 and 12114-12209"},
  {"claim": "The Pixiewood Hills Halloween article names candied apple supplies among its daily quests but does not name Pixiewood Apple. This is a non-source note only.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1854"},
  {"claim": "Repo and client searches for 'Pixiewood' and definition 23263 return no vendor, quest, drop, or store entry for this item. Only the locale strings and the collection catalogue mention it.", "source": "repo search (Pixiewood|23263); lookup (client, wiki, articles, video)"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is evidenced. No wiki page, vendor stock, quest reward, drop, event, coin store price, or video names Pixiewood Apple. Its source is unknown.",
  "The client definition has no coin store price (coin_store_prices is empty), so no coin vendor sale is evidenced.",
  "Red Apples collection membership rests on repo catalogue data and the client description. The earlier critique reports that wiki page 2038 (rev 27852) lists '* Red Apples', but I did not read that page myself. The 'Flora > Common' heading is unverified and is not used here.",
  "The 4 coin and 50 XP reward belongs to completing the whole Red Apples set, not to this item, so it is not listed as a source.",
  "The 'Apples!' daily (Pucca De'Flor, locale:415402/415268) is a caramel candy apple quest for another item and is excluded.",
  "The locale:1763333597 citation from the earlier answer is invalid. It is a raw hash, not a locale id, and is removed. Only locale:132416 is cited for the description.",
  "Live and retired status are unknown. The first-pass 'live: yes' is only a hint and no dated source confirms it.",
  "Next checks: an in-game look at the Red Apples collection page, a video of the apple being collected, or a dated patch note that names it."
 ]}
