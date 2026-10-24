<!-- fleet job=citem-infer id=ckai-s-tempered-circle-shard-3405-v5 status=nothing_found turns=2 usd=0.0023 tokens(read,write,in,out)=[6323, 10048, 6, 1989] model=claude-haiku-5-5 -->
# Kai's Tempered Circle Shard

{"item": {"name": "Kai's Tempered Circle Shard", "locale_id": 3405, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is Kai's Tempered Circle Shard, locale 3405; flavour line locale 150159 'This is a Kai's Tempered Circle Shard item.'", "source": "locale:3405; locale:150159"},
  {"claim": "Client description: increases the stars earned as a ninja while equipped. Slot 13, class 54, one definition (834). Client text only; not confirmed in play.", "source": "client definition in evidence pack"},
  {"claim": "Sibling shards Bullseye 3402 to Bordon 3410 share the 'This is a X's Tempered Circle Shard item.' pattern; no source says how the named shards are acquired.", "source": "locale:3402-3410"},
  {"claim": "Wiki pages exist for Stealth, Battle and Amplifier Tempered Circle Shards (Daily Wheel Shards wedge). None names Kai's shard.", "source": "wiki: Stealth Tempered Circle Shard; Battle Tempered Circle Shard; Amplifier Tempered Circle Shard"},
  {"claim": "stores.json item 834 shows purchase 6600, member 5940, sell 660, category 124, with tags L1,L2,L4,R2,T633,R1. R1 marks unknown or defaulted values. Items 831-840 carry identical rows, so the block looks like a family default.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 375-384"},
  {"claim": "The Cost field is used as a starting regular coin price and has not been checked against a real client transaction. The sell-back 660 is the max(1, purchase//10) rule, not a shipped value.", "source": "repo:notes/Research/Coin Shop.md lines 33-34, 38-41"}
 ],
 "confidence": 0.1,
 "open": [
  "No coin_shop source is claimed. The only price, 6600 on stores.json item 834, is a reference-derived starting price tagged R1 (unknown or defaulted). It is part of a flat block shared with items 831-840, and Coin Shop.md says it has not been checked against a real transaction. Treat it as a provisional placeholder, not an acquisition source or a live price. The client definition's coin_store_prices 6600 comes from the same reference data, not a verified shipped table.",
  "No vendor stock, quest reward, enemy drop, event, prize wheel, crafting, collection or promotion source names this item in the pack. The earlier vendor guess has no support and is dropped.",
  "Whether the named Tempered Circle Shard cluster (3402-3410) comes from the Daily Wheel Shards wedge, an event or a named-NPC reward is unconfirmed. Wiki coverage is limited to Stealth, Battle, Amplifier, Arrow and Champion shards.",
  "The star-boost effect comes from client text only and is unconfirmed in play. The Stealth wiki describes an experience boost for its own shard.",
  "Live status is unsure. no_sale=false is a catalogue default, not a sale signal. No retirement or live-date source was found.",
  "Wiki, articles and video lookups for the exact name failed with an FTS5 syntax error on the apostrophe; the wiki side was not re-queried under a quoted phrase, so a wiki page naming this shard may still exist.",
  "Not wireable: no evidenced acquisition source. Needs a player-facing listing, a vendor stock row, or a wiki page naming Kai's shard."
 ],
 "critiques_addressed": "Evidence critique: the coin_shop source is removed and the 6600 is treated as a defaulted R1 value. Coin-shop critique: the 831-840 flat block is flagged as a probable default. World critique: zero evidenced sources; live and retired left unknown."}
