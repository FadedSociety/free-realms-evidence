<!-- fleet job=citem-infer id=cbrawler-s-ring-of-energy-ii-131005-v5 status=done turns=2 usd=0.0038 tokens(read,write,in,out)=[7467, 16656, 6, 3208] model=claude-haiku-5-5 -->
# Brawler's Ring of Energy II

{"item": {"name": "Brawler's Ring of Energy II", "locale_id": 131005, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Fraz (pixie NPC merchant, Brawler job stock); listed in Sells, no price shown", "where": "Wugachug", "price": null, "currency": null, "source": "freerealms-wiki/wikitext/10132-48993-ec52c3832f5b.wiki:22"},
  {"type": "prize_wheel", "detail": "Brawler job prize wheel, Den of Secrets dungeon reward table (build-guide table, wiki-backed per note; drop rate not known)", "where": "Den of Secrets (dungeon)", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Den of Secrets.md:63-70; repo:prototype/osfr-tools/data/content/dungeons/den_of_secrets.json:1107"},
  {"type": "prize_wheel", "detail": "Brawler job prize wheel, Ice Troll Scout dungeon reward table (table marked [wiki] in note)", "where": "Ice Troll Scout (dungeon)", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Ice Troll Scout.md:56-61; repo:prototype/osfr-tools/data/content/dungeons/ice_troll_scout.json:851"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131005 is \"Brawler's Ring of Energy II\"; definition 75261, slot 8, class 25.", "source": "locale:131005; client definition pack"},
  {"claim": "Fraz's wiki Sells list names Brawler's Ring of Energy II, with no price.", "source": "freerealms-wiki/wikitext/10132-48993-ec52c3832f5b.wiki:22"},
  {"claim": "FreeRealms-Legacy definition Id 75261 (NameId 131005) has Cost 806, MemberDiscount 10 (member price would be 725).", "source": "refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1210472-1210480"},
  {"claim": "Repo stores.json row for item 75261 has purchase 81 / member 72 / sell 8, marked 'reconstructed' with no captured quote; it claims Legacy Cost as its basis, but Legacy says 806, so the row does not match its stated basis.", "source": "repo:prototype/osfr-tools/data/content/stores.json:17321"},
  {"claim": "Client coin_store_prices lists 81 for definition 75261.", "source": "client definition pack (coin_store_prices [81])"},
  {"claim": "The wiki's Ninja's Ring of Energy II (same Ring II tier, Legacy-sourced cost 806) is listed as a Coin Shop item at 806 coins, member 725. This supports 806 as the likely Coin Shop tier price for Brawler's Ring II, but it is a different item.", "source": "freerealms-wiki/wikitext/10878-32088-142f72e68822.wiki:1"},
  {"claim": "Den of Secrets and Ice Troll Scout build-guide tables list the item in Brawler reward rows.", "source": "notes/Build Guides/Content/Dungeons/Den of Secrets.md:63-70; Ice Troll Scout.md:56-61"}
 ],
 "confidence": 0.4,
 "open": [
  "PRICE CONFLICT, unresolved: stores.json purchase 81 / member 72 and client coin_store_prices 81 versus FreeRealms-Legacy Cost 806 (member 725) for the same definition 75261. The stores.json 'reconstructed' basis cites Legacy, which says 806, so the 81 is not Legacy-derived. Likely the true coin price is 806/725 by analogy with Ninja's Ring of Energy II on the wiki, but no captured quote for Brawler's Ring II confirms it. Coin store price and vendor are both unconfirmed.",
  "No coin-shop source is listed: the 81 is unverified and the 806 is only a Legacy cost plus an analogy to a different ring. Hold until a captured Coin Shop listing or quote resolves it.",
  "Bat Cave (the_bat_cave.json:1109; The Bat Cave.md:70) has a Brawler reward row listing this item, but the wheel mechanism is unconfirmed; dropped from prize_wheel sources.",
  "Prize-wheel rows rest on repo build-guide tables, not drop-rate or captured wheel evidence.",
  "Live status unsure: no source shows Fraz or the wheels still offer this item after the wiki's last revision. Retired status unknown.",
  "Resell value conflicts: stores.json sell_price_coins 8 versus Ring of Energy V tooltip 21; unresolved for II.",
  "Required level for II not confirmed (Ring V 16, Ring I 1, Ring IV 12).",
  "Kind 'clothing' is a best-fit guess for a slot-8 accessory."
 ]}
