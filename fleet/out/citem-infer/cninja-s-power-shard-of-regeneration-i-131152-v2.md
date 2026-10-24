<!-- fleet job=citem-infer id=cninja-s-power-shard-of-regeneration-i-131152-v2 status=done turns=4 usd=0.0050 tokens(read,write,in,out)=[47952, 21935, 10, 3548] model=claude-haiku-5-5 -->
# Ninja's Power Shard of Regeneration I

{"item": {"name": "Ninja's Power Shard of Regeneration I", "locale_id": 131152, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale record, store category 121, shop/vendor not named in our data (category 121 is unmapped; no stock row or NPC found)", "where": null, "price": "750 coins (member price 675 coins, 10% member discount; sell-back 75 coins)", "currency": "coins", "source": "prototype/osfr-tools/data/content/stores.json line 15292 (item_id 75408, category_id 121, purchase_price_coins 750, member_price_coins 675, sell_price_coins 75, no_sale false); item 75408 is the client definition id for this item"},
  {"type": "prize_wheel", "detail": "Ninja job prize wheel, Bixie Hive dungeon (one of six slots: Battle Item Mystery Pack, Kusa Ninja Cowl, Ninja's Training Sword of 1000 Storms, Ninja's Necklace of Bark Skin I, this shard, 68 Coins). Drop chance not stated.", "where": "Bixie Hive (Queensfields)", "price": null, "currency": null, "source": "repo: notes/Build Guides/Content/Dungeons/Bixie Hive.md line 85 (wiki-only tag, no client-name tag); prototype/osfr-tools/data/content/dungeons/bixie_hive.json lines 1671 and 2641 (per prior answer)"},
  {"type": "prize_wheel", "detail": "Ninja job prize wheel, Sheep Watch dungeon (wiki wheel listing; the Ninja section of the wheel includes 'Ninja's Power Shard of Regeneration I' next to 8 Coins)", "where": "Sheep Watch", "price": null, "currency": null, "source": "refs: freerealms-wiki/search-review.json line 359 (wiki page text 'Sheep Watch'); wiki-text extraction, not video-confirmed"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131152 is \"Ninja's Power Shard of Regeneration I\"; it sits in the set with Regeneration II-V and Precision (131153-131157) and the Ninja Ring/Necklace placeholders (131147-131151).", "source": "locale:131152"},
  {"claim": "Client definition id 75408 maps to this item; stores.json has a coin store record for item 75408 at 750 coins purchase, 675 member, 75 sell, category 121.", "source": "prototype/osfr-tools/data/content/stores.json line 15292"},
  {"claim": "Bixie Hive wheel lists the Ninja Power Shard of Regeneration I as one of the Ninja wheel slots.", "source": "repo: notes/Build Guides/Content/Dungeons/Bixie Hive.md line 85"},
  {"claim": "Sheep Watch wiki wheel text lists Ninja's Power Shard of Regeneration I in the Ninja wheel section.", "source": "refs: freerealms-wiki/search-review.json line 359"},
  {"claim": "Client has a sibling-family set: Ninja Regeneration I-V and Precision share a locale block; other jobs' Regeneration I shards exist in the client (e.g. Medic's Power Shard of Regeneration I, locale-test data en_us_data.dat), confirming the family but not this item's stats or sale status.", "source": "refs: FreeRealmsLocaleTools/test/FreeRealmsLocaleTools.Tests/data/en_us_data.dat line 267833582 (Ninja's Power Shard of Regeneration I)"}
 ],
 "confidence": 0.6,
 "open": [
  "The coin store record (item 75408, 750 coins) does not name a vendor or shop. Category 121 is not mapped to a shop in our data, so this is recorded as a coin shop sale with no named vendor. Need the category-to-shop mapping to name it.",
  "stores.json source_tags (L1, L2, L4, R2, T633, R1) are not decoded in our notes; availability today (live vs. retired) cannot be confirmed from them. no_sale is false in the record.",
  "The Medic sibling tooltip image is family context only; it is not evidence for this item's stats. The prior '+23 health regen' stat was not carried over; in-game stats for the Ninja Regeneration I shard are unsourced.",
  "Prize wheel drop chance is not stated anywhere in the pack. Both wheel sources are wiki-text only; no video frame confirms either.",
  "The Sheep Watch wheel source comes from a wiki search index extraction (search-review.json); the column layout is ambiguous, so it should be checked against the Sheep Watch page before relying on it.",
  "Earlier answer cited repo:data/content/stores.json; the correct path is prototype/osfr-tools/data/content/stores.json.",
  "Earlier answer typed the coin store record as 'vendor' with no vendor; corrected here to coin_shop, unnamed. Earlier citation of the Bixie Hive line as [wiki] [client names] is corrected: line 85 carries only the [wiki] tag."
 ]}
