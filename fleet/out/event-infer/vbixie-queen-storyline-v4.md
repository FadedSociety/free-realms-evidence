<!-- fleet job=event-infer id=vbixie-queen-storyline-v4 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[8111, 9146, 6, 2821] model=claude-haiku-5-5 -->
# Bixie Queen storyline

```json
{
  "event": {
    "name": "Bixies Gone Bad quest (Sanctuary Bixie Hive)",
    "aliases": ["Bixies Gone Bad (locale:15335)", "Save the Bixie Queen (candidate only, locale:417254; link unverified)"]
  },
  "kind": "other",
  "live": "unsure",
  "occurrences": [],
  "recurring": null,
  "zones": ["Sanctuary", "Bixie Hive instance (lobster-shaped; entered on the left claw, Queen in the top-left corner; http://www.tentonhammer.com:80/node/67379)"],
  "npcs": ["Sunflower (quest giver, southwest of Sanctuary; http://www.tentonhammer.com:80/node/67379)", "Bixie Queen (wiki page: Bixie Queen)", "Drone Fauzz (wiki page: Drone Fauzz; spelled 'Drone Fuzz' in video:PkDgb0sfUD8/00102.jpg)"],
  "quests": ["Bixies Gone Bad (locale:15335; objective locale:15339)"],
  "activities": [
    "Talk to Sunflower southwest of Sanctuary to start (http://www.tentonhammer.com:80/node/67379)",
    "Enter the Bixie Hive instance and defeat Unruly Warriors, Unruly Mages and Unruly Elites (http://www.tentonhammer.com:80/node/67379)",
    "Fight four enemy waves in the top-left corner, each with an Unruly Mage and two Unruly Warriors (http://www.tentonhammer.com:80/node/67379)",
    "Free Frightened Bixie Workers for bonus credit (http://www.tentonhammer.com:80/node/67379; video:5_U-uAzDuR4/00064.jpg)",
    "Use the Queen's power-ups during the fight (single frame: video:PkDgb0sfUD8/00088.jpg)",
    "Defeat Drone Fauzz, who captured the Queen (http://www.tentonhammer.com:80/node/67379; wiki: Drone Fauzz)"
  ],
  "items": [],
  "rewards": ["Bonus credit for freeing Frightened Bixie Workers (http://www.tentonhammer.com:80/node/67379)"],
  "evidence": [
    {"claim": "Client quest title 'Bixies Gone Bad', objective 'Save the bixie queen in the Bixie Hive next to Sanctuary.'", "source": "locale:15335; locale:15339"},
    {"claim": "Client quest title 'Save the Bixie Queen' exists (Sanctuary group). Its link to the same quest is not verified.", "source": "locale:417254; locale:417250; locale:417253"},
    {"claim": "Client string 'NOT LIVE - Bixies Gone Bad' is a pre-launch version with objective 'Guarantee the safety of the Bixie queen.' It is not live and is not counted in this record.", "source": "locale:10133; locale:10134 (both flagged not_live)"},
    {"claim": "Quest start, instance entry, enemy waves and the Drone Fauzz uprising are described in a Ten Ton Hammer guide. The guide gives no run dates.", "source": "http://www.tentonhammer.com:80/node/67379"},
    {"claim": "The Bixie Queen is in the Bixie Hive in Sanctuary; Drone Fauzz is the bixie drone who captured her.", "source": "wiki page: Bixie Queen; wiki page: Drone Fauzz"},
    {"claim": "The Trading Card Game card Invading Bixie Elite is tied to the Bixie Queen storyline in Free Realms article 209. That article is undated and is not used as an occurrence.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=209"}
  ],
  "confidence": 0.3,
  "open": [
    "Timing: no source dates a run of this quest or event. Article 209 is undated ('posted 1 week, 6 days ago'). The date 2009-04-29 on node/67379 is a generated summary, not a quoted line. The 'week of May 1, 2009' on node/67483 is a guide publication date, not an event run. occurrences is empty and the event is not wireable. Kind is recorded as 'other' (a quest line), not a timed event, until a dated run source is found.",
    "Live status unknown: confirm whether the Bixie Hive quest was live and for how long, or whether it stayed a permanent quest line.",
    "Two client titles: 'Bixies Gone Bad' (locale:15335) and 'Save the Bixie Queen' (locale:417254). They may be one quest renamed or two entries. The pack does not link them. The event name uses only 'Bixies Gone Bad'.",
    "Minimum level conflict, unresolved: node/67379, node/67381 and node/67397 say Brawler 4; video:5_U-uAzDuR4/00176.jpg and 00192.jpg show job_level 'Brawler 9'. No minimum level is set.",
    "Name spelling: 'Drone Fauzz' (wiki, Ten Ton Hammer) vs 'Drone Fuzz' (video dialog). Probably one NPC; not confirmed.",
    "The TCG card Invading Bixie Elite is a related card, not an event item. Its acquisition method, price and currency are unknown, so it is not listed under items. 'Tipping the Hive' is not tied to this event.",
    "Power-ups are listed under activities, not rewards. The only source is a single video frame.",
    "Excluded as different content: 'Briarwood Bixie Queen' (locale:16234), 'Et Tu, Buzzuz?' (video:Hu1ys1nYQRs/00656.jpg), 'Bixies vs Sprites' (locale:10119, not_live), 'Rebel Bixie Hive' (locale:423022), article 832, and Queensfields Bixie enemies. The 'Goal Complete! Chest' reward is dropped because it rests on one unverified frame. locale:14947 'bixie_f_queen' is an internal asset name and is not used as evidence.",
    "Which build the Ten Ton Hammer guides describe (NOT LIVE or live) is not confirmed."
  ]
}
```
