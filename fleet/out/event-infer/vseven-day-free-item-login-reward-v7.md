<!-- fleet job=event-infer id=vseven-day-free-item-login-reward-v7 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[8119, 8678, 6, 2988] model=claude-haiku-5-5 -->
# Seven-day free item login reward

```json
{
 "event": {
  "name": "Welcome Back to Free Realms! (returning-player login program, 2011)",
  "aliases": [
   "Seven-day free item login reward (pack's working label; the seven-day item series is one component, not the source title)",
   "7-day login gift (Spanish wording, articleId=2131)"
  ]
 },
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [
  {
   "year": 2011,
   "when": "approximately May 2011 (relative dates only; no start or end date in any source). Eligibility cutoff: May 2, 2011.",
   "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (title 'Welcome Back to Free Realms!', '2 months ago'); articleId=2129 ('posted about six days before' its 2011-05-21 capture); articleId=2138 ('posted 2 weeks, 3 days ago')"
  }
 ],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": [
  "Returning or lifetime members claim account-time gifts (Member days / free play, per the conflicting figures below)",
  "Log in on each of seven days to receive one free item per day; logging in before the last day allows collecting all seven (articleId=2127; articleId=2130 Spanish summary)",
  "Lifetime members also claim the Lonely Island Lot (articleId=2127)"
 ],
 "items": [
  {"name": "Sandy Beach Lot", "price": null, "currency": "reward", "source": "articleId=2127, Day 1; client name match locale:8321 (name only)"},
  {"name": "Oasis", "price": null, "currency": "reward", "source": "articleId=2127, Day 2; client name match locale:30162 (name only)"},
  {"name": "Basic Swimming Pool", "price": null, "currency": "reward", "source": "articleId=2127, Day 3; client name match locale:147854 (name only, unconfirmed)"},
  {"name": "New School Dragon Blade", "price": null, "currency": "reward", "source": "articleId=2127, Day 4; no client match found"},
  {"name": "Jackpot Plant", "price": null, "currency": "reward", "source": "articleId=2127, Day 5; client name match locale:5683 (a housing item shares the name, so id unconfirmed)"},
  {"name": "Large Launch Pad", "price": null, "currency": "reward", "source": "articleId=2127, Day 6; client name match locale:6180 (unconfirmed)"},
  {"name": "Pirate Ship", "price": null, "currency": "reward", "source": "articleId=2127, Day 7; client name match locale:9188 (name only)"},
  {"name": "Lonely Island Lot", "price": null, "currency": "reward", "source": "articleId=2127, Lifetime members only; client locale:8322 (name only)"}
 ],
 "rewards": [
  "Seven daily login items, Days 1-7 (articleId=2127)",
  "Lonely Island Lot for Lifetime members (articleId=2127)",
  "20,000 Coin for Lifetime members (articleId=2127 summary: '20,000 Coin for Lifetime Members'; corroborated by articleId=2131 Spanish quote, undated)",
  "Account time, UNRESOLVED: 45 Member days for accounts in good standing on or before May 2, 2011 (articleId=2127); 45 days free play (articleId=2129, 2138); 43 membership days plus extra play time for accounts updated before a garbled cutoff (articleId=2130)"
 ],
 "evidence": [
  {"claim": "One Welcome Back post for returning players bundles Member-day gifts, 20,000 Coin for Lifetime Members, a seven-day login item series, and a Lonely Island Lot for Lifetime Members", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (articles summary)"},
  {"claim": "Seven-day series gives one free item per day on login", "source": "articleId=2127; articleId=2131 ('durante siete días')"},
  {"claim": "Daily item names Day 1 Sandy Beach Lot through Day 7 Pirate Ship", "source": "articleId=2127"},
  {"claim": "Eligibility cutoff is May 2, 2011 (not a start date)", "source": "articleId=2127; articleId=2129; articleId=2138"},
  {"claim": "Posts date to roughly May 2011", "source": "articleId=2129 (about six days before 2011-05-21 capture); articleId=2138 ('2 weeks, 3 days ago'); articleId=2127 ('2 months ago', capture date per pack 2011-07-15, unverified by me)"},
  {"claim": "Item names exist in client as: 8321 Sandy Beach Lot, 30162 Oasis, 9188 Pirate Ship, 8322 Lonely Island Lot", "source": "locale lookup (name matches; not proof of the gift id)"}
 ],
 "confidence": 0.4,
 "open": [
  "Start and end dates unknown; every article is relative-dated. Not wireable as a dated live event.",
  "Account-time figures conflict: 45 Member days (2127) vs 45 free-play days (2129, 2138) vs 43 membership days plus play time (2130). Unresolved.",
  "Item ids are name matches only. Basic Swimming Pool (147854), Jackpot Plant (5683), Large Launch Pad (6180) are unconfirmed. New School Dragon Blade has no client match.",
  "Pirate Ship is cited to 2127 only; 2129 and 2138 were not confirmed to name it.",
  "Wiki pack names (vwelcome-back-gift, vwelcome-back-gifts, vwelcome-back-daily-login-gift, vwelcome-back-login-gift-series) dropped: no category members supplied.",
  "Alias '[Welcome] [Back]' (articleId=2142) dropped as unverified.",
  "Realmkeepers 'Welcome back' video frame (video:2nq801iM8kU/00198.jpg) is a different in-game event and excluded.",
  "Dropped the split into two events: the 2127 summary bundles the item series with the account-time gifts in one post, so they are treated as one program. The 2130 title 'Seven-day free item login reward' is a pack label, not an article title.",
  "20,000 Coin rests on the 2127 summary (secondary extraction) and an undated Spanish quote; era unknown."
 ]
}
```
