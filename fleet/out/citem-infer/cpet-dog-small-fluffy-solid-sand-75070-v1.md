<!-- fleet job=citem-infer id=cpet-dog-small-fluffy-solid-sand-75070-v1 status=done turns=9 usd=0.0054 tokens(read,write,in,out)=[86709, 19026, 20, 4376] model=claude-haiku-5-5 -->
# Pet: Dog: Small Fluffy: solid-sand

{"item": {"name": "Pet: Dog: Small Fluffy: solid-sand", "locale_id": 75070, "kind": "pet"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale, listed at 540 coins (unnamed vendor; the store row carries no vendor or NPC name)", "where": "Coin Shop (coin store row)", "price": "540 coins (member price 486 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23920 (purchase_price_coins 540, member_price_coins 486, sell_price_coins 54; tint_group_id 1); the 540 is a legacy Cost value, per notes/Research/Coin Shop.md:33-34 not checked against a real transaction"},
  {"type": "vendor", "detail": "Pet species York (dog_small_fluffy.adr model), wiki-listed as an SC Marketplace pet at 225 SC (202 SC member). The York species row does not bind to item 23920; the Pets Service note maps York to item 23930 (lightmark tint), so this sale applies to the species, not confirmed for the solid-sand tint", "where": "SC Marketplace", "price": "225 Station Cash (member 202 SC)", "currency": "station_cash", "source": "repo:prototype/osfr-tools/data/content/pets.json lines 26547-26586 (York, adoption_source sc_marketplace, wiki 'York' archived rev 2023-08-14); repo:notes/Research/Pets Service.md:154"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 75070 is 'Pet: Dog: Small Fluffy: solid-sand', one of 10 tints (75066-75075) sharing the dog_small_fluffy model family", "source": "locale:75070; client cluster locale:75066-75075"},
  {"claim": "Item 23920 is a Coin Shop row with purchase price 540 coins, member 486, not no_sale, tint_group 1", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23920"},
  {"claim": "Row source tags L1,L2,L4,R2,T633,R1 are data-field and arithmetic tags, not a vendor name; the 540 is a legacy Cost value", "source": "notes/Research/Coin Shop.md:33-34"},
  {"claim": "Sibling item 23913 has an SC Marketplace price of 225 with a wiki Pavel source, and its legacy coin cost 540 was cleared; 23920 was not given the same treatment", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23913 (price_provenance)"},
  {"claim": "Dog species York uses dog_small_fluffy.adr and is wiki-listed at 225 SC (202 member) on the SC Marketplace", "source": "repo:prototype/osfr-tools/data/content/pets.json lines 26547-26586"},
  {"claim": "Client has a separate 'Illusion: Dog Small Fluffy' 30-minute item, which is not this pet", "source": "locale:147585"}
 ],
 "confidence": 0.3,
 "open": [
  "No vendor or NPC is named for the 540-coin sale; the coin store row has no vendor binding, so the vendor 'where' is unknown. Needs a coin vendor stock list or a wiki page for the dog pet tints.",
  "The 540-coin price is a legacy Cost value that the store notes say was not checked against a real transaction. The 225 SC York price may or may not apply to this tint.",
  "No wiki page, image, article, video or quest/drop answer names locale 75070 or the solid-sand tint. The York species wiki page is the only source found for the dog model.",
  "Client-side ID mapping conflict: pets.json says York's item id is unresolved, while Pets Service maps York to item 23930 (lightmark), not 23920. Item 23920 is not confirmed as York.",
  "Retirement and later availability are unknown. The store row is not no_sale, so it may still be live, but no source confirms that."
 ]}
