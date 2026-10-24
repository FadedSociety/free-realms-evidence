<!-- fleet job=event-infer id=vvampire-and-werewolf-costumes-v5 status=done turns=3 usd=0.0034 tokens(read,write,in,out)=[14859, 10037, 8, 4022] model=claude-haiku-5-5 -->
# Vampire and werewolf costumes

{"event": {"name": "Vampires vs. Werewolves Dance-off", "aliases": ["Vampires vs Werewolves Dance-off", "Vampire vs. Werewolf Dance Off", "Super Spooktacular dance-off (Pumpkin Prince)"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": ["Blackspore Swamp (outside the gates of Bone Bog Cemetery)"],
 "npcs": ["Madam Zelda (starts the side-choice quest; Blackspore per articleId=1862)", "Pumpkin Prince (judges the dance-off)"],
 "quests": [],
 "activities": ["Choose a side (Vampires or Werewolves) via Madam Zelda", "Wear Team Vampire or Team Werewolf costume pieces when the in-game 'dance contest is about to begin' announcement appears", "Go to Bone Bog Cemetery / the Blackspore marsh to take part in the dance-off", "Side with the most fans wins a piece of the Pumpkin Prince's cake; the team with the most frightening dance is crowned scariest monster"],
 "items": [
  {"name": "Team Vampire T-Shirt", "price": null, "currency": null, "source": "locale:14692; wiki Vampires vs. Werewolves Dance-off (team item list)"},
  {"name": "Team Werewolf T-Shirt", "price": null, "currency": null, "source": "locale:14694; wiki Vampires vs. Werewolves Dance-off (team item list)"},
  {"name": "Vampire Outfit", "price": null, "currency": null, "source": "locale:14688 (existence only); wiki Vampires vs. Werewolves Dance-off (team item list)"},
  {"name": "Werewolf Outfit", "price": null, "currency": null, "source": "locale:14690 (existence only); wiki Vampires vs. Werewolves Dance-off (team item list)"}
 ],
 "rewards": ["Piece of the Pumpkin Prince's special cake for the winning side (articleId=1867; articleId=1862 says 'a piece of special cake')", "Scariest monster title for the team with the most frightening dance (articleId=1862)"],
 "evidence": [
  {"claim": "Vampires and Werewolves compete in a Dance Off for the Pumpkin Prince near Bone Bog Cemetery; players wear vampire or werewolf costumes", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1854"},
  {"claim": "The Vampires vs. Werewolves dance-off is part of the Spooktacular event; the Pumpkin Prince judges which side performs the most frightening dance, and that team is crowned scariest monster", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1862"},
  {"claim": "Players pick a side via Madam Zelda in Blackspore, then openly wear costume pieces at Bone Bog Cemetery when the in-game announcement starts the dance-off; side with more fans wins special cake", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1862"},
  {"claim": "Players wear costumes when the in-game 'dance contest is about to begin' announcement appears, then go to the marsh; the side with most fans wins a piece of the Pumpkin Prince's cake (Spanish-language post)", "source": "http://www.freerealms.com/article/detail.action?articleId=1867"},
  {"claim": "Team Werewolf and Team Vampire outfits (Boy and Girl versions) are sold in the Marketplace; this does not show them as dance-off rewards", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"},
  {"claim": "Client announcement: 'The Vampires vs Werewolves Dance-off is about to kick-off in Blackspore!'", "source": "locale:5197"},
  {"claim": "Wiki places the dance-off just outside the gates of Bone Bog Cemetery in Blackspore, hosted by the Pumpkin Prince, during Super Spooktacular", "source": "wiki Blackspore Swamp; wiki Vampires vs. Werewolves Dance-off; wiki Super Spooktacular"},
  {"claim": "In-game announcement appears in several video frames (shows the event existed in-game, not when)", "source": "video:dYq8DkeKGpw/00438.jpg; video:KV8lz53ZyZY/00098.jpg; video:KV8lz53ZyZY/00096.jpg; video:H4v00arihLk/00060.jpg"},
  {"claim": "Client team objectives 'Join Team Vampire!' and 'Join Team Werewolf!' exist", "source": "locale:432207, locale:432208"}
 ],
 "confidence": 0.4,
 "open": [
  "No source gives a year or month for any dance-off run. The articles in the pack (1854, 1862, 1867, 2304) are undated; 1867 says only 'posted 7 months, 2 weeks ago' against a 2011-06-04 capture, and 2304 says 'Posted 4 days, 17 hours ago' against its capture. occurrences stays empty. Do not infer October 2010 or any other month without a dated source.",
  "Parent-event candidate windows to check the dance-off against (these are Super Spooktacular seasons, not dance-off dates, and none is shown to contain the dance-off): 2009-10-14 to 2009-11-11 (Ten Ton Hammer node/75739); October 2010 (articleId=1845); 2013-10-01 to 2013-11-12 (articleId=2949). The wiki Blackspore Swamp page calls Super Spooktacular an 'annual event' and the wiki Eternal Purebloods page dates the dance-off to the 2012 Halloween event, but the wiki is not a dated article. Recurrence stays null until the dance-off itself is dated in two seasons or an article says it recurs.",
  "Zelda location conflict: articles 1857, 1862 and 1878 put Madam Zelda in Blackspore; summaries of 1866 and 1867 place her in Esporaumbria/Shadowbrook (Shadowmoor). No source supports Shadowmoor as a dance-off zone, so it is omitted. Zelda may have moved between seasons, or the articles may come from different years.",
  "The quest title 'Choose Vampires or Werewolves Dance for the Pumpkin King' appears only in article 1862 text ('Visit Madam Zelda in Blackspore to start the quest Choose [Vampires] or [Werewolves] Dance for the Pumpkin King'). It is not a wiki or quest-DB title, so no exact quest title is wired; verify before adding it to quests.",
  "Pre-Emptive Bite is not attributed to an NPC or to this event. The wiki Super Spooktacular page gives Drake Sullenfangs as giver; locale:432236 names Ed Sullenfangs only in dialog; the wiki line for Ed is the separate quest 'Another One Bites the Muck' (locale:432253). Its objective 'Help the vampires sabotage the werewolves' dance practice!' ties to Dance Practice battles, not the dance-off. The on-screen 'quicker the dance-off winner is decided' claim (video S8hbCvXj8Kg) was not verified.",
  "Team T-shirt and outfit locale ids (14688, 14690, 14692, 14694) confirm existence only; the dance-off link rests on the wiki item lists. Prices and currency unknown for all items.",
  "Excluded: LIMITED EDITION Werewolf Outfit (locale:119208; no source ties it to this event); Vampire Bat (wiki only; locale:5087 is an npc_name entry); Vampire and Werewolf Cake Slice (not confirmed as rewards); Jake Blackforest, Pumpkin Prince's Treasure (locale:432069) and Pumpkin Prince cards (locale:9919, 9921) (not tied to the dance-off); the Pumpkin Prince boss fight (not tied by any source).",
  "Possible merge or alias: locale:14564 'Vampires vs. Werewolves Costume Party' (locale:14568 'Wear your best costume to the biggest and most frightening party of the year!') shares the theme but no source ties it to the dance-off. Article 1221 is a separate Blackspore graveyard costume party on 8 April 2010. Treat the costume party as a possibly separate event until an article reads it.",
  "Pack title 'Vampire and werewolf costumes' is a costume-item label, not an event name; dropped. Frame KV8lz53ZyZY/00124 OCRs as 'Shrimpwolves' and was not used.",
  "Live status 'unsure': the event existed in-game (client announcement and video frames) but no source dates a run, so live cannot be set to 'yes'."
 ]}
