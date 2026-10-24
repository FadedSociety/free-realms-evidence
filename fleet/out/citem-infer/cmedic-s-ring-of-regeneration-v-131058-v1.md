<!-- fleet job=citem-infer id=cmedic-s-ring-of-regeneration-v-131058-v1 status=done turns=4 usd=0.0029 tokens(read,write,in,out)=[20445, 9808, 10, 3018] model=claude-haiku-5-5 -->
# Medic's Ring of Regeneration V

{"item": {"name": "Medic's Ring of Regeneration V", "locale_id": 131058, "kind": "clothing"},
 "sources": [
  {"type": "prize_wheel", "detail": "Medic prize wheel from the battle with Mudshell (level 13 combat goal; wheel lists Medic's Ring of Regeneration V)", "where": "Mudshell battle, Medic class wheel", "price": null, "currency": null, "source": "wiki page:ns0 Mudshell (Medic Prize Wheel section lists \"Medic's Ring of Regeneration V\")"},
  {"type": "vendor", "detail": "Coin store sale listed in our store data (item 75314, category 108); the only price in the pack, not confirmed by a captured NPC quote", "where": "Coin vendor (store not identified in data)", "price": "2152 coins (member price 1936 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 75314 (price_provenance kind: reconstructed, from Legacy reference cost; no captured retail quote)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name and locale ID 131058 are defined in the client; it sits in the Medic's Ring of Regeneration I-V / Necklace of Bark Skin I-V cluster", "source": "locale:131058 and cluster locale:131054 to 131063"},
  {"claim": "Client definition 75314 has one variant, slot 8, class 7, and a coin store price of 2152", "source": "client definition in pack; repo:data/content/stores.json item 75314 line 17329"},
  {"claim": "Mudshell's wiki page lists a Medic Prize Wheel that includes Medic's Ring of Regeneration V, alongside Medic's Power Shard of Regeneration V and Medic's Power Shard of Entangling", "source": "wiki page:ns0 Mudshell (Rewards, Medic Prize Wheel section)"},
  {"claim": "Medic's Power Shard of Entangling is acquired from the prize wheel of the Mudshell battle", "source": "wiki page:ns0 Medic's Power Shard of Entangling"},
  {"claim": "Other Mudshell-wheel Medic items (Shockrod of Antibodies) are also sold in the Coin Shop, so the coin store sale for this ring is plausible but not yet shown on the wiki", "source": "wiki page:ns0 Medic's Shockrod of Antibodies"}
 ],
 "confidence": 0.6,
 "open": [
  "The 2152-coin price is 'reconstructed' from the Legacy reference cost, with no captured in-game quote, and the store vendor is not named. Treat it as unverified until a vendor or Coin Shop page confirms it.",
  "The Mudshell wiki snippet shows '10 coins' next to the Brawler's Ring entry; it is unclear whether that is a wheel cost, a member bonus, or a different item. Not used as a price here.",
  "Whether the ring is still obtainable (retired or not) is not stated in any source. Live status is 'unsure'.",
  "The first-pass tag said 'vendor'; the wiki evidence supports the prize wheel (battle drop chain) as the stronger source. The vendor entry rests only on the store data price."
 ]}
