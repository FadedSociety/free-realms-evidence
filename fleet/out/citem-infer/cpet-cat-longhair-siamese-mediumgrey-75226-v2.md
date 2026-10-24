<!-- fleet job=citem-infer id=cpet-cat-longhair-siamese-mediumgrey-75226-v2 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[5760, 13042, 6, 2252] model=claude-haiku-5-5 -->
# Pet: Cat: Longhair: siamese_mediumgrey

{"item": {"name": "Pet: Cat: Longhair: siamese_mediumgrey", "locale_id": 75226, "kind": "pet"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for pet item 24076 (cat_longhair siamese_mediumgrey). Store data gives no vendor NPC or shop section; the listing is unverified (see open).", "where": null, "price": "540 coins (member price 486 coins, 10% member discount; sell price 54 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 24076 (line 6953); client definition coin_store_prices [540]"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name for item 24076 is 'Pet: Cat: Longhair: siamese_mediumgrey' (locale 75226), one definition, model cat_longhair.adr, slot 0, class 0", "source": "locale:75226; client definition in pack"},
  {"claim": "Store data has a 540-coin purchase price for item 24076, no_sale=false, 10% member discount to 486, sell price 54", "source": "repo:prototype/osfr-tools/data/content/stores.json item 24076 (line 6953)"},
  {"claim": "The same 540/486/54 block with identical source tags covers items 24063-24078 and 24079's provenance note calls its 540 a 'Legacy coin Cost' that was cleared (its price was reconstructed as 200 Station Cash, SC Marketplace, from the Tao wiki page, rev 47857). So the block-wide 540 is a legacy-style value that may not be a verified Coin Shop price", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6940-6956"},
  {"claim": "The 'Pet: Cat: Longhair' colour cluster is locale 75221-75229; the Shorthair siamese_mediumgrey is locale 75190, a separate item", "source": "locale:75190; locale:75226; locale:75221-75229"},
  {"claim": "cat_longhair.adr is a real client model used by several NPCs, so the model exists in the client; this does not show any sale channel", "source": "repo:prototype/osfr-tools/data/content/npc_spawns_extra.json; FreeRealms-Legacy/src/Resources/Npcs.json lines 960, 974, 10383, 16989"},
  {"claim": "Pets.md says pets are bought through the Station Cash Marketplace and adoption centres, and gives pet prices in Station Cash (175-749); this conflicts with the coin listing", "source": "repo:notes/Build Guides/Gameplay/Pets.md lines 214-220"}
 ],
 "confidence": 0.3,
 "open": [
  "The coin_shop source rests only on the stores.json row for 24076. The 540 value is shared across the 24063-24078 block and the 24079 provenance note calls its 540 a cleared legacy cost, so the coin price may be a placeholder. Not verified against a live coin shop listing.",
  "Pets.md (Station Cash 175-749, marketplace and adoption-centre purchase) conflicts with a coin price for this pet. Possible answers: SC Marketplace at an unknown price, or adoption-centre purchase. Neither is confirmed for this variant.",
  "No wiki page, article, video frame, quest, drop, event or prize-wheel source names this variant. The store tags (L1, L2, L4, R2, T633, R1) were not decoded to a named shop.",
  "Retired status unknown. The store row has no_sale=false, which is not evidence it is sold now. Live is therefore 'unsure', not confirmed.",
  "The other colour variants (75221-75229) were not individually checked for their own sources."
 ]}
