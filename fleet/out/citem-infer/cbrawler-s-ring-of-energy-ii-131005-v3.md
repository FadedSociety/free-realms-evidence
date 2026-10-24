<!-- fleet job=citem-infer id=cbrawler-s-ring-of-energy-ii-131005-v3 status=done turns=3 usd=0.0039 tokens(read,write,in,out)=[21950, 15884, 8, 3309] model=claude-haiku-5-5 -->
# Brawler's Ring of Energy II

{"item": {"name": "Brawler's Ring of Energy II", "locale_id": 131005, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Fraz (pixie NPC merchant, sells exclusively Brawler job items); stock listing only, price not captured", "where": "Wugachug", "price": "81 coins (member price 72 coins); UNVERIFIED, reconstructed from FreeRealms-Legacy Cost/MemberDiscount, not a captured Fraz quote", "currency": "coins", "source": "freerealms-wiki/wikitext/10132-48993-ec52c3832f5b.wiki:22 (Fraz Sells list, stock only); repo:prototype/osfr-tools/data/content/vendors.json:45904 (item 75261); repo:prototype/osfr-tools/data/content/stores.json:17321 (item 75261, purchase_price_coins 81, member_price_coins 72, price_provenance kind 'reconstructed')"},
  {"type": "prize_wheel", "detail": "Den of Secrets dungeon, Brawler job prize wheel (every wheel also has a 26 Coins slot)", "where": "Den of Secrets (dungeon)", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Den of Secrets.md:70 (Prize wheel by job table, Brawler row); repo:prototype/osfr-tools/data/content/dungeons/den_of_secrets.json:1107"},
  {"type": "prize_wheel", "detail": "Ice Troll Scout dungeon, Brawler job wheel (with Brawler's Hammer of Rumbling, Brawler's Power Shard of Vitality II, Peek-a-Boo Brawler Pants)", "where": "Ice Troll Scout (dungeon)", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Ice Troll Scout.md:61 (table marked [wiki]); repo:prototype/osfr-tools/data/content/dungeons/ice_troll_scout.json:851"},
  {"type": "prize_wheel", "detail": "The Bat Cave dungeon reward table, Brawler row (listed alongside Brawler's Power Shard of Regeneration II and Bum Rush Brawler Gloves); wheel mechanism not independently confirmed", "where": "The Bat Cave (dungeon)", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/The Bat Cave.md:70; repo:prototype/osfr-tools/data/content/dungeons/the_bat_cave.json:1109"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 131005 is \"Brawler's Ring of Energy II\"; item definition 75261, slot 8, class 25; no model files and no description in the client definition.", "source": "locale:131005; client definition pack"},
  {"claim": "The Fraz wiki Sells list names Brawler's Ring of Energy II (stock only, no price shown).", "source": "freerealms-wiki/wikitext/10132-48993-ec52c3832f5b.wiki:22"},
  {"claim": "Repo vendor data maps Fraz stock to item 75261 by exact name.", "source": "repo:prototype/osfr-tools/data/content/vendors.json:45904"},
  {"claim": "Coin store price 81 (member 72, 10% discount) exists in repo data but its provenance is 'reconstructed' from the FreeRealms-Legacy reference, not a captured in-game quote. Client coin_store_prices also lists 81, which is consistent with the reconstruction but is not independent confirmation of a live sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:17321"},
  {"claim": "Den of Secrets Brawler wheel contains Brawler's Ring of Energy II; the table says every item name exists in the client locale.", "source": "notes/Build Guides/Content/Dungeons/Den of Secrets.md:63-70"},
  {"claim": "Ice Troll Scout Brawler wheel contains Brawler's Ring of Energy II.", "source": "notes/Build Guides/Content/Dungeons/Ice Troll Scout.md:56-61"},
  {"claim": "Bat Cave Brawler reward row lists the name.", "source": "notes/Build Guides/Content/Dungeons/The Bat Cave.md:70"},
  {"claim": "Legacy client definition carries the same name for this item id region.", "source": "refs: FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1210473"}
 ],
 "confidence": 0.5,
 "open": [
  "The 81/72 coin price is reconstructed from the Legacy reference (stores.json price_provenance), not captured from Fraz or any live screen. Treat as unverified.",
  "Fraz's wiki Sells entry gives no price; the earlier claim that the page revision is 2025-05-31 could not be confirmed from the cached wikitext (revid 48993 only).",
  "Coin Shop: no confirmed Coin Shop listing. A claim that sibling Ring II-tier jewelry is sold in the Coin Shop was not verified in the wiki pages I could check, so no Coin Shop source is given.",
  "The three dungeon wheel sources rest on repo build-guide tables (which cite wiki and client-name checks), not on a drop-rate or captured wheel screen. The Bat Cave row's wheel mechanism is not confirmed beyond the note.",
  "Live status is unsure: no source shows Fraz or the wheels still offer this item after the wiki's last revision. Retired status is unknown.",
  "Resell value conflicts: stores.json sell_price_coins is 8; the Ring of Energy V sibling tooltip shows 21. Not resolved for II.",
  "Required level for II is not confirmed (Ring V is 16, Ring I is 1, Ring IV is 12).",
  "Kind 'clothing' is a best-fit guess for a slot-8 accessory."
 ]}
