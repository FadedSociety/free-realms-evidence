<!-- fleet job=event-infer id=vholiday-celebrations-v4 status=done turns=3 usd=0.0053 tokens(read,write,in,out)=[22497, 16925, 8, 5836] model=claude-haiku-5-5 -->
# Annual holiday celebrations

```json
{
 "event": {
  "name": "Snow Days",
  "aliases": ["Snow Days Are Here Again!", "Snow Days Return", "Snowhill Snow Days", "Seasonal: Snow Days (client quest title locale:4419465)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "Dec 18, 2009 to Jan 3, 2010 (daily community events and TCG tournaments)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
  {"year": 2010, "when": "Early Dec 2010 season; Snow Days party in Wintery Basin fishing area: Dec 9 2010 (US/Latin America) and Dec 10 2010 (UK/Europe), Server 1", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1953 (party times; posting date not shown, captured 2010-12-14); http://www.freerealms.com:80/article/detail.action?articleId=1950 (Snow Days Return post, captured 2010-12-19, relative date only)"},
  {"year": 2011, "when": "Dec 2011 (webcast recap says Snow Days is HERE; the article gives no month, so Dec 2011 comes from the pack's note and is not checked against the article)", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"}
 ],
 "recurring": "Yearly in December into early January. Dec-start runs are confirmed for 2009-10 and 2010, and article 892 says it 'is over until next year' (Jan 26, 2010 patch notes).",
 "zones": ["Snowhill", "Wintery Basin fishing area (above Snowhill)"],
 "npcs": ["Candi Ivy", "Abominable Snowman", "Everett (coal request, per article 1950)"],
 "quests": ["Snow Days Are Here Again!", "Seasonal: Snow Days"],
 "activities": [
  "Ask Candi Ivy daily for a present from under the Gifting Tree (article 828)",
  "Spin the Snow Days prize wheel (article 828; locale 426650 'Snow Days Wheel')",
  "Daily Snow Days quests for Snowhill residents including the Mayor (article 828)",
  "Defend the Gifting Tree from the Abominable Snowman and snowmen by pelting them with snowballs (article 1950 / facts)",
  "Fight Robgoblins for Snow Days clothing (articles 2429, 1950)",
  "Attend the Wintery Basin Snow Days community party (article 1953)",
  "Daily community events and TCG tournaments (article 705)"
 ],
 "items": [
  {"name": "Snow Days outfits", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=828 (sold in Marketplace for a limited time; 'won't reappear until the next Snow Days...if at all'); http://www.freerealms.com/article/detail.action?articleId=1957 (catalog or quests/gifts)"},
  {"name": "Snow Days Present", "price": null, "currency": "reward", "source": "locale:1729"},
  {"name": "Snow Days Wheel", "price": null, "currency": null, "source": "locale:426650 (place name; prize wheel)"},
  {"name": "Snow Days Lot", "price": null, "currency": null, "source": "wiki: Snow Days Lot; locale:441205"},
  {"name": "Snow Days Builders Pack", "price": null, "currency": null, "source": "wiki: Snow Days Builders Pack; locale:441209"},
  {"name": "Snow Days Unicorn Sweater", "price": null, "currency": null, "source": "wiki: Snow Days Unicorn Sweater; locale:441217"}
 ],
 "rewards": ["Snow Days clothing and outfits", "Gifting Tree presents", "Snow Days prize wheel prizes", "Snow Days housing and lot items (locale 441205 etc.)"],
 "evidence": [
  {"claim": "Snow Days ran daily community events and TCG tournaments Dec 18, 2009 to Jan 3, 2010", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
  {"claim": "Snow Days ended and would return the next year ('Snow Days is over until next year'), in Jan 2010 patch notes", "source": "http://www.freerealms.com:80/article/detail.action?articleId=892"},
  {"claim": "The Snow Days season party in Wintery Basin was held Dec 9 2010 (US/LatAm) and Dec 10 2010 (UK/EU) on Server 1, described as the first party of the season", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1953"},
  {"claim": "A Snow Days return post (Snowhill, Gifting Tree, Abominable Snowman, Robgoblins, outfits) appeared around early Dec 2010", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1950"},
  {"claim": "Snow Days is HERE in 2011 at the time of the webcast", "source": "http://www.freerealms.com/article/detail.action?articleId=2428"},
  {"claim": "Candi Ivy gives a daily present from under the Gifting Tree during Snow Days; the Mayor and Snowhill residents had daily Snow Days quests; the prize wheel was spun", "source": "http://www.freerealms.com:80/article/detail.action?articleId=828"},
  {"claim": "Snow Days outfits were sold in the Marketplace for a limited time and their return is unconfirmed ('if at all')", "source": "http://www.freerealms.com:80/article/detail.action?articleId=828"},
  {"claim": "Snow Days is a seasonal event in which Snowhill is decorated and presents are found under the Gifting Tree", "source": "http://www.freerealms.com/article/detail.action?articleId=2429"},
  {"claim": "The Abominable Snowman towers over players around the quest givers in Snowhill during Snow Days", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2815"},
  {"claim": "Client names the event: 'Snow Days!' and quest title 'Snow Days' and 'Seasonal: Snow Days'", "source": "locale:5103008; locale:5102485; locale:4419465"},
  {"claim": "The 2011 anniversary post lists annual holiday events among the year's updates, with no dates or event named", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2109"}
 ],
 "confidence": 0.7,
 "open": [
  "Umbrella: the pack name 'Annual holiday celebrations' covers several events. This answer covers only Snow Days. Super Spooktacular Halloween (article 1854), Fall Harvest/Thanksgiving (wiki Raw Turkey, Nov 2012-2013), Black Friday 2013 (wiki Geek Outfit bundle) and a Fourth of July holiday (TenTonHammer node/86237) need their own packs.",
  "Merge risk: the SOE '12 Days of Holidays' promotion (articles 2813, 2827, 2457, 2441, 2442, 2433, 2455; 13-24 Dec 2011 and 2012) is a different event. The wiki quest series '12 Days of Presents' sits inside Snow Days in 2012 (wiki only). Neither is an alias here.",
  "2012 run: wiki-only (Snow Days Lot, Unicorn Sweater, Icy Snow Days Flair Shard, Snow Days Builders Pack, 12 Days of Presents). No article confirms it. The wiki News archive has '[Snow Days] has ended' near the Jan 12, 2012 update, so the 2012 run ended by about early Jan 2012.",
  "2013: client/wiki update 122.1 (12/04/2013) lists Snow Days items, so a 2013 run is possible but not confirmed.",
  "2011 month: the article 2428 text gives no month. The Dec 2011 date comes from the pack note and needs checking against the article.",
  "Quest 'Snowhill Snow Days Are Here Again!' and client quest 'Snowhill Snow Days Are Back!' (locale 1653/1654, from an earlier critique): the locale lookup did not return 'Snowhill Snow Days Are Back', so it is unverified and not listed. 'Snow Days Are Here Again!' is a quest title in articles/quests.json; its source article was not traced.",
  "Station Cash: articles/facts.json says Snow Days items were bought with Station Cash from the Catalog, but no article URL is attached in the pack. Prices are left null until the source is found.",
  "Winter Holiday World Event (locale:424485) and Winter Holiday Wheel! (ui locale:4239) are not tied to Snow Days. 'Winter Holiday(s)' is not an alias. Locale 426649 ('Spin the special Snow Days wheel every day') may tie the wheel to Snow Days.",
  "Snowhill Lodge housing release (locale 829/830, 'Snow Days Housing Update!') is not confirmed as part of the event.",
  "Prize-wheel items (Candy Cane Hammer, Candy Striped Axe, Barber Pole Bow, Candy Stick Sword, Cinnamon Saw, Red Ryder Rod) are wiki-only and not re-checked. Santa Claus Outfit and Snow Days Gift Box are in the wiki category but not tied by a source.",
  "Mayor of Snow Hill's name is not in the sources. Zone spelling 'Snow Hill' (article 828) vs 'Snowhill' (most articles and client) is unresolved.",
  "Wireable: a month window (Dec to early Jan) is supported by the 2009-10 and 2010 starts. The exact daily window is not stated in any source for 2010 or 2011, so a calendar should use the 2009-10 window (Dec 18 to Jan 3) as the only exact one."
 ]
}
```
