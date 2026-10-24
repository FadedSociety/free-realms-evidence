<!-- fleet job=event-infer id=vhero-rises-v5 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[7965, 8556, 6, 3525] model=claude-haiku-5-5 -->
# Hero Rises

{"event": {"name": "Hero Rises", "aliases": ["A Hero Rises!", "A Hero Will Rise"]},
 "kind": "update",
 "live": "yes",
 "occurrences": [{"year": 2013, "when": "Aug 13, 2013 (08/13/2013): Chapter 4, 'A Hero Rises Chapter 4', in Game Update 108", "source": "wiki Template:News (ns10), 'Game Update 108 Overview 08/13/2013' (not an official article)"}],
 "recurring": null,
 "zones": ["Wilds South", "Wugachug", "Seaside", "Greenwood Forest", "Queensfields", "Merry Vale"],
 "npcs": ["Darkthorne", "Gloam Overlord"],
 "quests": ["A Hero Rises!", "A Brewing Darkness", "In Memoriam - Region 2 - Sticker - Hero Rises", "Mine Your Own Business - Region 2 - Sticker - Hero Rises", "The Slice Is Right - Region 2 - Sticker - Hero Rises", "Stop, Jacque, and Roll - Region 2 - Sticker - Hero Rises", "Fighting for Funds - Region 2 - Sticker - Hero Rises", "Margin of Victory - Region 2 - Sticker - Hero Rises", "Mentor's Mulligan - Region 2 - Sticker - Hero Rises", "Sort of Urgent - Region 2 - Sticker - Hero Rises"],
 "activities": ["Read the story chapters as they release", "Complete the first-release tutorial covering movement, combat and the UI", "Use the Hero's Journal", "Complete the Region 2 Hero Rises sticker quests"],
 "items": [{"name": "Hero's Journal", "price": null, "currency": null, "source": "article 2875 (replaces the quest journal); client locale:4419559, locale:4419598, locale:4419602, locale:4419604"}],
 "rewards": [],
 "evidence": [
  {"claim": "Hero Rises is a new storyline feature that brings new stories, content and items to Free Realms gradually over time, with chapters over the rest of the year.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875"},
  {"claim": "The first Hero Rises release is a tutorial for new players covering movement, combat and the UI. Article date is not given in the pack.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (article summary)"},
  {"claim": "Hero Rises introduces the Hero's Journal, which replaces the existing quest journal.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (article summary)"},
  {"claim": "The article reveals the Gloam Overlord as the first big bad guy. In the article's pre-release plan, his lieutenants will try to corrupt the regions of Free Realms over the rest of the year.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2875 (fact:npc, pre-release plan)"},
  {"claim": "Chapter 4 ('A Hero Rises Chapter 4', listed as 'A [Brewing] [Darkness] - A Hero Rises Chapter 4') went live 08/13/2013 in Game Update 108.", "source": "wiki Template:News (ns10), 'Game Update 108 Overview 08/13/2013'"},
  {"claim": "The quest 'A Brewing Darkness' is tied to Hero Rises by the News entry only; the client title does not name the event.", "source": "wiki Template:News (ns10); locale:442706, locale:442623, locale:5101356"},
  {"claim": "Client quest 'A Hero Rises!' exists and names the event.", "source": "locale:442319"},
  {"claim": "Eight Region 2 sticker quests carry the Hero Rises name in their client titles (locale:5100803 through 5100845, step 6).", "source": "locale:5100803, locale:5100809, locale:5100815, locale:5100821, locale:5100827, locale:5100833, locale:5100839, locale:5100845"},
  {"claim": "Hero's Journal is a client item with objectives 'Find the Hero's Journal', 'Interact with the Hero's Journal' and 'Close the Hero's Journal'.", "source": "locale:4419559, locale:4419598, locale:4419602, locale:4419604"},
  {"claim": "Weekly dev blogs of 4/12, 5/10, 6/7 and 7/23/2013 describe further Hero Rises updates as planned or released (Wilds South, a third installment, Wugachug). They are unofficial and show plans, not dated live releases.", "source": "wiki User blog:Soe amnerys/Weekly Development Update: 4/12/2013; User blog:Virrago/Weekly Development Update: 5/10/2013; User blog:Virrago/Development Update 6/7/2013; User blog:Virrago/Development Update 7/23/2013"},
  {"claim": "A file caption reads '[Hero] [Rises] (03/15/2013) - updated weapon damage'. It is a single unverified pre-launch caption, not an occurrence.", "source": "wiki File:Wizard's nature wand updated item.jpg (ns6)"}
 ],
 "confidence": 0.5,
 "open": [
  "Event start is unknown. The article 2875 date is null, and chapters 1-3 and the first release have no dated source. Only Chapter 4 (2013-08-13) is dated, and only by an unofficial wiki News entry, not an official article.",
  "The 2013 year comes only from the wiki News entry. No official article dates the event.",
  "Darkthorne dialogue strings (locale:4419601 'Darkthorne has summoned you and the Heartseed has a gift for you.', locale:4419607 'The Gloam have trapped Darkthorne in the Heartseed Chamber.', locale:5100071 sealing away the Gloam Overlord) are removed from quests. They are consistent with article 2875's story but do not name Hero Rises, so the tie is inferred, not confirmed. Queen Valerian (named in locale:5100071) is excluded for the same reason.",
  "Zones: Wilds South, Wugachug, Seaside, Greenwood Forest, Queensfields and Merry Vale are sourced only to blog plans or quest tags, not to a live confirmation. Briarwood Caverns is excluded (video-frame evidence from an earlier pass, not re-read). Sacred Grove and Cobblestone Village are unsourced and left out.",
  "Quest-tie caveats: 'SGRevamp - Wilds South - ...' and 'Stamp Fever: South Wilds II/III' are not named with Hero Rises in the client and are excluded. The 7/23/2013 blog is truncated, so its Wugachug tie is unconfirmed.",
  "Aliases: 'A Hero Rises!' is a client quest title (locale:442319). 'A Hero Will Rise' is only a wiki blog title. Both are listed so a merge catches them. The pack's names_seen missed them.",
  "Merge risk: the quest answer 'Hero's Journal (final, live yes)' is a UI feature this event introduced, so it is kept as an item here, not its own event.",
  "NPCs: Darkthorne is also called Princess Lavender in the wiki, but only Darkthorne and Gloam Overlord are listed, both tied by article 2875. The Gloam Overlord wiki page cites Free Realms Issue 6 comic material, which is a separate source type, so the Overlord is listed only from article 2875.",
  "Rewards and prices: none sourced. Hero's Journal has no price or currency source. Sticker quest rewards are not in the pack. Activities are partly inferred from the tutorial, article 2875 and quest titles.",
  "The critique's '30+ quests' claim is dropped. No source gives a count.",
  "recurring is null. Chapters run over a year as a one-time storyline; no second annual occurrence is evidenced. Scheduling in the calendar is limited to the 2013-08-13 Chapter 4 occurrence until a dated official source is found."
 ],
 "cross_notes": [],
 "id_check": []}
