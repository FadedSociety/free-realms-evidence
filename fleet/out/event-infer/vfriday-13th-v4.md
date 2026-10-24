<!-- fleet job=event-infer id=vfriday-13th-v4 status=done turns=2 usd=0.0033 tokens(read,write,in,out)=[7219, 13266, 6, 3144] model=claude-haiku-5-5 -->
# Friday the 13th event

{"event": {"name": "Friday the 13th event", "aliases": ["Frightening Friday the 13th Fun! (article title)", "Maskface's Revenge (client quest title, unconfirmed link)"]},
 "kind": "other",
 "live": "yes",
 "occurrences": [{"year": 2012, "when": "Friday April 13, 2012 (single dated occurrence)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2571 (\"Frightening Friday the 13th Fun!\"). The article's own date is not printed in the captured text; 2012-04-13 is inferred from 'posted 4 days, 4 hours ago' at a 2012-04-18 capture, and corroborated by the Template:News/Archive entry 'Update of April 13, 2012 / Event: Friday the 13th themed event' (reported by the prior pass, not re-pulled here)."}],
 "recurring": null,
 "zones": ["Greenwood Forest (camps area, inferred from wiki Jason Maskface)"],
 "npcs": ["Jason Maskface"],
 "quests": [],
 "activities": ["Players agreed to join Jason Maskface and spook other players (article 2571, fact:event)", "Joining turned the player into a creature such as a banshee, grave elemental or skeleton (article 2571, fact:mechanic)", "Participants were given the Scaredy Cat ability, which turns other players into a black cat (article 2571, fact:combat)"],
 "items": [],
 "rewards": ["Scaredy Cat ability (article 2571)"],
 "evidence": [
  {"claim": "Free Realms ran a Friday the 13th event in which players could join Jason Maskface to spook other players.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2571"},
  {"claim": "Jason Maskface was found near Camp Chatty and Camp Robbie Lake and recruited players for the Friday the 13th event; the article says 'Prepare to meet Jason Maskface near Camp Chatty and Camp Robbie Lake.'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2571"},
  {"claim": "Agreeing to join turned players into a creepy creature such as a banshee, grave elemental or skeleton.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2571"},
  {"claim": "Event participants were given the Scaredy Cat ability, which turns other players into a black cat.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2571"},
  {"claim": "A Friday the 13th Sale was also running on the same day (separate Marketplace promotion, not an item of this event).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2571"},
  {"claim": "Date 2012-04-13: inferred from the article's relative timestamp at capture and matches the Template:News/Archive entry for the April 13, 2012 update.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2571; Template:News/Archive"},
  {"claim": "Client text locale:437130 (quest_dialog, under quest title Maskface's Revenge): \"Boo! It's Friday the 13th! Want to help me scare people? Or are you a scaredy cat?\" The client names Friday the 13th in NPC recruitment dialog.", "source": "locale:437130"},
  {"claim": "NPC name 'Jason Maskface' exists in the client.", "source": "locale:437129"},
  {"claim": "Wiki Jason Maskface describes him as a human NPC who occasionally comes out on Friday the 13ths and roams Greenwood Forest around the camps recruiting players (text seen in the NPC pack's wiki extract; the live wiki lookup did not return this sentence, so treat as secondary).", "source": "wiki page Jason Maskface"},
  {"claim": "Wiki Maskface's Mask is an All Jobs, head slot, clothing item sold to everyone during Friday the 13th events through the Station Cash Marketplace; Members get a 10% discount. Regular price is blank in the wiki.", "source": "wiki page Maskface's Mask"}
 ],
 "confidence": 0.6,
 "open": [
  "Recurrence unverified: only one dated occurrence (2012-04-13). The wiki's 'occasionally comes out on Friday the 13ths' and the Mask's 'during Friday the 13th events' are plural hints, not dated occurrences. Do not schedule recurrences from them. The 2013-12-10 Hero TCG card 5P23 (Jason Maskface, 3 cards via TCG Lobby on Friday the 13th) is a separate promotion, not counted.",
  "Quest 'Maskface's Revenge' (locale:437133) is NOT attached as this event's quest. Its dialog (locale:437130) is generic Friday-the-13th text; no article names the quest and no dated source ties it to 2012-04-13. Candidate only. 'Scaredy Cat' quest title (locale:437137) also unlinked to any source.",
  "Maskface's Mask is NOT listed as an item of this event. Wiki ties it to 'Friday the 13th events' in general, not to the 2012-04-13 occurrence. Price is null (blank in wiki); currency would be station_cash only by inference from the Station Cash Marketplace listing.",
  "Pack may merge the 2012 article event with the wiki's general Friday-the-13th Jason appearances; the wiki's plural wording cannot be dated. Aliases are a pack name and a client quest title, not confirmed event names.",
  "Live status 'yes' rests on the 2012 article announcing the live event. The article's own date is inferred (see occurrences), not printed.",
  "Camp Chatty and Camp Robbie Lake are article locations; their membership in Greenwood Forest is inferred from the wiki, not stated.",
  "locale:437134 'jason maskface - scare - cfritchoff' is a flagged internal dev_note asset tag and is not used as evidence.",
  "Kind 'other': a themed Friday event fits no clear enum value."
 ],
 "critique_fixes": "Addressed: date basis stated as inferred plus archive corroboration; wiki quote flagged as secondary; Mask removed from items; quest demoted to open; occurrence limited to 2012-04-13; dev_note excluded. Mask 'All Jobs head slot' now confirmed from the wiki page."
}
