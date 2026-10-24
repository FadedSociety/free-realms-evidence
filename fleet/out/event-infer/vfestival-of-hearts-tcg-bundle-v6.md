<!-- fleet job=event-infer id=vfestival-of-hearts-tcg-bundle-v6 status=done turns=2 usd=0.0039 tokens(read,write,in,out)=[10967, 14886, 6, 3874] model=claude-haiku-5-5 -->
# Festival of Hearts TCG Bundle

{
 "event": {"name": "Festival of Hearts", "aliases": ["Festival des Cœurs (French, articleId 1009)"]},
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "February 12, 2010 update (Merry Vale)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=967"}
 ],
 "recurring": null,
 "zones": ["Merry Vale (articleId 967; locale:1418; locale:432861)"],
 "npcs": ["Cudip (locale:1418, locale:432861)", "Stone Heart (locale:427176)", "Jecca (locale:427178)", "Heart Breakers (locale:427262)", "Postmaster Vixie (locale:427172)", "Dubawug (locale:427242)"],
 "quests": [],
 "activities": [
  "Pick a petal from the heart flower every day (locale:426989)",
  "Spin the special Festival of Hearts wheel every day for bonus prizes (locale:400038)",
  "Help Cudip uncover the heart flower mystery in Merry Vale (locale:432861, locale:1418)",
  "Stop Stone Heart's heartbreakers with a love potion (locale:427176, locale:427178, locale:427262)",
  "Complete 100 Festival of Hearts repeatable quests (locale:5103220)",
  "Attend the Festival of Hearts semi-formal dance (locale:31034; the dated 2010 dance claim is not verified here)"
 ],
 "items": [
  {"name": "Festival of Hearts TCG Bundle", "price": null, "currency": "station_cash", "source": "http://www.freerealms.com/article/detail.action?articleId=1009 (limited-time, Marketplace, Station Cash, ends with the festival); locale:4874, locale:4875"}
 ],
 "rewards": [
  "Festival of Hearts wheel bonus prizes (locale:400038)",
  "TCG bundle contents: Emo Raptor loot card, Edwin Goldstory and Commander Kluggenkrush promo cards, booster packs (locale:4875; see open for count conflict)"
 ],
 "evidence": [
  {"claim": "The Festival of Hearts was live in Merry Vale starting with the February 12, 2010 update, with Cudip helping players", "source": "http://www.freerealms.com:80/article/detail.action?articleId=967"},
  {"claim": "Client event name is 'Festival of Hearts' and it 'has begun'", "source": "locale:4452; locale:1415; locale:5518"},
  {"claim": "Festival of Hearts TCG Bundle was a limited-time Station Cash Marketplace item that ends with the festival; French name Festival des Cœurs", "source": "http://www.freerealms.com/article/detail.action?articleId=1009"},
  {"claim": "Bundle includes Emo Raptor loot card, Edwin Goldstory and Commander Kluggenkrush promo cards, and booster packs", "source": "locale:4875"},
  {"claim": "Daily Festival of Hearts wheel for bonus prizes", "source": "locale:400038; locale:431950"},
  {"claim": "Heart Breakers and Stone Heart oppose players in Merry Vale during the festival", "source": "locale:427176; locale:427262"},
  {"claim": "Repeatable quest goal of 100 Festival of Hearts quests", "source": "locale:5103220"}
 ],
 "confidence": 0.5,
 "open": [
  "Bundle is an item sold inside the Festival of Hearts event, not a separate event. Article 1009 is undated (only 'posted 1 year, 3 months ago' relative to capture), so it cannot be tied to a year.",
  "Bundle contents conflict: article 1009 says 2 Free Realms booster packs; locale:4875 says two Premiere and two Shattered Past packs. 'Premiere' may be the Free Realms set name, which would reconcile the two, but no source says so. No bundle price is stated anywhere.",
  "Only one occurrence is dated (2010-02-12, article 967). The 'annual' recurrence claimed in earlier notes (articles 969, 2016, 2018, 2019, 2500, 2501) was not verified in this pass and the articles give no month, so recurring is null.",
  "Undated later mentions not placed in occurrences: articleId 2498/2499 (festival launched on PS3, per earlier notes), 2500/2501 (returned to Merry Vale with daily and members-only quests), 2522 (community webcast showing item animations). Not checked here.",
  "Zone conflict unresolved: French articles 976, 1057, 2026 say Joyful Valley; Spanish articles 2018, 2019 say Vegalegre; English and client text say Merry Vale. May be regional naming or a different festival. Do not merge into one schedule until dated.",
  "Legend conflict unresolved: English says Rylan and Arianna; French says Valentin and Arianna; Spanish says Rois and Araiana.",
  "Wiki-only items (She-Rex, Lovelectric Boombox, Snowheart, King of Hearts Costume, King of Broken Hearts Costume, Love Struck Piano, Stone Hearted Piano, Stone Heart's Gummy Bear, Stone Heart's Bear Costume, Lovely T-Shirt, Hearts Outfit, Dove, Cupid, Heart Critter) are not quoted or dated here; their 'sold during festival' claims and any price or currency are unverified and left out.",
  "Stone Heart's 15-minute spawn (wiki Festival of Hearts) is undated and is not tied to any occurrence.",
  "Removed: 'Throw Festival of Hearts house parties' (locale:3545, flagged as placeholder). Dance party (locale:2778), anti-festival rally (locale:3559) and semi-formal (locale:6672, 'Scheduled') are preview or community text and are excluded from occurrences.",
  "Not verified: Festival of Hearts Mystery Gift (locale:4418) and Semi-Formal (locale:31033) are names only. Aliases 'Heart Festival', 'Festival annuel des Coeurs' and 'Festival de Corazones' came from earlier notes and are not checked here.",
  "Quest titles: none confirmed from the pack. Stone Heart's Hideaway is unconfirmed as a quest.",
  "Prices: none in any source; price fields are null.",
  "Not ready for the calendar: one dated occurrence, unknown recurrence month, and an open zone conflict. Whether it runs on the rebuild is not decided here."
 ]
}
