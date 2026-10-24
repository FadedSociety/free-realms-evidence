<!-- fleet job=citem-infer id=cblacksmith-s-power-shard-of-talent-ii-132076-v5 status=nothing_found turns=2 usd=0.0021 tokens(read,write,in,out)=[6593, 9650, 6, 1725] model=claude-haiku-5-5 -->
# Blacksmith's Power Shard of Talent II

{"item": {"name": "Blacksmith's Power Shard of Talent II", "locale_id": 132076, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 132076 is \"Blacksmith's Power Shard of Talent II\", in the Blacksmith Talent/Timing shard cluster (locale:132071-132081).", "source": "locale:132076"},
  {"claim": "stores.json row item 75630 (category 121, purchase 806, member 725 at 10% off, sell 80, no_sale false) is a reference price row, not a captured sale or NPC quote. vendors.json labels its stores.json prices '(R) reference price, not captured NPC quote'.", "source": "repo:prototype/osfr-tools/data/content/stores.json:15438; repo:prototype/osfr-tools/data/content/vendors.json:175 (scope label)"},
  {"claim": "Wiki Seppa sell list (Blacksmith job items) lists Power Shard of Timing II, Ring of Talent II, Tongs of Timing II and Tongs of Talent II but not Power Shard of Talent II, so Seppa is excluded on that list.", "source": "wiki page Seppa (freerealms-wiki/wikitext/10153-48989-f9e7909fe9ba.wiki, lines 14-30)"},
  {"claim": "Sibling Talent II shards are sold by other job NPCs: Arel (Postman, Power Shard of Talent II, 2048454492) and Zamzani (Chef). A Miner Talent II shard also exists in the client. No Blacksmith NPC sell list found containing the Blacksmith Talent II shard.", "source": "notes/Build Guides/Content/Jobs/Postman.md:211; notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:79; repo:prototype/osfr-tools/data/content/npcs/merry_vale.json:925"}
 ],
 "confidence": 0.2,
 "open": [
  "No sold-at source found. The only price (806 coins, member 725, sell 80) is a reference price in stores.json category 121, shared with the rest of the Blacksmith/Talent cluster (e.g. item 75631 identical). It is not a coin store listing or NPC sale, so it is not listed as a source.",
  "Blacksmith vendor unconfirmed. Keller, Masa, Estus and Hess sell lists are still unchecked for a Talent II row. Seppa is excluded on her wiki list.",
  "Retired status unknown. The no_sale false flag and client name lines show the name is real, not that it is currently sold.",
  "Kind left as 'other': the client description is empty and slot 12 / class 14 are unmapped. The earlier 'clothing' first-pass guess is unsupported.",
  "Earlier answer's coin_shop source was withdrawn: the row is a reference price, not a store listing. If a Blacksmith NPC sell list is later found, add it as a vendor source with the NPC's own price.",
  "No quest reward, enemy drop, event, prize wheel or collection source found."
 ]}
