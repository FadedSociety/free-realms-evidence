<!-- fleet job=citem-infer id=cchef-s-power-shard-of-timing-i-132111-v2 status=done turns=2 usd=0.0018 tokens(read,write,in,out)=[5552, 6946, 6, 1658] model=claude-haiku-5-5 -->
# Chef's Power Shard of Timing I

{"item": {"name": "Chef's Power Shard of Timing I", "locale_id": 132111, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for item 75665 (stores.json category 121). No NPC vendor is evidenced for this item.", "where": "Coin store (stores.json category 121)", "price": "750 coins (member price 675 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:15463"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 132111 is \"Chef's Power Shard of Timing I\"; item definition 75665, slot 12, class 21, no client description.", "source": "locale:132111"},
  {"claim": "Item 75665 has a coin store row: purchase 750 coins, member discount 10%, member price 675 coins, sell price 75 coins, category 121.", "source": "repo:prototype/osfr-tools/data/content/stores.json:15463"},
  {"claim": "Item 75665 appears as the slot-12 equipped item in the Chef 45 starter-outfit research capture (an equipped-item capture, not a sale).", "source": "repo:notes/Research/Job Starter Outfits.md:53"},
  {"claim": "Sibling-job Timing I shards are sold by wiki NPCs: Ferd sells Postman's Power Shard of Timing I; Vela sells Miner's Power Shard of Timing I; Samune sells Blacksmith's Power Shard of Timing I. These show the tier exists for other jobs; they do not show a Chef NPC sale.", "source": "wiki Ferd, Vela, Samune (lookup results); locale:15165, locale:132147, locale:132075"},
  {"claim": "No wiki page found for Chef's Power Shard of Timing I itself; the Chef NPC pages (Gaston, Mikael, Ingrid, Lorraine, Nadia, Skye, Zamzani, Rachael) list Chef Timing II-V and Talent I-IV in the snippets reviewed, not Timing I. This is negative evidence against an NPC sale, not a source.", "source": "wiki Chef NPC pages (lookup results)"}
 ],
 "confidence": 0.5,
 "open": [
  "No Chef NPC vendor is confirmed for Timing I; the only evidenced sale is the coin store row (750 coins, member 675). Do not treat the Chef job NPCs as sellers without a page that lists this item.",
  "Store row source_tags (L1, L2, L4, R1, R2, R2, T633) are unexplained in the repo; they may indicate listing context but were not decoded.",
  "The coin store price is from our store data; no wiki price was found, so no sale price is confirmed.",
  "Retirement and current availability were not found in any source; live is 'unsure'.",
  "Kind is a guess: slot 12 and class 21 with no description; 'other' (shard/accessory) is unverified.",
  "Previous answer's claim that Ferd/Samune/Vela show a Chef counterpart was an analogy and has been removed; the previous 'Chef job vendor' label and the Chef NPC source were non-sources and have been removed."
 ]}
