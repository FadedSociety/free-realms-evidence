<!-- fleet job=citem-infer id=cminer-s-flair-shard-of-the-mother-load-132163-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[5910, 9958, 6, 2453] model=claude-haiku-5-5 -->
# Miner's Flair Shard of the Mother Load

{"item": {"name": "Miner's Flair Shard of the Mother Load", "locale_id": 132163, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Coin store listing for item 75717 (vendor/NPC not identified in the data; Kallie is a name-only candidate, not confirmed)", "where": null, "price": "2152 coins list; 1936 coins member price (10% discount); sell price 215 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75717 (line 15505, category 124, no_sale false)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 75717 is named 'Miner's Flair Shard of the Mother Load' (locale 132163), description 'Jackpot! Jackpot! Yeee-ha!', one definition, slot 13, class 12.", "source": "locale:132163; client definition in evidence pack"},
  {"claim": "Coin store entry exists for item 75717 at 2152 coins list, 1936 member price, category 124, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75717 (line 15505)"},
  {"claim": "Category 124 is a generic grouping: it also holds items 75710-75716 and 75718-75724 at 750 to 2152 coins, so category 124 alone does not identify a vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 15498-15512"},
  {"claim": "Kallie's wiki Sells list names \"Miner's Flair Shard of Mother Load\" (no 'the'), at Red's Haven, Sunstone Valley; the repo marks this name 'unmatched' with no candidate ids and rejects spelling substitutions.", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json lines 9261-9281; wiki Kallie (https://freerealms.fandom.com/wiki/Kallie, Sells, revision 2025-03-26)"},
  {"claim": "Kallie's resolved_item_ids include 75708, not 75717. 75708 carries the same 2152 coin price in category 121.", "source": "repo:prototype/osfr-tools/data/content/vendors_unresolved.json lines 9242-9253; stores.json line 15496"},
  {"claim": "Pack's earlier Kallie price (2152/1936 coins) was not verified as Kallie's sale price; the wiki price for this item was not captured.", "source": "critique of previous answer; vendors_unresolved.json lines 9261-9281"}
 ],
 "confidence": 0.35,
 "open": [
  "Vendor not confirmed. Kallie (Red's Haven, Sunstone Valley, NPC 9500000827) is the only candidate, and it rests on a name near-match ('Mother Load' vs 'the Mother Load') that the repo rejected as unmatched. Do not treat Kallie as a sourced vendor until a builder confirms the mapping.",
  "The 2152 coin price is store data for 75717 only. It is not shown as Kallie's sell price. Sell price 215 coins is store-list data, not a wiki figure.",
  "Wiki price for this item was not captured; the Kallie Sells excerpt in the pack does not show the flair shard line.",
  "Live status is unsure: the store row is active (no_sale false), but no dated wiki or client check confirms current sale. Retirement not found in any source.",
  "Jev's first pass said 'tool'. Slot 13 and class 12 give no tool evidence, so kind is set to 'other' (a Miner job flair/trinket).",
  "No drop, quest reward, crafting, collection, event, or prize-wheel source found. No video or image evidence.",
  "Sibling items 75708 and 75709 share the 2152 price in category 121; 75708 is Kallie-resolved. Confirm whether the Mother Load shard belongs to the same Kallie list."
 ]}
