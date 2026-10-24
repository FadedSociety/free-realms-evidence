<!-- fleet job=event-infer id=vbirthday-bash-v7 status=done turns=2 usd=0.0035 tokens(read,write,in,out)=[9200, 11557, 6, 3939] model=claude-haiku-5-5 -->
# Birthday Bash

{"event": {"name": "Birthday Bash", "aliases": ["Free Realms Birthday Bash", "Birthday Bash 2012 (locale:695)"]},
"kind": "holiday",
"live": "yes",
"occurrences": [
 {"year": 2012, "when": "Third-anniversary Birthday Bash; runs through May 24, 2012 (start not stated; article posted 2012-04-26)", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 ; locale:695 ('Birthday Bash 2012 marks the 3rd Anniversary of Free Realms.')"},
 {"year": 2013, "when": "4th birthday, April 29, 2013; 'Birthday Bash' area in Sanctuary (end date not stated; social visit only)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924 (checked via lookup summary)"}
],
"recurring": null,
"zones": ["Sanctuary", "Sacred Grove", "Marketplace"],
"npcs": ["Camellia (locale:707: speak to her near the great tree in Sanctuary to start the cake competition)", "Cakenstein (article 2580: monster loose in Sacred Grove stealing cakes)", "Queen Valerian (article 2580: runs the Sanctuary cake bake-off; conflicts with Camellia in locale:707, left open)"],
"quests": ["Birthday Bash! (client quest_title, locale:29341; tie to event by name only)", "Cakenstein Attacks! (client quest_title, locale:4917; link to Cakenstein by content, not dated; verify)"],
"activities": ["Help Sacred Grove chefs in the Sanctuary birthday cake competition (locale:707)", "Stop Cakenstein and the cakelings from ruining the party (locale:707; article 2580)", "Do daily party-prep quests (article 2580 summary)", "Invite someone to the birthday bash (client objective locale:4952)", "Log in during the event to get the Birthday Cake Hat (locale:707)", "Dance with the Ambassadors at the Sanctuary Birthday Bash area (article 2924 summary, 2013)"],
"items": [
 {"name": "Birthday Cake Hat", "price": null, "currency": "reward", "source": "locale:707 (free for logging in during Birthday Bash 2012); article 2580 (logging in during the Bash granted a free Birthday Cake hat)"}
],
"rewards": ["Birthday Cake Hat (free for logging in during the 2012 Bash; locale:707, article 2580)"],
"evidence": [
 {"claim": "Birthday Bash ran through May 24, 2012 as the third-anniversary celebration", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (posted 2012-04-26)"},
 {"claim": "Client names Birthday Bash 2012 as the 3rd anniversary", "source": "locale:695"},
 {"claim": "Sanctuary cake competition started via Camellia; Cakenstein and cakelings ruin the Bash; free Birthday Cake Hat for 2012 logins", "source": "locale:707"},
 {"claim": "Queen Valerian runs the Sanctuary cake bake-off; daily party-prep quests; Cakenstein loose in Sacred Grove; Marketplace pinata pets", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
 {"claim": "4th birthday on April 29, 2013 with a Birthday Bash area in Sanctuary; brief social post, no rewards", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"},
 {"claim": "'Birthday Bash!' is a client quest title", "source": "locale:29341"},
 {"claim": "'Cakenstein Attacks!' is a client quest title", "source": "locale:4917"}
],
"confidence": 0.55,
"open": [
 "Start dates are not stated for either year. 2012 has only an end date (May 24, 2012) and a posting date (2012-04-26). The calendar cannot place a window yet; wireable = false.",
 "2013 is a social visit to a Birthday Bash area (article 2924), with no quests, items or rewards in its source. Treat it as a weaker occurrence, not the same schedule as 2012.",
 "2010 and 2011 occurrences removed. They rest on unverified article wording (articles 1261, 2106).",
 "Recurrence: only two dated occurrences (2012, 2013), both near the April 29 anniversary. The wiki Events page says 'annual' but is single-sourced, and the Cakenstein wiki page says 'the only Birthday Bash'. No annual pattern is confirmed.",
 "Queen Valerian (article 2580) versus Camellia (locale:707) as the bake-off lead is unresolved.",
 "Quest titles from the pack (Cakenstein's Last Stand, Cakey Clue, Cakey Madness, Downing Cakenstein, Mysteriously Cakey Remains, Perfecting the Batter, A Piece of Cake, Forgivable Matter, Mystery Meat Mystery, Undelivered Confections) are not confirmed as client quest titles. Not listed.",
 "Birthday Bash Furniture Bundle (locale:691 item name; description locale:692: candles and balloons, 1350 Station Cash, 250 SC savings) is not tied to a year or to the event in its text. Not listed as an event item. Related client items with the same name family (Birthday Bash Bed/Chair/Sofa/Dining Table/Floor Lamp/Wall Sconce, locale 436980-436983, 437014, 666) also have no year.",
 "Piñata Pony and the four 2012 Marketplace pinata pets (article 2580 summary) are not tied to a named pet in a fetched source. Not listed as items.",
 "Streamer Flair Shard (250 SC): wiki-only, yearless, single source. Not listed.",
 "Balloon weapons (Balloon Sword, Saw, Bow, Axe, Hammer, Wand; locale:6792-6797 per earlier pass) were not re-verified this pass. Not listed.",
 "Birthday T-shirts (per-zone wiki category members) and Gifting Piñata: wiki-only, no year. Not listed. The earlier citation locale:1250569231 does not exist and was removed.",
 "Zones Briarwood, Blackspore, Merry Vale, Seaside, Wugachug, Snowhill and Shrouded Glade are not tied to a dated source. Dropped.",
 "Bake-off dialogue (Sal Monella, Bordon Cloo, Glerga; locale 428071, 428708-428711) is pre-event prep ('just around the corner', 'next year's cake bake-off') with no year. Not listed as live NPCs.",
 "Locale 19967-19968 ('Making this Birthday Bash a Summer Splash') may be a separate variant. Not merged; not verified.",
 "The pack may have merged 2012 and 2013 social content under one name. The 2013 article is kept as a separate, weaker occurrence."
]}
