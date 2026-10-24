<!-- fleet job=event-infer id=vbig-present-v4 status=done turns=2 usd=0.0035 tokens(read,write,in,out)=[8639, 9680, 6, 4333] model=claude-haiku-5-5 -->
# Big Present

```json
{
 "event": {
  "name": "12 Days of Presents",
  "aliases": ["Snow Days (wiki quest-event name)", "12 Days of Presents 2012 / 2013 (in-game)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "Dec 13 to Dec 24, 2012 (12:01 am to 11:59 pm PST); presents opened Dec 25", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813 (dates in body; posting date 2012-12-13 inferred from 'Posted 4 days, 9 hours ago')"},
  {"year": 2013, "when": "Dec 13 to Dec 24 (year and dates from client and wiki only; no article dates this occurrence)", "source": "locale:441125-441199 (12 Days 2013 - Day 1 to Day 12 titles); wiki page 12 Days of Presents (2013 section); wiki page Figgy Pudding Critter"}
 ],
 "recurring": "Annual in December (Dec 13-24, presents Dec 25). Basis: wiki page Snow Days / Figgy Pudding Critter call it an annual Snow Days quest event, and two occurrences (2012 article-dated, 2013 client/wiki-dated). Article-sourced only for 2012.",
 "zones": ["Snowhill"],
 "npcs": ["Trina Turtledove"],
 "quests": ["Big Present 1", "Big Present 2", "Big Present 3"],
 "activities": [
  "Complete one daily holiday challenge per day Dec 13-24 at Snowhill; each challenge completed on its first day gives a present with a bow",
  "Open presents on December 25",
  "Earn a bonus Big Present for every 4 daily presents opened",
  "Buy bows from the Marketplace for missed days (article 2827)"
 ],
 "items": [
  {"name": "Snowflake Glasses", "price": null, "currency": null, "source": "wiki page Snowflake Glasses (12 Days of Presents 2012 Snow Days quest series)"},
  {"name": "Snow Days Unicorn Sweater", "price": null, "currency": null, "source": "wiki page Snow Days Unicorn Sweater; wiki page 12 Days of Presents (2012 section)"},
  {"name": "Snow Days Lot", "price": null, "currency": null, "source": "wiki page Snow Days Lot; wiki page 12 Days of Presents (2012 section, Day 11)"},
  {"name": "Snow Days Builders Pack", "price": null, "currency": null, "source": "wiki page Snow Days Builders Pack; wiki page 12 Days of Presents (2012 section)"},
  {"name": "Arctic Cat", "price": null, "currency": null, "source": "wiki page Arctic Cat (acquired as part of the 12 Days of Presents 2013, an annual Snow Days quest event)"},
  {"name": "Icy Snowflake Glasses", "price": null, "currency": null, "source": "wiki page Icy Snowflake Glasses (12 Days of Presents 2013, an annual Snow Days quest event)"},
  {"name": "Figgy Pudding Critter", "price": null, "currency": null, "source": "wiki page Figgy Pudding Critter ('acquired as a part of the 12 Days of Presents 2013, an annual Snow Days quest event'); wiki page Pet Pals; client locale:5102963"}
 ],
 "rewards": [
  "Present with a bow for each daily challenge completed on its first day",
  "Bonus Big Present for every 4 daily presents opened",
  "Completing all 12 challenges: 12 bows and 15 presents in total (article 2813)",
  "2013 wiki-listed rewards: Figgy Pudding Critter, Icy Snowflake Glasses, Arctic Cat, Snow Days Gift Box - Cookies, Snow Days Gift Box - Decorations, Holigoblin Mask, Snow Days Unicorn Sweater, Snow Days Builders Pack (wiki page 12 Days of Presents, 2013 section)"
 ],
 "evidence": [
  {"claim": "Presents system: one daily challenge per day Dec 13-24, a present per challenge completed on its first day, presents opened Dec 25, bonus Big Presents, bows bought for missed days", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2827 (undated; supports rules, not year)"},
  {"claim": "2012 dates: 12 Days of Holidays event ran Dec 13, 2012 12:01 am PST through Dec 24, 2012 11:59 pm PST; daily challenge at Snowhill awards a present with a bow; present opening on Dec 25", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"claim": "A bonus Big Present per 4 daily presents opened; all 12 challenges give 12 bows and 15 presents", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"claim": "Big Present 1-3 quest titles; need 4, 8, 12 presents opened", "source": "locale:441944-441949"},
  {"claim": "In-game label 'Open on December 25th'", "source": "locale:441927"},
  {"claim": "2013 challenges titled 12 Days 2013 - Day 1 through Day 12", "source": "locale:441125-441199"},
  {"claim": "Trina Turtledove is the 2013 challenge NPC (objective 'Return to Trina Turtledove')", "source": "locale:441161, locale:441173, locale:441185, locale:441197"},
  {"claim": "Figgy Pudding Critter, Arctic Cat, Icy Snowflake Glasses are 2013 items; Snowflake Glasses and Snow Days Unicorn Sweater/Lot/Builders Pack are 2012 items", "source": "wiki pages Figgy Pudding Critter, Arctic Cat, Icy Snowflake Glasses, Snowflake Glasses, Snow Days Unicorn Sweater, Snow Days Lot, Snow Days Builders Pack"},
  {"claim": "Zone is Snowhill", "source": "article 2813 (2012); wiki category Category:Snowhill on Snow Days page (2013 not separately checked)"}
 ],
 "confidence": 0.6,
 "open": [
  "Name collision: '12 Days of Holidays' is also the 2011 SOE 12 Days of Holidays promotion (articles 2442, 2441, 2433, 2457; 13 Dec-25 Dec 2011). That promo is a separate event and needs its own entry. It is NOT an alias here; the only use of that name on this entry is the 2012 article 2813 body wording.",
  "2013 occurrence has no article date. Year and dates rest on client names and wiki pages only.",
  "Article 2827 is undated and cannot place a year. Do not use it as a dated source.",
  "2012 posting date 2012-12-13 is inferred from 'Posted 4 days, 9 hours ago' against a 2012-12-18 capture; the event dates themselves are stated in article 2813.",
  "Big Present rewards (wiki 2012 section: Day 8 Snow Days Gift Box - Cookies, Big Present St. Bernard Pet, Day 9 Snowman Mask, Day 10 5,000 Coins, Day 12 Temporary Snowflake Parachute, Big Present Polar Bear Ride) were read from a lookup excerpt; the 2012 section boundary was not verified against the full page (the full-page read failed). Not listed as rewards per occurrence.",
  "Bow price and currency: not sourced. Left null.",
  "Quest titles 'Day 2', 'Day 6', 'Day 8', 'Day 10' (2013) not checked by id; the 12 Days Present/Bow quest titles (locale:441513, 441525) have no year tie and are excluded.",
  "Excluded for no event tie: Snowglobe Helmet, Icy Snow Days Flair Shard, Winter Holiday Present (locale:132588), toys Fire Hawk / Hero Copter / Hover Ring / Blast Rover / Cyber Cycle (also on United We Stand achievement page), '12 Days of Sales' video banners.",
  "NPC conflict: Candi Ivy and Alana Yedra are tied to the Gifting Tree (Category:Snow Days), not confirmed as this event's NPCs. Not listed.",
  "Arctic Cat: locale:5102967 is an npc_name entry; treated as the ride item, not an NPC.",
  "Dec 25 'open' step rests on locale:441927 and the undated article 2827 only; no dated article confirms it for 2013."
 ]
}
```
