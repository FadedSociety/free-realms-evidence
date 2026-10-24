<!-- fleet job=event-infer id=vrio-cloud-jumps-rio-wolkenspr-nge-v6 status=done turns=4 usd=0.0025 tokens(read,write,in,out)=[21084, 7688, 10, 2676] model=claude-haiku-5-5 -->
# Rio Cloud Jumps (Rio Wolkensprünge)

{"event": {"name": "Rio Cloud Jumps (Cloud World daily)", "aliases": ["Rio Cloudjumps", "Rio Cloudjumper (article 1637 wording; not confirmed as a name)", "Rio Wolkensprünge (German, article 1689)", "Cloudy Days (name of the daily quest, not the event)"]},
 "kind": "other",
 "live": "unsure",
 "occurrences": [
  {"year": 2010, "when": "Return of Rio as a daily activity, July 22 (year and day come from the articles index summary only; page date fields are null)", "source": "http://www.freerealms.com/article/detail.action?articleId=1692&request_locale=en_US"},
  {"year": null, "when": "Introduction as a new Daily Activity in an update whose index summary is undated; may be the July 2010 patch. Not confirmed.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1637"},
  {"year": 2014, "when": "January 17, 2014 last-seen note: Game Update 125.1 reduced coin rewards and spawn locations for the Cloud World daily. Not a start date.", "source": "wiki Template:News (Game Update 125.1 Overview 01/17/2014)"}
 ],
 "recurring": "Daily, per articles 1692 and 1689 ('every day'). No reset time or end date in the pack, so not schedulable yet.",
 "zones": ["Sanctuary (article 1692, English)", "Freistatte (article 1689, German; same hill above the Royal Vault, treated as the same place)", "Cloud World (dimension entered through Rio; wiki 'Cloud World')"],
 "npcs": ["Rio Cloudjumps"],
 "quests": ["Cloudy Days (locale:430168 confirmed as the text 'Cloudy Days'; wiki 'Rio Cloudjumps' names it as the daily quest)"],
 "activities": ["Talk to Rio daily to warp to the Cloud World (locale:430216)", "Gather coins from the Cloud World (locale:430213)", "Help Rio clear overflowing clouds through the Cloudy Days daily (wiki 'Rio Cloudjumps'; locale:430168)"],
 "items": [{"name": "Cloud World coins", "price": null, "currency": "reward", "source": "video:e4XXSnnive0/00272.jpg ('You receive 1 coin'); locale:430213"}],
 "rewards": ["1 coin per Cloud World pickup (video:e4XXSnnive0/00272.jpg)"],
 "evidence": [
  {"claim": "Rio Cloudjumps returned as a daily activity; members can talk to him every day and help collect Cloud World coins; he is on the hill above the royal vault.", "source": "http://www.freerealms.com/article/detail.action?articleId=1692&request_locale=en_US"},
  {"claim": "German version of the same return: members can visit daily to collect Cloud World coins.", "source": "http://www.freerealms.com/article/detail.action?articleId=1689"},
  {"claim": "Rio is removing overflowing clouds; players collect coins from the Cloud World through the daily quest Cloudy Days.", "source": "wiki page 'Rio Cloudjumps'; locale:430168"},
  {"claim": "An update index summary says it adds a daily activity from Rio Cloudjumper above the royal vaults.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1637"},
  {"claim": "Game Update 125.1 (01/17/2014) adjusted the Cloud World daily instance.", "source": "wiki Template:News (Game Update 125.1 Overview 01/17/2014)"}
 ],
 "confidence": 0.5,
 "open": [
  "Start date not sourced. The 2010 year and the July 22 day rest on the index summary of articleId=1692; its date field is null. The July 15, 2010 introduction claimed in the critique is not confirmed: the only lookup hit is article 1637's summary, which has no date here. Do not state July 15.",
  "End date unknown. Last seen January 17, 2014 (last-seen note, not a start).",
  "Coin Clean-up (locale:430164; dialog locale:430163, 430167) is a separate story quest chain about clouds and Cloud World coins. Not tied to the daily window by any source here; not listed as a quest of this event. Its locale title was not re-checked in this pass.",
  "Merge risk: Cloudy Days (daily quest per wiki) and Coin Clean-up may be one activity or two. The pack does not settle it.",
  "'Rio Cloudjumper' is the name in article 1637's summary; not confirmed as a player-facing name. 'Cloud World daily instance' is not a sourced name.",
  "The July 22 update's monkey pets, saber-tooth mount and housing items are not tied to Rio in any source; excluded.",
  "The free warp (locale:430216) is a dialog hint, not a reward; listed under activities.",
  "No station cash or priced items are tied to this event. quest_answers_mentioning_it is empty.",
  "Recurrence is not schedulable: no reset time or window. Wireable only as 'daily, no window'."
 ]}
