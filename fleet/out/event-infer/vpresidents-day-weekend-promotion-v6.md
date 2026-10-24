<!-- fleet job=event-infer id=vpresidents-day-weekend-promotion-v6 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[13068, 7648, 8, 2258] model=claude-haiku-5-5 -->
# Presidents' Day weekend promotion

{
 "event": {
  "name": "Free Realms Presidents' Day weekend sale",
  "aliases": ["Presidents' Day weekend sale", "Presidents' Day sale"]
 },
 "kind": "promotion",
 "live": "yes",
 "occurrences": [
  {"year": 2011, "when": "Feb 18, 2011 (noon) to Feb 21, 2011 (23:59 PST), Presidents' Day weekend", "source": "http://www.freerealms.com/article/detail.action?articleId=2039 ; http://www.freerealms.com/article/detail.action?articleId=2040"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Buy Station Cash housing items and building lots at 50% off during the 2011 sale window"
 ],
 "items": [
  {"name": "Station Cash housing items (category; no named items sourced)", "price": "50% off", "currency": "station_cash", "source": "http://www.freerealms.com/article/detail.action?articleId=2039 ; http://www.freerealms.com/article/detail.action?articleId=2040 (2011)"},
  {"name": "Building lots (category; no named items sourced)", "price": "50% off", "currency": "station_cash", "source": "http://www.freerealms.com/article/detail.action?articleId=2039 ; http://www.freerealms.com/article/detail.action?articleId=2040 (2011)"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "2011: Free Realms ran a Presidents' Day weekend sale in which all Station Cash housing items and building lots were 50% off.", "source": "http://www.freerealms.com/article/detail.action?articleId=2039 ; http://www.freerealms.com/article/detail.action?articleId=2040"},
  {"claim": "The 2011 sale began at noon on February 18 and ended at 23:59 PST on February 21, 2011 (article facts for 2039 and 2040).", "source": "http://www.freerealms.com/article/detail.action?articleId=2039 ; http://www.freerealms.com/article/detail.action?articleId=2040"},
  {"claim": "2012 (probable, matched by window only, not named): a client string offers 50% off all Houses and Lots in Free Realms, 'This weekend only', valid 12:01 AM PST 2/17/12 to 11:59 PM PST 2/20/12. It does not name Presidents' Day or the sale, and it does not state a currency. Not counted as a confirmed occurrence.", "source": "locale:1420"},
  {"claim": "The SOE-wide Presidents' Day promotion (offers across several SOE games, starting Feb 18) is a separate multi-game event. Article 2037 is a pre-launch preview with no year, so it is not counted as a live occurrence of this Free Realms sale.", "source": "http://www.freerealms.com/article/detail.action?articleId=2037"}
 ],
 "confidence": 0.4,
 "open": [
  "Name merge: the pack's name 'Presidents' Day weekend promotion' merges this Free Realms sale with the SOE-wide multi-game Presidents' Day promotion (articles 2033, 2037, 2038; Ten Ton Hammer 95568). They are treated as separate events here.",
  "Recurrence is not established: only 2011 is sourced by name. The 2012 window (locale:1420) is an unnamed match. No source states the sale recurs, so recurring is null.",
  "2013 and 2014 unchecked. A possible neighbouring housing sale (article 2839, Feb 16 to 18, 2013, home decor 50% off) is not confirmed as this event.",
  "Live status 'yes' rests on the 2011 announced window, not a post-event recap. Confidence is moderate.",
  "Named housing items, lots, prices beyond 50% off, and any NPCs, zones, quests or rewards are not sourced. The item list is categories only.",
  "Marketplace as the sale location is sourced only for 2012 (locale:1420), not for 2011.",
  "Locales 614 and 1417 ('President's Day Sale!') are flagged not_live and are not used as aliases or evidence.",
  "TCG Booster Packs and Starter Decks (2012 discount) dropped: the only source is an unverified summary (article 2528), and locale 615 is flagged not_live.",
  "Article 2043 dropped as a citation (not re-read)."
 ]
}
