<!-- fleet job=citem-infer id=cpet-cat-longhair-calico-chocolate-75216-v2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5534, 6654, 6, 1655] model=claude-haiku-5-5 -->
# Pet: Cat: Longhair: calico_chocolate

{"item": {"name": "Pet: Cat: Longhair: calico_chocolate", "locale_id": 75216, "kind": "pet"},
 "sources": [{"type": "vendor", "detail": "Coin store sale of the pet (store data only; no named vendor NPC in our data)", "where": "Cobblestone Village Pet Adoption Center (inferred, unconfirmed)", "price": "540 coins (member price 486 coins at 10% member discount; sell-back 54 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 6943 item 24066 (purchase_price_coins 540, member_price_coins 486, sell_price_coins 54, no_sale false, source_tags L1,L2,L4,R2,T633,R1; no vendor or category set). Location support: locale:101822 (Pet Adoption Center welcome text: pets inside the fence can be tried or bought)"}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client definition 24066 is named 'Pet: Cat: Longhair: calico_chocolate' (locale 75216), slot 0, model cat_longhair.adr, one variant", "source": "locale:75216; client definition from pack"},
  {"claim": "Our coin store data lists item 24066 at 540 coins purchase, 486 member price, 54 sell price, not marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json line 6943"},
  {"claim": "Pets are sold from the Pet Adoption Center fence in Cobblestone Village; pet outfits and accessories come from Jennifer and Gloria, not the pets themselves", "source": "locale:101822"},
  {"claim": "A same-named Shorthair variant exists (Pet: Cat: Shorthair: calico_chocolate), so the name pattern recurs across cat families", "source": "locale:75180"},
  {"claim": "No wiki page, image, article fact, video frame, vendor stock list or other answer names this pet", "source": "lookup of client, wiki, articles, video (only client hits returned)"}
 ],
 "confidence": 0.4,
 "open": [
  "The 540-coin price comes only from our store data (stores.json item 24066); no wiki or live price confirms it.",
  "The stores.json row names no vendor, so the Pet Adoption Center location is inferred from locale:101822, not confirmed for this cat.",
  "Jennifer and Gloria sell pet outfits and accessories per locale:101822; do not treat them as pet vendors for this item.",
  "The earlier claim that T638 cleared other rows to no_sale was not verified here and is not relied on.",
  "Whether the cat was ever sold for Station Cash, as a prize, or as an event item is unverified.",
  "Retirement status is unknown; no source says it was removed or stayed on sale.",
  "The Longhair calico/tabby variants (75211-75221) and the Shorthair variant (75180) each need their own sourcing check."
 ]}
