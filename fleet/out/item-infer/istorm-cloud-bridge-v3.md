<!-- fleet job=item-infer id=istorm-cloud-bridge-v3 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6215, 8537, 6, 2824] model=claude-haiku-5-5 -->
# Storm Cloud Bridge

{"item": {"name": "Storm Cloud Bridge", "locale_id": 29552, "kind": "furniture"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, available to everyone (housing furniture, added in the June housing update)", "where": "Station Cash Marketplace (SC Marketplace)", "price": "275 SC (regular price)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Storm_Cloud_Bridge (rev 37185 wikitext, freerealms-wiki/wikitext/2455-37185-0891521ba71f.wiki line 1: 'available to everyone in the Station Cash Marketplace at the regular price of {{SC|275}}'); categories Furniture, Marketplace Items, SC Marketplace"},
  {"type": "quest_reward", "detail": "Rob Robbie Daily, Day-7 chest at Robbie's Tent (Camp Robbie): the '7th Day Chest Items' list includes '1 Storm Cloud Bridge'. Day 7 reward is 'a random Station Cash Item, housing items'. Chest contents are a list, so a given chest may or may not yield this item.", "where": "Camp Robbie, Robbie's Tent", "price": null, "currency": null, "source": "freerealms-wiki/wikitext/7326-23902-e7ea599f40c4.wiki lines 14-19 and 44-45 (Reward section; 7th Day Chest Items list)"},
  {"type": "marketplace", "detail": "Retired access route: Foreman Redd / Foreman Moser / Foreman Hetfield SC Marketplace filter (housing/playground items) listed the item", "where": "Station Cash Marketplace via Foreman NPCs (retired)", "price": "247 SC shown in those older filter lists", "currency": "station_cash", "source": "freerealms-wiki/wikitext/8625-44484-e804afc31e49.wiki line 34; 8623-50087-e07a869f0e80.wiki line 29; 8615-50082-d07e4eafbdd8.wiki line 28; quest-lines/npc-packs.json (Foreman entries)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Storm Cloud Bridge is available to everyone in the SC Marketplace at the regular price of 275 SC.", "source": "https://freerealms.fandom.com/wiki/Storm_Cloud_Bridge (freerealms-wiki/wikitext/2455-37185-0891521ba71f.wiki line 1)"},
  {"claim": "Client name text is 'Storm Cloud Bridge'.", "source": "locale:29552"},
  {"claim": "Storm Cloud Bridge was added as a housing item, with Suspension Bridge and Cloud Bridge.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1521 ; http://www.freerealms.com:80/article/detail.action?articleId=1532"},
  {"claim": "Day-7 Rob Robbie Daily chest contents include 1 Storm Cloud Bridge.", "source": "freerealms-wiki/wikitext/7326-23902-e7ea599f40c4.wiki lines 14-45"},
  {"claim": "A second SC list page prices Storm Cloud Bridge at 247 SC, alongside Stone Bridge 157 and Suspension Bridge 157 (a Station Cash list with no date shown).", "source": "freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki line 231"},
  {"claim": "The wiki's convention for SC items: regular price 275 SC, Members 10% discount 247 SC. Shown on Chuck (pet) and Jackhammer (tool), so 247 is most likely the Member price for SC items generally. Not stated directly for this item.", "source": "freerealms-wiki/wikitext/3591-48010-b4ea6e37f68d.wiki line 7; freerealms-wiki/wikitext/9320-45556-a1441372e3df.wiki line 2"},
  {"claim": "Foreman Redd, Moser and Hetfield were NPCs that opened the SC Marketplace filtered to housing/playground items and are no longer in-game.", "source": "quest-lines/npc-packs.json; freerealms-wiki/wikitext/8625-44484-e804afc31e49.wiki line 34"},
  {"claim": "A store bundle row exists on the server side (Id 4404, NameId 29552), with no price in the row.", "source": "Lxzxrus-Free-Realms-Server/src/Resources/StoreBundles.json:17512; FreeRealms-Legacy/src/Resources/StoreBundles.json:17580"}
 ],
 "confidence": 0.6,
 "open": [
  "Price: 275 SC is the regular price per rev 37185. 247 SC is most likely the Member 10% discount price, by the wiki's convention on Chuck and Jackhammer, but no page states it for Storm Cloud Bridge. Treat 247 as inferred.",
  "The Day-7 chest is random and the item appears only in the chest list; drop rate per chest is unknown.",
  "No coin vendor, enemy drop, crafting, prize wheel, or collection source found in the pack or repo searches.",
  "Live status unverified: the Foreman access route is retired, and the SC Marketplace listing and store bundle row have no removal date. Whether it is still sold is unknown. retired left null."
 ]}
