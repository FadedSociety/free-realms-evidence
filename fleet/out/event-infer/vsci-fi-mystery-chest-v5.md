<!-- fleet job=event-infer id=vsci-fi-mystery-chest-v5 status=done turns=4 usd=0.0034 tokens(read,write,in,out)=[27793, 10028, 10, 3727] model=claude-haiku-5-5 -->
# Sci-Fi Mystery Chest

{"event": {"name": "Sci-Fi Mystery Chest (Mystery Chest Series 2)", "aliases": ["Sci-Fi Mystery Chest", "Mystery Chest Series 2", "Mystery Chests Series 2: Sci-Fi", "Series 2 Mystery Chests: The Sci-Fi"]},
 "kind": "update",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": ["The Truth is Out There", "Beyond the Stars"],
 "activities": ["Open Sci-Fi Mystery Chests (per article 2604 summary: Mystery Key bought in the Marketplace; paraphrase only, not verbatim)", "Earn a UFO from a Sci-Fi Mystery Chest (quest objective)", "Earn Mystery Chests through activities (locale:482: 'Mystery chests can now be earned in different activities')"],
 "items": [
  {"name": "Robo Boombox (wiki: Robot Boombox)", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2604 (summary paraphrase); wiki: Robot Boombox; locale:436616"},
  {"name": "Robotic Chicken (Ride)", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2604 (article sentence: 'you could find a Robo Boombox, Alien clothing, a Robotic Chicken Ride'); wiki: Robotic Chicken (Ride)"},
  {"name": "Flying Saucer (Ride, Members)", "price": null, "currency": null, "source": "wiki: Mystery Chest (Sci-Fi section); wiki: Flying Saucer (Ride); locale:3861; article 2604 summary says Members can get a Flying Saucer ride"},
  {"name": "Alien Mask", "price": null, "currency": null, "source": "wiki: Alien Mask; wiki: Mystery Chest (Sci-Fi section)"},
  {"name": "Alien Pants", "price": null, "currency": null, "source": "wiki: Alien Pants (acquired by opening Sci-Fi Mystery Chests or trade; Category:Mystery Chest); locale:2678"},
  {"name": "Alien Gloves", "price": null, "currency": null, "source": "wiki: Alien Gloves; wiki: Mystery Chest (Sci-Fi section)"}
 ],
 "rewards": ["Robotic Chicken (ride)", "Flying Saucer (ride, Members)", "Robo Boombox", "Alien Mask", "Alien Pants", "Alien Gloves", "UFO (from quest 'Beyond the Stars' objective)"],
 "evidence": [
  {"claim": "The Sci-Fi Mystery Chest 'is here' as client announcement text, tied to the Mystery Chest rule change (undated)", "source": "locale:482"},
  {"claim": "Article 2604 is a 'What is New?' news post announcing the Sci-Fi 'Mystery Chest Series 2' loot release; its date is null, so no year or month is stated by the article", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2604"},
  {"claim": "Article 2604 headline: 'Mystery Chest Series 2 items are here, and they're out of this world!'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2604"},
  {"claim": "Article 2604 sentence: 'you could find a Robo Boombox, Alien clothing, a Robotic Chicken Ride'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2604 (fact:item)"},
  {"claim": "Wiki Mystery Chest page: the original limit was one chest per day, changed to one per hour per character, and 'The limit was later lifted upon introduction of the Series 2 Mystery Chests: The Sci-Fi'. This conflicts with the summary's daily-earning paraphrase and is recorded as the controlling wiki statement for the earning rule", "source": "wiki: Mystery Chest (page:ns0)"},
  {"claim": "Quest 'The Truth is Out There' has objective 'Open a Sci-Fi Mystery Chest.' (title locale:441427, objective locale:441428; 441430 is a duplicate)", "source": "locale:441428"},
  {"claim": "Quest 'Beyond the Stars' has objective 'Earn a UFO from a Sci-Fi Mystery Chest.' (title locale:441458, objective locale:441459; 441461 is a duplicate)", "source": "locale:441459"},
  {"claim": "Alien Pants is a Freestyle Jobs legs item acquired by opening Sci-Fi Mystery Chests or trade", "source": "wiki: Alien Pants; locale:2678"},
  {"claim": "Mystery Chest Sci-Fi section lists Flying Saucer opportunity, Alien Mask, Alien Gloves and Robot Boombox", "source": "wiki: Mystery Chest (Sci-Fi section)"}
 ],
 "confidence": 0.4,
 "open": [
  "Date: no article-dated occurrence. Article 2604 has date null (only relative 'Posted 3 days, 19 hours ago'). The OCR '7/23/2012' on video:e4XXSnnive0/00024.jpg is a menu/clock candidate only and is not used. Needs an archive date. Series 3 Clockwork articles (captured 2012-11-03) would only bound this release as earlier.",
  "Live: unsure. Client text (locale:482) and menu frames (video:e4XXSnnive0/00022.jpg, 00024.jpg) show the content existed in a build, but no dated source confirms when it was live.",
  "Earning rule unresolved. The 'one chest a day' rule was only a paraphrase of article 2604 and is dropped. The wiki says the limit was lifted with Series 2; locale:482 says the daily limit was removed; locale:690 says no daily limit; locale:436404 says 1 per hour (undated). locale:637 is FLAGGED not_live and is NOT used as evidence.",
  "Bandit Hideout frame video:9gfkEIFMV4s/00236.jpg is NOT cited: the lookup did not return that frame and the chest receipt is unverified. Not a drop-rate claim.",
  "Mystery Key (bought in Marketplace) appears only in the article 2604 summary paraphrase; price unknown; sale-event Mystery Key strings (locale:28240, 28241, 33689) and article 2611 do not tie to this release.",
  "Article 2604 verbatim text is only the headline and one item sentence; the rest of the item and ride list is from the summary and wiki.",
  "Alien Shirt and Alien Shoes appear in the wiki Sci-Fi list and video:XtvRqM7RejE/00302.jpg, but no item page was found, so they are excluded from items.",
  "Kind 'update' is a judgement (news post). 'promotion' is possible.",
  "Pack merged events: Series 1 (Original), Series 3 Clockwork (articles 2721, 2724, 2728), seasonal Snow Days, and the Mechanical chest teaser (article 2722) are separate and excluded. Article 2921 (Boombox effects) is not this event.",
  "Alias gap: article says 'Robo Boombox', wiki says 'Robot Boombox'; treated as one item.",
  "Zones and NPCs: none sourced for this event. Bandit Hideout is a single frame and is not enough to list as an event zone.",
  "Lookup of hyphenated 'Sci-Fi' terms in wiki/articles returned FTS5 errors; wiki and article coverage is partial."
 ]
}
