<!-- fleet job=citem-infer id=cgemstone-axe-139932-v4 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[6697, 7939, 6, 1605] model=claude-haiku-5-5 -->
# Gemstone Axe

{"item": {"name": "Gemstone Axe", "locale_id": 139932, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only; no NPC, quest, vendor, or enemy named by any source", "where": null, "price": null, "currency": null, "source": "wiki page 'Gemstone Axe' (\"can only be acquired through trade\")"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client name Gemstone Axe, locale 139932, item definition 48182, weapon slot 7, class 17, model axe_ar_ag_weapon_battleaxe.adr; one definition, no variants", "source": "locale:139932 (client definition)"},
  {"claim": "Level 5 Warrior weapon, Blue Text, 'can only be acquired through trade'; Sweeping Slash 853 dmg, Spinning Attack 1548 dmg", "source": "wiki page 'Gemstone Axe'"},
  {"claim": "Wiki categories include Retired Weapons and Blue Text Weapons, which marks the item retired", "source": "wiki page 'Gemstone Axe' categories"},
  {"claim": "Axe is listed in the Gemstone weapon group (Bow, Kendama Hammer, Scalpel, Blade, Wand) on the Blue Text weapon page", "source": "wiki page 'Blue Text weapon'"},
  {"claim": "A coin-store row for item 48182 exists at 811 purchase / 729 member / 81 sell, but it sits in a uniform source_tags block (48170-48191) with no vendor, wiki price, image, or video confirming a sale. Not used as a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json:13231"},
  {"claim": "Wiki 'Blacksmith' page lists a 'Blacksmith: [Gemstone] Roundup' quest title, but no quest text or reward names the axe", "source": "wiki page 'Blacksmith' (lookup)"}
 ],
 "confidence": 0.4,
 "open": [
  "Conflict: stores.json:13231 shows an 811-coin purchase row for 48182, but it is part of a uniform block with identical tags to neighbours and contradicts the wiki's trade-only statement. Not recorded as a coin_shop source. Confirm with a live vendor or wiki price before wiring as a sale.",
  "The 'Blacksmith: [Gemstone] Roundup' quest has not been checked for an axe reward; no evidence either way.",
  "The 'Blue Text weapons were members-only dungeon drops' claim was removed: the generic Blue Text page names no drop source for this axe.",
  "The 81 coin sell value is not supported by any image (the pack's images array was empty); it appears only in stores.json:13231.",
  "No retirement date is given by any source. Treated as unobtainable now because the wiki marks it Retired.",
  "Wireable: false. Only the trade line is evidenced, with no price or counterparty."
 ],
 "wireable": false,
 "confidence_note": "Trade-only acquisition is evidenced by the wiki; no priced source is confirmed."}
