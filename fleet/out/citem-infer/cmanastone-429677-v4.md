<!-- fleet job=citem-infer id=cmanastone-429677-v4 status=nothing_found turns=2 usd=0.0024 tokens(read,write,in,out)=[6448, 11620, 6, 1832] model=claude-haiku-5-5 -->
# Manastone

{"item": {"name": "Manastone Eye Color Card", "locale_id": 414190, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Locale 414190 is 'Manastone Eye Color Card', the client name of item 36002 (tint 72).", "source": "locale:414190"},
  {"claim": "stores.json item 36002 is in category 143, purchase_price_coins 90, member_price_coins 81, sell_price_coins null, no_sale true. The identical row covers items 35982-36002 and 79481-79489, so it is a category default and not an item-specific price. no_sale=true means no current coin sale is recorded.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11706-11734 (item 36002 at line 11725)"},
  {"claim": "Bundle 3519 names the card (GameItemId 3080 / MarketingItemId 36002, LaunchTime 2009-11-29, ExpireTime 2040-08-15). CurrencyType and Price fields are undecoded, so the bundle gives no price.", "source": "refs:Lxzxrus-Free-Realms-Server/src/Resources/StoreBundles.json:12200-12225"},
  {"claim": "No wiki page, article, video frame, quest, drop or event names this card.", "source": "lookup wiki/articles/video 'Manastone Eye Color' (only hit: locale:414190)"},
  {"claim": "Locale 429677 'Manastone' is a flagged cosmetic fragment and is not used as evidence. Definition 77620 shares the name and tint but its link to item 36002 is unresolved, so it is excluded.", "source": "locale:429677 (flagged); definition 77620 (unlinked)"}
 ],
 "confidence": 0.2,
 "open": [
  "No vendor, NPC, store or quest source is evidenced. The 90-coin price is a category-143 default with no_sale=true, not a sale price for this item, so no price or currency is given.",
  "Bundle 3519 CurrencyType 1 / Price 1 / AltCurrencyPrice 1 are undecoded and are not treated as prices.",
  "Definition 77620 ('Manastone', locale 429677, tint 72) may be a separate sold form or an alias. Unresolved.",
  "'consumable' rests only on client Type 12 and SingleUse. It may be a cosmetic eye-tint unlock; no wiki or article confirms its use.",
  "Live status and retirement are unverified. The 2040 ExpireTime is data, not proof of sale."
 ]}
