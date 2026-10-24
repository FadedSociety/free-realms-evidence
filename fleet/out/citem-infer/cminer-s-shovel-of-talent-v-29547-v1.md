<!-- fleet job=citem-infer id=cminer-s-shovel-of-talent-v-29547-v1 status=done turns=6 usd=0.0044 tokens(read,write,in,out)=[61716, 18414, 14, 3051] model=claude-haiku-5-5 -->
# Miner's Shovel of Talent V

{"item": {"name": "Miner's Shovel of Talent V", "locale_id": 29547, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Cortez, sells Miner job items (wiki 'Sells' list: 'Miner's Shovel of Talent V')", "where": "Briarwood Crafting Station near the Vale of the Ancients (Mother Lode Quarry / Vale of the Ancients dig camp)", "price": "2152 coins (stores.json reference price; not a captured NPC quote). Member price 1936 coins (10% member discount). Sell-back 215 coins.", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Cortez (revision 2025-03-08); repo:prototype/osfr-tools/data/content/vendors.json:9076-9116; repo:prototype/osfr-tools/data/content/stores.json:15432 (item 75614, purchase_price_coins 2152)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 29547 is exactly \"Miner's Shovel of Talent V\" (item, definition 75614, slot 7, class 12, model tool_ar_ag_weapon_shovel.adr).", "source": "locale:29547; client definition in pack"},
  {"claim": "Wiki page Cortez lists 'Miner's Shovel of Talent V' under Sells; Cortez is a human NPC merchant at the Briarwood Crafting Station near the Vale of the Ancients selling Miner job items.", "source": "https://freerealms.fandom.com/wiki/Cortez"},
  {"claim": "Wiki Cortez/Briarwood vendor entry says the Drift Miner set and Talent/Timing V items were added 15 Oct 2013 (Witts and Boddington carry the Talent II/IV shovels, not V).", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json:1703-1745; wiki pages Cortez, Witts, Boddington, Merchants"},
  {"claim": "Coin store price 2152 for item 75614 in stores.json (member price 1936, sell 215); the vendors.json entry links this price to the Cortez stock row, labelled a reference price rather than a captured NPC quote.", "source": "repo:prototype/osfr-tools/data/content/stores.json:15432; repo:prototype/osfr-tools/data/content/vendors.json:9076-9116"},
  {"claim": "Sibling items Talent V pickaxe, Timing V shovel/pickaxe/dynamite and Shovel of Talent IV sit in the same client block (locale 29542-29550), all Miner-job tools from the same 2013 Briarwood set.", "source": "client_cluster in pack; locale:29543"}
 ],
 "confidence": 0.6,
 "open": [
  "The 2152 coin price is a stores.json reference price, not a price confirmed on the wiki or by an NPC quote; the wiki Cortez page text seen did not state a price for this shovel.",
  "No retirement or removal date found; live status is unsure (the Cortez wiki entry is from 2025 but the item may have been removed later). Check the Retired category.",
  "No quest reward, enemy drop, crafting recipe, collection, or event source found for this item in the pack or repo; none was searched beyond the vendor data.",
  "The 'Sells' list was taken from search excerpts; the full Cortez page was not read, so the exact listed name and any sale price on the wiki are unverified in full.",
  "Client lookup for the Cortez row cited 'Miner's [Shovel of Talent] V' in the wiki page snippet; treated as the same item."
 ]}
