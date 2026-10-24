<!-- fleet job=citem-infer id=csnowhill-ice-cream-vanilla-23305-v3 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[14224, 8064, 8, 1838] model=claude-haiku-5-5 -->
# Snowhill Ice Cream: Vanilla

{"item": {"name": "Snowhill Ice Cream: Vanilla", "locale_id": 23305, "kind": "consumable"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop purchase. Wiki quest text tells players to purchase one from the Coin Shop for Sweets for Sniffles (Marzipan asks for Vanilla ice cream). No NPC vendor is confirmed for this sale.", "where": "Coin Shop (store category, not a single location)", "price": "12 coins (reconstructed reference price, not a captured Coin Shop quote; member price 10 is a derived policy value, 12 minus 10%, not observed)", "currency": "coins", "source": "wiki page Quest:Sweets for Sniffles ('Purchase one [Snowhill] [Ice] [Cream]: [Vanilla] from the Coin Shop'); repo:prototype/osfr-tools/data/content/stores.json line 17279 (item_id 2895, category 16, purchase_price_coins 12, price_provenance kind 'reconstructed')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 23305 is 'Snowhill Ice Cream: Vanilla'; description says it is usable in recipes", "source": "locale:23305"},
  {"claim": "Client definition id 2895 has a coin store row with purchase price 12 coins, category 16; the price is marked reconstructed, not captured", "source": "repo:prototype/osfr-tools/data/content/stores.json line 17279"},
  {"claim": "Wiki quest Sweets for Sniffles: Marzipan asks for Vanilla ice cream; the player is told to purchase one from the Coin Shop", "source": "wiki page Quest:Sweets for Sniffles"},
  {"claim": "Used as an ingredient in Chef recipes: Moonbean Sundae Sweettreat (Snowhill Ice Cream: Vanilla x3)", "source": "wiki page List of Recipes (Chef)"},
  {"claim": "No retirement or removal evidence found", "source": "no source found"}
 ],
 "confidence": 0.5,
 "open": [
  "The 12-coin price is reconstructed (stores.json price_provenance), not a captured Coin Shop quote. The only video store frame (ukTXIyG6EKI/00006) reads 'Snowhill Ice Cream: C... 12 coins', which is the Chocolate variant, not Vanilla.",
  "Member price 10 is a policy default (member_discount_percent 10), not observed.",
  "Bordon Cloo (cooking-supply NPC, vendors.json lines 47112-47120) dropped as a source: the 12-coin price is a reference value, the video name plate is unreadable, and identity rests only on client text. Kept as an unverified lead for a Sanctuary vendor.",
  "Razzle vendor row (vendors.json ~line 40866, npc_id 9500000845, lists Chocolate) dropped: it repeats the same wiki sentence and its NPC id conflicts with 9000000028.",
  "Coin Shop vs vendor: the wiki says Coin Shop; the repo says a cooking-supply NPC. No capture confirms which store stocks it now.",
  "Live status unsure: no current-era capture confirms it is still sold. The 2009-2014 window is inferred from the Sweets for Sniffles quest (the only dated source) and the Chef recipes."
 ]}
