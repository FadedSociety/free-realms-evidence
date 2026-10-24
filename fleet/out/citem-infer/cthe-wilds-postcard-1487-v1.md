<!-- fleet job=citem-infer id=cthe-wilds-postcard-1487-v1 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[28657, 14142, 10, 2619] model=claude-haiku-5-5 -->
# The Wilds Postcard

{"item": {"name": "The Wilds Postcard", "locale_id": 1487, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Member of the [Postman] Postcards collection (client UI text: \"This item can be added to the Postman Postcards Collection\", locale:132355). Listed on the wiki with Cobblestone Village, Briarwood, Sanctuary, and Snowhill Postcards. Acquisition route for the Wilds Postcard itself is not documented.", "where": null, "price": null, "currency": null, "source": "wiki: Job Specific (Collections) (lists \"Wilds Postcard\" under [Postman] [Postcards]); wiki: List of Collections (lists [Postman] [Postcards]); locale:7747, locale:132355"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item 3339 is 'The Wilds Postcard', NameId 1487, DescriptionId 24229 (\"This item can be added to a collection.\"), a stackable type-1 item with Cost 1 and CategoryId 19. It is not a coin store item.", "source": "refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 61953-61960"},
  {"claim": "The wiki's Job Specific (Collections) page lists 'Wilds Postcard' under the [Postman] [Postcards] collection, next to the Cobblestone Village, Briarwood, Sanctuary and Snowhill Postcards.", "source": "wiki: Job Specific (Collections)"},
  {"claim": "The wiki's List of Collections page includes the [Postman] [Postcards] collection.", "source": "wiki: List of Collections"},
  {"claim": "The client text ties the postcard to the Postman Postcards collection: locale 132355 'This item can be added to the Postman Postcards Collection' and locale 7747 'Postman Postcards'.", "source": "locale:132355, locale:7747"},
  {"claim": "Wiki page 'Postman' lists the Postman Postcards collection (with Packages and Envelopes and Stamps). The Sanctuary Postcard is the reward for completing [Postman] Packages and Envelopes, and the Penguin Stamp is the reward for completing [Postman] Postcards. Neither source says how the Wilds Postcard is earned.", "source": "wiki: Job Specific (Collections); wiki: Postman"},
  {"claim": "The Wilds Postcard has an icon asset (icon_item_postcard_wilds) in the asset manifest.", "source": "refs: osfr-asset-manifest/Assets_manifest.txt lines 104169-104171"},
  {"claim": "No coin vendor stock, quest reward, drop, or event source for the Wilds Postcard was found in the repo, the client, or the wiki. The coin store has no price for item 3339.", "source": "search repo/refs for 'Postcard|3339'; vendor_stock empty in pack"}
 ],
 "confidence": 0.5,
 "open": [
  "How a player obtains a Wilds Postcard is undocumented. The only confirmed link is collection membership. Check the Postman job quests and the Postman collection rewards for the source.",
  "No coin-store price (the item has no entry in stores.json) and no wiki price. Do not assume a vendor sale.",
  "Retirement status is unknown. The wiki lists it in the current collections page, so it is probably live, but no source gives a date.",
  "The client's 'Cost: 1' is an item-definition field, not a store price, and is not used as one here."
 ]}
