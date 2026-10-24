<!-- fleet job=event-infer id=vchild-s-play-charity-promotion-v3 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[7118, 8220, 6, 1908] model=claude-haiku-5-5 -->
# Child's Play 2010 charity promotion

{"event": {"name": "SOE Child's Play Charity Drive (2010)", "aliases": ["Child's Play 2010 charity promotion", "SOE Child's Play Charity Drive!", "Child's Play Charity Drive"]},
 "kind": "community",
 "live": "yes",
 "occurrences": [{"year": 2010, "when": "December 21-31 (2010)", "source": "http://www.freerealms.com/article/detail.action?articleId=1980 (window and terms; article title 'Child's Play 2010!'); wiki Tacky Sweater Penguin (2010 year)"}],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy the charity item with Station Cash; SOE donates $10 per purchase, up to $50,000 total"],
 "items": [{"name": "Tack the Penguin (Tacky Sweater Penguin)", "price": null, "currency": "station_cash", "source": "locale:6858 (charity donation text); wiki Tacky Sweater Penguin; article 1980 names the penguin pet"}],
 "rewards": ["Pet item (Tack the Penguin)"],
 "evidence": [
  {"claim": "SOE ran a Child's Play promotion where each selected in-game item bought raised $10, up to $50,000 total, from December 21 to December 31.", "source": "http://www.freerealms.com/article/detail.action?articleId=1980"},
  {"claim": "Client UI title 'SOE Child's Play Charity Drive!' names the event.", "source": "locale:827; locale:9300"},
  {"claim": "Client text says buying Tack the Penguin donates $10 per purchase, up to $50K, to Child's Play.", "source": "locale:6858"},
  {"claim": "Client pet line for Tack: 'Child's Play: I'm a playful penguin.'", "source": "locale:6857"},
  {"claim": "Client charity text describes buying Snowflake the Unicorn or other specified items; this is a separate drive's text, not the 2010 item.", "source": "locale:828; locale:2659"}
 ],
 "confidence": 0.6,
 "open": [
  "Article 1980 has no posting date in the text (only relative 'Posted 5 months, 2 weeks ago'); the year 2010 rests on its title and the wiki Tacky Sweater Penguin page, not on the quoted body.",
  "Wiki Pets list citation for Tack was not confirmed in the lookup; do not rely on it.",
  "Other Child's Play charity drives exist in the sources but are separate occurrences with their own items and windows, not confirmed as one recurring event: Ziggy the Triceratops (wiki Ziggy; article 732; Dec 17 2009 to Jan 17 2010; locale 156893, 426479) and Snowflake the Unicorn (wiki Snowflake; articles 2420, 2427; Dec 6-31 2011; locale 2659, 828). Snowflake is called a pet by the wiki and a riding mount by article 2420; type disputed. Their relative dates in the articles are unverified.",
  "Teddy Bear Parachute (locale 9299) carries the same donation text but has no year, window or wiki/article source; excluded from this occurrence.",
  "Recurrence (yearly in December) is not stated by any source; left null.",
  "No price is given in any source for Tack; price null.",
  "No zones, NPCs, quests or rewards beyond the pet are sourced for this event. Penguin Defense, Penguin Training Institute, Giant Penguin Meal and related quests are unrelated.",
  "The pack merges several Child's Play drives under one name; this record covers only the 2010 Tack drive."
 ]
}
