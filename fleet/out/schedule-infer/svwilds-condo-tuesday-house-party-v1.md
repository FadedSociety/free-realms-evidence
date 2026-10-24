<!-- fleet job=schedule-infer id=svwilds-condo-tuesday-house-party-v1 status=no_submit turns=2 usd=0.0018 tokens(read,write,in,out)=[5272, 6353, 6, 1812] model=claude-haiku-5-5 -->
# vwilds-condo-tuesday-house-party

```json
{
  "event": {"name": "Wilds Condo Tuesday (House Party special)", "key": "vwilds-condo-tuesday-house-party"},
  "kind": "one_off",
  "season": null,
  "slots": null,
  "weekly": null,
  "original_dates": [
    {"year": 2012, "start": "2012-01-31", "end": "2012-01-31", "source": "http://www.freerealms.com/article/detail.action?articleId=2492 (announced for Tue Jan 31 2012, Sanctuary, Server 1); articleId=2493 and articleId=2494 confirm it was hosted that day (re-checked via lookup)"}
  ],
  "zones": ["Sanctuary (Server 1)"],
  "runs": {
    "npcs": ["House Party (Community Team special character)"],
    "props_or_areas": ["Wilds Condo (player-decorated houses, about 8 visited per article 2493)"],
    "quests": [],
    "activities": ["Teleport to the House Party character from Sanctuary, who moved house to house through decorated Wilds Condos", "Add the House Party character to the Friends List to follow him"],
    "rewards": []
  },
  "announce": {"text": "We'll be hosting a special Wilds Condo Tuesday edition of the House Party community event", "locale_id": null},
  "revival": {"recurrence": "one_off_replay", "why": "A single dated special from 2012. It was not a yearly or daily activity. Revive it as a one-time replay on Jan 31, or as admin_only if staff want to run it again. The weekly House Party Tuesday series is a separate record and is not scheduled here."},
  "evidence": [
    {"claim": "Special Wilds Condo Tuesday edition of the weekly House Party event, Tuesday Jan 31 2012, Sanctuary Server 1", "source": "http://www.freerealms.com/article/detail.action?articleId=2492"},
    {"claim": "Community Team hosted the Wilds Condo version starting in Sanctuary, teleporting to the House Party character", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2493"},
    {"claim": "Hosted on Tue Jan 31 2012 (second confirmation)", "source": "http://www.freerealms.com/article/detail.action?articleId=2494"},
    {"claim": "Wilds Condo is the new starter home for new players", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2493; http://www.freerealms.com/article/detail.action?articleId=2494"},
    {"claim": "Wilds Condo is a place name in the client", "source": "locale:296"},
    {"claim": "Weekly series name in the client UI; not this one-off", "source": "locale:428314"},
    {"claim": "Wiki calls Wilds Condo Tuesday a special edition of House Party", "source": "wiki page: Community Events"}
  ],
  "confidence": 0.75,
  "open": [
    "Season is null: no season window for this event. The dates are one day in 2012, not a yearly window.",
    "No slot cadence and no weekly cadence for this special. The weekly House Party Tuesday series (articles 1214, 1168; locale 428314) is a separate record with an unknown start and unsure live status.",
    "No quests, items, prices or rewards are tied to this special by any source in the pack or lookup.",
    "Melanie Lane (Wilds Condo onboarding quests 436700-436778) is not tied to this event and is not listed.",
    "Not included as separate events: New Year House Party (locale 426815, 31364), Pirate House Party (436162), Snow Days House Party (436455, 436459), Treehouse Party (430483). Article 2286 (undated 'Tuesday, October 3rd') is not used.",
    "Futuristic Bicycle omitted: the tie is to House Party generally, not this special.",
    "Player reply count to the homeshow@soe.sony.com invitation is not stated in the sources.",
    "Starter-home date is undated in the sources. Article 2494 was captured 2012-08-19 and article 2493 about two weeks before 2012-02-19."
  ]
}
```
