<!-- fleet job=event-infer id=vvampire-and-werewolf-costumes-v4 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[8285, 9509, 6, 3406] model=claude-haiku-5-5 -->
# Vampire and werewolf costumes

{
 "event": {"name": "Vampires vs. Werewolves Dance-off", "aliases": ["Vampires vs Werewolves Dance-off", "Vampire vs. Werewolf Dance Off", "Super Spooktacular dance-off (Pumpkin Prince)"]},
 "kind": "community",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": ["Blackspore Swamp (Bone Bog Cemetery, outside its gates)"],
 "npcs": ["Madam Zelda (starts the side-choice quest)", "Pumpkin Prince (judges the dance-off)"],
 "quests": ["Choose Vampires or Werewolves Dance for the Pumpkin King (title taken from article text only; verify before wiring)"],
 "activities": [
  "Choose a side (Vampires or Werewolves) via Madam Zelda",
  "Wear Team Vampire or Team Werewolf costume pieces when the in-game 'dance contest is about to begin' announcement appears",
  "Go to Bone Bog Cemetery / Blackspore marsh to take part in the dance-off",
  "Side with the most fans wins a piece of the Pumpkin Prince's cake; the most frightening team is crowned scariest monster"
 ],
 "items": [
  {"name": "Team Vampire T-Shirt", "price": null, "currency": null, "source": "locale:14692; wiki Vampires vs. Werewolves Dance-off (team item list)"},
  {"name": "Team Werewolf T-Shirt", "price": null, "currency": null, "source": "locale:14694; wiki Vampires vs. Werewolves Dance-off (team item list)"},
  {"name": "Vampire Outfit", "price": null, "currency": null, "source": "locale:14688 (existence only); wiki Vampires vs. Werewolves Dance-off (team item list)"},
  {"name": "Werewolf Outfit", "price": null, "currency": null, "source": "locale:14690 (existence only); wiki Vampires vs. Werewolves Dance-off (team item list)"}
 ],
 "rewards": ["Piece of the Pumpkin Prince's cake for the winning side (article 1867)", "Scariest monster title for the winning team (article 1862)"],
 "evidence": [
  {"claim": "Vampires and Werewolves compete in a Dance Off for the Pumpkin Prince near Bone Bog Cemetery; players wear vampire or werewolf costumes", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1854"},
  {"claim": "The Vampires vs. Werewolves dance-off is part of the Spooktacular event; the Pumpkin Prince judges which side performs the most frightening dance", "source": "http://www.freerealms.com/article/detail.action?articleId=1862"},
  {"claim": "Players pick a side via Madam Zelda, then wear costume pieces when the in-game announcement starts at Bone Bog Cemetery", "source": "http://www.freerealms.com/article/detail.action?articleId=1862"},
  {"claim": "Players wear costumes when the in-game 'dance contest is about to begin' announcement appears, then go to the marsh; side with most fans wins a piece of the Pumpkin Prince's cake (Spanish-language post)", "source": "http://www.freerealms.com/article/detail.action?articleId=1867"},
  {"claim": "Boy and Girl Team Werewolf and Team Vampire outfits are sold in the Marketplace", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"},
  {"claim": "Client announcement: 'The Vampires vs Werewolves Dance-off is about to kick-off in Blackspore!'", "source": "locale:5197"},
  {"claim": "Blackspore wiki places the dance-off just outside the gates of Bone Bog Cemetery, hosted by the Pumpkin Prince, during Super Spooktacular", "source": "wiki Blackspore Swamp; wiki Vampires vs. Werewolves Dance-off"},
  {"claim": "In-game announcement appears in several video frames (live existence, not date)", "source": "video:dYq8DkeKGpw/00438.jpg; video:KV8lz53ZyZY/00098.jpg; video:KV8lz53ZyZY/00096.jpg; video:H4v00arihLk/00060.jpg"},
  {"claim": "Client team objectives 'Join Team Vampire!' and 'Join Team Werewolf!' exist", "source": "locale:432207, locale:432208"}
 ],
 "confidence": 0.4,
 "open": [
  "No source gives a year or month. Articles 1854, 1862, 1867, 2304 carry no date in the pack (1867 only says 'posted 7 months, 2 weeks ago' against a 2011-06-04 capture). occurrences is empty; do not infer October 2010 without a dated source.",
  "Recurrence: the wiki Blackspore Swamp page calls Super Spooktacular an 'annual event', but a wiki page is not an article, and only one dated season is evidenced. recurring stays null until two dated occurrences or an article saying it recurs.",
  "Pre-Emptive Bite is NOT attributed to an NPC here. The wiki Super Spooktacular page gives Drake Sullenfangs as its giver; locale:432236 names Ed Sullenfangs only in dialog pointing to him; the wiki line for Ed is the separate quest 'Another One Bites the Muck' (locale:432253). Giver unresolved. Pre-Emptive Bite is also not listed as a dance-off quest: its objective ('Help the vampires sabotage the werewolves' dance practice!') ties to the Dance Practice battles, and the on-screen 'quicker the dance-off winner is decided' claim (video S8hbCvXj8Kg frames) was not verified.",
  "Article 1854's 'Spooktacular season' link is not in its quoted fact; the season tie is taken from article 1862 instead.",
  "Team T-shirt and outfit locale ids (14688, 14690, 14692, 14694) confirm existence only. The dance-off link rests on the wiki item lists. Article 2304 says the outfits are sold in the Marketplace, so they are not shown to be dance-off rewards. Prices unknown for all items.",
  "LIMITED EDITION Werewolf Outfit (locale:119208) excluded: no source ties it to this event. Vampire Bat is wiki-only (locale:5087 is an npc_name entry). Vampire and Werewolf Cake Slice items are not confirmed as rewards by a re-read source.",
  "Location conflict: articles 1857/1878 put Madam Zelda at Blackspore; the summaries of 1866/1867 put her at Esporaumbria (Shadowmoor). No source supports Shadowmoor as a dance-off zone, so it is omitted. Zelda may have moved between seasons or the articles may be from different years.",
  "Possible merge or alias: locale:14564 'Vampires vs. Werewolves Costume Party' (locale:14568 'Wear your best costume to the biggest and most frightening party of the year!') shares the theme but no source ties it to the dance-off. Article 1221 is a separate Blackspore graveyard costume party on 8 April 2010. Treat the costume party as a possibly separate event until an article reads it.",
  "Live status 'unsure': the client announcement and video frames show the event existed in-game, but no source dates it. Frame KV8lz53ZyZY/00124 OCRs as 'Shrimpwolves' and was not used.",
  "The pack title 'Vampire and werewolf costumes' is a costume-item label, not an event name; dropped. The Pumpkin Prince boss fight is not tied to the dance-off by any source; excluded. Jake Blackforest, Pumpkin Prince's Treasure (locale:432069) and Pumpkin Prince cards (locale:9919, 9921) are not tied to the dance-off; excluded.",
  "Quest title 'Choose Vampires or Werewolves Dance for the Pumpkin King' comes from article 1862 text, not a wiki quest page or quest DB. Verify the exact title before wiring."
 ]
}
