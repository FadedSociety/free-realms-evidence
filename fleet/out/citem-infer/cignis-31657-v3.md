<!-- fleet job=citem-infer id=cignis-31657-v3 status=done turns=4 usd=0.0043 tokens(read,write,in,out)=[42706, 17843, 10, 3300] model=claude-haiku-5-5 -->
# Ignis

{"item": {"name": "Ignis", "locale_id": 31657, "kind": "weapon"},
 "sources": [
  {"type": "marketplace", "detail": "New School Ignis (Ninja level 1 weapon; Tiger Claw / Heat Wave). Sold for Station Cash; Members get 10% off. Price is wiki-sourced only (wiki rev 47363) and not re-checked on the live page. Client definition not confirmed (13665 or 38110).", "where": "SC Marketplace", "price": "199 Station Cash regular; 179 Station Cash Member price (10% off)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Ignis (New School section: acquired from the Station Cash Marketplace); repo:prototype/osfr-tools/data/content/stores.json item 13665 (line 3652) and item 38110 (line 12336), price_provenance wiki_prices [199,179], wiki_rev_id 47363"},
  {"type": "marketplace", "detail": "Old School Ignis (Ninja level 1; Flame Flash / Dragonstrike). Previously sold through the Station Cash Marketplace; no longer obtainable. No price or sale dates evidenced for this version.", "where": "SC Marketplace", "price": null, "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Ignis (Old School section, 'previously sold through the Station Cash Marketplace. It can no longer be acquired.'; categories Retired Weapons, Unobtainable Weapons)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Ignis' is locale 31657; two client definitions 13665 and 38110, both power 5, level 1, Ninja, slot 7, class 6, model sword_ar_ag_weapon_fx.adr.", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:21867-21913"},
  {"claim": "The wiki page covers two Ninja weapons named Ignis: a New School one sold on the SC Marketplace and an Old School one that was previously sold there and can no longer be acquired.", "source": "https://freerealms.fandom.com/wiki/Ignis"},
  {"claim": "Old School Ignis text: 'was previously sold through the Station Cash Marketplace. It can no longer be acquired.' (lookup confirmed this sentence).", "source": "lookup 'Ignis Station Cash Marketplace Ninja' on wiki page Ignis"},
  {"claim": "Store rows 13665 (tint group 2) and 38110 (tint group 3) both carry sc_price 199 and wiki_prices [199,179] with provenance 'the regular price on the fandom wiki page Ignis (revision 47363)'. The 179 is the sale/member price. Both rows are no_sale=true with no coin price. The rows do not say which definition is the New School one.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 3652 and 12336"},
  {"claim": "No coin vendor stocks Ignis. The legacy coin cost 3522 in weapons.json is cleared in the store rows and is not a coin price.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 3652 and 12336 (price_provenance.basis); repo:prototype/osfr-tools/data/reference/weapons.json:21903-21910"},
  {"claim": "Locale 98671 is also the text 'Ignis'; no further text is attached to it, so it is not tied to a definition.", "source": "locale:98671"}
 ],
 "confidence": 0.5,
 "open": [
  "Definition mapping is unknown. Both store rows cite the same wiki revision, and that revision describes only the New School version. A 199 SC price applied to both definitions is a reconstruction artifact, not per-definition evidence. The Old School definition should not be given the 199 price. Which of 13665 or 38110 is the New School version is not stated by any source (weapons.json shows 13665 resell 352 and min_profile_rank 0; 38110 resell 0 and min_profile_rank 1, which does not settle it).",
  "The 199/179 figures come only from repo provenance (wiki rev 47363). The live wiki text has its prices stripped, and lookup could not match them, so they are unverified against the live page.",
  "Store data marks both definitions no_sale=true, which conflicts with the wiki's New School SC Marketplace sale. Live availability of the New School version is therefore unconfirmed; treat it as unsure.",
  "Old School retirement date, sale dates and price are not in any source.",
  "Wiki effect values (Tiger Claw 254 to 2372, Heat Wave 1143 to 10674; Flame Flash 3083, Dragonstrike 13876) are not verified against client data.",
  "Locale 98671 'Ignis' was not tied to a definition."
 ]}
