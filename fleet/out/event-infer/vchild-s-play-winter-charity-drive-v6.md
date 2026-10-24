<!-- fleet job=event-infer id=vchild-s-play-winter-charity-drive-v6 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[17862, 9643, 8, 2529] model=claude-haiku-5-5 -->
# Child's Play Winter Charity Drive

{
 "event": {
  "name": "SOE Child's Play Charity Drive (Winter)",
  "aliases": ["SOE Child's Play Charity Drive! (client title, locale:827 and locale:9300)", "Child's Play Winter Charity Drive (article title, articleId 1972 / 732)", "Child's Play charity promotion"]
 },
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "Dec 21 through Dec 31, 2010 (penguin pet, Station Cash)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1972 (quote 'from Dec. 21 through Dec. 31'); http://www.freerealms.com/article/detail.action?articleId=1980 (summary states SOE's 2010 Child's Play promotion, Dec 21 to Dec 31)"},
  {"year": 2009, "when": "Dec 17, 2009 to Jan 17, 2010 (winter 2009 drive; summary-sourced)", "source": "http://www.freerealms.com/article/detail.action?articleId=732 (summary only; article text not re-read)"},
  {"year": 2011, "when": "Dec 6 to Dec 31, 2011 (wiki-only; unconfirmed as the same promotion)", "source": "wiki page 'Snowflake'; wiki 'Pets' note; http://www.freerealms.com/article/detail.action?articleId=2420 (no dates in summary)"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": ["Ziggy (pet; client locale:426479 'Ziggy Pet')", "Tack (pet; locale:6857 'Child's Play: I'm a playful penguin')"],
 "quests": [],
 "activities": ["Buy a select Child's Play item with Station Cash in the in-game Marketplace; SOE donates $10 per purchase, up to $50,000 total (locale:6858, locale:2659)"],
 "items": [
  {"name": "Ziggy the Triceratops (Child's Play Triceratops)", "price": "500", "currency": "station_cash", "source": "http://www.freerealms.com/article/detail.action?articleId=732 (summary: '500 Station Cash each'; 2009 drive, summary-only)"},
  {"name": "Tack the Penguin (2010 penguin pet)", "price": null, "currency": null, "source": "locale:6858; http://www.freerealms.com:80/article/detail.action?articleId=1972. No source in the pack gives the price."},
  {"name": "Snowflake the Unicorn (2011)", "price": null, "currency": null, "source": "wiki 'Snowflake' (SC Marketplace, Dec 6 to 31, 2011); poster text reads 500 with no currency, so price is unverified"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Promotion: SOE donates $10 per qualifying Station Cash Marketplace purchase, capped at $50,000 total", "source": "http://www.freerealms.com/article/detail.action?articleId=732; http://www.freerealms.com:80/article/detail.action?articleId=1972"},
  {"claim": "2010 window Dec 21 to Dec 31 with a penguin pet bought by Station Cash; year 2010 stated in the article 1980 summary", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1972; http://www.freerealms.com/article/detail.action?articleId=1980"},
  {"claim": "2009 drive sold a Child's Play Triceratops for 500 Station Cash, Dec 17 2009 to Jan 17 2010 (summary only)", "source": "http://www.freerealms.com/article/detail.action?articleId=732"},
  {"claim": "Client title 'SOE Child's Play Charity Drive!'", "source": "locale:827; locale:9300"},
  {"claim": "Ziggy is tied to the Child's Play donation string", "source": "locale:156893; locale:426479"}
 ],
 "confidence": 0.5,
 "open": [
  "Recurrence is not stated by any source. The three December occurrences (2009, 2010, 2011) are listed separately; the cross-year grouping under one name is unconfirmed. Do not schedule as a yearly rule.",
  "2009 window and 500 SC price rest on the article 732 summary only. Re-read article 732 text before scheduling.",
  "2011 Snowflake occurrence is wiki-only (Dec 6 to 31, 2011) and no article ties it to the $10-per-purchase promotion. Not counted as a confirmed occurrence.",
  "Snowflake price 500 comes from poster text with no currency; treated as unverified. Keep out of scheduled activity until confirmed.",
  "Tack the Penguin price is unknown. The earlier 500 value from the wiki 'Tacky Sweater Penguin' is not verified.",
  "Teddy Bear Parachute (locale:9299) removed from items: its only tie is a donation string with no year, window or price.",
  "Alias 'Child's Play Snowflake drive (2011)' removed: different pet and year.",
  "Client title 'SOE Child's Play Charity Drive!' ties to locale:827 headline text that names Snowflake, so it fits the 2011 drive best; it is not proven to cover 2009 or 2010.",
  "Client quirk: locale:426322 reads 'Iggy' where the NPC is Ziggy.",
  "No zones, quests or quest answers tie to this event; wiki category sweep was empty."
 ]
}
