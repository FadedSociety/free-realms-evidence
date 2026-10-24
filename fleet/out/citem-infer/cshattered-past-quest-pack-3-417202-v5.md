<!-- fleet job=citem-infer id=cshattered-past-quest-pack-3-417202-v5 status=done turns=2 usd=0.0030 tokens(read,write,in,out)=[6843, 14768, 6, 2207] model=claude-haiku-5-5 -->
# Shattered Past - Quest Pack 3

{"item": {"name": "Shattered Past - Quest Pack 3", "locale_id": 417202, "kind": "other"},
 "sources": [
  {"type": "marketplace", "detail": "Sold only inside the 'Shattered Past - Quest Bundle' (Quest Packs 1-3 bought together). No per-pack price is evidenced; 650 SC is the bundle price for all three packs, not Pack 3's price.", "where": "Station Cash marketplace (bundle listing)", "price": "bundle only: 650 SC for Packs 1-3 together (saves 100 SC); no per-pack price", "currency": "station_cash", "source": "locale:156877 (bundle price, 100 SC saving); locale:156876 (bundle title); locale:156878 and locale:417205 ('This item is also included in the Shattered Past - Quest Bundle')"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 62541 names the item with name_locale_id 417202, the text 'Shattered Past - Quest Pack 3'. The string is flagged placeholder (store listing), so it is a name pointer only.", "source": "locale:417202; client definition 62541"},
  {"claim": "The Pack 3 quest text (Tyrone Shadowshard, Blackspore, south of the Ancient's Wall, Card Duelist) is at locale:417205 and gates on completing 'Shattered Past Quest Pack 2'. It says the item is also in the Shattered Past - Quest Bundle. Locale 156878 is the same chapter text, not a title and not a price.", "source": "locale:417205; locale:156878"},
  {"claim": "The bundle text sells Packs 1-3 together for 650 SC, a 100 SC saving. It does not price Pack 3 alone.", "source": "locale:156877; locale:156876"},
  {"claim": "Snowhill promo (Card Duelist promo cards) requires having purchased and completed Quest Pack 3 and reaching Level 20 Card Duelist. This is a content gate, not sale evidence.", "source": "locale:2164"},
  {"claim": "Repo stores.json has no row for definition 62541 and the client definition has empty coin_store_prices, so no coin-vendor sale is evidenced.", "source": "repo:prototype/osfr-tools/data/content/stores.json (no match for 62541); client definition 62541"},
  {"claim": "Card Duelist build guide lists Pack 3 only as a quest gate (Dark Deal, row 43) and gives no giver or sale channel for the pack.", "source": "notes/Build Guides/Content/Jobs/Card Duelist.md:143"},
  {"claim": "Pack chain: Pack 1 (Dominic, locale:417204, gated on nothing) -> Pack 2 -> Pack 3 (Tyrone, locale:417205) -> Snowhill promo (locale:2164).", "source": "locale:417204; locale:417205; locale:2164"}
 ],
 "confidence": 0.4,
 "open": [
  "Pack 3's own price is unknown. The only price is the three-pack bundle at 650 SC; do not read it as Pack 3's price.",
  "Live status is unproven. The bundle is client text only; no stores.json row or sale record confirms it is currently sold.",
  "locale_id 417202 is a FLAGGED placeholder store listing, so it is only a name pointer. The unflagged in-game title is not confirmed. Locale 156878 is the Pack 3 description, not a title, so the previous answer's locale_id was wrong.",
  "No vendor, drop, prize-wheel, crafting or quest-reward source is evidenced. Pack 3 is a quest-content unlock sold only through the bundle, if at all.",
  "Retired status is unknown; no source calls Pack 3 retired or unobtainable.",
  "Kind is left as 'other' (quest-content pack). The first-pass 'quest_item' hint is not evidenced beyond the description text."
 ]}
