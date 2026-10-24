<!-- fleet job=event-infer id=vhero-rises-v8 status=done turns=3 usd=0.0036 tokens(read,write,in,out)=[18476, 13758, 8, 3356] model=claude-haiku-5-5 -->
# Hero Rises

```json
{
 "event": {
  "name": "Hero Rises",
  "aliases": ["A Hero Rises!", "A Hero Rises Chapter 4 (series tag, Game Update 108 News)"]
 },
 "kind": "update",
 "live": "unsure",
 "occurrences": [
  {
   "year": 2013,
   "when": "Feb 12, 2013 (lead only): wiki user blog title 'Soe amnerys/02-12-13 Update: Achievements, Home Decor Sale, Hero's Journal' ties the Hero's Journal to a Feb 12, 2013 update. Body not read; the title is the only evidence, and it does not name Hero Rises.",
   "source": "wiki ns500 'User blog:Soe amnerys/02-12-13 Update: Achievements, Home Decor Sale, Hero's Journal' (title only; freerealms-wiki/harvest/lists/categories.json)"
  },
  {
   "year": 2013,
   "when": "Aug 13, 2013 (Game Update 108), Chapter 4 'A Brewing Darkness' under the series tag 'A Hero Rises Chapter 4'",
   "source": "wiki Template:News (ns10), 'Game Update 108 Overview 08/13/2013' (unofficial wiki News entry; not re-read in this pass)"
  }
 ],
 "recurring": null,
 "zones": ["Seaside", "Wugachug"],
 "npcs": ["Gloam Overlord"],
 "quests": ["A Hero Rises!", "A Brewing Darkness"],
 "activities": [
  "Pre-launch plan (article 2875, undated): read story chapters as they release; complete the new-player tutorial (movement, combat, UI); use the Hero's Journal",
  "Live (unofficial, Game Update 108, Aug 13, 2013): play Chapter 4 'A Brewing Darkness'"
 ],
 "items": [
  {
   "name": "Hero's Journal",
   "price": null,
   "currency": null,
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (replaces the quest journal; undated); client locale:4419559, 4419598, 4419602, 4419604"
  }
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Hero Rises is announced by SOE as a new storyline feature releasing chapters gradually over time with new content and items.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875"},
  {"claim": "Article 2875 is undated (date null). Its first release is a new-player tutorial on movement, combat and the UI, and it introduces the Hero's Journal, which replaces the quest journal.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (article summary)"},
  {"claim": "Article 2875 says the first chapter reveals the Gloam Overlord and more chapters follow over the rest of the year (a plan, not a schedule).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (article summary)"},
  {"claim": "A wiki user blog title ties the Hero's Journal to a Feb 12, 2013 update. Only the title was checked.", "source": "wiki ns500 'User blog:Soe amnerys/02-12-13 Update: Achievements, Home Decor Sale, Hero's Journal'"},
  {"claim": "Chapter 4 appears in Game Update 108 dated 08/13/2013 as 'A Brewing Darkness - A [Hero] [Rises] [Chapter] [4]'. The chapter name is 'A Brewing Darkness'; 'A Hero Rises Chapter 4' is the series tag. Wiki-only and unofficial.", "source": "wiki Template:News (ns10), 'Game Update 108 Overview 08/13/2013' (not re-read in this pass)"},
  {"claim": "Client quest titled 'A Hero Rises!' exists.", "source": "locale:442319"},
  {"claim": "Client Hero's Journal objectives: 'Find the Hero's Journal', 'Interact with the Hero's Journal', 'Close the Hero's Journal'.", "source": "locale:4419559, 4419598, 4419602, 4419604"},
  {"claim": "Client titles 'A Brewing Darkness' appear in the locale (ids 187513015, 1669446019, 2958099636, 2969483822), but none names Hero Rises. The Chapter 4 tie comes only from the wiki News entry.", "source": "client locale (en_us_data.dat ids listed)"}
 ],
 "confidence": 0.35,
 "open": [
  "Start date unknown. Article 2875 is undated, so the announcement, tutorial, Hero's Journal and Chapters 1-3 have no article date.",
  "The Feb 12, 2013 date rests only on a wiki blog title, not the blog body. It is a lead, not a confirmed live date. The blog does not name Hero Rises in the title.",
  "The Aug 13, 2013 Chapter 4 date rests only on an unofficial wiki News entry. Its wording was taken from the critique, not re-read. No official article dates it.",
  "live is 'unsure'. No official source confirms any chapter went live. Keep wireable false until an official dated source is found.",
  "Eight Region 2 sticker quests carry 'Hero Rises' in their client titles (locale 5100803, 5100809, 5100815, 5100821, 5100827, 5100833, 5100839, 5100845: 'In Memoriam', 'Mine Your Own Business', 'The Slice Is Right', 'Stop, Jacque, and Roll', 'Fighting for Funds', 'Margin of Victory', 'Mentor's Mulligan', 'Sort of Urgent'). No source ties them to an occurrence. They may be a separate sticker campaign, so they are left out of quests.",
  "Merge risk: the quest-answer note 'Hero's Journal (final, live yes)' is kept here as an item of this event, not as a separate event. Its live status is not separately confirmed.",
  "Zones Seaside and Wugachug are sourced only to the Chapter 4 News text. Wilds South, Greenwood Forest, Queensfields and Merry Vale appear only in unofficial blog plans and are not listed. Darkthorne, Queen Valerian and Princess Lavender are not listed as NPCs because no source names them with this event.",
  "Unofficial 2013 dev blogs (4/12, 5/10, 6/7, 7/23) describe Hero Rises plans only, not dated releases. The 7/23 blog is truncated.",
  "The caption '[Hero] [Rises] (03/15/2013) - updated weapon damage' is a single unverified caption and is not an occurrence.",
  "Rewards and prices are not sourced. Hero's Journal has no price or currency source.",
  "recurring is null. The chapter series is a storyline run; no second dated occurrence is evidenced, and the year-long schedule in article 2875 is a plan."
 ]
}
```
