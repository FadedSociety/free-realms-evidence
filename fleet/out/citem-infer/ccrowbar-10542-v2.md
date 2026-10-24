<!-- fleet job=citem-infer id=ccrowbar-10542-v2 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[5486, 15522, 6, 1888] model=claude-haiku-5-5 -->
# Crowbar

{"item": {"name": "Crowbar", "locale_id": 10542, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Coin store sale of the base Crowbar (item 4400, tint group 1). Items 4401 (tint 2) and 4402 (tint 3) carry the same row. The selling NPC/vendor is not identified: no vendors.json entry stocks 4400-4402.", "where": null, "price": "5 coins (member price 4 coins, 10% member discount; sell-back 1 coin)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 840-842 (item 4400, 4401, 4402)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client item 4400 is named Crowbar (NameId 10542), weapon class 5, slot 7, model club_ar_ag_weapon_crowbar.adr, cost 5, member discount 10%, tintable.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json lines 81538-81558"},
  {"claim": "Store rows for 4400, 4401, 4402 give purchase_price_coins 5, member_price_coins 4, sell_price_coins 1, no_sale false, tags L1, L2, L4, R2, T633, R1. Item 4435-4437 (also 5 coins) share the same row shape.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 840-845"},
  {"claim": "Locale 10542 is the item name 'Crowbar'.", "source": "locale:10542"},
  {"claim": "No wiki page, article fact, or video frame names the Crowbar (lookup returned no matches in wiki, articles, video).", "source": "lookup wiki/articles/video 'Crowbar': no matches"}
 ],
 "confidence": 0.5,
 "open": [
  "Vendor not identified: the 5-coin store row is evidence of a coin sale, but no vendors.json stock entry or wiki page names the seller or zone, so 'where' is null.",
  "Crafting dropped as a source. Locale 4345 ('Match 3: Forging Clover Crowbar') and 4346 (its objective) show a forging quest for a clover crowbar exists, but nothing in the pack shows it grants item 4400. Needs a quest-reward check.",
  "Chocolate Crowbar forging quest (locale 4353, 4354) is FLAGGED placeholder text and is not used as evidence; its tint's availability is unverified.",
  "Only tints 4400-4402 (and 4435-4437 in the same price row) are priced. The other definitions (4403-4411 and up to 51 total) have no price in stores.json here, so they are unconfirmed.",
  "Retired status and current availability are unknown: the store row's tags (T633, R1) are the only availability signal and no dated source covers it.",
  "Previous 'vendor' label was inferred from the price alone; it is kept here because the rules treat a client coin store price as evidence of a coin vendor sale, but the seller remains unknown."
 ]
}
