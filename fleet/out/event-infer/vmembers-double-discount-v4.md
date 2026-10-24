<!-- fleet job=event-infer id=vmembers-double-discount-v4 status=done turns=1 usd=0.0016 tokens(read,write,in,out)=[0, 5773, 4, 1773] model=claude-haiku-5-5 -->
# Members Double Discount

```json
{
 "event": {
  "name": "Double Member Discount Event",
  "aliases": ["Member Discount Event"]
 },
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "September 1-8 (Sept 1 11:59am PDT to Sept 8 11:59am PDT)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1782"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Bought Station Cash Market items at the member discount rate (20% instead of 10%)"],
 "items": [],
 "rewards": [],
 "evidence": [
  {"claim": "The Double Member Discount Event was valid from September 1, 2010 at 11:59am PDT until September 8, 2010 at 11:59am PDT, and was limited to Members.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1782"},
  {"claim": "During the event, Members received 20% instead of the normal 10% on items bought from the Station Cash Market.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1782"},
  {"claim": "Article 1793 (French, 'Double Remise aux Membres Pour un Temps Limité!') raises the Station Cash Market discount for members from 10% to 20% for 1 September 20:59 CET to 8 September 20:59 CET. It states no year, so it does not corroborate 2010 and is not counted as an occurrence.", "source": "http://www.freerealms.com/article/detail.action?articleId=1793&request_locale=en_US"},
  {"claim": "Article 2258 (Back to School Bonanza, 50% off New School Items) is a different promotion and is not this event.", "source": "http://www.freerealms.com/article/detail.action?articleId=2258"},
  {"claim": "Locale entries '30% Members Only Discount!' (ids 1734, 1737) and 'Member Discount:' (427735) were found by search, but no source ties them to this event, so they are not claimed.", "source": "locale:1734, locale:1737, locale:427735"}
 ],
 "confidence": 0.7,
 "open": [
  "Year: only article 1782 states 2010. Article 1793 gives the same 1-8 September window and 10%-20% change with no year. Candidate occurrence, year unknown: September 1 20:59 CET to September 8 20:59 CET (article 1793). Not counted until a year is found.",
  "Name merge: 'Members Double Discount' (the pack title) and the article 1793 title are NOT confirmed aliases. They match 1782's window and discount numbers, but no source says they are the same event. Treat as unverified candidates, possibly a separate post or a separate event. Removed from aliases.",
  "Time zone: article 1793 says CET; 20:59 CET matches 11:59 PDT only if it means CEST. The post does not say so, so this is an inference.",
  "Recurrence: null. Only one dated occurrence is sourced, and the undated 1793 post cannot establish a second year.",
  "Locale ids 1734 and 1737 ('30% Members Only Discount!') may be a related member promotion. Not verified as the same or different, so not merged.",
  "Zones, NPCs, quests, rewards and items are empty: no source ties them to this event. The wiki category and quest-answer lists were empty.",
  "Kind 'promotion' comes from the article wording (a limited-time member discount). It is not confirmed against any official category.",
  "Live 'yes' rests on an official article (1782) with a stated 2010 window; the status of the event after 2010 is unknown."
 ]
}
```
