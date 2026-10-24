<!-- fleet job=schedule-infer id=svheart-flower-v2 status=no_submit turns=2 usd=0.0044 tokens(read,write,in,out)=[11908, 19117, 6, 3717] model=claude-haiku-5-5 -->
# Festival of Hearts

```json
{"event": {"name": "Festival of Hearts", "key": "festival-of-hearts"},
 "kind": "holiday",
 "season": {"name": "Festival of Hearts", "start_month": 2, "start_day": 4, "end_month": 3, "end_day": 31, "source": "(R) Start Feb 4 is the earliest dated start in the pack (2014, wiki Template:News, Game Update 128, 02/04/2014; wiki-only, not re-verified against an article). It is earlier than the 2010 kickoff week (Feb 8, TTH node 80708) and the 2012 Feb 9 update (wiki Template:News/Archive), so it covers all dated starts. End Mar 31 (R): the wiki pages 'Festival of Hearts' and 'Events' say 'held from February through March' (wiki-only). No dated end exists in the pack, so the day 31 is a choice within March. Not Halloween; a new season row is needed."},
 "slots": null,
 "weekly": null,
 "original_dates": [
  {"year": 2010, "start": "2010-02-08", "end": null, "source": "Press kickoff week per http://www.tentonhammer.com:80/node/80708 ('month-long event', week of Feb 8, 2010). In-game live start was the Feb 12, 2010 update per http://www.freerealms.com:80/article/detail.action?articleId=967. Community semi-formal dance Feb 12, 2010 per article 957."},
  {"year": 2011, "start": null, "end": null, "source": "Run confirmed by wiki only (Cupid, Heart Critter, Teddy Bear Costume 'February 2011'); exact dates not in pack."},
  {"year": 2012, "start": "2012-02-09", "end": null, "source": "wiki Template:News/Archive: 'Update of February 9, 2012' listing new Festival of Hearts Marketplace items and event bug fixes. This is an update date, not a confirmed event start."},
  {"year": 2014, "start": "2014-02-04", "end": null, "source": "wiki page Festival of Hearts and wiki Template:News (Game Update 128, 02/04/2014). Wiki-only, not re-verified against an article."}
 ],
 "zones": ["Merry Vale"],
 "runs": {
  "npcs": ["Cudip", "Stone Heart", "Heart Breakers", "Postmaster Vixie"],
  "props_or_areas": ["Merry Vale heart flower (sunflower field, red/pink/magenta; wiki Merry Vale, Festival of Hearts)"],
  "quests": ["Where is the Love?", "A Tale of Two Hearts", "Potent Love Potion", "Softening the Stone", "Sleeping Pixie", "Truffle Shuffle"],
  "activities": ["Daily prize wheel and Coin Wheel for players logged in 30+ minutes (article 967)", "Daily and Members Only quests against Stone Heart and the Heart Breakers (article 2501)", "Community Semi-Formal dance (articles 957, 960)", "Pick a petal from the heart flower daily (locale:426989; year not tied)"],
  "rewards": ["Dove pet pal (Sleeping Pixie, Members Only; wiki Dove)", "Festival daily prize wheel (article 967)", "Gifting Basket random pets, e.g. Cupid (wiki Cupid; 2011)", "Festival items in SC Marketplace: She-Rex and Snowheart (wiki; both introduced Feb 12, 2010), Hearts Outfit, Lovelectric Boombox"]
 },
 "announce": null,
 "revival": {"recurrence": "yearly_season", "why": "Annual Valentine's Day holiday in February, stated 'annual' in articles 969 and 2016 and 'held each February' in the wiki (Cudip, Events). It fits the seasons table. Because live status is unknown, ship it as a season with a staff-enable flag until the product decision is made."},
 "evidence": [
  {"claim": "Festival of Hearts was live in Merry Vale from the Feb 12, 2010 update, with Cudip and the daily prize wheel", "source": "http://www.freerealms.com:80/article/detail.action?articleId=967"},
  {"claim": "Kickoff was the week of Feb 8, 2010, described as a month-long event", "source": "http://www.tentonhammer.com:80/node/80708"},
  {"claim": "First annual community semi-formal dance, Friday Feb 12, 2010", "source": "http://www.freerealms.com:80/article/detail.action?articleId=957; http://www.freerealms.com/article/detail.action?articleId=960"},
  {"claim": "Annual event returned to Merry Vale", "source": "http://www.freerealms.com:80/article/detail.action?articleId=969; http://www.freerealms.com:80/article/detail.action?articleId=2016"},
  {"claim": "Feb 9, 2012 update added Festival of Hearts Marketplace items and fixed event bugs", "source": "wiki Template:News/Archive"},
  {"claim": "2014 run began Feb 4, 2014 (wiki-only)", "source": "wiki page Festival of Hearts; wiki Template:News (Game Update 128)"},
  {"claim": "Festival is 'held from February through March' (wiki-only; the wording appears on the Festival of Hearts and Events pages)", "source": "wiki Festival of Hearts; wiki Events"},
  {"claim": "She-Rex and Snowheart were introduced Feb 12, 2010 as part of the festival", "source": "wiki She-Rex; wiki Snowheart"},
  {"claim": "Festival of Hearts TCG bundle was available only until the festival ended", "source": "http://www.freerealms.com/article/detail.action?articleId=1009"},
  {"claim": "Zone is Merry Vale; Joyful Valley and Vegalegre mentions are excluded", "source": "articles 2501, 967, 969, 2016 (Merry Vale); articles 1057 and 2018 (excluded, unresolved)"}
 ],
 "confidence": 0.6,
 "open": [
  "live status unsure: no current-status source. Product decision.",
  "End date Mar 31 is (R): the day is a choice within the wiki's 'February through March' wording. Treat the end as approximate.",
  "Start Feb 4 is (R): it is the 2014 wiki date chosen to cover the 2010 (Feb 8/12) and 2012 (Feb 9) starts. It may begin early in some years.",
  "2010 has two dates: press kickoff Feb 8 (TTH) and in-game live Feb 12 (article 967). original_dates uses the kickoff; live start is Feb 12.",
  "2013: no evidence in the pack. 2011: run confirmed by wiki, month not dated.",
  "Station Cash prices: the pack's critique says the wiki gives She-Rex SC 349, Snowheart SC 249, Stone Heart's Gummy Bear SC 49 and Stone Heart's Bear Costume SC 199. I did not confirm these amounts in this check, so they are left out. Verify against the wiki wikitext before using them.",
  "Vegalegre (article 2018) and Joyful Valley (article 1057) are unresolved and not used as zones.",
  "No slot cadence and no clock times exist; none are invented. No evidenced announce text.",
  "Pack's 'Potent Love Potion' quest link is not independently verified."
 ],
 "critique_fixes": "Season start is now marked (R) with its reason. The 2010 row states the kickoff date and the live date. The prices claim is corrected to 'not confirmed in this check' rather than 'absent from the pack'. The 2014 source stays wiki-only."
}
```
