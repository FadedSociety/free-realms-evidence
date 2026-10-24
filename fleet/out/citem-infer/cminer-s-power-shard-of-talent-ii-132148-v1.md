<!-- fleet job=citem-infer id=cminer-s-power-shard-of-talent-ii-132148-v1 status=done turns=7 usd=0.0052 tokens(read,write,in,out)=[85616, 23103, 16, 2892] model=claude-haiku-5-5 -->
# Miner's Power Shard of Talent II

{"item": {"name": "Miner's Power Shard of Talent II", "locale_id": 132148, "kind": "other"},
 "sources": [
  {"type": "vendor", "detail": "Witts (pixie merchant, Miner job gear; sells Miner job items)", "where": "Dartmoor Quarry, Northern Wilds", "price": "806 coins (reference price from stores.json; member price 725 coins, 10% member discount)", "currency": "coins", "source": "wiki page Witts (https://freerealms.fandom.com/wiki/Witts, Sells section lists [[Miner's Power Shard of Talent II]]); repo:prototype/osfr-tools/data/content/vendors.json line 44463 (Witts item_ids include 75702); repo:prototype/osfr-tools/data/content/stores.json line 15490 (item_id 75702, purchase_price_coins 806); refs freerealms-wiki/wikitext/11445-48990-62cc71e4bce8.wiki lines 31-37"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 132148 is 'Miner's Power Shard of Talent II' (item, no FLAG).", "source": "locale:132148"},
  {"claim": "Witts sells Miner's Power Shard of Talent II; the wiki Witts page lists it under Sells, and the page's Trivia says Witts was introduced in-game on the October 15, 2013 update.", "source": "wiki page: Witts"},
  {"claim": "Coin store price 806 for item 75702 (member price 725, sell price 80) is stored as a reference price, not a captured NPC quote.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75702; repo:prototype/osfr-tools/data/content/vendors.json line 44499"},
  {"claim": "Witts' stock is also reflected in the repo vendor record (npc 9500000962, stock_completeness 'partial_evidence_reference').", "source": "repo:prototype/osfr-tools/data/content/vendors.json line 44266-44276"},
  {"claim": "Sibling Miner shards (Talent II/Timing II, Ring and Necklace) share the same Witts listing and reference price 806.", "source": "repo:prototype/osfr-tools/data/content/vendors.json lines 44378-44510"}
 ],
 "confidence": 0.8,
 "open": [
  "The 806-coin price is a stores.json reference price, not a captured in-game quote; no wiki page gives a price for this shard, so treat the price as unverified.",
  "The wiki Witts page does not state a price, so the wiki-side price is missing.",
  "Witts' Miner stock list in the wiki is undated per item; whether this shard was sold continuously or retired later is unknown. No retirement source was found, so retired is null.",
  "No quest reward, enemy drop, event, crafting, or collection source was found in the pack or repo for this item.",
  "The jev first-pass 'vendor' guess is consistent with the Witts listing; the 'other' kind is my classification of a job-gear shard (slot 12, class 12), not a confirmed category.",
  "The wiki Witts page is the only source; no image or video frame confirms Witts selling this shard."
 ]}
