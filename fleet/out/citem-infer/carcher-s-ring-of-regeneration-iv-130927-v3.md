<!-- fleet job=citem-infer id=carcher-s-ring-of-regeneration-iv-130927-v3 status=done turns=2 usd=0.0034 tokens(read,write,in,out)=[7829, 14355, 6, 3132] model=claude-haiku-5-5 -->
# Archer's Ring of Regeneration IV

{"item": {"name": "Archer's Ring of Regeneration IV", "locale_id": 130927, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Oliver, Archer Job merchant (introduced 6 August 2013); stock Bobtailed Archer set plus Ring of Regeneration IV", "where": "Blackspore Swamp, north-east of the Blackspore Warpstone", "price": "1504 Coins (reference price; member 1353 Coins, 10% discount; sell-back 150 Coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75183 (line 17290, price_provenance 'reconstructed' from FreeRealms-Legacy ClientItemDefinitions, no captured retail NPC quote); repo:prototype/osfr-tools/data/content/npcs/blackspore_swamp.json:25441; notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:94 (Oliver row names Ring of Regeneration IV)"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Croaking Vale (Smugglers led by Han and Hanna; level 9 combat job required)", "where": "Croaking Vale", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/dungeons/croaking_vale.json:887; notes/Build Guides/Content/Dungeons/Croaking Vale.md:69 (Archer row)"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Moldy Shamblers! battle (started from a Moldering Fungaloid)", "where": "Nettleseed, Briarwood", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Moldy Shamblers.md:64 (Archer row lists Archer's Ring of Regeneration IV); wiki page Moldy Shamblers! (Archer prize wheel section, excerpt truncated before the ring name)"},
  {"type": "prize_wheel", "detail": "Archer prize wheel, Mugwort's Hollow dungeon (same prize-table format as the other dungeon wheels)", "where": "Mugwort's Hollow", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Mugwort's Hollow.md:64 (Archer row lists Archer's Ring of Regeneration IV); table heading not read, so wheel vs. other reward type is unconfirmed"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Client item 130927 is named \"Archer's Ring of Regeneration IV\"; one definition (75183), slot 8, class 16", "source": "locale:130927; client definition 75183"},
  {"claim": "Coin store price 1504 Coins (member 1353, sell 150); provenance is reconstructed from the Legacy reference, not a captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75183 (line 17290)"},
  {"claim": "Oliver (Archer merchant, north-east of the Blackspore Warpstone) stocks the Bobtailed Archer set and Ring of Regeneration IV", "source": "notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:94; repo:prototype/osfr-tools/data/content/npcs/blackspore_swamp.json:25441"},
  {"claim": "Croaking Vale Archer prize wheel lists Archer's Ring of Regeneration IV", "source": "repo:prototype/osfr-tools/data/content/dungeons/croaking_vale.json:887; notes/Build Guides/Content/Dungeons/Croaking Vale.md:69"},
  {"claim": "Moldy Shamblers! Archer prize table lists Archer's Ring of Regeneration IV", "source": "notes/Build Guides/Content/Dungeons/Moldy Shamblers.md:64"},
  {"claim": "Mugwort's Hollow Archer row lists Archer's Ring of Regeneration IV", "source": "notes/Build Guides/Content/Dungeons/Mugwort's Hollow.md:64"},
  {"claim": "Video frame video:pfgmx-YRZD0/00016.jpg OCR is cut off at 'Archer's Ring' and does not confirm the Regeneration IV name; video:liVAgboeCLg/00004.jpg is a Daily Grab Bag store frame and is not a source", "source": "video:pfgmx-YRZD0/00016.jpg; video:liVAgboeCLg/00004.jpg"}
 ],
 "confidence": 0.55,
 "open": [
  "Coin prices (1504 / member 1353 / sell 150) are reconstructed from FreeRealms-Legacy reference data, not a captured Oliver quote. Treat as provisional.",
  "The Oliver vendor link rests on the repo notes and blackspore_swamp.json stock text; the wiki Oliver Sells list was truncated before the ring entry, so the ring is not seen directly on the wiki Sells list.",
  "The wiki Moldy Shamblers! excerpt was truncated before the ring name; the ring is supported only by the repo build-guide table (Moldy Shamblers.md:64). Full wiki page not re-read.",
  "Mugwort's Hollow row (Mugwort's Hollow.md:64) is in the same table format as the other dungeon wheels, but its heading was not read; confirm it is a prize wheel and not another reward type.",
  "Prize-wheel contents may have changed since the sources were written; current live status of each wheel is unverified.",
  "No retirement or removal evidence found; retired left null. Live status is inferred from current vendor stock and wheel data, not from a dated source.",
  "Earlier-cited repo:moldy_shamblers.json:774 was not verified and is not used."
 ]}
