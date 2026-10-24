<!-- fleet job=citem-infer id=cstudent-wizard-cap-26076-v2 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[5180, 9299, 6, 2047] model=claude-haiku-5-5 -->
# Student Wizard Cap

{"item": {"name": "Student Wizard Cap", "locale_id": 26076, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop catalogue row for item 26076 (tint group 2). Price is a reconstruction from the Legacy-derived CoinStoreItems Cost field, not confirmed against a client transaction. Not sold by any NPC vendor in our vendor data.", "where": "Coin Shop (tab unknown; stores.json category_id 6 is not mapped to a named tab)", "price": "270 coins as reconstructed (member price 243 coins, computed at 10% member discount; reconstruction, unverified)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:14262; repo:notes/Research/Coin Shop.md lines 25-34 (catalogue built from Legacy reference data; Cost-as-price mapping unchecked against a real client transaction)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Student Wizard Cap' is locale 26076 (item definition 12178, slot 1, class 8, model caster_<race>_<gender>_head_pointedcap.adr, one variant)", "source": "locale:26076"},
  {"claim": "Coin store catalogue has a non-no_sale row for item 26076 at 270 coins, member price 243 (reconstructed)", "source": "repo:prototype/osfr-tools/data/content/stores.json:14262"},
  {"claim": "The catalogue was built from Legacy reference data (CoinStoreItems.json from Legacy revision 9e082025...), not from the shipped client; the Cost-as-price mapping is unverified", "source": "repo:notes/Research/Coin Shop.md lines 25-34"},
  {"claim": "A Cakemstein video frame in Merry Vale lists 'Student Wizard Cap' among wizard hats seen on screen; it shows the name only, not a shop, seller or price", "source": "video:gxAPpQZccYw/00010.jpg"},
  {"claim": "Client text lookup finds only the item name; no wiki page or article names this cap", "source": "lookup client/wiki/articles for 'Student Wizard Cap' (only locale:26076)"}
 ],
 "confidence": 0.3,
 "open": [
  "Price 270 / member 243 are reconstructed from the Legacy-derived catalogue, not client-confirmed or wiki-confirmed. Treat as unverified.",
  "The 27-coin sell-back value was removed as a sourced fact. Per notes/Research/Coin Shop.md lines 36-41 it is a reconstruction rule (purchase // 10), not catalogue or client data.",
  "The pack's client_definition coin_store_prices field is empty, but the repo catalogue has a row for 26076. The field refers to the client, so the two do not conflict; the repo row is the only price source.",
  "The coin_shop source rests on the catalogue row alone. No wiki page, article or client transaction confirms the listing or that it is sold today.",
  "Row 26076 sits in a block 26069-26084 with the same 270-coin price and tag set. The client does not name this as a set or promotion, so no set or promotion is claimed.",
  "No evidence that the cap was a quest reward, enemy drop, prize-wheel item or event item. No other answer in the pack mentions it.",
  "Retired status and current availability are unknown. The row is not marked no_sale, but that is not proof it is sold now."
 ],
 "critiques_addressed": "Evidence critique: (1) price now labelled reconstructed/unverified; (2) 27-coin sell price dropped as sourced fact; (3) 'client CoinStoreItems' corrected to Legacy reference data; (4) confidence lowered from 0.6 to 0.3 and the video frame is treated as existence-only."}
