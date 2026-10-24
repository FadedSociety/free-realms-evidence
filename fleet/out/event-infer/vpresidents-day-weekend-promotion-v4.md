<!-- fleet job=event-infer id=vpresidents-day-weekend-promotion-v4 status=done turns=3 usd=0.0024 tokens(read,write,in,out)=[14647, 8304, 8, 2334] model=claude-haiku-5-5 -->
# Presidents' Day weekend promotion

{"event": {"name": "Free Realms President's Day weekend sale", "aliases": ["President's Day Sale!", "President's Day sale", "Presidents' Day weekend sale"]},
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "Feb 18 to Feb 21, 2011 (noon Feb 18 to 23:59 PST Feb 21, per the pack; French article gives 21:00 CET Feb 18 to 08:59 CET Feb 22)", "source": "http://www.freerealms.com/article/detail.action?articleId=2043&request_locale=en_US"},
  {"year": 2012, "when": "Feb 17 to Feb 20, 2012 (12:01 AM PST 2/17/12 to 11:59 PM PST 2/20/12)", "source": "locale:1420 ; http://www.freerealms.com:80/article/detail.action?articleId=2528"}
 ],
 "recurring": "Observed on the Presidents' Day weekend in 2011 and 2012 (two occurrences). No article states it recurs, so no yearly rule is claimed. 2013 and 2014 unchecked.",
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy housing and lots at a 50% discount in the Free Realms Marketplace during the sale window"],
 "items": [
  {"name": "Houses and Lots (2012)", "price": "50% off", "currency": "station_cash", "source": "locale:1420"},
  {"name": "Station Cash housing and land items (2011)", "price": "50% off", "currency": "station_cash", "source": "http://www.freerealms.com/article/detail.action?articleId=2043&request_locale=en_US"},
  {"name": "TCG Booster Packs and Starter Decks (2012, discounted)", "price": "not sourced in this pass", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2528 (summary only; locale 615 is flagged not_live and not used)"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "2011: all Station Cash housing and land items were discounted 50% over the Presidents' Day long weekend, starting 18 February 2011.", "source": "http://www.freerealms.com/article/detail.action?articleId=2043&request_locale=en_US"},
  {"claim": "2012: 50% off all Houses and Lots in Free Realms, valid 12:01 AM PST 2/17/12 to 11:59 PM PST 2/20/12, sold in the Marketplace.", "source": "locale:1420"},
  {"claim": "2012 sale window and offer (housing and lots 50% off on the Marketplace, discounted TCG booster packs and starter decks) also appear in article 2528.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2528"},
  {"claim": "The in-game banner name is \"President's Day Sale!\" (locale 614 and 1417 match this text, but both are flagged not_live, so they support the name only).", "source": "locale:614 ; locale:1417"}
 ],
 "confidence": 0.6,
 "open": [
  "Name merge: the pack's name 'Presidents' Day weekend promotion' merges two things. The SOE multi-game Presidents' Day promotion (articles 2033, 2037, 2038; Ten Ton Hammer 95568) is a separate SOE-wide event, not this sale. Article 2037 is a pre-launch preview ('may' include bonus XP days), not a live reward. Bonus XP is not counted as a reward. Those articles have no stated year on the page.",
  "2011 window: I read article 2043 (French) directly. Articles 2039 and 2040, cited by the pack, were not re-read by me, so the noon-to-23:59 PST times are from the pack only.",
  "Live status is inferred from announced windows (announcement texts, not post-event recaps). Moderate confidence.",
  "No named housing items for 2011 are sourced. The 2012 TCG pricing (200 SC boosters, 450 SC starter decks) comes from locale 615, which is flagged not_live, so it is not wired as fact.",
  "Article 2839 (freerealms.com, home decor sale, Feb 16 to 18, 2013 PST, 50% off everything) is a possible 2013 neighbouring housing sale. It is not confirmed as this event. 2013 and 2014 remain unchecked, so no recurrence beyond 2011 and 2012 is claimed.",
  "Zones, NPCs and quests: none sourced. The Marketplace is the store, not a zone. The wiki category was empty in the pack and no quest answers mention the event.",
  "Presidents' Day date varies each year; the dates above are the ones stated in the sources, not calculated."
 ]}
