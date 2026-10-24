<!-- fleet job=event-infer id=vchild-s-play-winter-charity-drive-v5 status=done turns=3 usd=0.0037 tokens(read,write,in,out)=[18161, 11810, 8, 4162] model=claude-haiku-5-5 -->
# Child's Play Winter Charity Drive

```json
{
 "event": {
  "name": "SOE Child's Play Charity Drive (Winter)",
  "aliases": [
   "Child's Play Winter Charity Drive (article title, articleId 1972 / 732)",
   "SOE Child's Play Charity Drive! (client title, locale:827 and locale:9300)",
   "Child's Play charity promotion"
  ]
 },
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "Dec 17, 2009 to Jan 17, 2010 (summary-sourced)", "source": "http://www.freerealms.com/article/detail.action?articleId=732 (archived summary only; article text not re-read)"},
  {"year": 2010, "when": "Dec 21 through Dec 31 (year 2010 taken from the wiki and article summaries, not from article 1972's text)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1972 (quote 'from Dec. 21 through Dec. 31'); year per wiki Tacky Sweater Penguin and article 1981 summary (not re-read)"},
  {"year": 2011, "when": "Dec 6 to Dec 31, 2011 (wiki-only dates; the Child's Play tie is from articles 2420/2427 with no dates)", "source": "wiki page 'Snowflake' (SC Marketplace, Dec 6 to Dec 31, 2011); wiki 'Pets' ('sales benefited Child's Play in 2011'); http://www.freerealms.com/article/detail.action?articleId=2420 (summary: players buy Child's Play items during December)"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": ["Ziggy (pet NPC; locale:426479 'Ziggy Pet'; dialog locale:426322 reads 'Iggy')", "Tack (pet NPC; locale:6857 'Child's Play: I'm a playful penguin')"],
 "quests": [],
 "activities": [
  "Buy a select Child's Play item with Station Cash in the in-game Marketplace; SOE donates $10 per purchase, up to $50,000 total (locale:6858, locale:156893, locale:2659)"
 ],
 "items": [
  {"name": "Ziggy the Triceratops (Child's Play Triceratops)", "price": "500", "currency": "station_cash", "source": "http://www.freerealms.com/article/detail.action?articleId=732 (summary: 'for 500 Station Cash each'); locale:156893 and locale:426479 tie Ziggy to Child's Play. Wiki 'Ziggy' price field is blank, so it does not confirm 500."},
  {"name": "Tack the Penguin", "price": null, "currency": null, "source": "locale:6858 ('Buy Tack the Penguin ... $10 ... up to $$50K to Child's Play'); article 1981 summary (not re-read). No source in the pack gives Tack's price."},
  {"name": "Snowflake the Unicorn", "price": "500 (poster text only; currency not stated)", "currency": null, "source": "wiki image Snowflake.jpg ('SOE Child's Play Charity Drive!' ... '500' ... 'Available now through December 31st'); locale:2659; article 2420 (featured Child's Play item); article 2427; wiki 'Snowflake' (SC Marketplace, Dec 6 to 31, 2011)"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Promotion: SOE donates $10 per qualifying in-game purchase, capped at $50,000 total", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1972; http://www.freerealms.com/article/detail.action?articleId=732; locale:6858; locale:2659"},
  {"claim": "Client title for the event is 'SOE Child's Play Charity Drive!'", "source": "locale:827 and locale:9300 (confirmed in this pass)"},
  {"claim": "2010 window was Dec 21 through Dec 31 for select in-game items bought with Station Cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1972 (quote 'from Dec. 21 through Dec. 31')"},
  {"claim": "2009 drive sold Child's Play Triceratops for 500 Station Cash, Dec 17, 2009 to Jan 17, 2010", "source": "http://www.freerealms.com/article/detail.action?articleId=732 (summary only)"},
  {"claim": "Ziggy is tied to the Child's Play donation (donation string)", "source": "locale:156893; locale:426479"},
  {"claim": "Snowflake was the featured Child's Play item in December 2011; sold Dec 6 to Dec 31, 2011", "source": "wiki 'Snowflake'; http://www.freerealms.com/article/detail.action?articleId=2420 (no date in text); http://www.freerealms.com/article/detail.action?articleId=2427"},
  {"claim": "Recurrence is NOT stated by any source. Three December windows (2009, 2010, 2011) suggest a yearly pattern, but this is an inference only.", "source": "the occurrences above; no article says the drive recurs"}
 ],
 "confidence": 0.55,
 "open": [
  "Recurrence: no source says this drive recurs. The three December occurrences are grouped by the pack under one name, but the sources do not show they are one promotion. Treat as three separate occurrences until confirmed. Each year's window and items are separate.",
  "2009 window and 500 price come from the article 732 summary only. Re-read the article text before scheduling.",
  "2010 year is not in article 1972's text; it comes from wiki and article summaries (1981, 1980), which were not re-read. Tack the Penguin's identity with the wiki 'Tacky Sweater Penguin' is not stated by one source.",
  "Tack the Penguin price is unknown in the pack. The earlier value of 500 (from the wiki 'Tacky Sweater Penguin') was not verified here, so it is left null.",
  "Snowflake price 500 comes from poster text only; currency is not stated on the poster. Treat currency as unknown and keep Snowflake out of scheduled activity until confirmed.",
  "Teddy Bear Parachute (locale:9299) is removed from items. Its only tie is a donation string saying 'buy it and SOE donates $10 per purchase up to $50K to Child's Play'; no year, window or price. It is an unplaced candidate for this drive family.",
  "The Snowflake 2011 alias 'Child's Play Snowflake drive (2011)' was removed; it is a different pet and year. 2011 is kept as an occurrence of the same charity program only because of the wiki's 'benefited Child's Play in 2011' note, and this link is not confirmed by an article with dates.",
  "The 2011 Snowflake poster says 'Available now through December 31st' but has no year; the year 2011 comes from the wiki page only.",
  "Client quirk: locale:426322 reads 'Iggy' where the NPC name is Ziggy.",
  "No zones, quests or quest answers tie to this event in the pack. wiki_category_members is empty, so no category sweep was confirmed."
 ]
}
```
