<!-- fleet job=event-infer id=vheart-festival-festival-des-c-urs-v8 status=done turns=2 usd=0.0038 tokens(read,write,in,out)=[8777, 11812, 6, 4487] model=claude-haiku-5-5 -->
# Heart Festival (Festival des Cœurs)

```json
{
 "event": {
  "name": "Festival of Hearts",
  "aliases": ["Heart Festival (used as the pack title only; see open)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Starting with the February 12, 2010 update (Merry Vale)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=967"},
  {"year": 2012, "when": "Update of February 7, 2012 launch section 'Festival of Hearts' (Merry Vale celebrating; Cudip and Stone Heart); February 9, 2012 update also fixed Festival of Hearts bugs", "source": "wiki: Template:News/Archive, 'Update of February 7, 2012' and 'Update of February 9, 2012'"}
 ],
 "recurring": "Annual, each February (wiki: Cudip, 'take places annually each February'; wiki: Festival of Hearts, 'annual Valentine's Day themed event'). Dated runs: Feb 2010 and Feb 2012 (2011 has wiki-only evidence, no month).",
 "zones": ["Merry Vale"],
 "npcs": ["Cudip (locale 1418, 432861; wiki: Cudip; article 1053)", "Stone Heart (locale 427176)", "Jecca (locale 427178)", "Postmaster Vixie (locale 427172)", "Dubawug (locale 427242)"],
 "quests": ["Petal Picker (wiki: Festival of Hearts questline, repeatable once a day, given by Cudip)", "A Bundle of Love (wiki: Festival of Hearts questline)"],
 "activities": [
  "Pick a petal from the heart flower every day (locale 426989)",
  "Spin the daily Festival of Hearts wheel for bonus prizes (locale 400038)",
  "Complete festival repeatable quests; 100 of them earns the Errand Lover achievement (locale 5103220, 5103221)",
  "Help Cudip study the heart-flower petals (locale 432861, 1418)",
  "Help stop Stone Heart's heartbreakers with a love potion (locale 427176, 427178)",
  "Buy the Festival of Hearts TCG Bundle while it lasts (locale 4874, 4875)"
 ],
 "items": [
  {"name": "Festival of Hearts Wheel", "price": null, "currency": "reward", "source": "locale:400039, locale:400038"},
  {"name": "Festival of Hearts TCG Bundle", "price": null, "currency": null, "source": "locale:4874, locale:4875"}
 ],
 "rewards": [
  "Daily wheel bonus prizes (locale 400038)",
  "Festival of Hearts TCG Bundle: Emo Raptor Loot card, Edwin Goldstory and Commander Kluggenkrush promo cards, two Premiere and two Shattered Past booster packs (locale 4875)",
  "Errand Lover achievement (locale 5103221)"
 ],
 "evidence": [
  {"claim": "Festival of Hearts went live in Merry Vale with the February 12, 2010 update; Cudip helps players uncover the secrets of love", "source": "http://www.freerealms.com:80/article/detail.action?articleId=967"},
  {"claim": "Festival launch in 2012: 'Merry Vale is celebrating the Festival of Hearts!' under Update of February 7, 2012", "source": "wiki: Template:News/Archive (Update of February 7, 2012)"},
  {"claim": "February 9, 2012 update lists Marketplace holiday items and fixes Festival of Hearts bugs", "source": "wiki: Template:News/Archive (Update of February 9, 2012)"},
  {"claim": "Festival is annual and held each February", "source": "wiki: Cudip; wiki: Festival of Hearts"},
  {"claim": "Cudip is found north-east of the Merry Vale warpstone during the festival; article 1053 says he appears when the festival begins", "source": "wiki: Cudip; http://www.freerealms.com:80/article/detail.action?articleId=1053"},
  {"claim": "'The Festival of Hearts has begun!' start string", "source": "locale:5518"},
  {"claim": "Daily wheel for bonus prizes", "source": "locale:400038"},
  {"claim": "Festival of Hearts Wheel is a named item", "source": "locale:400039"},
  {"claim": "Stone Heart and goons break hearts; love potion stops them", "source": "locale:427176"},
  {"claim": "TCG bundle tied to the festival and its promo cards", "source": "locale:4875"},
  {"claim": "Errand Lover achievement tied to 100 festival repeatable quests", "source": "locale:5103220, locale:5103221"}
 ],
 "confidence": 0.6,
 "open": [
  "Duration: wiki Events and Festival of Hearts pages reportedly say February through March in Merry Vale. I confirmed the wording of the annual February pattern but not the March end; treat the end date as unverified.",
  "Start 2010: article 967 text confirmed by lookup (February 12, 2010 update). The Feb 8, 2010 press-release preview is from a summary only and is not used as evidence.",
  "Start 2012: Feb 7 launch comes from the News/Archive wiki page (lookup confirmed the text). No article in the pack confirms it; the Feb 9 update is a mid-run bug-fix note.",
  "2011 run: wiki-only (Gifting Basket, Cupid, Heart Critter). No month or date is sourced, so no 2011 occurrence is listed.",
  "No dated run after 2012 is verified. Undated 'returned' articles (2016, 2500, 2501, 2498, 2499) do not give a date, so do not schedule a run from them.",
  "Unresolved variant: article 976 (French, undated, 'Le Festival des Cœurs vient de commencer') places a festival in Joyful Valley with pixies Valentin and Arianna and villain Cœur de Pierre. Lookup found no Cœur de Pierre or Joyful Valley match in articles, client or wiki, so I could not verify it. It is NOT merged here and is not in the occurrences. The pack title 'Heart Festival (Festival des Cœurs)' comes only from that article. The earlier 'Heart Festival (pack title)' alias is dropped. Article 2018/2019 (Spanish, Vegalegre) is a separate variant too.",
  "Pack merge warning: the pack may merge the Joyful Valley article 976 with this Merry Vale event under one name. This answer keeps them apart.",
  "Wiki-only items (Lovelectric Boombox, Gifting Basket, Snowheart, She-Rex, Hearts Outfit, Dove, Cupid, Heart Critter, Love Struck Piano, Stone Hearted Piano, Stone Heart's Gummy Bear, King of Broken Hearts Costume) are not listed because no explicit festival tie was re-checked. Prices and currency are null for all items; Station Cash is not sourced for any festival item here.",
  "Name-only strings (Festival of Hearts Mystery Gift locale 4418, house party locale 3545/3559, Festival of Hearts! locale 435369, Dance Party 2778, Semi-Formal 31033/6672) are not listed as items. The Semi-Formal dance and dance party are community events, not festival content.",
  "Quest titles from the wiki are not checked against the quest table; the exact titles should be verified before use.",
  "Article 2522 webcast mention is undated; no webcast occurrence recorded.",
  "The 'live' value 'yes' means the event ran on the live server in 2010 and 2012 (dated sources). The rebuild still needs a date to schedule it; wireable is false until a post-2012 run is dated."
 ]
}
```
