<!-- fleet job=citem-infer id=ctrolls-medal-of-honor-41092-v3 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6465, 10318, 6, 2321] model=claude-haiku-5-5 -->
# Trolls Medal of Honor

{"item": {"name": "Trolls Medal of Honor", "locale_id": 41092, "kind": "collection"},
 "sources": [{"type": "collection", "detail": "Entry 6 (id 808, index 6, item_definition_id 3876) of the Medals of Honor collection (collection id 111, name locale 7762). Membership only; no acquisition route for the individual medal is documented in any source checked.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9193-9200 (entry 808); repo:prototype/osfr-tools/data/content/collection_catalogue.json:9138-9219 (collection 111, eight entries)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Locale 41092 is 'Trolls Medal of Honor'. Locale 41087-41094 are the eight Medal of Honor names (Chugawugs, Pixies, Robgoblins, Humans, Dwarfs, Trolls, Elfs, Unidentified). Locale 1463 is 'Medal of Honor'.", "source": "locale:41092; locale:41087-41094; locale:1463"},
  {"claim": "Collection 111 has eight entries, ids 803-810, indexes 1-8, item definitions 3871-3878, names 41087-41094. Trolls is index 6 (id 808, definition 3876). Meteoric (41095), Silver Lining (41096) and Shooting Star (41097) are not entries of collection 111.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9138-9219 (re-read and verified)"},
  {"claim": "Completing collection 111 grants 7 coins, item definition 3889 x1, 50 profile-49 XP, and unlocks collection 113.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:9220-9239"},
  {"claim": "The client definition for definition 3876 describes the item as 'This item can be added to the Medals of Honor Collection'. This is the only description text in the pack; no locale id is cited for it.", "source": "client definition for definition 3876 (as carried in the evidence pack)"},
  {"claim": "stores.json row item_id 41092 (category 101, purchase 1027 coins, member price 924, sell 102) is keyed to the name locale id, not to definition 3876. The client definition has no coin store price for 3876, so this row is not attributed to this item and is not treated as a price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12562"},
  {"claim": "No wiki article, wiki image, article fact, video frame, vendor stock, quest text or enemy drop names this medal. A lookup of 'Medal of Honor collection' over wiki, articles and client returned no matches.", "source": "lookup (wiki, articles, client), re-run"}
 ],
 "confidence": 0.3,
 "wireable": false,
 "open": [
  "No acquisition route for the individual Trolls Medal of Honor is documented. Collection membership is the only sourced link, so no price, vendor, quest, drop or event source can be given.",
  "The stores.json row at line 12562 (1027 coins) is keyed to 41092, which is a name-locale id. Confirm whether the coin store keys on definition id before treating it as a vendor sale for definition 3876. It is unresolved, not a confirmed price.",
  "Live status is unsure and retired is null. No retirement or current-availability source was found in the pack.",
  "The earlier wiki key 'wiki:6:180' (List of Collections) and the locale:2099927307 citation were unsupported and are removed. The wiki list entry needs a fresh check against the wiki page before it can be cited.",
  "Every entry of collection 111 has item_link 'sanctuary'. This is unexplained and may point to a Sanctuary-only or legacy source; it was not checked.",
  "Previous answer's earlier count of seven entries was wrong; the catalogue shows eight."
 ]}
