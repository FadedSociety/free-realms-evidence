<!-- fleet job=event-infer id=vwelcome-back-gift-v7 status=done turns=3 usd=0.0053 tokens(read,write,in,out)=[17691, 18373, 8, 5631] model=claude-haiku-5-5 -->
# Welcome Back gift

{"event": {"name": "Welcome Back to Free Realms (2011 returning-player compensation)", "aliases": ["Welcome Back gift", "Welcome Back program", "Welcome Back to Free Realms!", "Welcome-back gifts", "Welcome Back login gift series"]},
 "kind": "other",
 "live": "yes",
 "occurrences": [{"year": 2011, "when": "c. mid-May 2011, no absolute start or end date stated. Eligibility cutoff: accounts in good standing on or before 2 May 2011. Capture dates: 2129 captured 2011-05-21 ('about six days' before capture); 2127 captured 2011-07-15 ('2 months ago'); 2130, 2131, 2138 captured 2011-06-04 ('2 weeks' relative).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 ; http://www.freerealms.com:80/article/detail.action?articleId=2129 ; http://www.freerealms.com/article/detail.action?articleId=2138 (relative dates; capture dates from articles.json)"}],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Log in on each of seven consecutive days to receive one free item per day (logging in before the last day needed to collect all seven, per 2127)", "Lifetime Members claim the extra Lonely Island Lot (2127)", "Returning members receive 45 Member days added to the account (2127, 2129, 2138)"],
 "items": [
  {"name": "Sandy Beach Lot", "price": null, "currency": "reward", "source": "articleId=2127, 'Day 1 - Sandy Beach Lot'"},
  {"name": "Oasis", "price": null, "currency": "reward", "source": "articleId=2127, 'Day 2 - Oasis' (client locale 30162 name match per pack, unverified)"},
  {"name": "Basic Swimming Pool", "price": null, "currency": "reward", "source": "articleId=2127, 'Day 3 - Basic Swimming Pool' (locale 147854 is a name match only per pack)"},
  {"name": "New School Dragon Blade", "price": null, "currency": "reward", "source": "articleId=2127, 'Day 4 - New School Dragon Blade' (no exact client match)"},
  {"name": "Jackpot Plant", "price": null, "currency": "reward", "source": "articleId=2127, 'Day 5 - Jackpot Plant' (client locale 5683 is a name match only, separate housing item per pack)"},
  {"name": "Large Launch Pad", "price": null, "currency": "reward", "source": "articleId=2127, 'Day 6 - Large Launch Pad' (client locale 6180 name match per pack, unverified)"},
  {"name": "Pirate Ship", "price": null, "currency": "reward", "source": "articleId=2127, 'Day 7 - Pirate Ship' (client locale 9188 name match per pack, unverified)"},
  {"name": "Lonely Island Lot", "price": null, "currency": "reward", "source": "articleId=2127, 'they can also claim a Lonely Island Lot!' (Lifetime Members only; client locale 8322 name match per pack, unverified)"}
 ],
 "rewards": ["45 Member (free play) days added to the account for members in good standing on or before 2 May 2011 (articleId=2127 'An extra 45 days as a Member has been added to your account.'; articleId=2129 'eine kostenlose Spielzeit von 45 Tagen'; articleId=2138 'Nous avons ajouté 45 jours de jeu gratuit')", "20,000 Coins instead of game time for Lifetime Members (articleId=2127 summary; 2130 and 2131 summaries)", "Seven daily free items on login: Sandy Beach Lot, Oasis, Basic Swimming Pool, New School Dragon Blade, Jackpot Plant, Large Launch Pad, Pirate Ship (articleId=2127 'Day 1'..'Day 7')", "Lonely Island Lot for Lifetime Members (articleId=2127)"],
 "evidence": [
  {"claim": "Returning-player welcome-back program: 45 Member days for accounts in good standing on or before 2 May 2011, 20,000 Coins for Lifetime Members, seven-day login gift series, extra Lonely Island Lot for Lifetime Members, all in one post.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (articles.json summary; facts 'An extra 45 days as a Member has been added to your account.' and 'One will be given out upon login each day for seven days.')"},
  {"claim": "Members in good account standing before 2 May 2011 received 45 days of free play as a welcome-back gift.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2129 (quote 'eine kostenlose Spielzeit von 45 Tagen')"},
  {"claim": "Seven-day item schedule: Day 1 Sandy Beach Lot, Day 2 Oasis, Day 3 Basic Swimming Pool, Day 4 New School Dragon Blade, Day 5 Jackpot Plant, Day 6 Large Launch Pad, Day 7 Pirate Ship.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (quotes 'Day 1 - Sandy Beach Lot' through 'Day 7 - Pirate Ship')"},
  {"claim": "Lifetime Members also get a Lonely Island Lot.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (quote 'they can also claim a Lonely Island Lot!')"},
  {"claim": "Spanish and French posts describe the same program: 43 membership days for accounts updated before a cutoff (2130, 2131), 45 days before 2 May 2011 (2138), 20,000 Coins for lifetime members (2130, 2131).", "source": "http://www.freerealms.com/article/detail.action?articleId=2130 ; http://www.freerealms.com/article/detail.action?articleId=2131 ; http://www.freerealms.com/article/detail.action?articleId=2138"},
  {"claim": "Live era: the posts describe rewards already added to accounts, not a plan.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2127 (quote 'An extra 45 days as a Member has been added to your account.')"}
 ],
 "confidence": 0.6,
 "open": [
  "Absolute date unknown. Articles are undated; only relative captures are given. Best estimate c. mid-May 2011, bounded by the 2 May 2011 eligibility cutoff and the 2011-05-21 capture of 2129. Do not schedule a window from this.",
  "Discrepancy: 2127, 2129 and 2138 say 45 days; 2130 and 2131 say 43 days for accounts updated before a cutoff. Either a translation/typo or two grants. Unresolved.",
  "The earlier 'SC Marketplace' price claim for Sandy Beach Lot and Pirate Ship has no source and was removed. All item prices are null.",
  "Client links for the item names (Oasis 30162, Basic Swimming Pool 147854, Jackpot Plant 5683, Large Launch Pad 6180, Pirate Ship 9188, Lonely Island Lot 8322, Sandy Beach Lot 8321) are name matches only, not confirmed as the gift items. New School Dragon Blade has no client match. Moderne Drachenklinge (earlier draft) is dropped as unverified.",
  "Jackpot Plant wiki claim (free welcome-back gift to all players; second free gift June 2011; first-gift month unknown) was not re-read in this pass. It is a separate item from the 2127 day-5 gift only if sources say so. Muenzpflanze link inferred, not verified.",
  "Not tied to this event by any source: Baby Unicorn 'Welcome Back' producer letter (May 18 2011), Spanish June 2011 farm 'Welcome back' letter (articles.json:17302), undated Farming and Ranching 'Welcome Back to Free Realms!' letter (articles.json:17890). Keep out unless a source links them.",
  "Name scope: the 2127 post lists the 45-day grant, login series and lifetime gifts together, so they are one program in the source. Keep the umbrella name; the sub-parts are components, not separate events.",
  "No zones, NPCs or quests are tied to this event by any source. Client lookup of the item names returned no confirmed matches.",
  "The 'Log in after the downtime' claim is not sourced to a quote. The downtime itself is undated and unsourced; removed from activities except the login-gift mechanic quoted from 2127."
 ]}
