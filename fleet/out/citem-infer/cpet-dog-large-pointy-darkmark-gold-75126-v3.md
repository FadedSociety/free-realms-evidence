<!-- fleet job=citem-infer id=cpet-dog-large-pointy-darkmark-gold-75126-v3 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[14311, 9247, 8, 1911] model=claude-haiku-5-5 -->
# Pet: Dog: Large Pointy: darkmark-gold

{"item": {"name": "Pet: Dog: Large Pointy: darkmark-gold", "locale_id": 75126, "kind": "pet"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop catalogue row for item 23976 only. No vendor NPC, zone or stock list is evidenced. Catalogue-membership, not confirmed stock.", "where": null, "price": "540 coins (purchase list price); 486 coins member price (10% discount, computed); 54 coins sell-back (server resale rule, not an observed price)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:6853 (item_id 23976, purchase_price_coins 540, member_discount_percent 10, member_price_coins 486, sell_price_coins 54, tags L1,L2,L4,R2,T633,R1); FreeRealms-Legacy/src/Resources/CoinStoreItems.json:31363; FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:489572-489590 (Cost 540); notes/Research/Coin Shop.md lines 33-41 (member price is R2 arithmetic; sell-back is T633 rule)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 23976 is named 'Pet: Dog: Large Pointy: darkmark-gold' at locale:75126, model dog_large_pointy.adr, one variant", "source": "locale:75126; client definition in pack"},
  {"claim": "Reference server CoinStoreItems lists item 23976 as a catalogue row with Cost 540", "source": "FreeRealms-Legacy/src/Resources/CoinStoreItems.json:31363; ClientItemDefinitions.json:489572-489590"},
  {"claim": "Repo derived store row carries purchase 540, member 486 (10%), sell 54, all computed from Cost by the Coin Shop rules", "source": "repo:prototype/osfr-tools/data/content/stores.json:6853; notes/Research/Coin Shop.md lines 33-41"},
  {"claim": "Sibling color variants share the naming pattern (locale 75121-75131, 75153 darkmark-tan seen in lookup); naming only, not sale status", "source": "lookup client results; client cluster in pack"},
  {"claim": "Repo search for 23976 finds no vendor, quest, drop, event or wiki reference beyond the stores.json row", "source": "search repo '23976'"},
  {"claim": "No wiki page, image, article fact, or video mention for this pet was found in lookup", "source": "lookup client/wiki/articles/video 'Dog Large Pointy darkmark'"}
 ],
 "confidence": 0.3,
 "open": [
  "No vendor NPC or zone evidenced. The coin_shop entry is a catalogue row derived from the Legacy CoinStoreItems Cost (540), not a stock list. Stocking in a live store is unverified.",
  "The 540 price is the Legacy Cost field, not checked against any wiki, article, video or in-game transaction. The sibling rows (e.g. stores.json item 23978, line 6855) are not corroboration; that row's note says no coin vendor stocks it.",
  "The 486 member price and 54 sell-back are computed arithmetic and server resale policy, not observed prices.",
  "live is unsure: the only sale signal is the catalogue row. No retirement source found either, so retired is null.",
  "Locale 75152 and 75154 store rows were not checked.",
  "No Station Cash, prize wheel, drop, event, quest or crafting source found."
 ]}
