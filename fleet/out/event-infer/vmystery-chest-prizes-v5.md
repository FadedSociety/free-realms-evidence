<!-- fleet job=event-infer id=vmystery-chest-prizes-v5 status=done turns=2 usd=0.0028 tokens(read,write,in,out)=[8072, 9873, 6, 3060] model=claude-haiku-5-5 -->
# Mystery Chest prizes

{
 "event": {"name": "Clockwork Mystery Chest (Series 3: Clockwork)", "aliases": ["Clockwork Mystery Chest", "Mystery Chest | Series 3: Clockwork (locale:3862)", "Mechanical Mystery Chest (articles 2728, 2729)", "Uhrwerk-Geheimnis-Truhen (German, article 2724)", "Baú Misterioso do Relógio (Portuguese, article 2731)"]},
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": ["Robgoblin Treasure Trove (world tag only; place a chest was received, not a confirmed event location): video:qCG_K2piQgE/00162.jpg"],
 "npcs": [],
 "quests": ["Snowhill Clockworker (quest_title per earlier pack at locale:441446; objective 'Open a Clockwork Mystery Chest' at locale:441447; the lookup tool shows 441447 tagged with this name, so the title is consistent but the id tagging should be rechecked)", "Clockto Awkto (locale:441463 quest_title; objective 'Earn a Clocktopus from a Clockwork Mystery Chest' at locale:441464)"],
 "activities": ["Open Clockwork Mystery Chests bought with a Mystery Key from the Marketplace (locale:19049)", "Earn Clocktopus from a chest (locale:441464; article 2721)", "Dance on the clockwork gear in the game (Spanish blurb, article 2729)", "Receive a Clockwork Mystery Chest as a reward in Robgoblin Treasure Trove (video:qCG_K2piQgE/00164.jpg)"],
 "items": [
  {"name": "Clockwork Mystery Chest", "price": null, "currency": null, "source": "locale:19048, locale:19049 (requires a Mystery Key bought on the Marketplace; key price not in pack)"},
  {"name": "Clockwork Head / Torso / Legs / Feet / Hands", "price": null, "currency": "reward", "source": "Wiki pages Clockwork Head, Clockwork Torso, Clockwork Legs, Clockwork Feet; locale:8769, 8773, 8777, 8775, 8771 (wiki acquisition sentences not quoted in pack; treat as unverified)"},
 {"name": "Clockwork Horse (ride)", "price": null, "currency": "reward", "source": "Wiki page Clockwork Horse; locale:8779 (unverified acquisition text)"},
  {"name": "Clockwork Boombox", "price": null, "currency": "reward", "source": "Wiki page Clockwork Boombox; locale:19018 (unverified acquisition text)"},
  {"name": "Clockwork Monkey Kit", "price": null, "currency": "reward", "source": "Wiki page Clockwork Monkey; locale:19044 (unverified acquisition text)"},
  {"name": "Clocktopus (Clockwork Octopus ride)", "price": null, "currency": "reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2721 (fact:item); locale:944"}
 ],
 "rewards": ["Clockwork gear wearable in-game (articleId=2721, fact:event)", "Clocktopus ride, members given a special opportunity (articleId=2721; locale:944)", "Clockwork clothing, horse ride, boombox, monkey kit (wiki pages, unverified text)", "Prizes can be won at freerealms.com (Spanish promo, articleId=2729; no details or odds)"],
 "evidence": [
  {"claim": "The chest is named 'Series 3: Clockwork' in the client beside other chest series", "source": "locale:3862"},
  {"claim": "Client text calls it 'the latest Mystery Chest' and says members have a special opportunity at getting Clocktopus; no date given", "source": "locale:944"},
  {"claim": "Mystery Key from the Marketplace is required to open the chest", "source": "locale:19049"},
  {"claim": "Clockwork gear is wearable in-game; rewards are clockwork gear", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2721 (fact:event)"},
  {"claim": "SOE announced Clockwork Mystery Chests featuring Chris and Lola (German)", "source": "http://www.freerealms.com/article/detail.action?articleId=2724 (fact:item)"},
  {"claim": "Portuguese promotion for the Clock Mystery Chest, players can earn rewards in-game via the site", "source": "http://www.freerealms.com/article/detail.action?articleId=2731 (fact:economy)"},
  {"claim": "Spanish promo: players can dance on the clockwork gear in the game and win prizes at freerealms.com; no odds", "source": "http://www.freerealms.com/article/detail.action?articleId=2729"},
  {"claim": "Quest objectives tie the chest to Clocktopus and to opening the chest", "source": "locale:441447; locale:441464 (duplicates 441448, 441449, 441465, 441466 are FLAGGED and not counted)"},
  {"claim": "Robgoblin Treasure Trove world tag where a Clockwork chest was received", "source": "video:qCG_K2piQgE/00162.jpg; video:qCG_K2piQgE/00164.jpg"}
 ],
 "confidence": 0.4,
 "open": [
  "No dated source. No article gives a year or month. Article captures dated 2012-11-03 are capture dates, and 'two months, one week ago' is relative. occurrences is empty and recurring is null.",
  "Live status is unsure. Locale:944 and a video frame show the chest was current at capture, but neither is dated. Article 2731 (Portuguese) reads as a live promotion, but its date is also unknown.",
  "Pack title 'Mystery Chest prizes' merged this event with the general Mystery Chest series (article 2604: Original, Sci-Fi Series 2, Snow Days, New Holiday chest). Those are separate events and the pack title is not used as an alias.",
  "Series 3 alias collides with the TCG 'Series 3' set (Clockwork Beetle, from a Sunstone Valley TCG loot card, article 2405 / locale:389). Excluded.",
  "Clockwork Hoverboard (article 1477, Station Cash Marketplace) is not tied to the chest. Excluded.",
  "Prices and odds: no source gives a chest price, the Mystery Key price, or drop odds. All item prices are null.",
  "Wiki acquisition claims for clothing, horse, boombox and monkey kit are cited to wiki page titles and locale ids; the acquisition sentences themselves were not quoted in the pack, so they are unverified.",
  "NPCs Chris and Lola appear only in promotional articles (2724, 2729, 2721, 2731). No in-game source, so npcs is empty.",
  "Quest 'Snowhill Clockworker': the pack's quest_title source is locale:441446, but the lookup tool tags 441447 with this name and the ids check tags them as 'Clockworker'. The full title is not independently confirmed by a single unambiguous source.",
  "Article 2728's own text says the client-name link is not confirmed by the article; it is used only as corroboration of the feature."
 ]
}
