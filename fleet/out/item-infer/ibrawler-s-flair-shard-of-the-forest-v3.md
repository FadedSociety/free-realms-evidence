<!-- fleet job=item-infer id=ibrawler-s-flair-shard-of-the-forest-v3 status=done turns=5 usd=0.0047 tokens(read,write,in,out)=[51226, 21331, 12, 2945] model=claude-haiku-5-5 -->
# Brawler's Flair Shard of the Forest

{"item": {"name": "Brawler's Flair Shard of the Forest", "locale_id": 131040, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop purchase of a level 1 Brawler flair shard (weapon particle effect)", "where": "Coin Shop", "price": "750 coins (wiki wikitext price; the rendered wiki sentence is blank)", "currency": "coins", "source": "freerealms-wiki/wikitext/16798-32680-3c22f158a8eb.wiki line 5: \"It is acquired from the [[Coin Shop]] where it sells for {{Coin|750}}\"; wiki page https://freerealms.fandom.com/wiki/Brawler's_Flair_Shard_of_the_Forest; Category:Coin Shop"},
  {"type": "vendor", "detail": "Miesha, human female Brawler-job merchant; stock list includes Brawler's Flair Shard of the Forest alongside Bell Brawler gear", "where": "Merry Vale", "price": "unknown (no price in any captured source; repo vendors.json figure of 750 is an unconfirmed reference, not an NPC quote)", "currency": "coins", "source": "freerealms-wiki/wikitext/10136-46798-5b3aa576c151.wiki lines 12 and 21 (Sells list, \"[[Brawler's Flair Shard of the Forest]]\"; intro: sells exclusively Brawler Job items; Trivia: introduced August 6, 2013)"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name text is \"Brawler's Flair Shard of the Forest\", NameId 131040", "source": "locale:131040"},
  {"claim": "Coin Shop price is 750 coins per the wiki wikitext template {{Coin|750}}; the rendered sentence on the wiki and in harvest lists reads 'sells for .' (blank), so the number rests on the wikitext alone", "source": "freerealms-wiki/wikitext/16798-32680-3c22f158a8eb.wiki line 5; freerealms-wiki/harvest/lists/weapons.json:9323"},
  {"claim": "Sibling Brawler flair shards on the Coin Shop use the same wikitext 750 template (e.g., Brawler's Flair Shard of Smoldering, Ice, Valentines; Archer, Medic, Ninja, Warrior, Wizard Forest shards)", "source": "freerealms-wiki/wikitext/16795-32678-35261aebbcaa.wiki line 5; 16814-32674-02157faf4824.wiki line 5; 16797-32681-d7af2b388f0a.wiki line 5"},
  {"claim": "Miesha's wiki Sells list includes Brawler's Flair Shard of the Forest; no price is given on the page", "source": "freerealms-wiki/wikitext/10136-46798-5b3aa576c151.wiki line 21"},
  {"claim": "Tooltip: 'Casts a green glow over your weapons. Minty Fresh!', Required Level 1 Brawler, Resell Value 75 (resell value, not a purchase price)", "source": "image:item_tooltip on https://freerealms.fandom.com/wiki/Brawler's_Flair_Shard_of_the_Forest; freerealms-wiki/harvest/lists/image_text.json:99639"},
  {"claim": "Member price 675 and sell-back 375 come only from the repo stores.json reference, not from any wiki statement; 375 conflicts with the tooltip resell 75 and is unresolved", "source": "prototype/osfr-tools/data/content/vendors.json:22878-22915 (reference, not a captured quote)"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin Shop price 750 is evidenced only by the wikitext template; the rendered wiki sentence is blank, and no live Coin Shop capture confirms it. Member price (675) is unsourced to the wiki and not verified.",
  "Miesha's price for this shard is unknown. The 750 in the repo vendors.json is a reference value, not evidenced for her stock; the Miesha wiki page lists the shard without a price.",
  "Sell-back 375 (repo) conflicts with the tooltip Resell Value 75; the tooltip is the only in-game evidence, so 375 is unresolved.",
  "No retirement date or retirement statement exists in any captured source; retired is null. Live status needs a check against the current Coin Shop and Miesha stock.",
  "No drop, quest, event, prize wheel, or crafting source is evidenced for this item.",
  "Kind 'other' is used because the schema has no flair category; it is a weapon-enhancing cosmetic shard."
 ]}
