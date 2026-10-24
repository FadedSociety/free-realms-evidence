<!-- fleet job=event-infer id=vbig-present-v5 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[8580, 9340, 6, 3516] model=claude-haiku-5-5 -->
# Big Present

{
 "event": {
  "name": "12 Days of Presents",
  "aliases": ["Snow Days (wiki quest-event name)", "12 Days 2013 (client quest titles, locale:441125-441199)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "Dec 13 to Dec 24, 2012 (12:01 am to 11:59 pm PST); presents opened Dec 25, 2012", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"year": 2013, "when": "Year inferred from client titles '12 Days 2013 - Day 1' to 'Day 12' and wiki; exact 2013 dates not article-confirmed. Wiki gives the schedule as December 13th through the 24th.", "source": "locale:441125-441199; wiki page 12 Days of Presents (2013 section)"}
 ],
 "recurring": "Wiki page 12 Days of Presents calls it an annual event running December 13th through the 24th. Article-dated only for 2012; 2013 is client/wiki-dated.",
 "zones": ["Snowhill"],
 "npcs": ["Trina Turtledove (2013 challenge NPC: locale:441161, 441173, 441185, 441197)"],
 "quests": ["Big Present 1", "Big Present 2", "Big Present 3", "12 Days 2013 - Day 1", "12 Days 2013 - Day 12"],
 "activities": [
  "Complete one daily holiday challenge per day Dec 13-24 at Snowhill; a challenge completed on its first day gives a present with a bow (article 2827 rule; article 2813 for 2012)",
  "Open presents on December 25 (article 2813 for 2012; locale:441927 'Open on December 25th' for 2013, undated)",
  "Earn a bonus Big Present for every 4 daily presents opened (article 2813, 2012)",
  "Buy bows from the Marketplace for missed days (article 2827, undated; year not tied)"
 ],
 "items": [
  {"name": "Snowflake Glasses", "price": null, "currency": null, "source": "wiki page Snowflake Glasses (2012 Snow Days series)"},
  {"name": "Snow Days Unicorn Sweater", "price": null, "currency": null, "source": "wiki page Snow Days Unicorn Sweater (2012)"},
  {"name": "Snow Days Lot", "price": null, "currency": null, "source": "wiki page Snow Days Lot (2012, Day 11)"},
  {"name": "Snow Days Builders Pack", "price": null, "currency": null, "source": "wiki page Snow Days Builders Pack (2012)"},
  {"name": "Arctic Cat", "price": null, "currency": null, "source": "wiki page Arctic Cat (2013)"},
  {"name": "Icy Snowflake Glasses", "price": null, "currency": null, "source": "wiki page Icy Snowflake Glasses (2013)"},
  {"name": "Figgy Pudding Critter", "price": null, "currency": null, "source": "wiki page Figgy Pudding Critter (2013); client locale:5102963"}
 ],
 "rewards": [
  "Present with a bow for each daily challenge completed on its first day (article 2827; 2012 article 2813)",
  "Bonus Big Present for every 4 daily presents opened (article 2813, 2012)",
  "All 12 challenges: 12 bows and 15 presents in total (article 2813, 2012)",
  "2013 wiki-listed rewards (unverified by year-section read): Figgy Pudding Critter, Icy Snowflake Glasses, Arctic Cat, Snow Days Gift Box - Cookies, Snow Days Gift Box - Decorations, Holigoblin Mask, Snow Days Unicorn Sweater, Snow Days Builders Pack (wiki page 12 Days of Presents)"
 ],
 "evidence": [
  {"claim": "2012 event ran Dec 13-24, 2012 (PST), one daily challenge at Snowhill giving a present with a bow, presents opened Dec 25", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"claim": "Bonus Big Present per 4 daily presents; all 12 challenges give 12 bows and 15 presents", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2813"},
  {"claim": "Presents system rules (daily challenge, first-day present, Dec 25 opening, bows bought for missed days); undated, supports rules not year", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2827"},
  {"claim": "Event described as an annual event Dec 13th-24th, part of SOE's 12 Days of Holidays", "source": "wiki page 12 Days of Presents"},
  {"claim": "Big Present 1-3 quest titles (need 4, 8, 12 presents opened)", "source": "locale:441944-441949"},
  {"claim": "2013 challenge titles 12 Days 2013 - Day 1 to Day 12", "source": "locale:441125-441199"},
  {"claim": "Trina Turtledove is the 2013 challenge NPC", "source": "locale:441161, locale:441173, locale:441185, locale:441197"},
  {"claim": "Zone Snowhill", "source": "article 2813 (2012); wiki Category:Snowhill (2013 not separately checked)"}
 ],
 "confidence": 0.55,
 "open": [
  "Name collision: '12 Days of Holidays' is the separate 2011 SOE promotion (articles 2442, 2441, 2433, 2457; 13-25 Dec 2011). It needs its own entry and is NOT an alias here. Dropped from aliases.",
  "2013 occurrence has no article date; year and schedule rest on client titles and wiki. Only 2012 dates are article-confirmed.",
  "Article 2827 is undated and cannot place a year; used only for rules.",
  "2012 posting date 2012-12-13 is inferred from 'Posted 4 days, 9 hours ago' against a 2012-12-18 capture; event dates themselves come from article 2813.",
  "Big Present is the bonus-reward sub-mechanic (quests Big Present 1-3) inside this event, not a separate event. Title 'Big Present' is a component name.",
  "Big Present per-occurrence rewards from the wiki 2012 section (Day 8 Snow Days Gift Box - Cookies, Big Present St. Bernard Pet, Day 9 Snowman Mask, Day 10 5,000 Coins, Day 12 Temporary Snowflake Parachute, Big Present Polar Bear Ride) were read from a lookup excerpt; the full page read failed. Not listed as verified rewards.",
  "Bow price and currency: not sourced; null.",
  "2013 'Dec 25 open' step rests on locale:441927 only; no dated 2013 article.",
  "Excluded for no event tie: Snowglobe Helmet, Icy Snow Days Flair Shard, Winter Holiday Present (locale:132588), toys Fire Hawk / Hero Copter / Hover Ring / Blast Rover / Cyber Cycle, '12 Days of Sales' banners.",
  "Candi Ivy and Alana Yedra tied to the Gifting Tree (Category:Snow Days), not confirmed as this event's NPCs; not listed.",
  "Arctic Cat: locale:5102967 is an npc_name entry; treated as the ride item, not an NPC.",
  "Critique asked for per-year item assignment: done above, but the 2012 vs 2013 split of the wiki reward list is still unverified against full page sections.",
  "Quest titles 'Day 2', 'Day 6', 'Day 8', 'Day 10' (2013) not checked by id; 12 Days Present/Bow quest titles (locale:441513, 441525) excluded for no year tie."
 ]
}
