<!-- fleet job=event-infer id=vrio-cloud-jumps-rio-wolkenspr-nge-v5 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[7542, 8583, 6, 2263] model=claude-haiku-5-5 -->
# Rio Cloud Jumps (Rio Wolkensprünge)

{
 "event": {"name": "Rio Cloud Jumps (Cloud World daily)", "aliases": ["Rio Cloud Jumps", "Rio Wolkensprünge", "Rio Cloudjumps", "Cloudy Days (daily quest name, per wiki)"]},
 "kind": "other",
 "live": "unsure",
 "occurrences": [
  {"year": 2010, "when": "July 22 (return of Rio as a daily activity). Year is index-sourced only; the article's date field is null in the pack, so unconfirmed.", "source": "http://www.freerealms.com/article/detail.action?articleId=1692&request_locale=en_US"},
  {"year": 2014, "when": "January 17, 2014 - last-seen note: Game Update 125.1 'Reduced coin rewards and spawn locations for Cloud World daily instance'. Not a start date; shows the instance still being tuned then.", "source": "wiki Template:News (Game Update 125.1 Overview 01/17/2014)"}
 ],
 "recurring": "Daily, per articles ('members can talk to him every day'). No reset time or end date in the pack, so not schedulable yet.",
 "zones": ["Sanctuary (article 1692, English)", "Freistatte (article 1689, German; same hill above the Royal Vault, treated as the same place)", "Cloud World (dimension entered through Rio; wiki 'Cloud World')"],
 "npcs": ["Rio Cloudjumps"],
 "quests": ["Cloudy Days (locale:430168; named as the daily quest on wiki 'Rio Cloudjumps')", "Coin Clean-up (locale:430164; dialog locale:430163, 430167). Separate quest chain; the pack does not tie it to the daily window."],
 "activities": ["Talk to Rio daily to warp to the Cloud World (locale:430216)", "Gather loose coins in the Cloud World before time runs out (locale:430213, 430215; the Coin Clean-up objective per the critique's video frames video:e4XXSnnive0/00252.jpg, 00272.jpg, not re-checked here)", "Help Rio clear the cloud overload (Cloudy Days, locale:430169)"],
 "items": [{"name": "Cloud World coins", "price": null, "currency": "reward", "source": "video:e4XXSnnive0/00272.jpg ('You receive 1 coin'); locale:430213"}],
 "rewards": ["1 coin per Cloud World pickup (video:e4XXSnnive0/00272.jpg)"],
 "evidence": [
  {"claim": "Rio Cloudjumps returned as a daily activity; members can talk to him every day and pick up Cloud World coins; he is on the hill above the royal vault.", "source": "http://www.freerealms.com/article/detail.action?articleId=1692&request_locale=en_US"},
  {"claim": "Same return in German; members can visit daily to collect Cloud World coins.", "source": "http://www.freerealms.com/article/detail.action?articleId=1689"},
  {"claim": "Rio is removing overflowing clouds; players help by collecting coins from the Cloud World through the daily quest Cloudy Days.", "source": "wiki page 'Rio Cloudjumps'; locale:430168"},
  {"claim": "Cloud World pickups are worded 'Gather coins from the Cloud World' and 'See Rio Cloudjumps to warp to the Cloud World'.", "source": "locale:430213; locale:430216"},
  {"claim": "Game Update 125.1 (01/17/2014) adjusted the Cloud World daily instance.", "source": "wiki Template:News (Game Update 125.1 Overview 01/17/2014)"}
 ],
 "confidence": 0.5,
 "open": [
  "Start date: the first run is not sourced. The 2010 year rests only on the articles index summary for articleId=1692; the page's date field is null. Articles 1637, 1639 and 1644 describe an earlier Rio daily but have null dates.",
  "End date unknown. 'Live' is last seen Jan 17, 2014; no later source in the pack.",
  "articleId=1687 ('every day') was not retrievable in this check; not cited as evidence.",
  "Merge risk: Cloudy Days (daily quest per wiki) and Coin Clean-up (story quest, locale:430163/430167, with the same coin pickup) may be one activity or two. The pack does not settle it. Coin Clean-up is listed as a separate chain with no schedule.",
  "Aliases 'Rio Cloudjumper' and 'Cloud World daily instance' are not sourced as names and were dropped.",
  "The July 22 update's monkey pets, saber-tooth mount and housing items are not tied to Rio in any source; excluded.",
  "No station cash or priced items are tied to this event.",
  "quest_answers_mentioning_it is empty in the pack."
 ]
}
