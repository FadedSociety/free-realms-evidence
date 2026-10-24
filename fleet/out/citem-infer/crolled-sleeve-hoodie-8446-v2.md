<!-- fleet job=citem-infer id=crolled-sleeve-hoodie-8446-v2 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[17355, 12549, 8, 2293] model=claude-haiku-5-5 -->
# Rolled-Sleeve Hoodie

{"item": {"name": "Rolled-Sleeve Hoodie", "locale_id": 8446, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale, vendor/NPC not identified (no vendors.json row for item 190). Row is category 103, tint group 1, same price band as items 191, 194, 199.", "where": null, "price": "270 coins (member price 243 coins, 10% member discount; sell price 27)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 119 (item 190); client coin_store_prices 270"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 190 is 'Rolled-Sleeve Hoodie', NameId 8446, chest slot, class 1; 67 definitions share the name", "source": "locale:8446; refs TCG-Files/Emulator/Resources/ClientItemDefinitions.json lines 4055-4062 (per evidence pack)"},
  {"claim": "Coin store row for item 190: category 103, purchase 270 coins, member 243, sell 27, not no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json line 119"},
  {"claim": "Farmer wiki page lists 'Rolled Sleeve Hoodie' under the 'Vaultberry items' heading, Girls Only, with no price or acquisition method. Page line 4 only says Farming yields coins and items including Vaultberries in the Station Cash item.", "source": "wiki page Farmer, refs freerealms-wiki/wikitext/3042-45266-69ff7be92ceb.wiki lines 4, 10, 43, 58"},
  {"claim": "Adventurer wiki page also lists the Rolled Sleeve Hoodie (Girls Only) in its Vaultberry clothing section; no acquisition method given", "source": "wiki page Adventurer, freerealms-wiki/wikitext/2101-46030-93596a5e3d45.wiki lines 168, 194 (per evidence pack)"},
  {"claim": "Locale string 2484 'Rolled Sleeve Hoodie' (no hyphen) and 2735521134 'Rolled Sleeve Hoodie' are separate string ids from 8446 and are not this item's NameId; the hyphenated 8446 is the definition's name. Unverified whether those strings belong to other item definitions.", "source": "locale:2484; locale dump opening-mining-native-20261009T121330Z/locale/en_us_data.dat line 72092 (2735521134)"},
  {"claim": "No retirement or live-date evidence found for this item in wiki, articles or video", "source": "lookup not repeated; absence in pack (wiki_page null, video [], articles [])"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin vendor/NPC that sells item 190 is unknown: no vendors.json row and no vendor_stock in the pack. Find the coin store category 103 vendor to name it.",
  "The Vaultberry listing on the Farmer and Adventurer pages is NOT counted as a source: the pages list it under 'Vaultberry items' but give no price and no acquisition method. Farmer line 4 ties Vaultberries to Farming and the Station Cash item only. Record as unconfirmed listing if needed.",
  "Live status unsure: the Legacy-era coin row (source tags L1,L2,L4,R2,T633,R1) shows past sale, not current sale. No dated retirement evidence either way.",
  "67 client definitions share the name; the coin row is for definition 190 only. Other tints/races (e.g. 984-988, 15520-15525) have no store rows checked here, so their sources are unverified.",
  "Confirm whether locale 2484 and 2735521134 ('Rolled Sleeve Hoodie', no hyphen) are the same item or a different one before merging any wiki listing with item 190."
 ]}
