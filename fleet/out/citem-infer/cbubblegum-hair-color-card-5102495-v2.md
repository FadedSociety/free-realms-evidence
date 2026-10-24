<!-- fleet job=citem-infer id=cbubblegum-hair-color-card-5102495-v2 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[5407, 7800, 6, 1679] model=claude-haiku-5-5 -->
# Bubblegum Hair Color Card

{"item": {"name": "Bubblegum Hair Color Card", "locale_id": 5102495, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Coin store row, store category 142 (name not confirmed in our data); purchase price 180 coins, member price 162 (10% member discount). Row is flagged no_sale=true, so this shows a store entry, not a confirmed current sale. Sibling cards 79465-79475 share the same row values.", "where": "Coin store (stores.json, category 142)", "price": "180 coins (member 162 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:17186 (item_id 79466); client coin_store_prices [180]"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Bubblegum Hair Color Card' (definition 79466, slot 3, class 1) with description 'This style card allows you to change your hair color.'", "source": "locale:5102495"},
  {"claim": "Super Spooktacular page, Week #1 - 10/1/2013 (Game Update 113): 'New [Hair] [Color] Style Cards were introduced: Snowstorm, Pumpkin, Ectoplasm, Phantasm Blue, Bubblegum'. This is a release note only; it does not name an acquisition method.", "source": "wiki: Super Spooktacular"},
  {"claim": "Coin store row for item 79466: purchase 180, member 162 (10%), no_sale true, category 142", "source": "repo:prototype/osfr-tools/data/content/stores.json:17186"},
  {"claim": "Wiki file File:Bubblegum Hair Color Card.PNG exists but its transcribed text gives no source or price", "source": "wiki: File:Bubblegum Hair Color Card.PNG"},
  {"claim": "October 2013 Monthly Member Pack items are Pinkeye and Toeny, not this card, so membership is not a source", "source": "wiki: Super Spooktacular"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor source rests on stores.json alone; no wiki, article or video confirms the coin store sale or its dates. The no_sale flag suggests it is no longer sold, but no source gives the date it left the store, so retired status is unconfirmed.",
  "The Game Update 113 release is not treated as an acquisition source; no reward, prize or event mechanic for this card is shown anywhere in the pack.",
  "Category 142 is shared with sibling Spooktacular-era cards (79465-79475) at the same 180 coin price; the category name is not confirmed.",
  "Source tags L1/L2/L3/L4/R1/R2 in stores.json are undecoded.",
  "Kind set to 'other' (style card, slot 3); the first pass said consumable, which is not confirmed by the client definition.",
  "No drop, quest, crafting or prize-wheel source was found."
 ]
}
