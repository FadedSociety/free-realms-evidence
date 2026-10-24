<!-- fleet job=citem-infer id=cpink-small-sweater-blouse-106880-v1 status=done turns=5 usd=0.0046 tokens(read,write,in,out)=[40921, 20102, 12, 3388] model=claude-haiku-5-5 -->
# Pink Small Sweater Blouse

{"item": {"name": "Pink Small Sweater Blouse", "locale_id": 106880, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Coin Shop sale of the Pink Small Sweater Blouse (tint groups 1-3 are separate rows: stores.json item_id 33798, 33799, 33800; all three at the same price, category 103)", "where": "Coin Shop", "price": "270 coins (member price 243 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:7762-7764 (item 33798/33799/33800, purchase_price_coins 270); repo:notes/Research/Coin Shop.md (stores.json rows are the Coin Shop price data)"}],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client name 'Pink Small Sweater Blouse' is locale 106880, one name shared by 35 client definitions (ids 33798-33809 listed in the pack); slot 3, class 1, model freestyle_<race>_f_chest_fittedshortslvshirt.adr", "source": "locale:106880"},
  {"claim": "Coin Shop row exists for definition 33798 at 270 coins, with the same 270 price on tint groups 2 and 3 (33799, 33800); no_sale false, so it is sellable; sell-back is 27 coins under the T633 rule (one tenth of price)", "source": "repo:prototype/osfr-tools/data/content/stores.json:7762-7764; repo:notes/Autopilot/T633.md"},
  {"claim": "Video frame shows a farm reward line 'You receive 1 Pink Small Sweater Blouse Basic Topsoil' at Wilds Farm during Power Hour, so the name appears in a farming context", "source": "video:pjvw6oAT-zQ/00134.jpg"},
  {"claim": "Wiki pages Farmer and Adventurer list an item named '[Pink] [Small] [Sweater] [Blouse]' among their clothing listings", "source": "lookup wiki page:ns0 Farmer; page:ns0 Adventurer"}
 ],
 "confidence": 0.55,
 "open": [
  "The Coin Shop price is the only firm source. No vendor_stock, drop, quest or event answer names this item, so no vendor source is claimed.",
  "The video line reads 'Pink Small Sweater Blouse Basic Topsoil', which is most likely a farm item (topsoil) whose name shares the bracketed name template. It is not evidence that the blouse itself is a farm reward. Needs a clean frame check.",
  "The wiki Farmer and Adventurer listings are not explained by the pack (they could be class-outfit or item-template lists). They are not used as a source here; check the pages for whether this is a Coin Shop or job outfit entry.",
  "Retirement status is unknown: the repo has no date or retirement flag for the Coin Shop row, and no wiki category like 'Retired' or 'Coin Shop' was found for this item. Confirm against the Coin Shop wiki category.",
  "The pack gives 35 definitions but the store rows listed are only 33798-33800 in the stores data; the rest of the tints (33801-33809 and others) have no verified price."
 ]}
