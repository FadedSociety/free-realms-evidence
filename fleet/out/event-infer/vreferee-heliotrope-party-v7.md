<!-- fleet job=event-infer id=vreferee-heliotrope-party-v7 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5453, 6048, 6, 1697] model=claude-haiku-5-5 -->
# Referee Heliotrope party

```json
{
  "event": {
    "name": "Referee parties (in-game Referee-hosted parties; editorial label)",
    "aliases": ["Referees Party Too! (article title, articleId=1118)"]
  },
  "kind": "other",
  "live": "unsure",
  "occurrences": [],
  "recurring": null,
  "zones": ["Seaside", "Blackspore", "Sanctuary"],
  "npcs": ["Referee Shadow", "Referee Blue", "Referee Heliotrope", "Referee Ruby"],
  "quests": [],
  "activities": [
    "Players join Referee-hosted parties in the named zones; the article invites players to watch for them",
    "Example party themes in the article: beach (Referee Shadow), pet (Referee Blue), Sanctuary party (Referee Heliotrope, described as crowded), holiday (Referee Ruby)"
  ],
  "items": [],
  "rewards": [],
  "evidence": [
    {
      "claim": "Article 'Referees Party Too!' says in-game Referees also hold parties, usually in Seaside, Blackspore or Sanctuary, and shows example parties run by Referees Shadow, Blue, Heliotrope and Ruby",
      "source": "http://www.freerealms.com:80/article/detail.action?articleId=1118"
    },
    {
      "claim": "A party with Referee Heliotrope in Sanctuary is described as crowded ('It can get pretty crowded in Sanctuary with Referee Heliotrope.')",
      "source": "http://www.freerealms.com:80/article/detail.action?articleId=1118"
    },
    {
      "claim": "The article is undated: it gives only a relative 'posted 5 days, 16 hours ago' and was captured March 2010",
      "source": "http://www.freerealms.com:80/article/detail.action?articleId=1118"
    },
    {
      "claim": "Client has Referee party-dialog lines for other themed parties (Pet Party, Luau Party, Winter Party). These are neighbouring seasonal events, not confirmed as the same event as the Referee parties in article 1118",
      "source": "locale:31353; locale:31371 (Pet Party); locale:31354; locale:31369 (Luau Party); locale:4264 (Winter Party)"
    }
  ],
  "confidence": 0.2,
  "open": [
    "Single source: the pack holds only articleId 1118. The event name is an editorial label. 'Referee Heliotrope party' is one example from that article, not a title the site or client uses.",
    "No dated occurrence. The article gives no year or month, so occurrences stays empty.",
    "Live status unknown: the article is a March 2010 capture and does not show whether Referee parties ran after that.",
    "Recurring is null. 'Usually in Seaside, Blackspore or Sanctuary' describes where parties happen, not a schedule.",
    "No quests, wiki category members, or items tied to this event in the pack. Nothing listed.",
    "Theme links (beach, pet, holiday) to Luau, Pet and Winter parties are inferred from the client dialog lines, not stated by article 1118. Treat them as cross-references only.",
    "The Luau Beach Party answer previously attached to this pack is a different event. Its Seaside vs Playa Azul place conflict is not resolved here and should be handled on that event's record.",
    "Pack mismatch: the previous answer's aliases ('Referee party', 'Referee Heliotrope party') were not source titles and were dropped."
  ]
}
```
