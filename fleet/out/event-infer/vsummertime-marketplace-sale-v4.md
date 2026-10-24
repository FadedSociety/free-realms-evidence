<!-- fleet job=event-infer id=vsummertime-marketplace-sale-v4 status=done turns=2 usd=0.0020 tokens(read,write,in,out)=[6439, 7152, 6, 2112] model=claude-haiku-5-5 -->
# Summertime Marketplace Sale

{
 "event": {"name": "Summertime Marketplace Sale", "aliases": []},
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [
  {"year": 2009, "when": "early July (4th of July promotion); exact day not stated in the article, inferred as 2009-07-03 from a relative 'Posted 3 days, 23 hours ago' stamp", "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"}
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buying the featured SC Marketplace items on sale"],
 "items": [
  {"name": "Uncle Sam Outfit (locale:151336)", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=142 (fact: 'An Uncle Sam suit was featured on sale in the SC Marketplace')"},
  {"name": "Fireworks Crate (locale:394790)", "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=142 (fact: place it on the ground to deliver exclusive fireworks on demand)"}
 ],
 "rewards": [],
 "evidence": [
  {"claim": "Official news post announces a Summertime sale of 'fabulous deals' on the SC Marketplace; quoted line: 'Some fabulous deals just hit the SC Marketplace!'", "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"},
  {"claim": "Article 142 features an Uncle Sam suit on sale in the SC Marketplace ('see how your character would look in an Uncle Sam suit!'), tying Uncle Sam Outfit (locale:151336) to this sale", "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"},
  {"claim": "Article 142 describes the Fireworks Crate: placed on the ground, it delivers exclusive fireworks on demand ('You can place it on the ground and have it deliver exclusive fireworks on demand!')", "source": "http://www.freerealms.com:80/article/detail.action?articleId=142"},
  {"claim": "Client name for the Fireworks Crate is 'Fireworks Crate'", "source": "locale:394790"},
  {"claim": "The 4th of July tie-in is stated in the pack's author-written article summary, not in quoted article text", "source": "pack article_summaries, articleId=142"},
  {"claim": "Uncle Sam Outfit is also attributed to Seaside Summer Splash (began 2 July 2009) in article 137, and the wiki Template:News mentions the Uncle Sam Outfit on the Welcome Screen; these overlap with this sale", "source": "http://www.freerealms.com:80/article/detail.action?articleId=137"}
 ],
 "confidence": 0.4,
 "open": [
  "Date unverified: 2009-07-03 is inferred from the capture date and a relative stamp. Needs a second dated source (archive timestamp or dated article) before it can be scheduled. Occurrences rest on that inference.",
  "Possible alias or merge: 'Seaside Summer Splash' (article 137, began 2 July 2009, Uncle Sam Outfit added) overlaps with this sale (article 142, 3 July 2009 inferred, Uncle Sam suit featured). Both name the same outfit. Kept as separate events until a dated source settles it; treat as a likely alias.",
  "Wiki attributes the Uncle Sam Outfit to Independence Day; that framing is not sourced to this event and conflicts with article 137. Unresolved.",
  "Uncle Sam Jacket, Pants, Shoes and Top Hat are excluded: article 142 does not name them.",
  "Prices are null for all items: article 142 gives none.",
  "Currency is null: article 142 says SC (Subscriber Currency); a store frame (video:9NOkMosko1E/00024.jpg) shows a Fireworks Crate at 315 station_cash, undated and not tied to this sale.",
  "End date and duration unknown; article 142 gives none.",
  "Quest objective locale:400873 ('summertime reward' in a Grekel deck battle) is not tied to this sale by any source; not listed.",
  "Fireworks ids locale:115748, 115583, 115590, 115346, 431153, 399473 (Highroad Junction Crate of Fireworks) are a different event and excluded. Note the Fireworks Crate (locale:394790) is linked to this sale only by article 142; its identity with the Highroad crate is unverified.",
  "Live status 'unsure': the article reads as a live announcement, but the date and end are unverified."
 ],
 "wireable": false
}
