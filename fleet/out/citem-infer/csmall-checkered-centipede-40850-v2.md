<!-- fleet job=citem-infer id=csmall-checkered-centipede-40850-v2 status=done turns=2 usd=0.0033 tokens(read,write,in,out)=[6443, 16839, 6, 2180] model=claude-haiku-5-5 -->
# Small Checkered Centipede

{"item": {"name": "Small Checkered Centipede", "locale_id": 40850, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry of the 'Checkered Centipedes' insect collection (collection 7732; collection_catalogue entry 566, item definition 3634). This is membership only, not an acquisition source. How a player gets an individual centipede is unknown.", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:6102-6119; locale:40850; locale:132340; locale:7732"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item definition 3634 is 'Small Checkered Centipede' (name locale 40850), a member of the 'Checkered Centipedes' collection (locale 7732). Its client description reads 'This item can be added to the Checkered Centipedes Collection' (locale 132340).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:6102-6119; locale:40850; locale:132340"},
  {"claim": "The wiki's List of Collections (rev 27852, 2013-07-13) lists 'Checkered Centipedes' under Insects > Common.", "source": "refs:freerealms-wiki/wikitext/2038-27852-f0e36d086ea8.wiki:162-166; https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "The wiki's second Insects table (Stage 1 to Stage 4, then Final Reward) lists 'Checkered Centipedes' (with Checkered Ants, Snails, Spiders, Fireflies) in its Stage 1 group. The chain ends at Reinforcements Have Arrived / Espionage / Ground Support / Special Forces / Air Support, then Objective Complete, then Mission Accomplished. This is NOT the Cocoons / Magnificent Butterflies chain, which is the separate first table (lines 388-399) and lists only Caterpillars.", "source": "refs:freerealms-wiki/wikitext/2038-27852-f0e36d086ea8.wiki:400-410"},
  {"claim": "No coin store price exists for definition 3634 (empty coin_store_prices in the client definition; no stores.json match for the item).", "source": "repo:data/content/stores.json (no match); client definition"},
  {"claim": "No vendor, quest, enemy drop, event or prize-wheel source for definition 3634 was found in repo, refs, client text or wiki search. The first-pass 'drop' tag has no evidence and is not used.", "source": "search of repo, refs and locale; vendor_stock and mentioned_by_other_answers empty in pack"},
  {"claim": "'Checkered Centipede Brigade' (locale 66691) is a separate item and is not covered here.", "source": "locale search: 'Checkered Centipede Brigade' ucdt 1651551367"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition is unknown. The only evidenced link is collection membership. No price, vendor, quest, enemy drop, event or crafting source was found, so the sources list has no acquisition entry. Wireable: false.",
  "Whether the Small variant feeds the wiki's Stage 1-4 Centipede chain (ending Mission Accomplished) is unverified. The chain is listed by name in the wiki, but the item is not linked to it.",
  "Live status is unsure. The client defines the item and the 2013 wiki lists the collection, but no server-side or post-2013 confirmation was found. Retired is null for the same reason.",
  "The previous answer's claim that the Insects table links Centipedes to Cocoons / Magnificent Butterflies was wrong and is withdrawn. The critiques were correct on this point.",
  "The previous answer's 'drop' guess is unsupported. Remove it unless an enemy drop record is found."
 ]}
