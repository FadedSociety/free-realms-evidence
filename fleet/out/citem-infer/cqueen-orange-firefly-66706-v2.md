<!-- fleet job=citem-infer id=cqueen-orange-firefly-66706-v2 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5601, 8411, 6, 2077] model=claude-haiku-5-5 -->
# Queen Orange Firefly

{"item": {"name": "Queen Orange Firefly", "locale_id": 66706, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry 8 of the Orange Fireflies collection (collection id 134; name locale 67500, description locale 67612). The item is added to the collection as one of its eight orange firefly entries (Small, Large, Smart, Angry, Slimy, Smelly, King, Queen).", "where": null, "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:10325-10404 (entry id 968, index 8, name_id 66706, item_definition_id 23093); locale:132393 'This item can be added to the Orange Fireflies Collection'; wiki List of Collections (https://freerealms.fandom.com/wiki/List_of_Collections) lists '[Orange] [Fireflies]' under Insects"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Queen Orange Firefly is item definition 23093 and collection entry id 968 (index 8) of collection 134, Orange Fireflies.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:10325-10404"},
  {"claim": "Client text: name locale 66706; collection name locale 67500 'Orange Fireflies'; description locale 67612 'A collection of orange fireflies.'; item text locale 132393 'This item can be added to the Orange Fireflies Collection'.", "source": "locale:66706; locale:67500; locale:67612; locale:132393"},
  {"claim": "The wiki List of Collections has an Insects section that includes '[Orange] [Fireflies]' alongside Green and Red Fireflies.", "source": "https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "Completing the collection grants 10 coins, item 23111 x1, 50 XP and collection 137 added. Item 23111 is unnamed in this pack.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:10405-10423"},
  {"claim": "All eight entries of collection 134 carry item_link 'sanctuary'; the meaning of that tag is not verified.", "source": "repo:prototype/osfr-tools/data/content/collection_catalogue.json:10330-10402"},
  {"claim": "The wiki Collections page says sparkling spawn objects yield one item from any collection depending on area. It does not name a firefly colour or a Queen spawn.", "source": "wiki Collections (locale:7816 text)"}
 ],
 "confidence": 0.5,
 "open": [
  "Wild source unconfirmed: the earlier claim that orange fireflies spawn in the central wilds at night is not supported by any wiki or client text found. Removed. Lead only: firefly spawns in the central wilds at night (wiki Spawn Types), colour not stated.",
  "No coin store price (coin_store_prices empty), no vendor, quest, enemy-drop, or marketplace source found for item 23093.",
  "Collection entry is the only evidenced acquisition; a builder cannot wire a price or drop from it, so the item is not wireable as a purchasable source.",
  "Item 23111, the collection reward, is unnamed and unverified.",
  "Live status and retirement date unverified; the wiki list is from 2013 and gives no end date. The 'sanctuary' item_link tag meaning is unverified.",
  "Revision number 27852 for the wiki list was not checked and is not cited here."
 ]
}
