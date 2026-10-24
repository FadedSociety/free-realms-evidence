<!-- fleet job=citem-infer id=cpolished-handle-384228-v1 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[10897, 10218, 8, 2196] model=claude-haiku-5-5 -->
# Polished Handle

{"item": {"name": "Polished Handle", "locale_id": 384228, "kind": "other"},
 "sources": [{"type": "crafting", "detail": "Crafting ingredient for Brawler weapons (component, not a finished item). The recipe that consumes it was not found in our data.", "where": null, "price": null, "currency": null, "source": "Client definition, definition_ids 48326 and 48327 (description: \"Used in the construction of Brawler weapons. Requires quest: 'Brawler: Paying your Dues.'\"); repo search for 'Polished Handle' / 48326 found no recipe entry"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client item name 'Polished Handle' exists as locale:384228 (item) and as ugdt/ucdt strings in the client locale tables.", "source": "locale:384228"}, {"claim": "Client definition describes it as a Brawler weapon construction part that requires the quest 'Brawler: Paying your Dues'.", "source": "client definition, definition_ids 48326, 48327"}, {"claim": "Brawler weapons are craftable/questline items in our reference data (e.g., Amateur Brawler Hammer, All-Star Brawler Hammer, Brawler's Anvil Hammer of Cheapshot), and the Brawler questline is an achievement ('The Big Brawler').", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:470-481 and repo:prototype/osfr-tools/data/content/achievements.json:5779-5780"}, {"claim": "The jev first-pass tag (live, other, crafting) agrees with the description, but it is only a hint.", "source": "evidence pack first_pass"}],
 "confidence": 0.35,
 "open": ["No wiki page, article, video, or coin-store record names Polished Handle; no coin vendor stocks it. Crafting is supported only by the client description, not by a recipe in repo data or the wiki.",
 "Quest 'Brawler: Paying your Dues' was not found in client text or the wiki search, so the quest that gates the handle is unverified.",
 "The client text neighbours (locale 384223-384233: Venomous Frogs, Ramirez's Dig Site, Flitter mail, Shaming the Sheriff) belong to other quests and are not a set with this item; the cluster does not show its sources.",
 "No price or Station Cash listing; the coin_store_prices list is empty.",
 "Live status is inferred from the presence of the client definition only; no in-game or wiki confirmation that the handle is still obtainable. Need a Brawler recipe source (crafting table/recipe id) and the Paying your Dues quest record to confirm."]}
