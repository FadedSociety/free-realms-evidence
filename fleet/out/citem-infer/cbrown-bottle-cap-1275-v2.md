<!-- fleet job=citem-infer id=cbrown-bottle-cap-1275-v2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5280, 6501, 6, 1595] model=claude-haiku-5-5 -->
# Brown Bottle Cap

{"item": {"name": "Brown Bottle Cap", "locale_id": 1275, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text locale:1275 is the item name 'Brown Bottle Cap'; the cap family is locale 1270-1277 (Blue, Red, Green, Silver, Orange, Brown, Black, Tin Bottle Cap).", "source": "locale:1275; locale:1270-1277"},
  {"claim": "The companion line 'This item can be added to the Multicolor Bottle Caps Collection' is locale:132282 (ui). The link from this line to the cap is only the client definition description for definition ids 3127, 3972, 11062; the earlier cite of 'description line 324828889' and flags.tsv:10389 was not verified and is dropped.", "source": "locale:132282"},
  {"claim": "The Multicolor Bottle Caps collection exists: client name locale:20774 'Multicolor Bottle Caps' (zone The Wilds), description locale:20775 'A collection of colorful bottle caps. Just looking at them can make you thirsty!'. It is listed on the wiki's List of Collections.", "source": "locale:20774; locale:20775; https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "The sibling Old Bottle Caps companion line is locale:132283 and its name is locale:20778. The earlier cite of id 1766483181 was fabricated and is withdrawn.", "source": "locale:132283; locale:20778"},
  {"claim": "Locale 1278 'Bottle Color Placeholder' is flagged placeholder and is not a cap; locale 421984 'Multicolored Bottle Caps' is a separate string not verified as this collection.", "source": "locale:1278; locale:421984"},
  {"claim": "The client definition has 3 variants (3127, 3972, 11062), no coin store price, no models, and no vendor stock.", "source": "evidence pack client_definition"},
  {"claim": "Repo collections.json names the Multicolor Bottle Caps collection at line 10098 and Old Bottle Caps at line 10154; neither lists entries for the caps.", "source": "repo prototype/osfr-tools/data/content/collections.json:10098; :10154"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is evidenced. The wiki List of Collections has the Multicolor Bottle Caps entry but no entry list, so which enemy, quest, event or vendor yields the Brown Bottle Cap (or its sibling caps) is unknown.",
  "No coin vendor sale: the store price list is empty and no vendor stocks it.",
  "Live status and retirement are unverified; no retirement evidence was found.",
  "Kind is 'other' because the schema has no collectible-member kind; the item is a member of the Multicolor Bottle Caps collection, not the collection itself.",
  "Wiki and video searches for 'Bottle Cap' found no pages or frames naming the cap."
 ]}
