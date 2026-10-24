<!-- fleet job=citem-infer id=cjourneyman-wizard-cap-133414-v1 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[20223, 12980, 10, 3098] model=claude-haiku-5-5 -->
# Journeyman Wizard Cap

{"item": {"name": "Journeyman Wizard Cap", "locale_id": 133414, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Redsden (Wizard job-items vendor), 'Sells' list", "where": null, "price": "453 coins (purchase reference price); 407 coins member price; 45 coins sell-back", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Redsden (Sells: [Journeyman] [Wizard] [Cap]); repo:prototype/osfr-tools/data/content/vendors.json:42353-42394 (item_id 76406)"},
  {"type": "drop", "detail": "Combat mini-game loot, Difficulty 1 and Difficulty 2 dungeons while playing as Wizard (the Journeyman set's listed source; the Cap is not named individually in these sources)", "where": "Difficulty 2 dungeons e.g. Den of Secrets, Robgoblin Treasure Trove, Highroad Hijinx, Danger Peaks, The Bat Cave!, Sweetwater Climb, Arachnia's Lair (Wilds, Merry Vale, Snowhill, Wugachug, Bristlewood)", "price": null, "currency": null, "source": "wiki Category:Journeyman (https://freerealms.fandom.com/wiki/Category:Journeyman); dungeon pages list '[Wizard]: Hedge, [Journeyman]'; wiki Nekark page lists '1 piece from the [Journeyman] [Wizard] Set'"},
  {"type": "coin_shop", "detail": "Coin Shop, per wiki set category", "where": "Coin Shop", "price": null, "currency": null, "source": "wiki Category:Journeyman ('can be acquired through the Coin Shop')"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 133414 is 'Journeyman Wizard Cap'; kind clothing, slot 1, class 8, model caster_<race>_<gender>_head_pointedcap.adr", "source": "locale:133414; client definition definition_ids 76406"},
  {"claim": "Redsden sells Journeyman Wizard Cap (Wizard job items)", "source": "https://freerealms.fandom.com/wiki/Redsden"},
  {"claim": "Journeyman was a Level 6 Wizard combat clothing set obtainable via Coin Shop or Difficulty 1 and 2 combat mini-games as Wizard; past tense 'was' is not a retirement statement", "source": "https://freerealms.fandom.com/wiki/Category:Journeyman"},
  {"claim": "Mini-game dungeon pages list Journeyman Wizard set drops for Wizard players", "source": "wiki Den of Secrets, Robgoblin Treasure Trove, Highroad Hijinx, Danger Peaks, The Bat Cave!, Sweetwater Climb, Arachnia's Lair; wiki Nekark (1 piece from the Journeyman Wizard Set)"},
  {"claim": "Reference price 453 coins / member 407 / sell 45 is recorded for item 76406 in our vendor data, sourced from stores.json, and is labelled a reference price, not a captured NPC quote", "source": "repo:prototype/osfr-tools/data/content/vendors.json:42353-42394"}
 ],
 "confidence": 0.6,
 "open": [
  "The 453-coin price is not traceable: a text search of prototype/osfr-tools/data/content/stores.json finds no entry with item_id 76406. The client's coin_store_prices value (453) matches many other items' prices, and vendors.json cites stores.json for item 76406 but the row is missing. Treat the price as unverified until stores.json is checked.",
  "Redsden's location (zone) is not given in the sources reviewed.",
  "Which Wizard mini-game drops or set pieces give this specific Cap is not confirmed; the wiki names only the set.",
  "Retirement status is unknown. The wiki lists the Cap on Redsden with a 2025-03-21 revision, so it appears live there, but no source states it was retired or still sold.",
  "The Coin Shop claim comes only from the category text, with no Coin Shop listing or price for this Cap."
 ]}
