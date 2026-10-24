<!-- fleet job=citem-infer id=cninja-s-power-shard-of-vitality-iv-131166-v1 status=done turns=5 usd=0.0048 tokens(read,write,in,out)=[50086, 20837, 12, 3446] model=claude-haiku-5-5 -->
# Ninja's Power Shard of Vitality IV

{"item": {"name": "Ninja's Power Shard of Vitality IV", "locale_id": 131166, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Shivering Shark (Ninja Job merchant, client name id 1096850988; wiki says he sells exclusively Ninja Job items, Sensei Ninja set and Vitality IV/Regeneration IV items)", "where": "Blackspore Swamp (behind the Blackspore Pet Adoption Center)", "price": "1504 coins (store reference price; member price 1353 coins; sell price 150 coins)", "currency": "coins", "source": "wiki page Shivering Shark (https://freerealms.fandom.com/wiki/Shivering_Shark, rev 2013-11-03, section Sells, lists \"Ninja's Power Shard of Vitality IV\"); repo:prototype/osfr-tools/data/content/vendors.json item 75422 (stock_source wiki Shivering Shark); repo:prototype/osfr-tools/data/content/stores.json line 15306 item_id 75422 purchase_price_coins 1504; repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md line 96 (Ninja Job merchant, 27 August 2013)"},
  {"type": "prize_wheel", "detail": "Ninja job prize wheel of the Treeleaf's Retreat dungeon (one of the per-job dungeon wheel prizes)", "where": "Treeleaf's Retreat (dungeon)", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/Dungeons/Treeleaf's Retreat.md line 75 (Ninja row, cites wiki with client names); same Ninja wheel pattern on other dungeon pages (e.g. Vale of the Ancients, Mugwort's Hollow)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item as Ninja's Power Shard of Vitality IV, locale 131166, definition 75422, slot 12, class 2, one variant, with a coin store price of 1504", "source": "locale:131166; client definition in pack; repo:prototype/osfr-tools/data/content/stores.json line 15306"},
  {"claim": "Shivering Shark's wiki Sells list includes Ninja's Power Shard of Vitality IV (also Flair Shard of Harmony and Regeneration IV items, Sensei Ninja set)", "source": "wiki page Shivering Shark, https://freerealms.fandom.com/wiki/Shivering_Shark (rev 2013-11-03)"},
  {"claim": "Blackspore Swamp vendor stock row resolves item 75422 under Shivering Shark, Ninja Job merchant, added 27 August 2013", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json line 1323 and NPCs - Blackspore Swamp.md line 96"},
  {"claim": "1504 coins is a store reference price, not a captured NPC quote; member price 1353 coins; sell price 150 coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json line 6585 (price_basis) and stores.json line 15306"},
  {"claim": "Ninja wheel in Treeleaf's Retreat lists this item as a prize", "source": "repo:notes/Build Guides/Content/Dungeons/Treeleaf's Retreat.md line 75"},
  {"claim": "Client cluster of Ninja's Power Shard of Vitality I-V and Shard of the Vampire/Armadillo sits in the same locale block", "source": "locale:131161 to 131167 (client_cluster in pack)"}
 ],
 "confidence": 0.6,
 "open": [
  "The 1504-coin price is the stores.json reference price; no wiki or captured NPC quote confirms the Shivering Shark's own price for this item.",
  "No wiki price was found for the Shark's listing in the lookup excerpt; the wiki revision is 2013-11-03, so later changes are unknown.",
  "Retired/unobtainable status is unknown: no source states that the Shivering Shark or the Ninja job items were removed.",
  "The Treeleaf's Retreat prize-wheel entry comes from a repo dungeon note that cites the wiki; the wiki page itself was not re-read, so the wheel's current status is unverified.",
  "The client name's flag cluster (Valentines leftover markup) does not affect this item (131166 is clean)."
 ]}
