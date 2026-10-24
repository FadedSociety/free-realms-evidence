<!-- fleet job=citem-infer id=cmedium-health-potion-422910-v2 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[6141, 14155, 6, 2470] model=claude-haiku-5-5 -->
# Medium Health Potion

{"item": {"name": "Medium Health Potion", "locale_id": 422910, "kind": "consumable"},
 "sources": [
  {"type": "coin_shop", "detail": "Sold for coins in the Coin Shop (Supplies > Potions). Price conflicts: wiki says 25 coins; a Coin Shop video frame shows 33 coins. Neither is dated or labelled as a sale price.", "where": "Coin Shop (Supplies > Potions)", "price": "25 (wiki) / 33 (video frame, undated); unresolved", "currency": "coins", "source": "wiki page 'Medium Health Potion' (\"acquired from the Coin Shop where it sells for 25 coins\"); video:Sy-W_AHbwcw/00334.jpg (Coin Shop frame shows Medium Health Potion 33 coins)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 422910 is 'Medium Health Potion'; sibling potions share locales 422906-422915", "source": "locale:422910; locale:422906 through locale:422915"},
  {"claim": "Wiki page says it is a level 1 potion usable by any job, sold in the Coin Shop for 25 coins", "source": "wiki page: Medium Health Potion"},
  {"claim": "Coin Shop frame lists Medium Health Potion at 33 coins (undated)", "source": "video:Sy-W_AHbwcw/00334.jpg"},
  {"claim": "Tooltip: Resell Value 2, Required Level 1 Any Job, heals 16% health/second for 3 seconds, instantly heals 2%", "source": "image:item_tooltip Medium Health Potion.jpg (wiki File:Medium Health Potion.jpg)"},
  {"claim": "Battle Item Mystery Pack is a prize-wheel prize that grants 3 random battle items; it is not a health potion source by its own description", "source": "wiki page: Battle Item Mystery Pack; image:item_tooltip Battle item mystery pack.jpg; locale:6667"},
  {"claim": "Id 3021 with name locale 422910 appears only in a test fixture; in tests/pieces/test_piece_012.py 3021 is paired with the text 'This item is useable in recipes.'", "source": "repo:tests/pieces/test_piece_046.py:55-58; repo:tests/pieces/test_piece_012.py:71,113"},
  {"claim": "No coin_store_prices entry for this item in the client definition or repo stores.json", "source": "client definition; repo:prototype/osfr-tools/data/content/stores.json (no match for item 3021)"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin Shop price unresolved: wiki 25 coins vs video frame 33 coins (undated). Needs a dated store observation or a stores.json row before a price is wired.",
  "Battle Item Mystery Packs source removed: the pack's description says it grants 3 battle items, and no pack contents list confirms a Medium Health Potion. Wiki sentence alone is not enough.",
  "Effect duration conflict: client description (locale 422910) says 'over 5 seconds'; wiki and tooltip say 3 seconds at 16%/second. Check the client effect data.",
  "Item id 3021 link to locale 422910 rests on a test fixture (tests/pieces/test_piece_046.py) and test_piece_012 uses 3021 for different text; confirm against the shipped client definition table.",
  "Live status unsure: the only current-availability evidence is one undated Coin Shop frame. No retirement date found.",
  "No quest reward, enemy drop, event, crafting, or collection source was found in the pack."
 ]}
