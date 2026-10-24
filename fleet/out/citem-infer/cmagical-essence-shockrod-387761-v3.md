<!-- fleet job=citem-infer id=cmagical-essence-shockrod-387761-v3 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6731, 10105, 6, 1647] model=claude-haiku-5-5 -->
# Magical Essence Shockrod

{"item": {"name": "Magical Essence Shockrod", "locale_id": 387761, "kind": "weapon"},
 "sources": [
  {"type": "collection", "detail": "Reward for completing the Medic Magical Essences collection (a collection of magical shock rod essences). The number of essences required is not stated on the wiki.", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Magical_Essence_Shockrod; https://freerealms.fandom.com/wiki/Medic_Magical_Essences; locale:132460 (\"This item can be added to the Medic Magical Essences Collection\")"}
 ],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Level 20 Medic weapon, Power 5, Cannot Trade; acquired by completing the collection Medic Magical Essences", "source": "https://freerealms.fandom.com/wiki/Magical_Essence_Shockrod"},
  {"claim": "Medic Magical Essences is a wiki collection of magical shock rod essences, listed under Medic collections on List of Collections", "source": "https://freerealms.fandom.com/wiki/Medic_Magical_Essences; https://freerealms.fandom.com/wiki/List_of_Collections"},
  {"claim": "Client name is locale 387761 'Magical Essence Shockrod'; definition 55816, slot 7, class 20, model club_ar_ag_weapon_shockrod.adr", "source": "locale:387761"},
  {"claim": "Wiki tooltip shows Resell Value 236, matching the store sell price of 236", "source": "image:item_tooltip Magical Essence Shockrod; repo:prototype/osfr-tools/data/content/stores.json:13978"},
  {"claim": "Store row for item 55816 (category 207) lists 2363 coins, member price 2126, sell 236, but names no vendor, shop or stock location; the same 2363 price is shared by about a dozen neighbouring essence/weapon rows (stores.json:13977-13983) with generic source_tags, so the row shows a price, not a confirmed vendor sale. Not used as a source.", "source": "repo:prototype/osfr-tools/data/content/stores.json:13977-13983"},
  {"claim": "The earlier 'four essence items' count and the Medic Materials crate mechanic are not supported by any source in the pack; removed from the detail", "source": "critiques (evidence, world lenses); wiki Medic_Magical_Essences"}
 ],
 "confidence": 0.6,
 "open": [
  "Coin vendor sale not confirmed: the store row (stores.json:13978, category 207, 2363 coins / member 2126 / sell 236) has no resolved vendor and no wiki sale page. Kept out of sources until a vendor is identified. If one is found, it would be a coin_shop source at 2363 coins (member 2126).",
  "Number of essences required for the collection, and how essences are obtained (crate clicks in dungeons, per an earlier unverified note), are not stated in the pack. Needs a Medic job note or dungeon video citation before adding.",
  "Retirement not stated by any source; live is yes from the wiki page and client definition only."
 ]}
