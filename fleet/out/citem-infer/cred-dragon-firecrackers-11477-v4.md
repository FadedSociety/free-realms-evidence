<!-- fleet job=citem-infer id=cred-dragon-firecrackers-11477-v4 status=nothing_found turns=4 usd=0.0032 tokens(read,write,in,out)=[31942, 15023, 10, 1970] model=claude-haiku-5-5 -->
# Red Dragon Firecrackers

{"item": {"name": "Red Dragon Firecrackers", "locale_id": 11477, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Red Dragon Firecrackers' is locale 11477; description 'Fireworks that explode in the sky!' is locale 11496. Definition id 2686, class 69, slot 0, no model file, no coin store price.", "source": "locale:11477; locale:11496; client definition in evidence pack"},
  {"claim": "No coin store row exists for item_id 2686 in the repo store data.", "source": "repo:prototype/osfr-tools/data/content/stores.json (search for \"item_id\":2686 found no match)"},
  {"claim": "The wiki's Series 1 Virtual Rewards List heading is on the Trading Card Game page, line 16; the entry 'Red Dragon Firecrackers - 1L38' is on line 17, in the cards #52-101 range, which are in virtual Booster Packs only.", "source": "freerealms-wiki/wikitext/1947-48103-33406a0c7640.wiki lines 16-17 (page 'Trading Card Game')"},
  {"claim": "SC Marketplace booster packs include 10 random cards and 1 virtual reward card based on the series. Line 2 gives no price for the pack.", "source": "freerealms-wiki/wikitext/1947-48103-33406a0c7640.wiki line 2"},
  {"claim": "The wiki says the virtual reward cards are not codes for the listed items; they can be found in packs but are very rare, so the card is not a redeemable code.", "source": "freerealms-wiki/wikitext/1947-48103-33406a0c7640.wiki line 17"},
  {"claim": "Client lookup returns only the two locale lines (name and description); no wiki article, article fact, or video frame names the item.", "source": "lookup over client, wiki, articles, video"}
 ],
 "confidence": 0.2,
 "open": [
  "No evidenced acquisition source. The only link is TCG virtual reward card 1L38, and the wiki (line 17) says these cards are not codes for the items. Nothing shows that pulling the card grants in-game item 2686, so it is not listed as a source.",
  "The 'event' first-pass guess is unsupported: no event, holiday, quest, drop, vendor, or coin-shop source was found.",
  "Pack price is unknown; no source gives a Series 1 booster price, so price is null.",
  "Retirement status unknown; no source says when the Series 1 virtual card or the item stopped being obtainable.",
  "Critique fixes applied: the marketplace row is removed from sources; wireable is false; the 'Series 1 Virtual Rewards List' heading is cited at line 16 and the 1L38 entry at line 17.",
  "Live status is unsure: the client defines the item, but no source shows it was ever obtainable in-game."
 ],
 "wireable": false}
