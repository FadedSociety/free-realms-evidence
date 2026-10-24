<!-- fleet job=event-infer id=vfree-realms-holiday-v7 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[5024, 10962, 6, 3362] model=claude-haiku-5-5 -->
# Free Realms holiday events

{"event": {"name": "Snow Days", "aliases": ["Snow Days holiday event", "Snow Days Returns", "Días de Nieve", "Colina Nevada (Snowhill, Spanish name)", "Winter Basin 'Snow Days' party (Wintery Basin / Cuenca Invernal)"]},
"kind": "holiday",
"live": "yes",
"occurrences": [
 {"year": 2009, "when": "Dec 18, 2009 to Jan 3, 2010, daily", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705 (also freerealms.com articleId=709 and 718, Spanish posts with the same dates)"},
 {"year": 2009, "when": "December 2009 (roundup dated 2009-12-16 says Free Realms holiday events were underway; it does not name Snow Days)", "source": "http://tentonhammer.com/node/78134 (corroboration only)"},
 {"year": 2010, "when": "Wintery Basin Snow Days party: US/Latin America session Thursday Dec 9, 2010, 3pm Pacific; UK/Europe Dec 10 (per the community-event notices in the pack)", "source": "articles.json community-event notices for the Wintery Basin Snow Days party (Dec 2010); not verified against a live URL in this pass"},
 {"year": 2010, "when": "Snow Days member reward: noon Wed Dec 15, 2010, delivery from Dec 16 over 2-3 days", "source": "articles.json Snow Days Special Member Reward notices (Dec 2010 season)"},
 {"year": 2010, "when": "Snow Days ended by the Jan 26, 2010 update patch notes (end of Snow Days listed)", "source": "articles.json patch notes for the January 26, 2010 Free Realms update"},
 {"year": 2013, "when": "Dec 1, 2013 through Jan 14, 2014", "source": "wiki page 'Snow Days' (2013 section)"}
],
"recurring": "yearly in December to early January (at least 2009, 2010 and 2013 per the sources above)",
"zones": ["Snowhill", "Wintery Basin (fishing area above Snowhill)"],
"npcs": ["Candi Ivy", "Trina Turtledove", "Everett", "Abominable Snowman", "Robgoblins"],
"quests": [],
"activities": ["Gifting Tree present gifts daily", "Snow Days prize wheel spins", "Fighting Snowmen and Robgoblins that steal presents", "Snowball defense against the Abominable Snowman attacks", "Snowball fights", "Trading card game (JCC) tournaments (2009 season)", "Wintery Basin fishing and boombox party (2010)", "Present Tracker collecting bows (2013 season)"],
"items": [
 {"name": "Snow Days outfits", "price": null, "currency": "station_cash", "source": "articles/facts.json: Snow Days items are purchased with Station Cash from the Catalog (price per item not given)"},
 {"name": "Snow Days Unicorn Sweater", "price": null, "currency": null, "source": "wiki category member list (freerealms-wiki); price not in pack"},
 {"name": "Snow Days Toy [2013 Edition]", "price": null, "currency": null, "source": "client locale text (en_us_data.dat), name only"}
],
"rewards": ["Snow Days clothing from fighting Robgoblins", "Snow Days outfits from quests and opened presents", "Snow Days prize wheel bonus prizes", "Snow Days Special Member Reward (2010, member accounts)"],
"evidence": [
 {"claim": "Snow Days was a holiday season running every day from Dec 18, 2009 through Jan 3, 2010, with in-game community events and TCG/JCC tournaments.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=705"},
 {"claim": "The Spanish official posts give the same Dec 18, 2009 to Jan 3, 2010 run, with daily community events at 15:00 Pacific.", "source": "http://www.freerealms.com/article/detail.action?articleId=709 and articleId=718"},
 {"claim": "The Dec 2009 Ten Ton Hammer roundup says Free Realms had holiday events with themed events, special quests and seasonal treats in December 2009. It does not name Snow Days; the tie is by date only.", "source": "http://tentonhammer.com/node/78134"},
 {"claim": "Snow Days Returns: the Snowhill seasonal event with Gifting Tree presents, Candi Ivy's daily quest, Abominable Snowman attacks and snowball fights.", "source": "articles.json 'Free Realms - What is New? (Snow Days Return)' summary"},
 {"claim": "Snow Days ended by the Jan 26, 2010 patch.", "source": "articles.json patch notes for the January 26, 2010 update"},
 {"claim": "Snow Days 2013 ran Dec 1, 2013 through Jan 14, 2014.", "source": "wiki page 'Snow Days'"}
],
"confidence": 0.6,
"open": [
 "Merge risk: the pack's 2010 'Snowy Days' Winter Basin festival, the Snow Days Returns post and the 2013 wiki season may be the same recurring event or separate seasons. This entry treats them as one recurring event, which the sources support by name, but the exact 2011 and 2012 runs are not dated in the pack.",
 "The Dec 2009 Ten Ton Hammer roundup is not tied to Snow Days by name; it supports only that the December 2009 holiday season was running.",
 "Quest titles: the pack has no exact quest titles for Snow Days. 'Snow Days daily quests (Candi Ivy and Gifting Tree)' is a catalog label in articles/quests.json, not a confirmed in-game title, so quests is left empty.",
 "Item prices are not in the pack. Only the currency (Station Cash) is sourced, and only as a general statement for Snow Days outfits.",
 "The 2010 Wintery Basin party and Dec 15, 2010 member reward dates come from articles.json summaries whose article URLs were not re-checked in this pass.",
 "The 'live' field is yes for the 2009-10 season and 2013-14 season (both dated). Whether a live server will run it is outside this pack.",
 "Earlier-answer critique: the 2009 umbrella entry and the Snow Days entry are now merged as one event. The critique asked for this, and the official articles 705/709/718 confirm the dates."
]}
