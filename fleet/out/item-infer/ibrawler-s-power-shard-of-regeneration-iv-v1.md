<!-- fleet job=item-infer id=ibrawler-s-power-shard-of-regeneration-iv-v1 status=done turns=5 usd=0.0053 tokens(read,write,in,out)=[48714, 22120, 12, 4165] model=claude-haiku-5-5 -->
# Brawler's Power Shard of Regeneration IV

{"item": {"name": "Brawler's Power Shard of Regeneration IV", "locale_id": 131025, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop, sold to everyone; Members pay the 10% discount price", "where": "Coin Shop", "price": "1504 coins (everyone); 1353 coins (Members, 10% discount)", "currency": "coins", "source": "wiki: https://freerealms.fandom.com/wiki/Brawler's_Power_Shard_of_Regeneration_IV (rev 32651; categories 'Coin Shop', 'Coin Power Shards'; coins [1504, 1353]; text 'sells to everyone ... and to Members at the 10% discount price')"},
  {"type": "vendor", "detail": "Evander, Brawler job merchant (introduced 6 August 2013, replaced Ned); sells it in stock list", "where": "Mire's Edge, campfire near Donovan Shadeweaver's home (Blackspore Swamp area)", "price": "1504 coins (purchase); 1353 coins (member price); 752 coins (sell-back)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/vendors.json:2096-2137 (stock_source: wiki page Evander, https://freerealms.fandom.com/wiki/Evander, section Sells); repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:88. Prices are the stores.json reference price, not a captured NPC quote (price_basis)."},
  {"type": "prize_wheel", "detail": "Moldy Shamblers dungeon, Brawler prize wheel", "where": "Moldy Shamblers dungeon", "price": null, "currency": null, "source": "repo:prototype/osfr-tools/data/content/dungeons/moldy_shamblers.json:984 (wiki-cited, via notes/Build Guides/Content/Dungeons/Moldy Shamblers.md > Rewards > Prize wheel by job > Brawler); another answer: enemy 'Moldy Shambler' (final)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Item name and client locale ID 131025 match exactly", "source": "locale:131025"},
  {"claim": "Wiki lists it under Coin Shop, sold to everyone at 1504 coins and to Members at a 10% discount price of 1353 coins (1353 is the Members price, not a temporary sale)", "source": "https://freerealms.fandom.com/wiki/Brawler's_Power_Shard_of_Regeneration_IV"},
  {"claim": "Brawler job merchant Evander sells the item; price 1504 purchase / 1353 member / 752 sell", "source": "repo:prototype/osfr-tools/data/content/vendors.json:2096-2137; wiki page https://freerealms.fandom.com/wiki/Evander (Sells section, rev 2023-05-28)"},
  {"claim": "Evander is a Brawler job merchant at the Mire's Edge campfire, introduced 6 August 2013", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Blackspore Swamp.md:88"},
  {"claim": "Moldy Shamblers Brawler prize wheel contains the item", "source": "repo:prototype/osfr-tools/data/content/dungeons/moldy_shamblers.json:984 and :2148 (the item has no definition ID yet)"},
  {"claim": "Wiki Marketplace Items category is present, but no SC Marketplace or Station Cash price is given", "source": "https://freerealms.fandom.com/wiki/Brawler's_Power_Shard_of_Regeneration_IV (categories)"}
 ],
 "confidence": 0.7,
 "open": [
  "Prince of Low Tide as a Brawler prize-wheel source is unverified: the only support is an 'unresolved' answer citing 'Prize wheel, Brawler (wiki)' with no page or repo line. Left out.",
  "The Evander prices come from stores.json reference data, not a captured in-game quote; the wiki Coin Shop prices (1504/1353) agree with them.",
  "The Moldy Shamblers prize-wheel entry rests on a repo reconstruction (the item has no definition ID); the underlying notes page's wiki citation was not re-read here.",
  "The wiki's Coin Shop and Evander vendor listings both exist; the vendor and Coin Shop may be the same stock, or the item may have been sold in both places at different times. Not resolved.",
  "Retirement status not stated in any source; live = yes is based on the current wiki Coin Shop category and the Evander 2023 listing."
 ]}
