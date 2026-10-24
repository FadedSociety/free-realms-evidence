<!-- fleet job=citem-infer id=cantibiotic-medic-cap-133101-v2 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6296, 10703, 6, 2179] model=claude-haiku-5-5 -->
# Antibiotic Medic Cap

{"item": {"name": "Antibiotic Medic Cap", "locale_id": 133101, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Bev (Medic job merchant; sells exclusively [Medic] job items; the wiki 'Sells' list includes [Antibiotic] [Medic] [Cap])", "where": "Wugachug (Wugachug Brewery / Cooking Table area, per the previous answer's wiki Merchants note)", "price": "453 coins purchase (store data); member price 407 coins (10% member discount); sell-back 45 coins", "currency": "coins", "source": "wiki page Bev (https://freerealms.fandom.com/wiki/Bev); repo:prototype/osfr-tools/data/content/stores.json items 76093, 79154, 79155 (lines 15805 for 76093, 16918-16919 for the other two) at 453/407/45. Which of the three tint definitions Bev sells is unresolved (repo:prototype/osfr-tools/data/content/vendors_unresolved.json ~line 10152-10160, ambiguous_item_id)."},
  {"type": "prize_wheel", "detail": "[Medic] Prize Wheel at Danger Peaks (one roll per wheel spin; the cap is one of five Medic-wheel garment/item entries)", "where": "Danger Peaks (dungeon)", "price": "One wheel roll costs 70 Coins; this is the whole-wheel price, not a per-item price", "currency": "coins", "source": "wiki page Danger Peaks ('[Medic] Prize Wheel' section lists '[Antibiotic] [Medic] [Cap]' and '70 Coins'); repo:notes/Build Guides/Content/Dungeons/Danger Peaks.md:63 and :69"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Antibiotic Medic Cap' is locale 133101, part of the Antibiotic Medic garment set (shirt, pants, gloves, boots, backpack, cap).", "source": "locale:133101; locale:133098-133103"},
  {"claim": "Bev's wiki 'Sells' list includes [Antibiotic] [Medic] [Cap]; the page says she sells exclusively Medic job items.", "source": "wiki page Bev"},
  {"claim": "Store data prices definitions 76093, 79154, 79155 at 453 coins purchase, 407 member, 45 sell-back.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 15805 (76093); lines 16918-16919 (79154, 79155)"},
  {"claim": "The Danger Peaks [Medic] Prize Wheel lists the Antibiotic Medic Cap; the wheel carries a 70 Coins roll slot.", "source": "wiki page Danger Peaks; repo:notes/Build Guides/Content/Dungeons/Danger Peaks.md:63, :69"}
 ],
 "confidence": 0.6,
 "open": [
  "Bonus-goal clothing drop removed: the wiki lists the Medic bonus set only as 'Antibiotic or Urgent Care' with no piece list, and the cited video frame shows a backpack, not the cap. Not evidenced as a drop.",
  "Vendor price 453 is for one of three tint definitions (76093, 79154, 79155); the store row does not say which tint Bev sells. All three share the 453/407/45 price, so the price holds regardless.",
  "The 2013 Bev sale date (repo NPCs - Wugachug.md:80) was not re-checked in this pass; it is a repo note, not a wiki price.",
  "The 407 member price and 45 sell-back are store-data values, not wiki-confirmed. No wiki sale price exists to compare.",
  "No source states whether Bev or the Danger Peaks wheel still offers the cap after 2013-2014, so retired is null and live is 'unsure' despite the first-pass 'yes'.",
  "Client description is empty; nothing to check."
 ]
}
