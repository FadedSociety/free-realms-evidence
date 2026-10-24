<!-- fleet job=citem-infer id=crare-snowhill-rose-16970-v1 status=done turns=5 usd=0.0037 tokens(read,write,in,out)=[36079, 13520, 12, 3223] model=claude-haiku-5-5 -->
# Rare Snowhill Rose

{"item": {"name": "Rare Snowhill Rose", "locale_id": 16970, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry in the 'Rare Snowhill Flowers' collection (client collection name locale 16965; objective text locale 16966: 'A collection of flowers that bloom in Snowhill.'). The item's own client text (ui locale 132280) says it 'can be added to the Rare Snowhill Flowers Collection'. This is a collection piece, not a purchasable item.", "where": "Snowhill", "price": null, "currency": null, "source": "locale:16970; locale:132280; locale:16965; locale:16966; repo:prototype/osfr-tools/data/content/collections.json (key wiki:3:101, name 'Rare Snowhill Flowers', name_id 16965); wiki page List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections) lists 'Rare [Snowhill] Flowers' among collections"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 'Rare Snowhill Rose' is locale 16970, item class, two definitions (9189, 11044), no coin store price.", "source": "locale:16970; client definition pack"},
  {"claim": "Client UI text says the rose can be added to the Rare Snowhill Flowers Collection.", "source": "locale:132280"},
  {"claim": "'Rare Snowhill Flowers' is a wiki-listed collection (category 3) in the List of Collections, revision 27852 (2013-07-13).", "source": "https://freerealms.fandom.com/wiki/List_of_Collections; repo:prototype/osfr-tools/data/content/collections.json wiki:3:101"},
  {"claim": "Sibling items in the same client cluster (Rare Snowhill Tulip, Orchid, Carnation, Daisy, Lily, Sunflower, Daffodil) share the collection; the Rare Snowhill Rose is one of the 8 flower entries in the set.", "source": "locale:16967-16974"},
  {"claim": "Wiki List of Collections has a separate 'Snowhill Roses' collection (name locale 17573), which is a different collection from the Rare set; it should not be conflated with this item.", "source": "repo:collections.json wiki:3:88; List of Collections"}
 ],
 "confidence": 0.4,
 "open": [
  "No source found for how a player obtains a Rare Snowhill Rose (gathering node, enemy drop, quest, or purchase). The collection record has entries_known=false and an empty entries list, so no wiki page or other answer names the acquisition method.",
  "Locale 17590 ('1 out of every 9 flowers found is this rare') belongs to 'Exotic Snowhill Flowers', not to the Rare set. It suggests the rare flowers are found while playing, but it is not evidence for this item and was not used as a source.",
  "No coin store price exists in the client definition or stores.json, so no vendor or Coin Shop sale is claimed.",
  "No retirement or availability date was found; retired is left null.",
  "The wiki list is ambiguous on the Rare set ('Rare [Snowhill] Flowers' in one revision, 'Rare Snowhill Flowers' in another), so the collection name should be confirmed on the live wiki before import.",
  "Two definitions (9189, 11044) exist; no tint or race variant data was found to say what distinguishes them."
 ]}
