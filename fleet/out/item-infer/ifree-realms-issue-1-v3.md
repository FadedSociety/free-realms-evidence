<!-- fleet job=item-infer id=ifree-realms-issue-1-v3 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6749, 8115, 6, 2463] model=claude-haiku-5-5 -->
# Free Realms Issue 1

{"item": {"name": "Free Realms #1 (Free Realms Issue 1, WildStorm comic)", "locale_id": null, "kind": "other"},
 "sources": [
  {"type": "promotion", "detail": "Printed comic cover promo: 'Exclusive In-Game Reward'. Cover says 'Inside! Collect all 12. See page 28 for details on collecting the SPIDER BITE SWORD!' This is a stated promotion for the Spider Bite sword, not a confirmed source for the comic itself. No mechanism, dates, or vendor is given.", "where": null, "price": null, "currency": null, "source": "image:art_or_promo 'Free realms issue 1.jpg' transcription, https://freerealms.fandom.com/wiki/Free_Realms_Issue_1"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Free Realms #1 is a WildStorm comic published July 29, 2009, first of a 12-issue series; categories Comic and Real-world articles; no coin, Station Cash or IGD entries.", "source": "https://freerealms.fandom.com/wiki/Free_Realms_Issue_1"},
  {"claim": "Cover marked 'Exclusive In-Game Reward' and promises the Spider Bite sword for collecting all 12 issues (see page 28).", "source": "image:art_or_promo 'Free realms issue 1.jpg' transcription, https://freerealms.fandom.com/wiki/Free_Realms_Issue_1"},
  {"claim": "Client text has a comic collection structure: 'Free Realms Comic Book Issues 1-4' (locale:416364), 'Issues 5-8' (locale:416370), 'Issues 9-12' (locale:416376), and 'Free Realms Comic Book Series 1' described as 'for obtaining the Free Realms comic books 1 through 12' (locale:416382, 416383). Per-issue 'Issue 1 Certificate of Authenticity' is locale:416366 (Issues 2-12 are 416367-416381). These confirm the comics were client items in collections, but the client text does not say how a player obtains them.", "source": "locale:416364-416383"},
  {"claim": "Client has the name 'Spider Bite' (locale:400987) and 'Spider-Bite' (locale:400989), which match the cover's SPIDER BITE SWORD by name only. Nothing in the pack links that sword to the comic reward.", "source": "locale:400987, locale:400989"},
  {"claim": "Repo search for 'spiderbite', 'Certificate of Authenticity' and 'Free Realms Comic' returned no matches, so the earlier ClientItemDefinitions.json (~49762) claim could not be verified in the repo.", "source": "search repo (no matches)"},
  {"claim": "locale:400990 ('Spider Bite Item Proc Set up') is a dev_note internal proc string and is not used as evidence.", "source": "id_check flag"}
 ],
 "confidence": 0.3,
 "open": [
  "The comic is a printed WildStorm book, not a confirmed game item. No wiki page, vendor, quest, drop, price, or dates give it a game source. The only game link is the cover's promo text, so it is not a live source yet.",
  "Mechanism for the promo is unconfirmed: the cover says collecting all 12 issues earns the Spider Bite sword, but no page, record, or article gives the reward rule, dates, or whether it still runs.",
  "Client comic collections (locale:416364-416383) show the series was tracked in game, but not how issues were obtained (promo, drop, code, or purchase). Needs a wiki page for Issues 2-12, the Spider Bite sword, or a client item record for the acquisition type.",
  "Critique items addressed: the claim that the sword is absent was corrected to 'name match only'. Locale ids 416366-416381 and 416382-416383 were checked here. The ucdt/ugdt IDs cited by a critique were not verified. The repo has no spiderbite record, so the earlier ClientItemDefinitions.json line stays unverified.",
  "Not wireable as a game item: no price, currency, or confirmed acquisition method."
 ]}
