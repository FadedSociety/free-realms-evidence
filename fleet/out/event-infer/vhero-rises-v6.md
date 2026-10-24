<!-- fleet job=event-infer id=vhero-rises-v6 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[8327, 9085, 6, 3795] model=claude-haiku-5-5 -->
# Hero Rises

```json
{
 "event": {
  "name": "Hero Rises",
  "aliases": ["A Hero Rises!"]
 },
 "kind": "update",
 "live": "yes",
 "occurrences": [
  {
   "year": 2013,
   "when": "Aug 13, 2013 (Game Update 108). Chapter 4, 'A Hero Rises Chapter 4'",
   "source": "wiki Template:News (ns10), 'Game Update 108 Overview 08/13/2013' (unofficial wiki News entry; not an official article)"
  }
 ],
 "recurring": null,
 "zones": ["Seaside", "Wugachug"],
 "npcs": ["Darkthorne", "Gloam Overlord"],
 "quests": [
  "A Hero Rises!",
  "A Brewing Darkness",
  "In Memoriam - Region 2 - Sticker - Hero Rises",
  "Mine Your Own Business - Region 2 - Sticker - Hero Rises",
  "The Slice Is Right - Region 2 - Sticker - Hero Rises",
  "Stop, Jacque, and Roll - Region 2 - Sticker - Hero Rises",
  "Fighting for Funds - Region 2 - Sticker - Hero Rises",
  "Margin of Victory - Region 2 - Sticker - Hero Rises",
  "Mentor's Mulligan - Region 2 - Sticker - Hero Rises",
  "Sort of Urgent - Region 2 - Sticker - Hero Rises"
 ],
 "activities": [
  "Read the story chapters as they release",
  "Complete the first-release tutorial covering movement, combat and the UI (undated)",
  "Use the Hero's Journal (undated)",
  "Complete the Region 2 Hero Rises sticker quests (undated)"
 ],
 "items": [
  {
   "name": "Hero's Journal",
   "price": null,
   "currency": null,
   "source": "article 2875 (replaces the quest journal; undated first release); client locale:4419559, locale:4419598, locale:4419602, locale:4419604"
  }
 ],
 "rewards": [],
 "evidence": [
  {
   "claim": "Hero Rises is a new storyline feature that brings new stories, content and items to Free Realms gradually over time, with chapters over the rest of the year (pre-release plan).",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875"
  },
  {
   "claim": "The first Hero Rises release is a tutorial for new players covering movement, combat and the UI. Article date is null in the pack, so this release is undated.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (article summary)"
  },
  {
   "claim": "Hero Rises introduces the Hero's Journal, which replaces the existing quest journal.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (article summary)"
  },
  {
   "claim": "The article reveals the Gloam Overlord as the first big bad guy; his lieutenants are planned to corrupt the regions over the rest of the year (plan, not dated).",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (fact:npc)"
  },
  {
   "claim": "Chapter 4 ('A Hero Rises Chapter 4', listed as 'A Brewing Darkness - A Hero Rises Chapter 4') appears in Game Update 108 dated 08/13/2013, with a Bug Fixes entry for the same chapter.",
   "source": "wiki Template:News (ns10), 'Game Update 108 Overview 08/13/2013'"
  },
  {
   "claim": "The quest 'A Brewing Darkness' is tied to Hero Rises by the News entry only; the client title (locale:442706, 442623, 5101356) does not name the event.",
   "source": "wiki Template:News (ns10); locale:442706, locale:442623, locale:5101356"
  },
  {
   "claim": "Client quest 'A Hero Rises!' exists and names the event.",
   "source": "locale:442319"
  },
  {
   "claim": "Eight Region 2 sticker quests carry the Hero Rises name in their client titles (locale:5100803, 5100809, 5100815, 5100821, 5100827, 5100833, 5100839, 5100845; step 6). Verified in the client. No date or occurrence is sourced for them.",
   "source": "locale:5100803 through locale:5100845"
  },
  {
   "claim": "Hero's Journal is a client item with objectives 'Find the Hero's Journal', 'Interact with the Hero's Journal' and 'Close the Hero's Journal'.",
   "source": "locale:4419559, locale:4419598, locale:4419602, locale:4419604"
  },
  {
   "claim": "Weekly dev blogs of 4/12, 5/10, 6/7 and 7/23/2013 describe further Hero Rises updates as planned or released (Wilds South, a third installment, Wugachug). Unofficial; they show plans, not dated live releases.",
   "source": "wiki User blog:Soe amnerys/Weekly Development Update: 4/12/2013; User blog:Virrago/Weekly Development Update: 5/10/2013; User blog:Virrago/Development Update 6/7/2013; User blog:Virrago/Development Update 7/23/2013"
  },
  {
   "claim": "A file caption reads '[Hero] [Rises] (03/15/2013) - updated weapon damage'. A single unverified caption; not treated as an occurrence.",
   "source": "wiki File:Wizard's nature wand updated item.jpg (ns6)"
  }
 ],
 "confidence": 0.45,
 "open": [
  "Event start is unknown. Article 2875 has no date (null), so the tutorial, Hero's Journal and chapters 1-3 are undated. Only Chapter 4 (2013-08-13) is dated, and only by an unofficial wiki News entry, not an official article.",
  "The 2013 year comes only from the wiki News entry. No official article dates the event.",
  "Live status is 'yes' only on the strength of the wiki News entry for Chapter 4. Article 2875 is a pre-launch announcement and gives no live confirmation.",
  "Darkthorne dialogue strings (locale:4419601, 4419607, 5100071) are consistent with article 2875's story but do not name Hero Rises, so the tie is inferred, not confirmed. Queen Valerian is excluded for the same reason.",
  "Zones: Seaside and Wugachug are tied to Chapter 4 only (News text and quest tag). Wilds South, Greenwood Forest, Queensfields and Merry Vale are sourced only to unofficial blog plans or quest tags and are left unscheduled. Briarwood Caverns is excluded (unverified in this pass). Sacred Grove and Cobblestone Village are unsourced and left out.",
  "Quest-tie caveats: 'SGRevamp - Wilds South - ...' and 'Stamp Fever: South Wilds II/III' are not named with Hero Rises in the client and are excluded. The 7/23/2013 blog is truncated, so its Wugachug tie is unconfirmed.",
  "Sticker quests (8, verified in the client) have no date and no source tying them to an occurrence. They may belong to a separate sticker campaign; occurrence is unknown.",
  "'A Brewing Darkness' is a Chapter 4 quest by News entry only. It is not a standing Hero Rises quest.",
  "Aliases: 'A Hero Rises!' is a client quest title (locale:442319) and is kept. 'A Hero Will Rise' is only a wiki blog title and is dropped. The pack's names_seen missed 'A Hero Rises!'.",
  "Merge risk: the quest answer 'Hero's Journal (final, live yes)' is a UI feature this event introduced. It is kept as an item here, not as its own event.",
  "NPCs: Darkthorne is also called Princess Lavender in the wiki, but the pack gives no source for that alias in this event. The Gloam Overlord wiki page cites Free Realms Issue 6 comic material, a separate source type; the Overlord is listed only from article 2875.",
  "Rewards and prices: none sourced. Hero's Journal has no price or currency source. Sticker quest rewards are not in the pack. Activities are partly inferred from the tutorial, article 2875 and quest titles.",
  "The critique's '30+ quests' claim is dropped. No source gives a count.",
  "recurring is null. The chapters are a one-time storyline run; no second annual occurrence is evidenced. The year-long chapter run in article 2875 is a plan, not a schedule."
 ],
 "cross_notes": [],
 "id_check": ["locale:442319, 5100803-5100845 (step 6) and 4419559/4419598/4419602/4419604 re-checked this pass"]
}
```
