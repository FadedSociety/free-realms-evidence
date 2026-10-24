<!-- fleet job=citem-infer id=cbrawler-s-necklace-of-vitality-v-131003-v1 status=done turns=7 usd=0.0053 tokens(read,write,in,out)=[76809, 19165, 16, 4365] model=claude-haiku-5-5 -->
# Brawler's Necklace of Vitality V

{"item": {"name": "Brawler's Necklace of Vitality V", "locale_id": 131003, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale (Brawler gear, necklace tier V). Store row lists purchase price 2152 coins; members 1936 coins (10% member discount). Sell-back 215 coins.", "where": "Coin Shop", "price": "2152 coins (member price 1936 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75259 (price_provenance kind 'reconstructed': from legacy reference Cost and MemberDiscount, no captured retail quote); sibling wiki pattern: 'Brawler's Necklace of Vitality III' page says acquired from the Coin Shop with member 10% discount"},
  {"type": "prize_wheel", "detail": "Brawler Prize Wheel at Mushroom Mania! (wheel cost 77 coins)", "where": "Mushroom Mania!", "price": "77 coins per wheel spin", "currency": "coins", "source": "wiki page 'Mushroom Mania!' (Brawler Prize Wheel list)"},
  {"type": "prize_wheel", "detail": "Brawler Prize Wheel at Trail of Betrayal (wheel cost 307 coins)", "where": "Trail of Betrayal", "price": "307 coins per wheel spin", "currency": "coins", "source": "wiki page 'Trail of Betrayal' (Brawler Prize Wheel list)"},
  {"type": "prize_wheel", "detail": "Brawler Prize Wheel at Snowy Canyon (wheel cost 117 coins); the notes name Snowy Canyon as the tier V dungeon", "where": "Snowy Canyon", "price": "117 coins per wheel spin", "currency": "coins", "source": "wiki page 'Snowy Canyon' (Brawler Prize Wheel list); repo:notes/Build Guides/Gameplay/Items and Inventory.md:192 (tier V = Snowy Canyon)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name and locale id: 'Brawler's Necklace of Vitality V', locale 131003, single definition 75259, slot 8, class 25", "source": "locale:131003"},
  {"claim": "Store row for definition 75259 exists with purchase price 2152 coins, member price 1936 coins, sell price 215 coins, not marked no_sale", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75259"},
  {"claim": "Wiki prize wheel pages list 'Brawler's Necklace of Vitality V' on the Brawler Prize Wheel at Mushroom Mania!, Trail of Betrayal and Snowy Canyon, each with a per-spin coin cost", "source": "wiki pages: Mushroom Mania!, Trail of Betrayal, Snowy Canyon"},
  {"claim": "Sibling Brawler necklaces (Vitality III) are documented as Coin Shop items with a 10% member discount", "source": "wiki page: Brawler's Necklace of Vitality III"},
  {"claim": "Dungeon wheels carry a necklace per job with tier numeral equal to difficulty; V is Snowy Canyon", "source": "repo:notes/Build Guides/Gameplay/Items and Inventory.md:192"}
 ],
 "confidence": 0.6,
 "open": [
  "The 2152-coin Coin Shop price is 'reconstructed' in stores.json (legacy reference cost), not a captured retail quote. The wiki Vitality III page gives the Coin Shop route but its price text is blank in the extract, so 2152 is unconfirmed.",
  "The Coin Shop claim for the V tier specifically is inferred from the stores row and the sibling tiers; no wiki page for Vitality V itself was in the pack.",
  "The stores.json row sits in category 108; the category name was not resolved, so the exact Coin Shop section is unknown.",
  "The coin pack field 'coin_store_prices: [2152]' is the price value, not an item id; the store row is keyed by item 75259.",
  "Live status: the wiki prize wheel lists are the only current-era evidence. Whether those wheels are still running today is not confirmed, and no retirement note was found, so live is marked yes on the first-pass tag and the wiki lists. Confidence is limited accordingly.",
  "Wheel costs are per spin and were read from wiki text; the members' extra coin amount on the results screen is not counted here."
 ]}
