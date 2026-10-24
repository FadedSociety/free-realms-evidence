<!-- fleet job=citem-infer id=cnokizaru-ninja-shoulderguard-133227-v1 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[16933, 14721, 8, 2836] model=claude-haiku-5-5 -->
# Nokizaru Ninja Shoulderguard

{"item": {"name": "Nokizaru Ninja Shoulderguard", "locale_id": 133227, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Twisting Hornet (Ninja job merchant, added 27 August 2013); sells the Nokizaru Ninja set as Job Items", "where": "Kai's Shack, southern Seaside", "price": "403 coins (member price 362 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 76219 (purchase_price_coins 403); repo:prototype/osfr-tools/data/content/vendors.json Twisting Hornet item_ids includes 76219; https://freerealms.fandom.com/wiki/Twisting_Hornet (Sells: [Nokizaru] [Ninja] Shoulderguard)"},
  {"type": "drop", "detail": "Dungeon bonus-goal reward (Ninja clothing set chosen by job; difficulty 2 gives Nokizaru or Sekkou). Listed on the Feisty Floren and Petty Yetis dungeon pages as a bonus-goal reward option", "where": "Feisty Floren; Petty Yetis (Wilds dungeons)", "price": null, "currency": null, "source": "wiki: Feisty Floren! and Petty Yetis! (bonus reward lists, '[Nokizaru] [Ninja] Shoulderguard'); wiki: Danger Peaks / Robgoblin Treasure Trove (difficulty 2 Ninja Nokizaru or Sekkou); notes/Build Guides/Content/Jobs/Ninja.md:182"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 133227 is 'Nokizaru Ninja Shoulderguard', definition 76219, slot 6, class 2, one definition, shared with Nokizaru set pieces Gi, Armwraps, Cowl, Tabi Boots, Hakama (locale:133222-133226)", "source": "client definition; locale:133227"},
  {"claim": "Coin store price 403 (member 362, sell 40) for item 76219, category 106", "source": "repo:prototype/osfr-tools/data/content/stores.json:15909"},
  {"claim": "Twisting Hornet sells exclusively Ninja job items including the Nokizaru Shoulderguard", "source": "wiki page Twisting Hornet (revision 2013-10-02); repo:prototype/osfr-tools/data/content/vendors.json:27750-27776"},
  {"claim": "Seaside NPC note: Twisting Hornet, Ninja job merchant at Kai's Shack, added 27 August 2013", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md:128"},
  {"claim": "Nokizaru Shoulderguard appears in the bonus-goal reward lists of Feisty Floren and Petty Yetis", "source": "wiki pages Feisty Floren!, Petty Yetis!"},
  {"claim": "Live status: store data carries source tags L1,L2,L4,R2,T633,R1 and the vendor is on the 2013 wiki", "source": "repo:stores.json:15909; wiki Twisting Hornet"}
 ],
 "confidence": 0.8,
 "open": [
  "The wiki Twisting Hornet snippet gives no NPC price for the Shoulderguard; the 403 coin price comes from the store reference data (vendors.json marks it as a reference price, not a captured NPC quote).",
  "Retirement status is not stated by any source; the Twisting Hornet and set data are from 2013, so later retirement is unverified.",
  "The dungeon bonus-goal entries are wiki reward-list claims only; the exact bonus chest mechanic (drop vs reward) is not confirmed. The 'other' type was not used because the vendor source is the primary one.",
  "The pack's 'coin_store_prices: 403' matches item 76219 in stores.json, but no SC Marketplace or Coin Shop listing was found for this item."
 ]}
