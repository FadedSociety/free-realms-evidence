<!-- fleet job=event-infer id=vfree-pet-outfit-promotion-feb-v4 status=done turns=3 usd=0.0021 tokens(read,write,in,out)=[13505, 7354, 8, 2114] model=claude-haiku-5-5 -->
# Free pet outfit promotion (Feb 2012)

{"event": {"name": "Free dog or cat outfit with 400 Station Cash pet purchase (10-15 Feb 2012 CET)", "aliases": ["Free pet outfit promotion (Feb 2012) (pack working title, not an official name)"]},
 "kind": "promotion",
 "live": "unsure",
 "occurrences": [{"year": 2012, "when": "10 Feb 2012 09:01 CET to 15 Feb 2012 08:59 CET", "source": "http://www.freerealms.com/article/detail.action?articleId=2518"}],
 "recurring": null,
 "zones": [],
 "npcs": [],
 "quests": [],
 "activities": ["Buy a dog or cat for 400 Station Cash and receive a free cat or dog outfit matching the pet"],
 "items": [],
 "rewards": ["A free dog or cat outfit matching the purchased pet (the 15 outfit-to-pet pairings in article 2518 are not in the evidence pack, so no outfit names are listed)"],
 "evidence": [
  {"claim": "For a limited time, buying a dog or cat for 400 Station Cash gave a free cat or dog outfit matching the pet (German-language SOE 'What is New?' post; pack quote: 'ein Hund oder eine Katze für 400 Station Cash kauft').", "source": "http://www.freerealms.com/article/detail.action?articleId=2518"},
  {"claim": "The window was 10 February 2012 09:01 CET to 15 February 2012 08:59 CET (pack quote: 'startet am 10. Februar um 09:01 Uhr und endet am 15. Februar 2012 um 08:59 Uhr CET'). Pack-sourced; my lookup could not re-find the article text, so this is not independently re-verified.", "source": "http://www.freerealms.com/article/detail.action?articleId=2518"},
  {"claim": "Client text locale:3677 'Valentine's Special! Buy Jinx and get the Doggy Fairy Outfit free!' and locale:3662 'Jinx with Doggy Fairy Outfit' exist. Article 2521 (undated in the pack) describes Jinx's promo pet outfit as the Doggy Fairy Outfit, per the lookup fact.", "source": "locale:3677"}
 ],
 "confidence": 0.5,
 "open": [
  "Live status is 'unsure': the 10-15 Feb 2012 window and the 400 SC price come only from the pack's quote of article 2518. I could not re-fetch that article, so verify it before wiring.",
  "The 15 outfit-to-pet pairings (10 dog, 5 cat) from article 2518 are missing from the pack. Fetch http://www.freerealms.com/article/detail.action?articleId=2518, then check each outfit name with locale/ids and add them as items sourced to 2518.",
  "Possible overlap, not resolved: locale:3677 and locale:3687 ('Valentine's Special!' Jinx/Doggy Fairy Outfit, Luna/Kitty Sassy Outfit) fall in the same February season and article 2521 (undated) pairs these pets and outfits under a 400 SC mechanic. They may be the same promotion, a related promo, or a separate one. Not merged and not stated as different. Locale 72309 (Doggy Fairy Outfit) and 72336 (Kitty Sassy Outfit) are left out of items until a dated source ties them to 10-15 Feb 2012. Article 2521 itself is not in the pack and its outfit list is unverified.",
  "The name is a pack working title. The official article title is the generic 'Free Realms - What is New?'; no official event name is confirmed.",
  "Not merged with locale:4849 'PET OUTFIT SALE!' (100 SC off, locale:4850), the marketplace bonus text at locale:431858, or article 299 (Doggy and Kitty Bionic Outfits, Marketplace).",
  "NPCs are empty: names in article 2521 (Scout, Diego, Marlin, Scooter, Summer, Allie, Dashes, Mr. Kitty, Pooky, Kiri, Gizmo, Luna) look like promo pet or owner names and are not verified as NPCs.",
  "Recurrence is null: only one dated occurrence is sourced.",
  "No zones or quests tie to this event; the pack's quest answers mentioning it are empty."
 ]}
