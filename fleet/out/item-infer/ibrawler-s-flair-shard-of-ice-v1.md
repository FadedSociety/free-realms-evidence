<!-- fleet job=item-infer id=ibrawler-s-flair-shard-of-ice-v1 status=done turns=5 usd=0.0032 tokens(read,write,in,out)=[29361, 13440, 12, 2542] model=claude-haiku-5-5 -->
# Brawler's Flair Shard of Ice

{"item": {"name": "Brawler's Flair Shard of Ice", "locale_id": 131039, "kind": "consumable"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop (flair shard; wiki page says it is acquired from the Coin Shop)", "where": "Coin Shop", "price": "750 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Brawler's_Flair_Shard_of_Ice (categories: Coin Shop, Coin Flair, Flair Shard, Marketplace Items; body: 'It is acquired from the Coin Shop where it sells for' 750 coins)"},
  {"type": "vendor", "detail": "Miesha (Brawler job merchant, sells list)", "where": "Merry Vale (repo: prototype/osfr-tools/data/content/npcs/merry_vale.json:19826, NPC 'Miesha')", "price": "750 coins purchase; 675 coins member price; 375 coins sell-back", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Miesha (Sells section, 'Brawler's Flair Shard of Ice'); repo:prototype/osfr-tools/data/content/vendors.json:22836-22870 (item_id 75295, name_id 131039)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name and client locale ID 131039 = \"Brawler's Flair Shard of Ice\"", "source": "locale:131039"},
  {"claim": "Wiki item page: level 1 Brawler flair shard, acquired from the Coin Shop, sells for 750 coins; categories Coin Shop and Marketplace Items", "source": "https://freerealms.fandom.com/wiki/Brawler's_Flair_Shard_of_Ice"},
  {"claim": "Miesha's wiki Sells list includes Brawler's Flair Shard of Ice; repo records purchase 750 coins, member 675 coins, sell 375 coins", "source": "https://freerealms.fandom.com/wiki/Miesha; repo:prototype/osfr-tools/data/content/vendors.json:22836"},
  {"claim": "Miesha is a Brawler merchant located in Merry Vale", "source": "repo:prototype/osfr-tools/data/content/npcs/merry_vale.json:19826"},
  {"claim": "Client image files exist for the wiki item page (item and held images)", "source": "lookup wiki: File:Brawler's Flair Shard of Ice item.jpg"}
 ],
 "confidence": 0.7,
 "open": ["The 750-coin price comes from the wiki and is the repo's stores.json reference price; the repo itself notes there is no captured retail NPC quote, so treat 750 as a reference, not a verified live quote.",
  "Member price 675 coins and sell-back 375 coins are repo values from the stores reference; no wiki page in the pack confirms them. The 675 member price is a membership discount, not a separate source.",
  "The Coin Shop and Miesha are both listed; it is unclear whether these are the same sale (Coin Shop listing sold by Miesha) or two separate listings. The pack does not settle it.",
  "The wiki page carries 'Pages with broken file links' and the pack has no direct wiki evidence for a Miesha location beyond the repo NPC record.",
  "No quest reward, enemy drop, event, prize wheel, crafting, or collection source was found for this item in the pack or repo.",
  "Live status and retirement are not stated by any source here. The wiki's marketplace category does not indicate retirement; a live check is needed."]}
