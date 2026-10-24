<!-- fleet job=event-infer id=vparty-invitations-contest-v5 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[8566, 10255, 6, 3435] model=claude-haiku-5-5 -->
# Party invitations contest

{
 "event": {
  "name": "Free Realms Birthday Party (anniversary celebration)",
  "aliases": ["Birthday Bash", "Birthday Party", "Free Realms anniversary party", "Party invitations contest (sub-activity, not a standalone event)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "First anniversary party, from the posting day until May 10, 2010 (start day not sourced; anniversary is April 28)", "source": "http://www.freerealms.com/article/detail.action?articleId=1267"},
  {"year": 2011, "when": "Second anniversary party, running until May 18, 2011 (post date not given as a day)", "source": "http://www.freerealms.com/article/detail.action?articleId=2107"},
  {"year": 2012, "when": "Third birthday Birthday Bash; SOE release April 30, 2012; festivities concluded May 24, 2012", "source": "http://www.tentonhammer.com:80/free-realms/news/free-realms-celebrates-its-3rd-birthday-with-new-events; http://www.freerealms.com/article/detail.action?articleId=2580"}
 ],
 "recurring": "Yearly around the April 28 anniversary, ending mid-to-late May; three dated occurrences (2010, 2011, 2012).",
 "zones": ["Sanctuary", "Queensfields", "Sacred Grove", "party areas (eight zones per articleId=1267)"],
 "npcs": ["Papillonnette", "Camellia", "Plumette", "Helga", "Camilla", "Cakenstein"],
 "quests": ["Cakenstein Attacks!"],
 "activities": [
  "Party invitations sub-activity: pick up invitations near Papillonnette, invite people; receiving more invitations than Papillonnette earns a special prize (articleId=1300, undated; year inferred, not confirmed)",
  "Help Camellia with the cake-baking contest (articleId=1300, articleId=2580)",
  "Collect balloons for Plumette and food ingredients for Helga (articleId=1300)",
  "Daily party-prep quests from Sanctuary NPCs, including subscriber-only quests (articleId=2107)",
  "Birthday Party Crates: place one on the ground to start a party; crates can randomly yield fireworks (locale:5666; wiki Birthday Crates)",
  "Cakenstein Attacks! world event with a prize wheel (2012; wiki Birthday Bash)"
 ],
 "items": [
  {"name": "Birthday Party Crate", "price": null, "currency": "station_cash", "source": "wiki Birthday Crates (bought from the SC Marketplace); articleId=2107 (bought on the Marketplace); locale:5664, 5666"},
  {"name": "Anniversary Firework", "price": null, "currency": "reward", "source": "video:C3fysVLxrMg/00540.jpg; locale:14571"},
  {"name": "Birthday Cake hat", "price": null, "currency": "reward", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (2012, per pack; the Tom Ton Hammer article is the cited 2012 source)"},
  {"name": "Party Pinata pet and birthday furniture", "price": null, "currency": null, "source": "http://www.tentonhammer.com:80/free-realms/news/free-realms-celebrates-its-3rd-birthday-with-new-events (Marketplace items, 2012; currency not stated)"}
 ],
 "rewards": [
  "Anniversary Firework and fireworks from Birthday Party Crates (crate contents, wiki Birthday Crates; video:C3fysVLxrMg/00540.jpg)",
  "Birthday Cake hat for all players (2012; TTH 3rd-birthday article, per pack)",
  "Special prize for out-inviting Papillonnette (articleId=1300, prize not named, year unconfirmed)"
 ],
 "evidence": [
  {"claim": "The first-anniversary party ran from the posting day until May 10, 2010, with party areas in eight zones, birthday quests from Camellia in Sanctuary, and party items for sale.", "source": "http://www.freerealms.com/article/detail.action?articleId=1267"},
  {"claim": "The second-anniversary party ran until May 18, 2011; Sanctuary NPCs gave daily and subscriber-only party quests.", "source": "http://www.freerealms.com/article/detail.action?articleId=2107"},
  {"claim": "The third-birthday celebration (SOE release April 30, 2012) included birthday story quests, daily rewards, a Cakenstein world event, and Marketplace items; it concluded May 24, 2012.", "source": "http://www.tentonhammer.com:80/free-realms/news/free-realms-celebrates-its-3rd-birthday-with-new-events; http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "Birthday Party Crates are sold in the Marketplace and contain party supplies that start a party.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2106; http://www.freerealms.com/article/detail.action?articleId=2107; http://www.freerealms.com:80/article/detail.action?articleId=1268; locale:5666"},
  {"claim": "Invitations sub-activity: receiving more invitations than Papillonnette earns a special prize.", "source": "http://www.freerealms.com/article/detail.action?articleId=1300"},
  {"claim": "Cakenstein is the cake monster of the party; Birthday Bash pages say he appears in the party.", "source": "wiki Birthday Bash; articleId=1300"}
 ],
 "confidence": 0.6,
 "open": [
  "'Party invitations contest' is a sub-activity of the birthday party, not a standalone event. Filed under the parent event.",
  "articleId=1300 is undated; its 2010 attachment is inferred from first-birthday wording. The invitation contest is not confirmed for any dated year.",
  "Start days are not sourced for 2010 or 2011 (only end dates). Wireable is false.",
  "2011 balloon weapons (Balloon Bow, Hammer, Axe, Sword), per-area T-shirts and illusions are cited to articleId=2106/2099 in the prior record, but I could not confirm them in indexed text. They are dropped from the record until verified. Wiki balloon pages are not tied to a dated source.",
  "Birthday Party Crate currency: the wiki says SC Marketplace (station_cash); the price is not sourced.",
  "Quests 'Cakey Madness', 'Downing Cakenstein' and 'Queensfields Downing Cakenstein' are client text (locale:4918, 4949, 707) with no year; the 2010 tie rests on articleId=1282, which is undated. Left out of the quest list.",
  "'Cakenstein Attacks!' is tied to 2012 only by the wiki (locale:4917, 4948, 4949); not confirmed by a dated article.",
  "Launch-date conflict: wiki Birthday Bash says April 29, 2009 launch; the anniversary convention used here is April 28. Not reconciled.",
  "The pack may merge the 2010 party, 2011 anniversary and 2012 Birthday Bash under one name. This record treats them as occurrences of one yearly holiday; the merge is an assumption.",
  "Commander Kiggle (locale:428677) is not named in any dated article; omitted. Cakenstein 'risen' warp messages (locale:6707-6713) have no year; omitted.",
  "Orange/Blue Silly String and Anniversary Ring have no source tying them to the event; dropped. Seaside party invitations (locale:384070) is an unrelated match; dropped.",
  "Article 1197 (all-day birthday party schedule) has no year; not assigned."
 ]
}
