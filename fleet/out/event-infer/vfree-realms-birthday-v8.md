<!-- fleet job=event-infer id=vfree-realms-birthday-v8 status=done turns=2 usd=0.0039 tokens(read,write,in,out)=[9146, 11958, 6, 4608] model=claude-haiku-5-5 -->
# Free Realms Birthday

```json
{
 "event": {
  "name": "Free Realms Birthday Bash",
  "aliases": ["Birthday Bash", "Birthday Bash!"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "1st birthday; announced to start April 29, 2010 (end May 10 per the prior pack, not re-verified this pass). Start conflicts with a Ten Ton Hammer item giving April 28.", "source": "http://www.tentonhammer.com:80/node/83604 (start April 29); http://www.tentonhammer.com:80/node/83041 (says April 28); articleId=1268 and articleId=1267 (not re-verified)"},
  {"year": 2011, "when": "2nd birthday party; runs from the post date (approx. April 21, inferred from 'Posted 1 week, 1 day ago') to May 18, 2011. Start approximate.", "source": "http://www.freerealms.com/article/detail.action?articleId=2106"},
  {"year": 2012, "when": "3rd birthday Bash; ran through May 24, 2012. Start not sourced. Marketplace furniture update April 24, 2012. Login day April 28, 2012 is not separately sourced here.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580; wiki:Birthday Cake Hat; wiki:Template:News/Archive"},
  {"year": 2013, "when": "4th birthday, April 29, 2013 start (per prior pack). End not sourced.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924; wiki:Template:News/Archive (banner 'Free Realms Turns Four!' with Birthday Bash, floating furniture, free cake hat, Piñata pet)"}
 ],
 "recurring": "Annual, in April around the April 29 launch anniversary (Free Realms launched April 29, 2009). The wiki Events page says the Bash is 'an annual event held throughout the month of April' celebrating launch day, and the 2010, 2011, 2012 and 2013 occurrences support it. Exact start and end days vary by year and are not fully sourced.",
 "zones": ["Sanctuary", "Happy Valley", "Sacred Grove"],
 "npcs": ["Camellia", "Queen Valerian", "Chef Jarvie", "Sal Monella", "Bordon Cloo", "Glerga", "Quills"],
 "quests": ["Free Realms Turns Three!"],
 "activities": [
  "2010: party prep quests; regional community parties; helping Chef Jarvie with cake monsters (source: articleId=1268 / node/83604 summaries, not re-verified)",
  "2011: start party quests by speaking to Camellia in Sanctuary; battle the Cakenstein boss (spelled Kuchenstein in the 2011 article) (articleId=2106)",
  "2012: cake bake-off storyline led by Queen Valerian; stop Cakenstein and the cakelings; daily party-prep quests; log in for the free hat (articleId=2580; locale:707)",
  "2013: join the Ambassadors at the Birthday Bash area in Sanctuary (articleId=2924)",
  "Buy Birthday Bash furniture and the Piñata Pony from the Station Cash Marketplace"
 ],
 "items": [
  {"name": "Birthday Bash Furniture Bundle", "price": "1350", "currency": "station_cash", "source": "locale:691; locale:692 (1350 Station Cash, 250 saved)"},
  {"name": "Birthday Bash Bed", "price": null, "currency": "station_cash", "source": "locale:436981; wiki:Template:News/Archive (Marketplace update April 24, 2012)"},
  {"name": "Birthday Bash Chair", "price": null, "currency": "station_cash", "source": "locale:436982; wiki:Template:News/Archive (April 24, 2012)"},
  {"name": "Birthday Bash Sofa", "price": null, "currency": "station_cash", "source": "locale:436983; in the April 24, 2012 Marketplace update per the prior pack"},
  {"name": "Birthday Bash Dining Table", "price": null, "currency": "station_cash", "source": "locale:436980; wiki:Template:News/Archive (April 24, 2012)"},
  {"name": "Birthday Bash Wall Sconce", "price": null, "currency": "station_cash", "source": "locale:666; wiki:Template:News/Archive (April 24, 2012)"},
  {"name": "Birthday Bash Floor Lamp", "price": null, "currency": "station_cash", "source": "locale:437014; wiki:Template:News/Archive (April 24, 2012)"},
  {"name": "Piñata Pony", "price": null, "currency": "station_cash", "source": "wiki:Piñata Pony (sold during the annual Birthday Bash); wiki:Pets. Year and price not sourced."},
  {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "wiki:Birthday Cake Hat (rewarded to all players who logged in during the 2012 Bash; unobtainable); articleId=2580 ('Logging in during the Birthday Bash granted a free Birthday Cake hat, available until the Bash ended')"}
 ],
 "rewards": [
  "Birthday Cake Hat, free for logging in during the 2012 Bash (articleId=2580; wiki:Birthday Cake Hat)",
  "Birthday Bash furniture, Station Cash (April 24, 2012 Marketplace update)",
  "Piñata Pony pet, Station Cash (year not sourced)"
 ],
 "evidence": [
  {"claim": "The 2012 Bash is the 3rd anniversary, ran through May 24, 2012, and granted a free Birthday Cake hat for logging in.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "The Birthday Cake Hat is unobtainable and was rewarded to all players who logged in during the 2012 Bash.", "source": "wiki:Birthday Cake Hat"},
  {"claim": "The annual Bash is held throughout April in celebration of the April 29 launch anniversary.", "source": "wiki:Events"},
  {"claim": "The 2011 2nd birthday party ran to May 18, 2011; start approximate.", "source": "http://www.freerealms.com/article/detail.action?articleId=2106"},
  {"claim": "The quest 'Free Realms Turns Three!' starts by speaking to Camellia near the great tree in Sanctuary; Cakenstein is the antagonist. Scoped to 2012.", "source": "locale:706; locale:707"},
  {"claim": "'Birthday Bash!' is an in-game string.", "source": "locale:29341"},
  {"claim": "Birthday Bash furniture names exist in the client; Bundle costs 1350 Station Cash.", "source": "locale:691; locale:692; locale:436980-436983; locale:437014; locale:666"},
  {"claim": "articleId=1197 is a pre-launch preview of the 1st birthday (April 29). It is a plan, not a live occurrence.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1197"}
 ],
 "confidence": 0.6,
 "open": [
  "2010 start conflict: node/83041 says April 28; node/83604 and articles 1267/1268 say April 29. Not resolved. The 2010 end (May 10) was not re-verified this pass.",
  "2011 start is approximate (about April 21), inferred from 'Posted 1 week, 1 day ago'.",
  "2012 start date not sourced. 2013 end date not sourced.",
  "Quest 'Free Realms Turns Three!' is sourced only to 2012; no quest names are sourced for 2010, 2011 or 2013.",
  "Birthday Cake Hat login window is sourced to the 2012 Bash only; the separate April 28, 2012 login-day claim from the critique was not verified and is not used.",
  "Furniture other than the Bundle: prices unsourced; sale window sourced only to the April 24, 2012 update. Sofa dating rests on the prior pack, not verified.",
  "Piñata Pony price and year not sourced.",
  "Cakenstein (2012) and Kuchenstein (2011) are not linked by any source; not merged.",
  "Aliases dropped as unsourced: 'Free Realms anniversary', 'Free Realms 1st birthday', '2nd Birthday Party For Free Realms', 'Free Realms Turns Three!' (a quest title, not an event alias), 'Happy 3rd Birthday, Free Realms!'.",
  "Merge risk: 'Free Realms Birthday' may cover other birthday-named content. Excluded for lack of a source tying them to the Bash: Five Birthday T-shirts, Birthday Cake Samples, Cakenstein Attacks!, Glerga's Birthday Cake, Birthday Party Crate, Birthday Firework, Birthday Boomer, Birthday Candle, Birthday Pinata, Birthday Invitation, Community Event: Birthday Hide and Seek, Free Realms Birthday T-Shirt.",
  "Ambassadors is a Community Team group, not an NPC. Cakenstein is a monster, not an NPC.",
  "Boss Cake, Balloon Animal and balloon weapons were reported as Bash items but are not re-verified; not listed.",
  "Schedule: only 2010 has a near-complete window. Treat the recurrence as annual in April, with exact days to be confirmed per year before scheduling."
 ]
}
```
