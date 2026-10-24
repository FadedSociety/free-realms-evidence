<!-- fleet job=event-infer id=vwelcome-back-gifts-v5 status=done turns=4 usd=0.0046 tokens(read,write,in,out)=[36252, 16425, 10, 4294] model=claude-haiku-5-5 -->
# Welcome Back gifts

```json
{"event": {"name": "Welcome Back gifts", "aliases": ["Welcome-back gifts", "Welcome Back login gift series", "Welcome Back program (SOE returning-player program)"]},
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "about mid-May 2011 (estimate; no article gives an absolute post date)", "source": "http://www.freerealms.com/article/detail.action?articleId=2129 (German 'Welcome Back' post, capture-dated about six days before 2011-05-21; summary only, exact post date not shown). Supporting: http://www.freerealms.com:80/article/detail.action?articleId=2127 (its 'two months ago' relative stamp is cited in the pack summary but not confirmed in article text)"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Log in after returning from downtime/lapse to claim the welcome-back login gifts (one free item per day over seven days)", "Receive membership or play-time bonus on the account if standing qualified"],
 "items": [
  {"name": "Sandy Beach Lot", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (Day 1); confirmed by 2129 (German). Client name match only: locale:8321 (place type)"},
  {"name": "Oasis", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (Day 2); also 2138 (French, not re-verified). Client name match only: locale:30162 (place type)"},
  {"name": "Basic Swimming Pool", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (Day 3). Client name match only: locale:147854 (item type)"},
  {"name": "New School Dragon Blade", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (Day 4); 2129 calls it a modern dragon blade, 2138 a next-generation dragon blade. No exact client locale match; generic Dragon Blade entries only (locale:31655, locale:386844)"},
  {"name": "Jackpot Plant", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (Day 5, fact in articles index: 'Day 5 - Jackpot Plant', locale 5683). Wiki: http://freerealms-wiki Jackpot Plant page (wikitext: 'In April, 2011, all players received a free Jackpot Plant as a welcome back gift.'; also reports a second free plant in June 2011). The wiki April/June gifts are a separate wiki claim, not an article; treat as unresolved"},
  {"name": "Large Launch Pad", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (Day 6). Client name match only: locale:6180 (item type)"},
  {"name": "Pirate Ship", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (Day 7); also 2138 (French, not re-verified). Client name match only: locale:9188 (item type)"}
 ],
 "rewards": ["Seven-day login gift series of free items (Days 1-7 as above)", "45 extra Member days for accounts in good standing on or before 2 May 2011 (2127 and 2129 article text per pack; 2130/2131 say 43 days)", "20,000 Coins for Lifetime Members (2127 summary only, not verified in article text)", "Extra Lonely Island Lot for Lifetime Members (2127 summary only; locale:8322 is a housing lot name, not an item id)"],
 "evidence": [
  {"claim": "Members in good account standing on or before 2 May 2011 received an extra 45 days as a Member", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127"},
  {"claim": "Members in good standing before 2 May 2011 received 45 days of free play as a welcome-back gift (German post)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2129"},
  {"claim": "Spanish post lists 43 days of membership for members whose Station account was updated before an early-May cutoff (cutoff garbled); conflicts with 45 days", "source": "http://www.freerealms.com/article/detail.action?articleId=2130"},
  {"claim": "Seven-day login gift series of free items; Day 5 is Jackpot Plant", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127"},
  {"claim": "Day 2 Oasis, Day 4 next-generation dragon blade and Day 7 pirate ship listed in a French post (not re-verified in this pass)", "source": "http://www.freerealms.com/article/detail.action?articleId=2138"},
  {"claim": "Jackpot Plant was given as a welcome-back gift in April 2011 (wiki statement; not an article, and the event's own date is not confirmed)", "source": "Jackpot Plant (wiki page, freerealms-wiki wikitext)"},
  {"claim": "Pre-launch announcements 2139, 2142, 2143 said the welcome-back details were being defined; rewards not listed. These are plans, not the live window", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2139"},
  {"claim": "Client name matches only (not proof of event membership): Sandy Beach Lot locale:8321, Oasis locale:30162, Basic Swimming Pool locale:147854, Large Launch Pad locale:6180, Pirate Ship locale:9188, Lonely Island Lot locale:8322", "source": "locale:8321, locale:30162, locale:147854, locale:6180, locale:9188, locale:8322"},
  {"claim": "Excluded: locale:435868 is the item 'June Member's Pack' (a separate bundle listing Sandy Beach Lot, Palm Tree Hat, Beach Ball); not part of this gift", "source": "locale:435868"},
  {"claim": "Excluded: locale:430516 is a client placeholder label ('Preview - Sandy Beach Lot', FLAGGED, not live content)", "source": "locale:430516"},
  {"claim": "Excluded: locale:28292 is a ui-type sale banner string 'Basic Swimming Pool Special!', not a gift item", "source": "locale:28292"},
  {"claim": "Baby Unicorn wiki cites a Welcome Back Letter / Producer Letter dated May 18, 2011; no source ties it to these gifts, so excluded", "source": "Baby Unicorn (wiki)"}
 ],
 "confidence": 0.5,
 "open": [
  "Date: no article gives an absolute post date or month. The best estimate is mid-May 2011 from capture stamps (2129, about six days before 2011-05-21). The 2127 'two months ago' stamp is unconfirmed. The wiki's April 2011 Jackpot Plant gift conflicts with mid-May; not resolved.",
  "Membership days conflict: 45 (2127, 2129) vs 43 (2130, 2131). Possibly a translation error or two offers; unresolved.",
  "The 2 May 2011 date is a membership-standing cutoff, not the event start. Do not read it as the window.",
  "Lifetime bonus (20,000 Coins and Lonely Island Lot) rests only on the 2127 summary; not verified in article text.",
  "Day 2, 4 and 7 item names confirmed by 2138 and 2130 were not re-verified in article text in this pass; 2130 also gives the conflicting 43 days.",
  "Day 4 'New School Dragon Blade' has no exact client locale match.",
  "Client ids for Sandy Beach Lot, Oasis, Basic Swimming Pool, Large Launch Pad, Pirate Ship are name matches only. Tradeability and price are unknown; no price in sources, so currency is null.",
  "Article 2153 ties Sandy Beach Lot to a separate Summer Bundle offer; not re-verified here.",
  "Possible merge: the wiki's April and June 2011 Jackpot Plant gifts may be separate from the Day 5 login gift. Unresolved.",
  "Zones, NPCs and quests: none tied to this event in the pack. The video 'Welcome back' dialog belongs to Card Duelist: Return from the Rumbledome, a different quest.",
  "Recurrence: one occurrence only, so recurring is null.",
  "Kind 'promotion' is my classification from the article wording; no source states it.",
  "Critique fixes applied: wiki April 2011 cited to the Jackpot Plant wiki page; locale:435868, locale:430516 and locale:28292 described per client text; relative-date and lifetime claims marked unverified; 430516 moved out of gift evidence."
 ]}
```</result>
