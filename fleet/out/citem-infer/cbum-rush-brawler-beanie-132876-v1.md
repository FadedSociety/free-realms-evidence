<!-- fleet job=citem-infer id=cbum-rush-brawler-beanie-132876-v1 status=done turns=6 usd=0.0054 tokens(read,write,in,out)=[70956, 21279, 14, 4098] model=claude-haiku-5-5 -->
# Bum Rush Brawler Beanie

{"item": {"name": "Bum Rush Brawler Beanie", "locale_id": 132876, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Fraz (pixie NPC merchant, sells exclusively Brawler job items)", "where": "Wugachug", "price": "453 coins (member price 407 coins with 10% member discount; sell-back 45 coins)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75868 (purchase_price_coins 453, member_price_coins 407, sell_price_coins 45, category 101); wiki page Fraz, Sells list (https://freerealms.fandom.com/wiki/Fraz, revision 2025-05-31); repo:prototype/osfr-tools/data/content/vendors.json:46113-46154"},
  {"type": "prize_wheel", "detail": "Danger Peaks prize wheel, Brawler job slot (one of the Brawler wheel items)", "where": "Danger Peaks (dungeon)", "price": null, "currency": null, "source": "notes/Build Guides/Content/Dungeons/Danger Peaks.md lines 61-68 (Prize wheel by job > Brawler; cites wiki and client names); repo:prototype/osfr-tools/data/content/dungeons/danger_peaks.json:2299"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item name locale:132876 'Bum Rush Brawler Beanie'; definition 75868, slot 1, class 25, model brawler_<race>_<gender>_head_beaniewglasses.adr", "source": "client definition in task pack; locale:132876"},
  {"claim": "Fraz, a pixie merchant in Wugachug who sells exclusively Brawler job items, stocks Bum Rush Brawler Beanie", "source": "wiki page Fraz (https://freerealms.fandom.com/wiki/Fraz), Sells section"},
  {"claim": "Store reference price 453 coins for item 75868 (member 407, sell 45)", "source": "repo:prototype/osfr-tools/data/content/stores.json:15628 item_id 75868"},
  {"claim": "Danger Peaks prize wheel for the Brawler job includes Bum Rush Brawler Beanie", "source": "notes/Build Guides/Content/Dungeons/Danger Peaks.md:68"},
  {"claim": "Bum Rush set is also the Brawler bonus-goal clothing set in dungeons (random piece per player)", "source": "notes/Build Guides/Content/Dungeons/Danger Peaks.md:56,74 (wiki-based)"}
 ],
 "confidence": 0.75,
 "open": [
  "The 453 coin price is a stores.json reference price, not a captured NPC quote (vendors.json price_basis says so). The wiki Fraz entry gives no price, so confirm the live Fraz price before trusting 453.",
  "Retired status not established: no source states whether Fraz still sells this piece or whether the prize wheel still includes it. Left null.",
  "Dungeon bonus-goal clothing (Danger Peaks and other Brawler dungeons) gives a random piece of the Bum Rush or Peek-a-Boo set, with random slot and colour. It may yield this beanie, but no source names the beanie specifically, so it is not listed as a source.",
  "The Danger Peaks prize-wheel entry is cited from a build-guide note based on the wiki. The dungeon data marks the item ID as unresolved (target_id null), so the wheel link rests on the name match alone.",
  "No wiki article, image, or video covers this item, and no collection, crafting, promotion, or Coin Shop listing was found for it."
 ]}
