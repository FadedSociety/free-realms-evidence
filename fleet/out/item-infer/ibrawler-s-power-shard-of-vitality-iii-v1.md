<!-- fleet job=item-infer id=ibrawler-s-power-shard-of-vitality-iii-v1 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[2995, 9576, 6, 2466] model=claude-haiku-5-5 -->
# Brawler's Power Shard of Vitality III

{"item": {"name": "Brawler's Power Shard of Vitality III", "locale_id": 131035, "kind": "other"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop sale to everyone (wiki page text; category 'Coin Shop')", "where": "Coin Shop", "price": "1055 coins", "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Brawler's_Power_Shard_of_Vitality_III (rev 32643; coins list [1055, 1055])"},
  {"type": "vendor", "detail": "Dempsy, Brawler gear merchant (ucdt 2929861923), stocks Brawler's Power Shard of Vitality III", "where": "Snowhill, near the Snowhill Post Office", "price": null, "currency": null, "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:105"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name matches client text id 131035 exactly", "source": "locale:131035"},
  {"claim": "Brawler level 8 power shard, Passive: increases health by 233 in combat; required level 8, Brawler", "source": "https://freerealms.fandom.com/wiki/Brawler's_Power_Shard_of_Vitality_III"},
  {"claim": "Wiki says it is acquired from the Coin Shop, sold to everyone at 1055 coins; categories include Coin Shop and Marketplace Items", "source": "https://freerealms.fandom.com/wiki/Brawler's_Power_Shard_of_Vitality_III"},
  {"claim": "Dempsy, the Snowhill Brawler gear merchant, stocks the Power Shard of Vitality III", "source": "repo:notes/Build Guides/Content/NPCs/NPCs - Snowhill.md:105"},
  {"claim": "Brawler's Power Shard of Vitality III appears in the Bone Bog Cemetery, Bristlewood Glade, Floren Forest, Howling Hills, Mushroom Cavern and Return to Sender dungeon reward/loot tables (listed beside 'Battle Item Mystery Pack')", "source": "repo:notes/Build Guides/Content/Dungeons/Bone Bog Cemetery.md:80; repo:notes/Build Guides/Content/Dungeons/Howling Hills.md:77; repo:notes/Build Guides/Content/Dungeons/Floren Forest.md:69"}
 ],
 "confidence": 0.6,
 "open": [
  "Price conflict: the wiki text says the Coin Shop price is 'the price of' (blank) for everyone and a 10% member discount, but the numeric coins field is [1055, 1055]: both values are identical, so the member discount is not reflected in the data. Needs checking; I kept 1055 coins as the single price and did not invent a member price.",
  "The wiki's Coin Shop and Marketplace Items categories disagree on where it is sold: 'Marketplace Items' may mean the coin-currency marketplace, not Station Cash. No station_cash or igd prices are given, so no Station Cash source is listed.",
  "Dungeon tables in repo notes (Bone Bog Cemetery, Bristlewood Glade, Floren Forest, Howling Hills, Mushroom Cavern, Return to Sender, Seaside Swoopers and others) list the shard next to 'Battle Item Mystery Pack'. I did not confirm whether these are enemy drops, chest rewards, or a dungeon reward table, so no drop or quest_reward source is listed. Needs a check against the dungeon notes.",
  "Kimi (Lakeshore) stocks a 'Power Shard of Vitality III' for Pixie Archer (repo:notes/Build Guides/Content/NPCs/NPCs - Lakeshore.md:77). That is the Archer shard, not this Brawler item, so it is not listed.",
  "The repo Dempsy stock entry gives no price. Dempsy's coin price is unconfirmed; if Dempsy sells at the same 1055 coins, that needs a check. Live status is unsure: the Coin Shop category is on the wiki, and Dempsy's stock is in repo notes, but no revision date or retirement note was found.",
  "Wiki article text has no published date or retirement note; the retired field is null."
 ]}
