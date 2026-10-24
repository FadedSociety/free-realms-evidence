<!-- fleet job=item-infer id=ininja-s-power-shard-of-vitality-iii-v3 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6285, 7901, 6, 2478] model=claude-haiku-5-5 -->
# Ninja's Power Shard of Vitality III

{"item": {"name": "Ninja's Power Shard of Vitality III", "locale_id": 131165, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Dizzy Toad (Pixie NPC Merchant, npc_id 9500000742; wiki says he sells exclusively Ninja job items; stock row added 27 Aug 2013)", "where": "Perry's Pastures, south of Snowhill", "price": "1055 coins (purchase); 949 coins for Members (sell 527)", "currency": "coins", "source": "repo: prototype/osfr-tools/data/content/vendors.json:33059-33078 (Dizzy Toad stock row, item_ids includes 75421, stock_completeness partial_evidence_reference); vendors.json:33297-33306 (item 75421, name_id 131165, purchase 1055, member 949, sell 527, price_basis: stores.json reference price, no captured NPC quote); wiki: https://freerealms.fandom.com/wiki/Dizzy_Toad (Pixie NPC Merchant, introduced August 27 2013, sells exclusively Ninja Job Items)"},
  {"type": "coin_shop", "detail": "Coin Shop listing: sold to everyone; Members get a 10% discount", "where": "Coin Shop", "price": null, "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Ninja's_Power_Shard_of_Vitality_III (rev 32489: text 'acquired from the Coin Shop... sells to everyone... Members at the 10% discount price'; category Coin Shop). Price digits are blank in the page text."}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name is Ninja's Power Shard of Vitality III, locale 131165", "source": "locale:131165"},
  {"claim": "Wiki page: level 8 Ninja power shard, sold in Coin Shop to everyone with a 10% Member discount; passive increases health by 233 in combat (text only, unchecked in client)", "source": "https://freerealms.fandom.com/wiki/Ninja's_Power_Shard_of_Vitality_III"},
  {"claim": "Dizzy Toad's stock row includes item 75421 (this shard)", "source": "repo: prototype/osfr-tools/data/content/vendors.json:33059-33078"},
  {"claim": "Vendor row for item 75421: purchase 1055, member 949, sell 527; price basis is a stores.json reference, not a captured NPC quote", "source": "repo: prototype/osfr-tools/data/content/vendors.json:33297-33306; prototype/osfr-tools/data/content/stores.json:15300"},
  {"claim": "Dizzy Toad is a Pixie NPC Merchant at Perry's Pastures south of Snowhill, introduced Aug 27 2013, sells exclusively Ninja Job Items", "source": "https://freerealms.fandom.com/wiki/Dizzy_Toad"},
  {"claim": "The wiki coins field for the shard reads [1055, 1055], but the page text's price digits are blank; this is an unverified parse, not a readable wiki price", "source": "wiki pack field coins for rev 32489"}
 ],
 "confidence": 0.6,
 "open": [
  "The 1055 / 949 prices come from the repo's stores.json reference (vendors.json:33302-33303), not an in-game Dizzy Toad quote. Confirm in-game before relying on them.",
  "The Coin Shop price is unknown. The wiki's coins field [1055, 1055] is an unverified parse of blank price text, and it is not confirmed as the Coin Shop price. The Coin Shop and Dizzy Toad rows may describe the same sale; they are kept as separate sources and not merged.",
  "The Dizzy Toad wiki 'Sells' list was truncated in the lookup text, so this shard is confirmed only by the repo stock row, not by a visible wiki Sells line. The critique saying the wiki Sells section lists it (rev 2013-10-03) could not be verified here.",
  "Live status is unsure. Dizzy Toad dates from 2013 and nothing in the pack shows he is still stocked. Retirement is unknown.",
  "The 'Marketplace Items' category is not evidence of the Station Cash Marketplace; no Station Cash price is recorded, so no station_cash source.",
  "The 233 health effect is from wiki text only and was not checked against the client.",
  "The earlier citations snowhill.json:10066 and lakeshore.json:5718 are generic Brawler/Archer lines and are dropped as sources for this item."
 ]}
