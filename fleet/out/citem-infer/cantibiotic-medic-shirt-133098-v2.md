<!-- fleet job=citem-infer id=cantibiotic-medic-shirt-133098-v2 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[13348, 9409, 8, 2111] model=claude-haiku-5-5 -->
# Antibiotic Medic Shirt

{"item": {"name": "Antibiotic Medic Shirt", "locale_id": 133098, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Bev (human merchant; wiki says she sells exclusively Medic job items)", "where": "Wugachug", "price": "unverified (no captured NPC quote)", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Bev (Sells section, revision 2023-05-28, lists '[Antibiotic] [Medic] [Shirt]'); repo:prototype/osfr-tools/data/content/vendors.json:44842-44858 (npc_id 9500000966, item_ids include 76090); repo:prototype/osfr-tools/data/content/vendors.json:45078-45119 (stock_source wiki Bev)"},
  {"type": "other", "detail": "Coin-store reference price for item 76090 (category 103): 453 coins, member price 407 (10% member discount), sell-back 45. Not tied to a confirmed sale location or to Bev.", "where": null, "price": "453 coins (member 407; sell 45)", "currency": "coins", "source": "repo:data/content/stores.json:8563 (item 76090); repo:prototype/osfr-tools/data/content/vendors.json:45087 and :45116 mark this as a '(R) stores.json reference price; no captured retail NPC quote'"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 133098 is 'Antibiotic Medic Shirt'; item definition 76090, chest slot, one variant", "source": "locale:133098; client definition in pack"},
  {"claim": "Wiki page Bev lists 'Antibiotic Medic Shirt' among her sells, alongside Backpack, Pants, Cap, Gloves, Boots", "source": "https://freerealms.fandom.com/wiki/Bev"},
  {"claim": "vendors.json stock row for Bev includes item 76090, marked stock_completeness 'partial_evidence_reference'", "source": "repo:prototype/osfr-tools/data/content/vendors.json:44846-44854"},
  {"claim": "The 453/407/45 coin figures are stores.json reference prices, not an observed Bev quote", "source": "repo:data/content/stores.json:8563; repo:prototype/osfr-tools/data/content/vendors.json:45087"},
  {"claim": "Robgoblin Treasure Trove wiki page lists '[Antibiotic] [Medic] [Shirt]' under a '[Medic] Prize Wheel' heading, but the trailing '49 Coins' line sits with the adjacent Battle Item Mystery Pack entry; no prize-wheel source is confirmed", "source": "https://freerealms.fandom.com/wiki/Robgoblin_Treasure_Trove (lookup excerpt)"}
 ],
 "confidence": 0.6,
 "open": [
  "Bev's live price for the shirt is unverified; the 453-coin figure is a stores.json reference, and it is not confirmed that the shirt is sold in the coin shop at that price. Either a coin_store source (stores.json:8563) or the Bev vendor price needs a captured quote to be final.",
  "Prize wheel: the Robgoblin Treasure Trove wiki excerpt lists the shirt under a '[Medic] Prize Wheel' heading, which is ambiguous, since the '49 Coins' line appears to belong to the adjacent entry. Needs the page revision checked before adding a prize_wheel source.",
  "No retirement notice found for Bev's stock, but the Bev wiki revision is dated 2023-05-28, so current availability is unconfirmed and live is set to 'unsure'.",
  "Client description is empty; no in-game description evidence.",
  "The wiki page for the shirt was not found as its own article; the sourcing is entirely from list entries."
 ]}
