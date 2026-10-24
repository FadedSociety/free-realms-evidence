<!-- fleet job=citem-infer id=ccrystal-caster-2146-v2 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[12360, 6939, 8, 2577] model=claude-haiku-5-5 -->
# Crystal Caster

{"item": {"name": "Crystal Caster", "locale_id": 2146, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Coin store, weapon category 107: Crystal Caster definition 870 (Class 39, Cost 338), sold for coins. No vendor NPC named in any source; the store row is a store listing, not a confirmed NPC vendor", "where": "coin store, category 107 (weapons)", "price": "338 coins (purchase_price_coins; member_price_coins 304 at 10% member discount)", "currency": "coins", "source": "prototype/osfr-tools/data/content/stores.json line 385 (item_id 870, category_id 107, purchase_price_coins 338, member_price_coins 304); client ClientItemDefinitions Id 870 Cost 338"},
  {"type": "other", "detail": "Coin store, weapon category 107: Crystal Caster definition 1187 (Class 23, NoTrade). Low-price variant; relation to 870 not established. No vendor NPC named", "where": "coin store, category 107 (weapons)", "price": "10 coins (purchase_price_coins; member_price_coins 9)", "currency": "coins", "source": "prototype/osfr-tools/data/content/stores.json line 420 (item_id 1187, category_id 107, purchase_price_coins 10, member_price_coins 9); client ClientItemDefinitions Id 1187 Cost 10"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Crystal Caster' is locale 2146, item class text; the name covers 12 client definitions (870, 871, 872, 1187-1189, 7245-7250) with 55 variants", "source": "locale:2146; client definition pack"},
  {"claim": "Definition 870: Crystal Caster, Cost 338, Class 39, slot 7, model wand_ar_ag_weapon_crescent.adr", "source": "refs FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json Id 870"},
  {"claim": "Store row for item 870: category 107, purchase 338 coins, 10% member discount, member price 304 coins, sell price 33", "source": "prototype/osfr-tools/data/content/stores.json:385"},
  {"claim": "Store row for item 1187: category 107, purchase 10 coins, member price 9, sell price 1", "source": "prototype/osfr-tools/data/content/stores.json:420"},
  {"claim": "Store rows carry source_tags (L1, L2, L4, R2, T633, R1) whose meaning is not documented in the pack", "source": "prototype/osfr-tools/data/content/stores.json:385, :420"},
  {"claim": "No wiki page, article, image or video frame names Crystal Caster (lookup returned no matches for wiki, articles, video)", "source": "lookup wiki/articles/video 'Crystal Caster'"},
  {"claim": "Collection catalogue ids 870 and 1187 point to different item_definition_ids, so not a collection reward for this weapon", "source": "repo:data/content/collection_catalogue.json lines 9882 and 12745 (as reported in pack; not re-checked)"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin store listing is the only evidence of acquisition. Which vendor NPC or store page sells 870 (338 coins) and 1187 (10 coins) is not named in any source.",
  "Store row source_tags (L1, L2, L4, R2, T633, R1) are not decoded here; they may indicate where the item is sold but this is unverified.",
  "Why one name has two coin prices: 1187 is Class 23 NoTrade at 10 coins, 870 is Class 39 at 338 coins. Not established whether 1187 is a starter or separate version.",
  "Live status unconfirmed: the price rows come from the rebuild's store data and the Legacy dump, and no wiki or article confirms current sale. The first-pass 'live: yes' is a hint only.",
  "Definitions 871, 872, 1188, 1189 and 7245-7250 not checked for their own prices or sources.",
  "No quest reward, enemy drop, event, or crafting source found in the pack.",
  "Client description empty (DescriptionId 1114); locale 1114 lookup returned no matches, so no description text is available.",
  "Critique correction: the evidence critic could not open the store file at data/content/stores.json, but the file exists at prototype/osfr-tools/data/content/stores.json and the 338 and 10 coin prices and the 304 and 9 member prices are present there (lines 385 and 420). The pack's price claims stand; the critic's 'unverified' objection is resolved for the store price. The Legacy CoinStoreItems.json rows still carry no price field, so cite the repo store file rather than CoinStoreItems.json for prices.",
  "Critique on type labels: the pack typed both sources 'vendor'. Changed to 'other' (coin store listing) because no vendor NPC is evidenced."
 ]}
