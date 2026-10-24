<!-- fleet job=citem-infer id=csnowy-tulip-17494-v2 status=nothing_found turns=2 usd=0.0025 tokens(read,write,in,out)=[5412, 11667, 6, 2017] model=claude-haiku-5-5 -->
# Snowy Tulip

{"item": {"name": "Snowy Tulip", "locale_id": 17494, "kind": "collection"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name 'Snowy Tulip' is client text locale 17494; the item definition is 9126 and it is entry 3 of 8 in collection 234 (Snowhill Tulips, name locale 17572, description locale 17582).", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:17644-17679; repo:prototype/osfr-tools/data/content/collections.json:5839 ('Snowhill Tulips')"},
  {"claim": "All eight collection entries (items 9124-9131, including 9126) carry item_link 'sanctuary'. This is a link tag in the catalogue, not an acquisition source, and it suggests the entries come from the Sanctuary reference set.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:17660, 17669, 17678 (and the same field on the other five entries)"},
  {"claim": "The collection-completion reward (3 coins, item 11041 x1, 50 XP, unlocks collection 242) belongs to the whole collection 234. It does not name item 9126 and is not a source for it.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:17726-17745"},
  {"claim": "Client description 'This item can be added to the Snowhill Tulips Collection' is said to be locale:132491. Not re-verified in this pass.", "source": "pack client_definition (unverified)"},
  {"claim": "No coin store price: item 9126 has no entry in stores.json. Repo search for 9126 found only collection_catalogue.json:17677, so no vendor, quest, drop, or event source mentions it.", "source": "repo search for '9126' across data/content (only collection_catalogue.json:17677 matches)"},
  {"claim": "Lookup of 'Snowy Tulip' returned only the client text entry locale:17494. No wiki article, article fact, or video frame names this item.", "source": "lookup(client, wiki, articles, video) 'Snowy Tulip'"},
  {"claim": "The earlier wiki citation 'List of Collections (rev 27852) lists [Snowhill] [Tulips]' was not re-checked. The claim that a Snowhill location page lists the tulips was not found and is dropped.", "source": "pack previous_answer (unverified)"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found for item 9126. Collection membership says what the tulip can be added to, not how a player gets it. The previous answer's collection-completion reward is collection-level, not an item source, and has been removed from sources.",
  "No coin vendor, Station Cash marketplace, coin shop, quest, drop, event, prize wheel, crafting, or promotion source found in repo or wiki. Next step: check the Snowhill tulip gathering or seasonal event sources in client/video material, or check whether the Sanctuary reference set lists the tulip under a source.",
  "Live status is unconfirmed. The item_link 'sanctuary' tag on all eight tulips is the only field bearing on it, and no retirement source was found.",
  "Locale 132491 (description) was cited in the pack but not re-verified here.",
  "The other seven tulip variants (9124, 9125, 9127-9131) share the same collection and were not checked for their own sources."
 ]}
