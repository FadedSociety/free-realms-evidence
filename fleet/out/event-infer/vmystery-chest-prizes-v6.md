<!-- fleet job=event-infer id=vmystery-chest-prizes-v6 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[7498, 8170, 6, 2940] model=claude-haiku-5-5 -->
# Mystery Chest prizes

{
 "event": {
  "name": "Clockwork Mystery Chest (Series 3: Clockwork)",
  "aliases": [
   "Clockwork Mystery Chest",
   "Mystery Chest Series 3: Clockwork (locale:3862)",
   "Spanish article title 'Cofres Misteriosos Mecánicos' (articleId=2729; not a confirmed client alias)",
   "German 'Uhrwerk-Geheimnis-Truhen' (articleId=2724)",
   "Portuguese 'Baú Misterioso do Relógio' (articleId=2731)"
  ]
 },
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [
  "Clockto Awkto (title confirmed by locale:441463; objective 'Earn a Clocktopus from a Clockwork Mystery Chest' at locale:441464)"
 ],
 "activities": [
  "Open a Clockwork Mystery Chest bought with a Mystery Key from the Marketplace (locale:19048, locale:19049)",
  "Earn a Clocktopus from a Clockwork Mystery Chest (locale:441464)",
  "Dance on the clockwork gear in the game (promotional text only, articleId=2728 fact:event; not an in-game-verified activity)"
 ],
 "items": [
  {
   "name": "Clockwork Mystery Chest",
   "price": null,
   "currency": null,
   "source": "locale:19048, locale:19049 (needs a Mystery Key from the Marketplace; key price not in pack)"
  },
  {
   "name": "Clocktopus (Clockwork Octopus ride)",
   "price": null,
   "currency": "reward",
   "source": "locale:944; http://www.freerealms.com:80/article/detail.action?articleId=2721"
  },
  {
   "name": "Clockwork gear (wearable)",
   "price": null,
   "currency": "reward",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2721 (fact:event)"
  }
 ],
 "rewards": [
  "Clocktopus ride; members given a special opportunity to get it (locale:944)",
  "Clockwork gear wearable in-game (articleId=2721)"
 ],
 "evidence": [
  {"claim": "Chest is named 'Series 3: Clockwork' in the client", "source": "locale:3862"},
  {"claim": "Client text: 'The latest Mystery Chest is here... Clockwork Mystery Chest... members have a special opportunity at getting Clocktopus, the Clockwork Octopus ride' (undated)", "source": "locale:944"},
  {"claim": "A Mystery Key is needed to open the chest; Mystery Keys are bought on the Marketplace", "source": "locale:19049"},
  {"claim": "Quest title 'Clockto Awkto' confirmed", "source": "locale:441463"},
  {"claim": "Quest objective 'Earn a Clocktopus from a Clockwork Mystery Chest'", "source": "locale:441464"},
  {"claim": "Clockwork gear wearable in-game; Clocktopus reward", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2721"},
  {"claim": "German article announces Clockwork Mystery Chests featuring Chris and Lola", "source": "http://www.freerealms.com/article/detail.action?articleId=2724"},
  {"claim": "Portuguese promo: rewards earnable in-game via the site", "source": "http://www.freerealms.com/article/detail.action?articleId=2731"},
  {"claim": "Spanish blurb: dance on the clockwork gear in game (promo only); prizes can be won at freerealms.com, no odds or details", "source": "http://www.freerealms.com/article/detail.action?articleId=2728 (fact:event); http://www.freerealms.com/article/detail.action?articleId=2729"},
  {"claim": "Robgoblin Treasure Trove: a Clockwork chest was received there (world tag only)", "source": "video:qCG_K2piQgE/00162.jpg; video:qCG_K2piQgE/00164.jpg (frame text not re-verified)"}
 ],
 "confidence": 0.35,
 "open": [
  "No dated source. No article gives a year or month. Capture dates (2012-11-03) and 'two months, one week ago' are not event dates. occurrences is empty, recurring is null, and live is unsure.",
  "Quest 'Snowhill Clockworker' is NOT confirmed: locale:441446 reads 'Clockworker', not 'Snowhill Clockworker'. locale:441447 (objective 'Open a Clockwork Mystery Chest') is tagged with the name 'Snowhill Clockworker' by lookup, but no source confirms that full title. Left out of quests until checked.",
  "Pack title 'Mystery Chest prizes' merged this event with the general Mystery Chest series (articleId=2604: Original, Sci-Fi Series 2, Snow Days, New Holiday chest). Those are separate events; the pack title is not used as an alias.",
  "'Series 3' collides with the TCG 'Series 3' set (Clockwork Beetle, articleId=2405 / locale:389). Excluded.",
  "Clockwork Hoverboard (articleId=1477, Station Cash Marketplace) is not tied to the chest. Excluded.",
  "Wiki items (Clockwork Head, Torso, Legs, Feet, Hands, Horse, Boombox, Monkey Kit) were removed from items and rewards: the pack quotes no acquisition text tying them to this chest. Needs a source quoting the wiki acquisition sentence before re-adding.",
  "Prices and drop odds: no source gives the chest price, the Mystery Key price, or odds. All prices are null.",
  "Chris and Lola appear only in promotional articles (2724, 2729, 2721, 2731). No in-game source, so npcs is empty.",
  "Robgoblin Treasure Trove zone rests on video frames 00162 and 00164, not re-verified here; zones left empty.",
  "Dance activity is promotional text only (articleId=2728); the Spanish-article-title alias is kept as a title only, not a confirmed client alias.",
  "Article 2731 reads as a live promotion, but it is undated, so live status is unsure."
 ]
}
