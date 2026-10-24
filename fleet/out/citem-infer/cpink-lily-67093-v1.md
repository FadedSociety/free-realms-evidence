<!-- fleet job=citem-infer id=cpink-lily-67093-v1 status=done turns=7 usd=0.0046 tokens(read,write,in,out)=[72887, 16611, 16, 3576] model=claude-haiku-5-5 -->
# Pink Lily

{"item": {"name": "Pink Lily", "locale_id": 67093, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Pink Lily is one of 8 entries (index 6, item_definition_id 23480) of the 'Lilies' collection (collection id 184, name locale 67550). Completing the collection's entries gives the reward: 3 coins, item 9123 x1, and 50 XP (profile 14).", "where": "Sanctuary", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:14706-14800 (id 184, entry id 1355); repo:prototype/osfr-tools/data/content/collections.json:5415-5440 ('Lilies', wiki:3:75, source wiki 'List of Collections'); wiki page 'List of Collections' lists [Lilies] under Collections"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 'Pink Lily' is locale 67093 with description 'This item can be added to the Lilies Collection' (locale 2289795387 family), definition 23480.", "source": "locale:67093; locale text table (ucdt 'This item can be added to the Lilies Collection')"},
  {"claim": "Pink Lily is entry index 6 of the Lilies collection (id 184, description locale 67662 'A collection of lilies as beautiful as the sunrise.'), item_link sanctuary, icon tint 92.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:14763-14768"},
  {"claim": "The Lilies collection's sibling entries are Red Lily (67088), Orange, White, Purple, Yellow, Pink, Green, Blue Lily (67088-67095), with Purple/Red/Pink Orchid in the same cluster.", "source": "client_cluster in pack; repo:collection_catalogue.json:14706-14787"},
  {"claim": "The collection is listed on the wiki's 'List of Collections' page as [Lilies], separate from 'Snowhill [Lilies]' (a different collection with its own client text 'This item can be added to the Snowhill Lilies Collection').", "source": "wiki page 'List of Collections' (lookup wiki); locale:132496"},
  {"claim": "Pink Lily is a collection piece, not a coin-store item: client coin_store_prices is empty and no stores.json entry was found.", "source": "client definition in pack; repo search of data/content for 23480 / Lilies"}
 ],
 "confidence": 0.6,
 "open": [
  "How an individual Pink Lily is obtained (gathering, drops, or purchase) is not shown in any source checked; the only confirmed source is the collection itself. The Briarwood notes mention Ammi Lily gathering, but that is a different item.",
  "Reward item 9123 (part of the completion reward) was not named; its locale was not resolved.",
  "No wiki article or video frame names Pink Lily directly; the wiki 'List of Collections' page confirms the Lilies collection only by name and has no per-entry detail.",
  "The 'Lilies' collection's date and any retirement were not found; retired is left null."
 ]}
