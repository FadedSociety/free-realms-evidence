<!-- fleet job=citem-infer id=cjumbo-energy-potion-1941-v1 status=done turns=2 usd=0.0013 tokens(read,write,in,out)=[3721, 4387, 6, 1493] model=claude-haiku-5-5 -->
# Jumbo Energy Potion

{"item": {"name": "Jumbo Energy Potion", "locale_id": 1941, "kind": "consumable"},
 "sources": [{"type": "other", "detail": "Trading Card Game virtual reward cards 1L31 Jumbo Mana Potion and 1L73 Jumbo Mana Potion (virtual reward cards, not a coin vendor or drop)", "where": null, "price": null, "currency": null, "source": "wiki page: Jumbo Energy Potion (Category:TCG Supplies, Category:Virtual Rewards)"}],
 "retired": null, "live": "unsure",
 "evidence": [{"claim": "Client definition: name locale 1941, description 'This jumbo potion restores a large portion of your energy.', definition id 2676, one definition, item class 50, no coin store price", "source": "locale:1941; locale:11527; repo store data (no coin store price found)"},
  {"claim": "Wiki: item is a level 1 potion usable in any job, restores up to 42%-47% of energy, Cannot Sell / Cannot Trade", "source": "wiki page: Jumbo Energy Potion"},
  {"claim": "Wiki: acquired from TCG virtual reward cards 1L31 and 1L73 (both named 'Jumbo Mana Potion')", "source": "wiki page: Jumbo Energy Potion"},
  {"claim": "Client cluster: sits with Jumbo Health Potion (1940) and Jumbo Replenishing Potion (1942), same family of consumables", "source": "locale:1936-1946"},
  {"claim": "Newer client line 151282 describes the potion as restoring 'a large amount of your total energy' (wording changed, item still present in client)", "source": "locale:151282"}],
 "confidence": 0.6,
 "open": ["Only one wiki page supports the sources; no article, video, or vendor evidence was found. The TCG card-source claim rests on that single wiki page.",
  "The cards are named 'Jumbo Mana Potion' but the item is 'Jumbo Energy Potion'. Probably the same potion under an older name, but this is unconfirmed; verify that card 1L31/1L73 rewards this item.",
  "No price or sale data: the item has no coin store price and is marked Cannot Sell/Cannot Trade, so no marketplace or coin shop source.",
  "Retirement status unknown; the wiki does not say when the TCG virtual reward cards stopped granting it.",
  "The wiki's 42%-47% restore figure is the only numeric detail; the client text gives no number."]}
