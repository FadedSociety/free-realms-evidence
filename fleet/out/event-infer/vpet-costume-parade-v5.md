<!-- fleet job=event-infer id=vpet-costume-parade-v5 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[7579, 8303, 6, 2330] model=claude-haiku-5-5 -->
# Pet Costume Parade

{"event": {"name": "Pet Parade", "aliases": ["Community Event: Pet Parade (client locale:31293)"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [{"year": 2010, "when": "Sep 2 and Sep 3 (Server 1; US/LatAm on Sep 2, UK/Europe on Sep 3)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1780"}],
 "recurring": null,
 "zones": ["Crossroads", "Sanctuary"],
 "npcs": [],
 "quests": [],
 "activities": ["Bring your pet to Crossroads and march up the road to gather near the Sanctuary warpstone (article 1780)"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "Article 1780 says a community Pet Parade had players bring pets to Crossroads and march up the road to gather near the Sanctuary warpstone. Re-checked in lookup: the fact row and the summary both say this.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1780"},
  {"claim": "The article 1780 summary gives the event as held on Server 1 on September 2 and 3, 2010 (US/LatAm and UK/Europe times). Re-checked in lookup. The weekday names and clock times from the earlier pack were not confirmed in the excerpts, so they are left out.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1780"},
  {"claim": "Client string 31293 is titled 'Community Event: Pet Parade'. Re-checked with locale.", "source": "locale:31293"},
  {"claim": "Client string 31294 says 'Bring your favorite pet to a pet parade in Blackspore! SERVER 1'. It conflicts with the Crossroads start in article 1780, so Blackspore is not added to zones.", "source": "locale:31294"}
 ],
 "confidence": 0.4,
 "open": [
  "Live status: this is an archived 2010 official notice. The occurrence is sourced, but the rebuild should not schedule it as live until someone decides whether it should run again. Wireable: no.",
  "Name merge: 'Pet Costume Parade' was the pack's name and no source uses it as a title, so it is dropped as an alias. The pack seems to merge several events. Costume Parade (article 516, Fri Oct 23 2009, Server 1, 3-5pm Pacific) has a different name and is not counted as an occurrence of this entry. Dress Up Your Pet Day (article 877) has no year or date. Pet Week (article 1775) has a 2010 year in its summary only and no month or day. Article 889 (Spanish recap, Wugachug march to Sanctuary) has no date. Ghostly Pet Party (article 1845, Blackspore) was not in the pack and was not checked. Each needs its own entry or a family record.",
  "Activity merge removed: the earlier 'show off pet costumes and tricks' activity came from article 1775 (Pet Week) and was removed from this entry.",
  "Zone conflict: client 31294 places the start in Blackspore and article 1780 in Crossroads. Seaside (locale:424963) and Sanctuary (locale:424964) come only from strings the pack flagged as dev_note with a possibly internal 'SERVER 1' tag. Seaside is left out, and the Sanctuary zone comes from article 1780 instead.",
  "Summer Camp conflict: article 1780 calls this the last Summer Camp event and article 1775 calls Pet Week the final weekly theme. Both cannot be last without a source reading. Unresolved, and neither claim is used.",
  "Recurrence: only one dated occurrence under this name. Pet parades in 2009 and 2010 have different names, so no yearly pattern is inferred.",
  "Wiki category members and quest answers were not re-run in this pass. The empty NPC, quest, item and reward lists are carried, not re-verified.",
  "The 1780 summary was checked in lookup, not the full article text. Weekdays and clock times stay unverified until the full text is read."
 ]}
