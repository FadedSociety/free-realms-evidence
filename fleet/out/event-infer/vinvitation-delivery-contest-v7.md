<!-- fleet job=event-infer id=vinvitation-delivery-contest-v7 status=done turns=2 usd=0.0033 tokens(read,write,in,out)=[8562, 9757, 6, 3976] model=claude-haiku-5-5 -->
# Invitation delivery contest

{
 "event": {
  "name": "Birthday Bash (Free Realms anniversary celebration)",
  "aliases": ["Birthday Bash", "Birthday Party", "Free Realms 1st Birthday Party events", "Invitation delivery contest (daily sub-activity only)"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2010, "when": "1st anniversary; exact dates not sourced (undated article)", "source": "http://www.freerealms.com/article/detail.action?articleId=1282 (1st-birthday framing, no date; the pack's April 22 / April 29-May 10 dates are unverified and not used)"},
  {"year": 2011, "when": "2011 Birthday Bash; no dates found", "source": "wiki Gifting Piñata; wiki Balloon Bow (both say 'available during 2011 Birthday Bash')"},
  {"year": 2012, "when": "3rd anniversary Bash, ended May 24, 2012 (start not stated)", "source": "http://www.freerealms.com/article/detail.action?articleId=2580; locale:695"},
  {"year": 2013, "when": "4th birthday, April 29, 2013 (end not stated)", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"}
 ],
 "recurring": "Yearly around the April 29 Free Realms anniversary; attested 2010-2013 (four years). Window length varies and is not fixed; wiki Category:Birthday Bash Weapons says 'throughout April', which conflicts with the May 24, 2012 end date and is unresolved.",
 "zones": ["Sanctuary", "Sacred Grove", "Queensfields"],
 "npcs": ["Flitter", "Camellia", "Queen Valerian", "Quills", "Helga", "Cakenstein"],
 "quests": ["Sanctuary Birthday Invitation (quest objective text, locale:428074; exact quest title not confirmed)"],
 "activities": [
  "Trade for and hand out daily Birthday invitations with Flitter in Sanctuary, repeatable once per day (wiki Birthday Bash; locale:4952 'Invite someone to the birthday bash!')",
  "Invitation contest: having more invitations than Flitter earns a special prize (article 1282; locale:428074)",
  "Cake bake-off: help chefs for Camellia, repeatable daily (locale:707; wiki Birthday Bash)",
  "Daily party-prep quests (article 2580)",
  "Balloon trading with Quills in Sanctuary (article 1282)",
  "Cakenstein boss fights in Sanctuary and Queensfields, 2010 (article 1282 summary)",
  "Cakenstein minigame in Sacred Grove, 2012 (article 2580)",
  "Dancing and socializing at the Birthday Bash area in Sanctuary, 2013 (article 2924)"
 ],
 "items": [
  {"name": "Birthday Party Balloons", "price": null, "currency": null, "source": "locale:14427 ('Nothing says Birthday Bash like party balloons.')"},
  {"name": "Balloon Hammer / Balloon Wand / Balloon Bow / Balloon Axe", "price": null, "currency": null, "source": "wiki Balloon Bow, Balloon Hammer, Balloon Axe (versions of Gifting Piñata; 'available during 2011 Birthday Bash')"},
  {"name": "Gifting Piñata", "price": null, "currency": "station_cash", "source": "wiki Gifting Piñata ('sold through the Station Cash Marketplace during the 2011 Birthday Bash'); price not found"},
  {"name": "Birthday T-Shirts (e.g. Sanctuary Birthday T-Shirt)", "price": null, "currency": null, "source": "wiki Category:[Birthday] [Bash] (Sanctuary Birthday T-Shirt: 'acquired during the Birthday Bash event')"},
  {"name": "Birthday Bash Furniture (Wall Sconce, Chair, Floor Lamp, Dining Table, Bed, Sofa, Bundle)", "price": null, "currency": null, "source": "wiki Marketplace listings in Update of April 24, 2012 (wiki Template:News/Archive); locale:691, 666, 436980-437014 (names only)"}
 ],
 "rewards": [
  "Birthday Cake hat (free login during the 2012 Bash, article 2580)",
  "Flitter's special prize for holding more invitations than Flitter (article 1282; prize unnamed in any source)"
 ],
 "evidence": [
  {"claim": "The invitation contest is a daily sub-activity of the Birthday Bash, with Flitter as a rival who gives the invitations.", "source": "http://www.freerealms.com/article/detail.action?articleId=1282 (quote: 'When you've gotten more invitations than Flitter, head back and you'll get a special prize!'); locale:4952; locale:428074"},
  {"claim": "Birthday invitations come from Flitter in Sanctuary, repeatable once per day.", "source": "wiki Birthday Bash"},
  {"claim": "The 2012 Bash was the 3rd anniversary and ran through May 24, 2012.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580; locale:695"},
  {"claim": "The 4th birthday was April 29, 2013, with a Birthday Bash area in Sanctuary.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2924"},
  {"claim": "The Bash is tied to the April 29 anniversary.", "source": "wiki Category:Birthday Bash Weapons"},
  {"claim": "A 2011 Birthday Bash existed.", "source": "wiki Gifting Piñata; wiki Balloon Bow"},
  {"claim": "Cake bake-off hosted by Camellia in Sanctuary.", "source": "locale:707; wiki Birthday Bash"},
  {"claim": "Birthday Party Balloons is a Bash item.", "source": "locale:14427"}
 ],
 "confidence": 0.45,
 "open": [
  "Not wireable as a calendar entry: only the 2012 end date (May 24) and 2013 date (April 29) are sourced. 2010 is undated (article 1282 has no date); 2011 has no dates. Article 1267 and 1330 (pack's April 22 / April 29-May 10 dates) were not found, so those dates are excluded.",
  "Summer Splash is a separate Seaside event (locale 399659-400900 'Seaside Summer Splash'). locale:19968 'Making this Birthday Bash a Summer Splash' is a single client line that ties the Bash name to Summer Splash, unresolved; Summer Splash is excluded from this calendar.",
  "Birthday Party Balloons 4-Pack (locale:14423) is name-only. Its link to a Cakenstein minigame reward is NOT confirmed; article 2580 as checked shows no balloon reward. Dropped from items and rewards. Birthday Party Balloons 3-Pack (locale:14422) also excluded as unconfirmed.",
  "Birthday Party Crate (locale:5664) dropped: no source ties it to the Bash.",
  "Bake-off host conflict: Camellia (article 1282, locale:707) vs Queen Valerian (article 2580). Both kept as sourced; not reconciled.",
  "Cakenstein location conflict: 2010 boss fights in Sanctuary and Queensfields vs 2012 minigame in Sacred Grove. Not reconciled.",
  "Flitter's special prize is unnamed in any source.",
  "Exact quest titles ('Birthday Invitation', 'Birthday Bash!') are not confirmed; only the objective text 'Sanctuary Birthday Invitation' (locale:428074) was found.",
  "Gifting Piñata price not found.",
  "Articles 1261, 2106, 2107 mention Cakenstein party battles but no year was assigned; not read.",
  "Birthday Hide and Seek, Birthday Party Hat/Banner/Guest NPC, Birthday Cake food, and 'Finding Flitter' (NOT LIVE) excluded as unconfirmed for this event.",
  "Kind 'holiday' chosen; 'community' is a plausible alternative."
 ]
}
