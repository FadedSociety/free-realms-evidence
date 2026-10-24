<!-- fleet job=citem-infer id=cworn-down-tires-67396-v1 status=nothing_found turns=7 usd=0.0050 tokens(read,write,in,out)=[71983, 20775, 16, 3456] model=claude-haiku-5-5 -->
# Worn Down Tires

{"item": {"name": "Worn Down Tires", "locale_id": 67396, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Worn Down Tires' (locale 67396); description reads 'This item can be added to the Derby Driver Tires Collection' (locale:132479, ui string, shared text).", "source": "locale:67396; locale:132479"},
  {"claim": "The collection it feeds is the client item 'Derby Driver Tires' (locale 67588), listed as a Demolition Derby collection with id 2129583338.", "source": "locale:67588; repo:notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:215"},
  {"claim": "Locale 67700 'Demolition Derby tires collection' says: 'A collection of Demolition Derby Driver tires. Give me anything that rolls.' This is a separate string, and it does not name who takes the tires.", "source": "locale:67700"},
  {"claim": "Sister tire items sit in the same id block (67391 to 67401): Upgraded Brakes, Patched Tires, Flat Tires, Recycled Tires, Old Tires, Monster Tires, Spike Tires, Muddy Tires, plus two fuel items. No wiki page, article, video frame, vendor stock, quest or drop names any of them.", "source": "locale:67391-67401; lookup client 'Patched Tires', 'Muddy Tires', 'Spike Tires', 'Monster Tires'"},
  {"claim": "The client definition has no coin store price (coin_store_prices is empty), so no coin vendor sale is evidenced. Searches of repo data (23783, 67396, 2129583338) and wiki/article text found no acquisition source.", "source": "repo search; lookup wiki/articles"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. The item's only known link is membership in the Derby Driver Tires collection (2129583338 / locale 67588). How players get that collection, and where its tire pieces come from (Demolition Derby rewards, prize, drop, or crafting), is not documented in any source here.",
  "Not verified: the Demolition Derby quest and reward chain, and the 'Give me anything that rolls' collection NPC (locale 67700). Check whether a derby NPC accepts tires for a reward.",
  "Kind is marked 'other'. The first-pass 'collection' tag describes the collection, not this item. The item is a Demolition Derby tire part (slot 0, class 0, no models).",
  "Live status is unsure. The client ships the string, but no store, wiki, or video evidence shows it being sold, dropped, or retired.",
  "Wiki lists the Demolition Derby Driver job, but the wiki Demolition Derby page has no collection/tire list. Retirement status unknown."
 ]}
