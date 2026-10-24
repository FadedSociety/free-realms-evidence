<!-- fleet job=citem-infer id=cchef-s-eggbeater-of-talent-iv-29527-v2 status=done turns=3 usd=0.0023 tokens(read,write,in,out)=[12945, 9302, 8, 2006] model=claude-haiku-5-5 -->
# Chef's Eggbeater of Talent IV

{"item": {"name": "Chef's Eggbeater of Talent IV", "locale_id": 29527, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Ingrid (pixie female Chef gear merchant); wiki Sells list names Chef's Eggbeater of Talent IV", "where": "Stillwater Crossing (NPC placement from repo npc data, not from the wiki Sells section)", "price": "1504 coins listed as a stores.json reference price, not a captured NPC quote; member price field 1353 coins (10% member discount field in stores.json). No wiki price was found.", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Ingrid (Sells section, revision 2025-03-26); repo:prototype/osfr-tools/data/content/vendors.json:38178-38217 (price_basis marked '(R) stores.json reference price; no captured retail NPC quote'); repo:prototype/osfr-tools/data/content/stores.json:15412 (item 75594, purchase_price_coins 1504, member_price_coins 1353, sell_price_coins 150); locale:29527"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Chef's Eggbeater of Talent IV', locale 29527, definition 75594, slot 7, class 21, one variant", "source": "locale:29527; client definition in pack; repo:prototype/osfr-tools/data/content/vendors.json:38178-38181"},
  {"claim": "Ingrid's wiki Sells list includes Chef's Eggbeater of Talent IV (listed by name, no price shown in the excerpt)", "source": "https://freerealms.fandom.com/wiki/Ingrid (Sells); vendors.json:38193-38201 stock_source"},
  {"claim": "Wiki Ingrid trivia says she was introduced in-game on the update of October 1, 2013", "source": "https://freerealms.fandom.com/wiki/Ingrid (Trivia)"},
  {"claim": "Other Chef vendors also list Talent/Timing Chef eggbeaters at different tiers: Zamzani (Eggbeater of Talent II/Timing II range), Rachael (Eggbeater of Timing IV), Mikael (Eggbeater of Talent V). None of these lists Talent IV for Zamzani, Rachael or Mikael in the excerpts.", "source": "wiki pages Zamzani, Rachael, Mikael (lookup excerpts)"},
  {"claim": "Price 1504 is a stores.json reference price, not an NPC-verified quote; the 'member discount' is a stores.json field value only", "source": "vendors.json:38186, 38215; stores.json:15412"}
 ],
 "confidence": 0.6,
 "open": [
  "Vendor price is unverified at the NPC: 1504 coins is the stores.json reference price and no wiki or captured quote confirms it.",
  "Current availability is unknown. The wiki Sells list (2025 revision) names the item, which suggests it was sold at some point, but no retirement date or 'no longer sold' statement was found.",
  "No drop, quest, crafting, event, or membership source was found in the pack.",
  "Kind set to 'other' (Chef tool, class 21, slot 7); the model file name says weapon, but the client classes it as a tool."
 ]}
