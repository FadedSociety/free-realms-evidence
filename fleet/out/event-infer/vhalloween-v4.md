<!-- fleet job=event-infer id=vhalloween-v4 status=done turns=2 usd=0.0035 tokens(read,write,in,out)=[8223, 10880, 6, 4093] model=claude-haiku-5-5 -->
# Halloween

```json
{
 "event": {
  "name": "Super Spooktacular",
  "aliases": ["Spooktacular", "Halloween Spooktacular (2011 article title, alias unconfirmed)", "Halloween (2009 costume promo, articleId=457; alias unconfirmed)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2009, "when": "Oct 14 through Nov 11, 2009 (SCHEDULE ONLY: pre-launch, not confirmed as run)", "source": "http://www.tentonhammer.com:80/node/75739"},
  {"year": 2010, "when": "October (year-level; 'October is Super Spooktacular month', community events every Thursday afternoon and Friday morning)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1845"},
  {"year": 2011, "when": "Oct 13 through Nov 23, 2011 (article names it 'Halloween Spooktacular'; alias to be confirmed)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"},
  {"year": 2013, "when": "Oct 1 through Nov 12, 2013 (fourth annual). Conflict: wiki video page says Nov 15", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2949"}
 ],
 "recurring": "yearly in October into November (2009, 2010, 2011, 2013 occurrences; articles 1854, 1860, 1861 call 2010 the second annual and 2949 calls 2013 the fourth annual)",
 "zones": ["Sanctuary", "Pixiewood"],
 "npcs": [],
 "quests": ["Candy Gram", "Halloween Fanatic"],
 "activities": [
  "Wear seasonal costumes (e.g. Werewolf Tail and Vampire Fangs, which cannot be worn together)",
  "Complete spooky quests and festive live events",
  "Trick or Treat party in Sanctuary (celebrated 2nd anniversary of the edition)",
  "Buy seasonal decorations for the house"
 ],
 "items": [
  {"name": "Super Spooktacular Parachute", "price": "899", "currency": "station_cash", "source": "video:1TNyzyI62nc/00122.jpg (frame-read price, unverified in text); locale:5102560 (name only)"},
  {"name": "Super Spooktacular 2009 Member Pack", "price": null, "currency": null, "source": "locale:156839; locale:156830"},
  {"name": "Chatty Costume", "price": null, "currency": null, "source": "wiki Chatty Costume (category Super Spooktacular)"},
  {"name": "Necrowart Wrist Wraps", "price": null, "currency": "station_cash", "source": "wiki Necrowart Wrist Wraps (SC Marketplace during Super Spooktacular; price blank)"},
  {"name": "Candy Corn", "price": null, "currency": "coins", "source": "wiki Candy Corn (pet pal, Coin Shop, Members only; price blank in wiki; currency inferred from Coin Shop, unverified)"},
  {"name": "Super Spooktacular decoration", "price": null, "currency": null, "source": "locale:91963"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Free Realms held Super Spooktacular as its first Halloween event, scheduled Oct 14 to Nov 11, 2009 (pre-launch schedule).", "source": "http://www.tentonhammer.com:80/node/75739"},
  {"claim": "Post 'Free Realms Super Spooktacular 09' dated Oct 19, 2009 exists; body not captured, so it does not confirm the 2009 run.", "source": "http://www.tentonhammer.com:80/node/75724"},
  {"claim": "October 2010 was Super Spooktacular month, with community events every Thursday afternoon and Friday morning.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1845"},
  {"claim": "2010 was the second annual Super Spooktacular, returning with the previous year's content plus more.", "source": "http://www.freerealms.com/article/detail.action?articleId=1860; http://www.freerealms.com/article/detail.action?articleId=1861; http://www.freerealms.com:80/article/detail.action?articleId=1854"},
  {"claim": "Werewolf Tail and Vampire Fangs are Super Spooktacular costume items that cannot be worn together.", "source": "http://www.freerealms.com/article/detail.action?articleId=1860"},
  {"claim": "Halloween Spooktacular ran Oct 13 to Nov 23, 2011.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"},
  {"claim": "An October 2011 webcast discussed the Spooktacular event.", "source": "http://www.freerealms.com/article/detail.action?articleId=2301"},
  {"claim": "Super Spooktacular 2013 was the fourth annual, running Oct 1 through Nov 12, 2013.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2949"},
  {"claim": "Super Spooktacular is the event name in the client and wiki (Category:Super Spooktacular, Category:Holiday, Category:Events).", "source": "wiki Category:Super Spooktacular; locale:436400"},
  {"claim": "Candy Gram and Halloween Fanatic are quest titles in the client.", "source": "locale:415311 (Candy Gram); locale:416806 is dialog only, not a title, so Halloween Fanatic title is not confirmed by it"},
  {"claim": "Chatty Costume, Necrowart Wrist Wraps and Candy Corn are tagged to the event in the wiki.", "source": "wiki Chatty Costume; wiki Necrowart Wrist Wraps; wiki Candy Corn"},
  {"claim": "Super Spooktacular 2009 Member Pack exists and was available only during Super Spooktacular 2009.", "source": "locale:156839; locale:156830"}
 ],
 "confidence": 0.55,
 "open": [
  "Alias merge NOT confirmed. Articles 1845, 1854, 1860, 1861, 1870, 1876, 2949 and tentonhammer 75724/75739 use 'Super Spooktacular'. Article 2304 (2011) says 'Halloween Spooktacular'. Article 457 ('Halloween Around the Corner!', Oct 2009 Halloween costume promo, Wolfman costume, promises content 'between now and the 31st') never uses the Spooktacular name. Treat 457 and 2304 as aliases only pending Bryce's confirmation.",
  "Date conflict: article 457 says Halloween content runs to Oct 31, 2009; tentonhammer 75739 says Super Spooktacular scheduled Oct 14 to Nov 11, 2009. Unresolved; the 2009 window is schedule-only.",
  "2009 live run not confirmed: only the schedule (75739) and an uncaptured post (75724) exist.",
  "2010 has month only (no day range).",
  "2013 end date conflict: article 2949 says Nov 12; wiki video page says Nov 15. Nov 12 used.",
  "Quests Bag Snatchers, A Formal Report, Delicious Goo'd Candy and Trick-or-Treat come only from the pack's quest-answer list or dialog; not verified as client titles. Not listed as quests. The wiki page 'Halloween Harry' (cited in an earlier critique as the event tie) was not verified in this pass; the Halloween Harry NPC (locale:415047) is therefore not listed in npcs.",
  "Halloween Fanatic: client title not confirmed (locale:416806 is dialog only). Kept in quests on the pack's answer list; verify.",
  "Rewards left empty. Halloween Fanatic reward 'Chatty Suit' (wiki Chatty Suit, per a critique) was not checked here; the wiki page is 'Chatty Costume' and the naming difference is unresolved. TCG-listed rewards (Jack O' Lantern costume, Scary Transistor, Chiller Boombox; articles 476 and 1857) have no verified tie to this event.",
  "Only the Parachute has a price (899 Station Cash, frame-read from video, not in text). Other items have no price in sources.",
  "Excluded for lack of event tie: Halloween Haunting, A Dark Future, The Great Scare, Greyli, Flaming Skull Wobblehead, Halloween Cart, Halloween Chicken Suit, Blackspore Ghostly Pet Party. Pumpkin Patch flooring/wallpaper (locales 8866/8868/8870/8872) left out: the housing article ties are 2306/2309 and are not verified for this event.",
  "Zones: Sanctuary (client, Trick or Treat party) and Pixiewood (article 1860 summary, decorations) only."
 ]
}
```</result>
<parameter name="status">done
