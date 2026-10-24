<!-- fleet job=citem-infer id=cgold-cheerleading-trophy-66966-v2 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[5259, 7314, 6, 2146] model=claude-haiku-5-5 -->
# Gold Cheerleading Trophy

{"item": {"name": "Gold Cheerleading Trophy", "locale_id": 66966, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Gold Trophies collection (collection id 168; name locale:67534; description locale:67646 'A collection of gold trophies for being the best!'). Entry index 7, item_definition_id 23353, icon 611 / tint 112. The item's own text (locale:132427 'This item can be added to the Gold Trophies Collection') says the player adds it to the set. This is a collection member, not an acquisition route.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13170-13251; locale:67534; locale:67646; locale:132427"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: 'Gold Cheerleading Trophy', name locale:66966, definition 23353, no coin store price in stores data, so no coin vendor sale is evidenced", "source": "locale:66966; client definition pack"},
  {"claim": "Collection 168 'Gold Trophies' has 8 catalogue entries (index 1-8, name_ids 66960-66967, item_definition_ids 23347-23354). This trophy is index 7. The catalogue has no entry-count of 11. The 11 figure in the pack comes from the client name cluster (locale 66961-66971), which mixes Gold trophies with Last Man Standing, Team, Capture The Flag and Dueling trophies.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13178-13251"},
  {"claim": "Collection completion reward is 10 coins and 50 XP (profile_id 48). The reward is for completing the collection, not for obtaining the trophy.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13252-13260"},
  {"claim": "Every catalogue entry for this collection carries item_link 'sanctuary'. That marks the community-server source of the catalogue, not live-era evidence.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:13186-13240"},
  {"claim": "The wiki 'List of Collections' lists '[Gold] Medals', 'Silver Medals', 'Bronze [Trophies]' and 'Silver [Trophies]', but no 'Gold Trophies' collection. It does not confirm collection 168 as a live set.", "source": "lookup wiki page 'List of Collections'"},
  {"claim": "Sibling cheerleading trophies exist in client text: Bronze Cheerleading Trophy (locale:66950) and Silver Cheerleading Trophy (locale:66958), alongside Gold (locale:66966).", "source": "locale:66950; locale:66958; locale:66966"},
  {"claim": "No wiki article, article fact, video frame, vendor stock, or other pack answer names how a player obtains this trophy (no vendor, drop, quest, event, Coin Shop or SC Marketplace evidence).", "source": "pack fields wiki_page=null, article_facts=[], video=[], vendor_stock=[]; lookup 'Cheerleading Trophy' returned only client text"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition method is unknown. No source names a vendor, quest, drop, event, prize wheel or store for the Gold Cheerleading Trophy. The only source is collection membership, which says where the item goes, not how a player gets it.",
  "Live status is unsure. The catalogue entry is sourced from the community server ('sanctuary'), and no live-era wiki, article or video source confirms the trophy or collection 168 was live.",
  "Prior answer's claim that collection 168 has 11 entries was wrong. The catalogue has 8 entries (name_ids 66960-66967). The previous answer's wiki claim about a 'Gold Trophies' family was also wrong: the wiki lists '[Gold] Medals' and Bronze/Silver Trophies, not Gold Trophies.",
  "The 10 coins + 50 XP is the collection completion reward, not a source of the trophy, so it is not listed as a source.",
  "Next step: check the sibling trophies (locale 66950, 66958, 66961-66971) and the events where these trophies were awarded, or a 'Gold Trophies' wiki/forum source, before wiring any acquisition route."
 ]}
