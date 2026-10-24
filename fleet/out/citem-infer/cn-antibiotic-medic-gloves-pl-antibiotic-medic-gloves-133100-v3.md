<!-- fleet job=citem-infer id=cn-antibiotic-medic-gloves-pl-antibiotic-medic-gloves-133100-v3 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[19746, 14608, 8, 2677] model=claude-haiku-5-5 -->
# {n}Antibiotic Medic Gloves{pl="Antibiotic Medic Gloves"}

{"item": {"name": "Antibiotic Medic Gloves", "locale_id": 133100, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Bev (human merchant, sells exclusively Medic job items; her Sells list includes Antibiotic Medic Gloves, with the rest of the Antibiotic Medic set)", "where": "Wugachug Brewery (Wugachug)", "price": null, "currency": null, "source": "wiki page Bev (https://freerealms.fandom.com/wiki/Bev), Sells section; repo:prototype/osfr-tools/data/content/vendors.json line 45163 (stock_source kind wiki, page Bev, section Sells)"},
  {"type": "coin_shop", "detail": "Coin store row for item 76092 (category 102); the row is a store reference price, not a captured Bev or NPC quote", "where": "Coin store (stores.json category 102)", "price": "453 coins purchase; 407 coins member price (10% member discount); 45 coins sell-back", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15804 (item_id 76092); vendors.json line 45167 marks it as '(R) reference price; no captured retail NPC quote'"},
  {"type": "prize_wheel", "detail": "Medic job prize wheel slot, The Bat Cave dungeon (wheel also holds Battle Item Mystery Pack, Medic's Power Shard of Regeneration II, Medic's Scalpel of Triage, and a fifth slot)", "where": "The Bat Cave (dungeon)", "price": null, "currency": null, "source": "wiki page The Bat Cave! ([Medic] Prize Wheel list); repo:notes/Build Guides/Content/Dungeons/The Bat Cave.md line 71. Wheel odds and spin cost unknown; the separate '49 Coins' entry is a wheel slot on every job's wheel, not this item's price."}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 133100 is 'Antibiotic Medic Gloves'; definition 76092; slot 2; class 7; one definition", "source": "locale:133100"},
  {"claim": "Bev's wiki Sells list includes [Antibiotic] [Medic] [Gloves] alongside the other five Antibiotic Medic pieces, and she 'sells exclusively Medic job items'", "source": "wiki page Bev (https://freerealms.fandom.com/wiki/Bev)"},
  {"claim": "Bev is at the Wugachug Brewery per the wiki; the repo NPC note records a conflict with the wiki Merchants list ('near the Wugachug Cooking Table')", "source": "notes/Build Guides/Content/NPCs/NPCs - Wugachug.md line 80"},
  {"claim": "Coin store reference price 453 coins, member 407, sell-back 45 for item 76092", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15804"},
  {"claim": "Medic prize wheel in The Bat Cave includes Antibiotic Medic Gloves", "source": "wiki page The Bat Cave!; repo:notes/Build Guides/Content/Dungeons/The Bat Cave.md line 71; repo:prototype/osfr-tools/data/content/dungeons/the_bat_cave.json line 2375"}
 ],
 "confidence": 0.6,
 "open": [
  "The 453-coin price is a stores.json coin-store reference row (category 102), not a captured Bev quote. It is listed as a coin_shop source, not as Bev's price. Bev's wiki Sells list gives no price, so Bev's price is null.",
  "The wiki's Bev page does not state a sale price or date. The vendors.json stock_source revision timestamp (2023-05-28) is not verified against the live page and is not relied on.",
  "The Bat Cave Medic wheel has no confirmed spin cost or odds. The wheel's fifth slot is unresolved in the client (wiki 'Medic's Necklace of Regeneration II' is not in the client; the note suggests Ring of Energy II).",
  "Robgoblin Treasure Trove bonus goal gives a random piece of the Antibiotic or Urgent Care set (notes Medic.md line 202; Trove note line 118 names the Backpack in the video). Gloves are not confirmed among the bonus pieces, so no drop source is listed.",
  "Retirement status is not stated in any source. The wiki Bev Sells list shows the gloves as currently sold, but no source confirms they were never retired, so retired is null.",
  "No drop, quest reward, event, promotion, or membership source is evidenced for this item."
 ]}
