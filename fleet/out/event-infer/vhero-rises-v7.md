<!-- fleet job=event-infer id=vhero-rises-v7 status=done turns=1 usd=0.0027 tokens(read,write,in,out)=[0, 7945, 4, 3450] model=claude-haiku-5-5 -->
# Hero Rises

```json
{
 "event": {
  "name": "Hero Rises",
  "aliases": ["A Hero Rises!"]
 },
 "kind": "update",
 "live": "unsure",
 "occurrences": [
  {
   "year": 2013,
   "when": "Aug 13, 2013 (Game Update 108), Chapter 4 'A Hero Rises Chapter 4'",
   "source": "wiki Template:News (ns10), 'Game Update 108 Overview 08/13/2013' (unofficial wiki News entry, not an official article)"
  }
 ],
 "recurring": null,
 "zones": ["Seaside", "Wugachug"],
 "npcs": ["Gloam Overlord"],
 "quests": ["A Hero Rises!"],
 "activities": [
  "Read story chapters as they release (plan, article 2875)",
  "Use the Hero's Journal (article 2875; undated)",
  "Complete the new-player tutorial covering movement, combat and the UI (first release, pre-launch plan, article 2875; undated)"
 ],
 "items": [
  {
   "name": "Hero's Journal",
   "price": null,
   "currency": null,
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (replaces the quest journal; undated); client locale:4419559, locale:4419598, locale:4419602, locale:4419604 ('Find/Interact with/Close the Hero's Journal')"
  }
 ],
 "rewards": [],
 "evidence": [
  {
   "claim": "Hero Rises is announced as a new storyline feature that brings new stories, content and items gradually over time (pre-launch plan).",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875"
  },
  {
   "claim": "The first release is a new-player tutorial covering movement, combat and the UI, and introduces the Hero's Journal, which replaces the quest journal. Article date is null, so this is undated.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (article summary)"
  },
  {
   "claim": "The article reveals the Gloam Overlord as the first big bad guy, with more chapters planned over the rest of the year (plan, not a schedule).",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (article summary)"
  },
  {
   "claim": "Chapter 4 ('A Hero Rises Chapter 4') appears in Game Update 108 dated 08/13/2013, with Seaside-to-Wugachug continuation text and a Bug Fixes entry for the same chapter.",
   "source": "wiki Template:News (ns10), 'Game Update 108 Overview 08/13/2013' (unofficial)"
  },
  {
   "claim": "Client quest 'A Hero Rises!' exists and names the event.",
   "source": "locale:442319"
  },
  {
   "claim": "Hero's Journal is a client item with objectives 'Find the Hero's Journal', 'Interact with the Hero's Journal' and 'Close the Hero's Journal'.",
   "source": "locale:4419559, locale:4419598, locale:4419602, locale:4419604"
  }
 ],
 "confidence": 0.4,
 "open": [
  "Start date unknown. Article 2875 has date null, so the announcement, tutorial, Hero's Journal and chapters 1-3 are undated. The only dated occurrence (Chapter 4, Aug 13, 2013) rests on an unofficial wiki News entry. No official article dates the event, so the year 2013 is wiki-sourced only.",
  "live is 'unsure'. The wiki News entry suggests Chapter 4 went live in Game Update 108, but article 2875 is a pre-launch announcement with no live confirmation.",
  "Eight Region 2 sticker quests carry 'Hero Rises' in their client titles (locale:5100803, 5100809, 5100815, 5100821, 5100827, 5100833, 5100839, 5100845; step 6): 'In Memoriam', 'Mine Your Own Business', 'The Slice Is Right', 'Stop, Jacque, and Roll', 'Fighting for Funds', 'Margin of Victory', 'Mentor's Mulligan', 'Sort of Urgent' (each 'Region 2 - Sticker - Hero Rises'). No source ties them to an occurrence, so they are left out of quests. They may be a separate sticker campaign.",
  "'A Brewing Darkness' is tied to Hero Rises only by the Chapter 4 News entry (wiki Template:News, Game Update 108). Its client titles (locale:442706, 442623, 5101356) do not name the event, so it is not listed as a standing Hero Rises quest.",
  "Darkthorne is not listed as an NPC. Her dialogue (locale:4419601, 4419607, 5100071) fits article 2875's story, but no source names Hero Rises with her. The wiki also gives the alias Princess Lavender, which no source here ties to this event. Queen Valerian is excluded for the same reason.",
  "Zones: Seaside and Wugachug are sourced only to the Chapter 4 News text. Wilds South, Greenwood Forest, Queensfields and Merry Vale appear only in unofficial blog plans or quest tags and are left unscheduled. Briarwood Caverns, Sacred Grove and Cobblestone Village are unsourced and excluded. 'SGRevamp - Wilds South - ...' and 'Stamp Fever: South Wilds II/III' do not name Hero Rises in the client and are excluded.",
  "Unofficial weekly dev blogs (4/12, 5/10, 6/7 and 7/23/2013; User blog:Soe amnerys and User blog:Virrago) describe Hero Rises plans (Wilds South, a third installment, Wugachug). They are plans, not dated live releases. The 7/23 blog is truncated, so its Wugachug tie is unconfirmed.",
  "File caption '[Hero] [Rises] (03/15/2013) - updated weapon damage' (wiki File:Wizard's nature wand updated item.jpg) is a single unverified caption and is not treated as an occurrence.",
  "Merge risk: the quest-answer note 'Hero's Journal (final, live yes)' is a UI feature this event introduced. It is kept here as an item, not as a separate event. Its live status is not separately confirmed.",
  "Aliases: 'A Hero Will Rise' appears only as a wiki blog title and is dropped. 'A Hero Rises!' is kept as an alias (client quest title, locale:442319). names_seen in the pack missed it.",
  "Rewards and prices: none sourced. Hero's Journal has no price or currency source. Sticker quest rewards are not in the pack.",
  "recurring is null. Chapters are a storyline run; no second dated occurrence is evidenced. The year-long chapter schedule in article 2875 is a plan, not a schedule.",
  "Wiki category 'Hero Rises' had no members in the pack, so no wiki-category tie is available."
 ],
 "cross_notes": [],
 "id_check": ["locale:442319, 5100803-5100845 (step 6) and 4419559/4419598/4419602/4419604 checked in the prior pass; critique re-confirmed titles. Not re-run in this pass."]
}
```
