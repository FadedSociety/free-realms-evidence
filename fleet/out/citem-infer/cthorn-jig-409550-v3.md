<!-- fleet job=citem-infer id=cthorn-jig-409550-v3 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[16487, 11291, 8, 1761] model=claude-haiku-5-5 -->
# Thorn Jig

{"item": {"name": "Thorn Jig", "locale_id": 409550, "kind": "consumable"},
 "sources": [
  {"type": "coin_shop", "detail": "Fishing lure, sold in the Coin Shop under the supplies category (wiki lists it with the other lures)", "where": "Coin Shop (supplies category)", "price": null, "currency": null, "source": "wiki page ns0 Fisherman, revision 45839 (2021-12-27), section 'Lures', lines 39-52 (refs: freerealms-wiki/wikitext/2369-45839-27f27de169db.wiki)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Thorn Jig' is locale 409550, definition 68162, class 142, slot 0. Client definition has no coin_store_prices, so there is no store price evidence.", "source": "locale:409550; client definition 68162"},
  {"claim": "Description: 'This lure gives a 10% better chance of catching Blue Thornfin, Chipsen Fish and Thorny Trout.'", "source": "client definition description; wiki page Fisherman, line 52"},
  {"claim": "Wiki Fisherman 'Lures' section says fishing lures are bought from the Coin Shop under the supplies item category, and lists Thorn Jig among them.", "source": "wiki page Fisherman rev 45839, lines 39-40 and 52"},
  {"claim": "Server fishing data maps definition 68162 to Blue Thornfin, Chipsen Fish and Thorny Trout, matching the client description.", "source": "repo: Lxzxrus-Free-Realms-Server/src/Sanctuary.Game/Minigames/Fishing/FishingGear.cs:67"},
  {"claim": "NPC dialog lines say the target fish like the Thorn Jig.", "source": "locale:29751, locale:29770, locale:29773"},
  {"claim": "Guppie (Sacred Grove Shallows) is NOT listed as a source: the quest/lure lines only say players buy 'a lure' there and name no Thorn Jig stock row.", "source": "locale:408625, 408623, 408632, 408645 (generic lure lines)"}
 ],
 "confidence": 0.6,
 "open": [
  "No coin price or currency is evidenced for Thorn Jig. The client has no coin_store_prices and the wiki Lures section gives no price. Price stays null until a Coin Shop row or wiki price is found.",
  "The Coin Shop source rests on one 2021 wiki revision (45839). It does not confirm the lure is sold today.",
  "Retirement is unknown. The 2021 revision is the last evidence of sale; no source says it was retired.",
  "'Thorn Jig - Lure' (locale 412940/412941, and 29371259 in the test data) carries the same description. Not verified as the same item as definition 68162.",
  "The Guppie vendor link from the previous answer was dropped: no item-specific stock row or quote names Thorn Jig there.",
  "No quest reward, enemy drop, event, prize wheel, crafting or collection source was found."
 ]}
