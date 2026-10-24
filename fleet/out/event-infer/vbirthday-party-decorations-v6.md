<!-- fleet job=event-infer id=vbirthday-party-decorations-v6 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[17364, 10073, 8, 4030] model=claude-haiku-5-5 -->
# Birthday party decorations

```json
{
 "event": {
  "name": "Free Realms Anniversary Birthday Party",
  "aliases": ["Birthday Party (2010 article title)", "Birthday Bash (2012 article title, locale:695)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Posted for the first anniversary (April 29, 2010) and running until May 10, 2010. Start: posting day per the French article; the German article (1268) says 'launch-day kickoff'. These two starts conflict; the end date agrees.", "source": "http://www.freerealms.com/article/detail.action?articleId=1267 (French; anniversary April 29, 2010; party from posting day until May 10, 2010); http://www.freerealms.com:80/article/detail.action?articleId=1268 (German; until May 10, 2010)"},
  {"year": 2011, "when": "Second anniversary, April 28, 2011 (article's stated anniversary date); party runs from the post date until May 18, 2011. The article says 'second anniversary', so the year is inferred from that, not from a dated line.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 (German; summary read this run)"},
  {"year": 2012, "when": "Third-anniversary Birthday Bash; ran through May 24, 2012. Start date not sourced.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580; locale:695"}
 ],
 "recurring": "Yearly, tied to the game's anniversary, running from late April into May. Observed in 2010, 2011 and 2012 (three sourced occurrences). A 2013 post (articleId 2924) was not checked as live and is not counted.",
 "zones": [
  "Sanctuary (hub; Camellia and Queen Valerian; articleIds 2106, 2100, 2580)",
  "Merry Vale, Seaside, Snowhill, Shrouded Glade, Wugachug, Blackspore, Briarwood (party areas; articleId 1261, year not stated in the summary)"
 ],
 "npcs": [
  "Camellia (starts the birthday party quests, near the great tree in Sanctuary; articleIds 2106, 2100, 1261; locale:707)",
  "Queen Valerian (cake bake-off storyline in Sanctuary, 2012; articleId 2580)",
  "Cakenstein (cake monster that eats the birthday cake; articleIds 1268, 2580; locale:4918, 4949)",
  "Kuchenstein (German name of the boss with cakelings, 2011; articleId 2099)"
 ],
 "quests": [],
 "activities": [
  "Start birthday party quests from Camellia in Sanctuary (articleIds 2106, 2100)",
  "Help with party preparation and the cake bake-off for Queen Valerian in Sanctuary (2012; articleId 2580)",
  "Fight Cakenstein / Kuchenstein and the cakelings that eat the birthday cake (articleIds 1268, 2099, 2580)",
  "Visit party areas in the zones listed above (articleIds 1267, 1261)"
 ],
 "items": [
  {"name": "Birthday Bash Furniture Bundle", "price": "1350 Station Cash (saves 250)", "currency": "station_cash", "source": "locale:691 (name), locale:692 (price). Year not sourced; ties to the event by name only."},
  {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "locale:694. Year not sourced."}
 ],
 "rewards": ["Birthday Cake Hat (locale:694; year not sourced)"],
 "evidence": [
  {"claim": "2010: anniversary April 29, 2010; party held from the announcement until May 10, 2010, with party areas in eight zones.", "source": "http://www.freerealms.com/article/detail.action?articleId=1267"},
  {"claim": "2010: German post, party from launch-day kickoff until May 10, 2010.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1268"},
  {"claim": "2011: second anniversary, April 28; party runs from the post date until May 18, 2011, with a boss Kuchenstein and cakelings.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099"},
  {"claim": "2012: third-anniversary Birthday Bash ran through May 24, 2012; Queen Valerian cake bake-off storyline; Cakenstein; daily party-prep quests.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580; locale:695"},
  {"claim": "Camellia in Sanctuary near the great tree starts the birthday party quests.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106; http://www.freerealms.com/article/detail.action?articleId=2100"},
  {"claim": "Birthday Bash Furniture Bundle costs 1350 Station Cash, saving 250.", "source": "locale:691; locale:692"},
  {"claim": "Pre-launch preview (2010-04-02) said decorations would appear from mid-April. This is a plan, not a live event, so it is not an occurrence or alias.", "source": "http://www.tentonhammer.com:80/node/83041"}
 ],
 "confidence": 0.6,
 "open": [
  "Pack title 'Birthday party decorations' is the 2010 pre-launch preview (tentonhammer 83041), kept separate from the live event. Pack may merge 2010 and 2012 content.",
  "2010 start conflicts: articleId 1267 says posting day; articleId 1268 says launch-day kickoff; the preview says April 28 decorations. Exact start is unresolved; end is May 10, 2010.",
  "2011 year rests on the 'second anniversary' wording in articleId 2099, not a dated line. 2011 zones and quests not verified.",
  "2012 start date unsourced; only the May 24, 2012 end is known.",
  "Zone list is from articleId 1261, which has no date in the summary. Its names (Merry Vale, Seaside, etc.) differ from the German zone names in 1268 and 2099; not reconciled. Which year the list applies to is unknown.",
  "No quest titles are confirmed. 'Birthday Cake Bake-off', 'A Piece of Cake', 'Undelivered Confections', 'Cakey Madness', 'Bundles of Balloons' and 'Downing Cakenstein' come from wiki or inference without year; unverified. 'Cakenstein Attacks!' (locale:4917) is a client title not yet checked for year.",
  "Birthday Bash Furniture Bundle, Birthday Party Crate, Birthday Cake Hat, Wall Sconce, Wugachug Birthday T-Shirt and balloon weapons have no year tie; not attached to occurrences.",
  "Four pinata pets (articleId 2580, per prior run's summary) not re-read this run; left out.",
  "2013 (articleId 2924) and 2014 not checked as live; not counted.",
  "Earlier citations to articleId 2107 for 2011 and to 1267 for the launch-day start were wrong and are withdrawn. Glerga (articleId 1282) is not tied to this event."
 ]
}
```
