<!-- fleet job=citem-infer id=cnature-s-stem-46861-v3 status=done turns=3 usd=0.0032 tokens(read,write,in,out)=[19968, 14963, 8, 2257] model=claude-haiku-5-5 -->
# Nature's Stem

{"item": {"name": "Nature's Stem", "locale_id": 46861, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only (no vendor, store, quest or event source documented)", "where": null, "price": null, "currency": null, "source": "wiki page: Nature's Stem ('can only be acquired through trade'); wiki Category:Blue Text Weapons ('They are currently only acquired through trade')"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Nature's Stem is a level 1 Brawler, Power 2 Blue Text weapon with Glancing Blow (444 damage) and Leg Sweep (1554 damage).", "source": "wiki page: Nature's Stem; repo:prototype/osfr-tools/data/reference/weapons.json:30797-30836"},
  {"claim": "Blue Text weapons were members-only weapons acquired in dungeons, dropped at random by certain 'boss' enemies; on December 14, 2009 they were retired and renamed to white font.", "source": "wiki Category:Blue Text Weapons; wiki page: Blue Text weapon"},
  {"claim": "The Blue Text category states that these weapons are currently only acquired through trade (the category, not just the item page, carries this wording).", "source": "wiki Category:Blue Text Weapons"},
  {"claim": "Nature's Stem carries the Retired Weapons category.", "source": "wiki page: Nature's Stem (category tags)"},
  {"claim": "Client name entry locale:46861 is \"Nature's Stem\", item definition 22111, class 71, slot 7. The client definition has no coin store price, so no coin vendor sale is evidenced.", "source": "locale:46861; client definition in evidence pack"},
  {"claim": "The reference record gives a client item cost of 640 for definition 22111. This is an internal cost field, not a store listing or price, and no currency is stated.", "source": "repo:prototype/osfr-tools/data/reference/weapons.json:30833"}
 ],
 "confidence": 0.6,
 "open": [
  "The original boss-drop acquisition (random drops from unnamed 'boss' enemies in dungeons) is documented only at the Blue Text class level (category and 'Blue Text weapon' page). Nothing names this item, its boss, its dungeon or a drop rate, so it is not listed as a source for Nature's Stem.",
  "The trade-only status is current-as-of-the-wiki and carries no price, counterparty or trade venue. Whether it was ever sold in a coin or Station Cash store is not evidenced.",
  "The client cost of 640 (weapons.json) has no currency or source. It is not treated as a price until confirmed.",
  "Sister items Juiced Anvil (locale:46859) and the other 'Juiced', 'Bubbleburst' and 'Nature's' names were not verified as trade-only. The 'set' grouping is not tied to an event or promotion.",
  "The client description is empty.",
  "Wiki image files File:Nature's Stem item.jpg and File:Nature's Stem held.jpg were not inspected.",
  "The earlier pack's drop source is treated as class-level and unverified for this item, and wireable is false: no source carries a price, quest, enemy or event a builder can set."
 ]}
