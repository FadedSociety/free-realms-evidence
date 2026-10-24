<!-- fleet job=citem-infer id=chydrostatic-medic-helmet-133119-v1 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[14728, 13549, 8, 2662] model=claude-haiku-5-5 -->
# Hydrostatic Medic Helmet

{"item": {"name": "Hydrostatic Medic Helmet", "locale_id": 133119, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Farnsworth, Medic Job merchant (\"sells exclusively Medic Job items\"; listed under Sells)", "where": "Blackspore Swamp (north-east of the Blackspore warpstone)", "price": "752 Coins (reference price from stores.json; member price 676 Coins; sell-back 75 Coins)", "currency": "coins", "source": "wiki page Farnsworth (https://freerealms.fandom.com/wiki/Farnsworth, Sells section); repo:prototype/osfr-tools/data/content/stores.json item 76111 (purchase_price_coins 752, category 101); repo:prototype/osfr-tools/data/content/vendors.json line 2927 (item 76111, stock_source Farnsworth); repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md line 92"},
  {"type": "prize_wheel", "detail": "Medic prize wheel at the Vale of the Ancients dungeon (one of five wheel items plus the 202 Coins slot)", "where": "Vale of the Ancients (dungeon)", "price": null, "currency": null, "source": "wiki page Vale of the Ancients (Prize wheel by job table); repo:notes/Build Guides/Content/Dungeons/Vale of the Ancients.md lines 71 and 63-65; locale:133119"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name 'Hydrostatic Medic Helmet' is locale 133119, item definition 76111, slot 1 (head), class 7, one variant", "source": "client definition; locale:133119"},
  {"claim": "Farnsworth, Medic Job merchant introduced 27 August 2013, sells Hydrostatic Medic Helmet among the Hydrostatic Medic set", "source": "wiki page Farnsworth; repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md line 92 (Farnsworth, Medic Job merchant, 27 August 2013)"},
  {"claim": "Coin store reference price 752 Coins (member 676 Coins)", "source": "repo:data/content/stores.json item 76111; repo:prototype/osfr-tools/data/content/vendors.json line 2931"},
  {"claim": "Hydrostatic Medic Helmet is one of the Medic wheel items at Vale of the Ancients", "source": "wiki page Vale of the Ancients; repo:notes/Build Guides/Content/Dungeons/Vale of the Ancients.md line 71"},
  {"claim": "Hydrostatic Medic set is a Medic bonus clothing set in dungeon prize wheels (Vale, Treeleaf's Retreat)", "source": "wiki pages Vale of the Ancients and Treeleaf's Retreat (bonus clothing sets by job: Medic Hydrostatic or Pressure Wave)"},
  {"claim": "Jev first-pass tag (live yes, clothing, vendor) agrees with the Farnsworth sale", "source": "jev_first_pass hint; corroborated by the wiki Farnsworth page"}
 ],
 "confidence": 0.8,
 "open": [
  "The 752 Coins price is a stores.json reference price, not a captured NPC quote (vendors.json price_basis); the wiki Farnsworth page snippet did not show a price beside the helmet, so confirm the live price.",
  "The Vale of the Ancients wheel is a dungeon prize wheel; whether the helmet is also on the Medic wheel at other dungeons (Prince of Low Tide, Stealthy Despoilers) was not confirmed for the helmet specifically (those pages list the gloves and fatigues).",
  "Whether the helmet was retired or left Farnsworth's stock later is not stated in the pack; no retirement source found.",
  "Video frames, articles and forum facts for this item were not found."
 ]}
