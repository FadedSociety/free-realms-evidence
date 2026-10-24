<!-- fleet job=citem-infer id=cparty-blade-139943-v1 status=done turns=4 usd=0.0037 tokens(read,write,in,out)=[22381, 16866, 10, 2821] model=claude-haiku-5-5 -->
# Party Blade

{"item": {"name": "Party Blade", "locale_id": 139943, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin vendor: store record for item 48193 (weapon store category 207), 811 coins. The vendor NPC and zone are not identified in the store data.", "where": null, "price": "811 coins (member price 729 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48193 (line 13242)"},
  {"type": "other", "detail": "Player-to-player trade only, per the wiki. This is not a shop source; listed here for completeness.", "where": null, "price": null, "currency": null, "source": "wiki: Party Blade (\"can only be acquired through trade\")"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Party Blade is a level 5 Ninja weapon (Blue Text, Power 3, Dragonstrike), with Flame Flash 776 damage and Dragonstrike 3492 damage.", "source": "wiki: Party Blade"},
  {"claim": "The wiki page is in Category:Retired Weapons.", "source": "wiki: Party Blade (categories)"},
  {"claim": "The wiki says the weapon can only be acquired through trade, which implies it is no longer sold.", "source": "wiki: Party Blade"},
  {"claim": "The client defines it as definition 48193, slot 7, class 6, model sword_ar_ag_weapon_twistedblade.adr, with one variant. The client name is locale 139943.", "source": "client definition in the evidence pack; locale:139943"},
  {"claim": "Store data prices definition 48193 at 811 coins in weapon category 207. Other items in that category (48172-48196) share the 811 price, and some items are priced at 640, 1236, 1656 and 2204.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 48193"},
  {"claim": "The wiki's Blue Text weapon page says Blue Text weapons were members-only weapons acquired in dungeons where they were dropped, and that they were retired.", "source": "wiki: Blue Text weapon"},
  {"claim": "The Party Blade name sits in a client cluster with Party Axe, Party Bow, Party Wand, Party Scalpel, Party Kendama Hammer, Confetti Axe, Confetti Wand, Carbon Bow, Carbon Kendama and Carbon Scalpel (locale 139938-139948). This suggests a shared party or event set, but no source names that event.", "source": "locale:139938 through locale:139948"}
 ],
 "confidence": 0.3,
 "open": [
  "The vendor that sells item 48193 at 811 coins is not identified. Store category 207 has no vendor name in the repo data, so the vendor and zone are unknown.",
  "The wiki says trade only, while the Blue Text page says dungeon drops. These conflict. No drop enemy or dungeon is named for Party Blade, so no drop source is listed.",
  "The 'Party' cluster may be a birthday or anniversary event set. The fan article only says birthday gifts include balloon weapons, which does not name Party Blade. The event is unconfirmed, so no event source is listed.",
  "The retirement date is not given. The wiki says Retired, and the Ninja weapons sold by vendors were retired 14 Dec 2009, but that date is not sourced for this item.",
  "The client's own description is empty, so no in-game text backs up the claims."
 ]}
