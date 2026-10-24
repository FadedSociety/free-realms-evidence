<!-- fleet job=citem-infer id=cbrawler-s-ring-of-energy-ii-131005-v4 status=done turns=2 usd=0.0045 tokens(read,write,in,out)=[7874, 22831, 6, 3214] model=claude-haiku-5-5 -->
# Brawler's Ring of Energy II

{"item": {"name": "Brawler's Ring of Energy II", "locale_id": 131005, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Fraz (pixie NPC merchant, Brawler job stock; wiki Sells list names this item, no price shown)", "where": "Wugachug", "price": null, "currency": null, "source": "freerealms-wiki/wikitext/10132-48993-ec52c3832f5b.wiki:22; quest-lines/npc-packs.json:87977 (Fraz Sells text); repo:prototype/osfr-tools/data/content/vendors.json:45904 (item 75261)"},
  {"type": "vendor", "detail": "Coin store sale (vendor not named in any captured source); price is unverified", "where": null, "price": "81 coins (member price 72 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75261 (purchase_price_coins 81, member_price_coins 72, price_provenance kind 'reconstructed'); client coin_store_prices [81] in client definition 75261. Conflict: FreeRealms-Legacy ClientItemDefinitions.json:1210480 gives Cost 806 for NameId 131005, so the 81 is not confirmed by the Legacy reference it cites"},
  {"type": "prize_wheel", "detail": "Den of Secrets dungeon, Brawler job prize wheel", "where": "Den of Secrets (dungeon)", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Den of Secrets.md:63-70; repo:prototype/osfr-tools/data/content/dungeons/den_of_secrets.json:1107 (build-guide table, wiki-backed per note)"},
  {"type": "prize_wheel", "detail": "Ice Troll Scout dungeon, Brawler job prize wheel", "where": "Ice Troll Scout (dungeon)", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Ice Troll Scout.md:56-61 (table marked [wiki]); repo:prototype/osfr-tools/data/content/dungeons/ice_troll_scout.json:851"},
  {"type": "prize_wheel", "detail": "The Bat Cave dungeon reward table, Brawler row; wheel mechanism NOT confirmed", "where": "The Bat Cave (dungeon)", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/The Bat Cave.md:70; repo:prototype/osfr-tools/data/content/dungeons/the_bat_cave.json:1109 (weak: reward row only)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131005 is \"Brawler's Ring of Energy II\"; item definition 75261, slot 8, class 25.", "source": "locale:131005; client definition pack"},
  {"claim": "Fraz's wiki Sells list names Brawler's Ring of Energy II (stock only, no price).", "source": "freerealms-wiki/wikitext/10132-48993-ec52c3832f5b.wiki:22"},
  {"claim": "Repo stores.json item 75261 has purchase 81 / member 72, but provenance is 'reconstructed', not a captured quote.", "source": "repo:prototype/osfr-tools/data/content/stores.json:17321"},
  {"claim": "FreeRealms-Legacy definition for NameId 131005 has Cost 806, not 81, so the stores.json basis cited does not match the Legacy row.", "source": "refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1210476-1210480"},
  {"claim": "Den of Secrets, Ice Troll Scout and Bat Cave build-guide tables list the item in Brawler reward rows.", "source": "notes/Build Guides/Content/Dungeons/Den of Secrets.md:63-70; Ice Troll Scout.md:56-61; The Bat Cave.md:70"}
 ],
 "confidence": 0.4,
 "open": [
  "Price conflict: stores.json and client coin_store_prices say 81 (member 72), but FreeRealms-Legacy Cost for this NameId is 806. No captured in-game quote resolves it. Treat 81/72 as unverified.",
  "Fraz's wiki Sells entry gives no price; the Fraz vendor source carries no price.",
  "Coin Shop: no confirmed Coin Shop listing. The claim that Ninja's Ring of Energy II (wiki 10878-32088) says Ring II-tier jewelry is sold in the Coin Shop was not verified in this pass, so no Coin Shop source is given. The coin-store sale row above is unnamed.",
  "Bat Cave wheel mechanism is not confirmed; that row is a reward-table note only.",
  "Den of Secrets and Ice Troll Scout wheel rows rest on repo build-guide tables, not drop-rate or captured wheel evidence.",
  "Live status unsure: no source shows Fraz or the wheels still offer this item after the wiki's last revision. Retired status unknown.",
  "Resell value conflicts: stores.json sell_price_coins 8 vs. Ring of Energy V tooltip 21; unresolved for II.",
  "Required level for II not confirmed (Ring V 16, Ring I 1, Ring IV 12).",
  "Kind 'clothing' is a best-fit guess for a slot-8 accessory."
 ]}
