<!-- fleet job=citem-infer id=celite-pink-twisted-blade-11014-v1 status=done turns=6 usd=0.0037 tokens(read,write,in,out)=[45111, 14105, 14, 3033] model=claude-haiku-5-5 -->
# Elite Pink Twisted Blade

{"item": {"name": "Elite Pink Twisted Blade", "locale_id": 11014, "kind": "weapon"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale of item 4872 (Ninja Level 4 weapon, Elite Pink Twisted Blade). The store row gives no vendor name, so the NPC is unconfirmed; the wiki ties the base Twisted Blade to Ned in Blackspore, which is not proven for this tint.", "where": "Blackspore (unconfirmed)", "price": "640 coins (member price 576 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 4872 (line 927; category 207, purchase_price_coins 640)"},
  {"type": "vendor", "detail": "Ned (weapon vendor), base Twisted Blade sale; the elite tint is not named on the wiki page", "where": "Blackspore", "price": "coins (amount truncated in the wiki extract; the store row for this tint says 640 coins)", "currency": "coins", "source": "wiki page 'Twisted Blade' (lookup result: 'It was previously sold by Ned in Blackspore for [coins], until retired on December 14, 2009.')"}
 ],
 "retired": true,
 "live": "no",
 "evidence": [
  {"claim": "Client text: item 11014 is 'Elite Pink Twisted Blade', sitting with 'Twisted Blade' (11009) and 'Elite Black Twisted Blade' (11015).", "source": "locale:11014; locale:11009; locale:11015"},
  {"claim": "Client definition 4872 is in slot 7, class 6, model sword_ar_ag_weapon_twistedblade.adr, and has a coin store price of 640.", "source": "repo:prototype/osfr-tools/data/content/stores.json:927 (item 4872, category 207, purchase_price_coins 640, member_price_coins 576, sell_price_coins 64)"},
  {"claim": "The Twisted Blade family (level 4 Ninja weapon) was sold for coins by Ned in Blackspore and retired on December 14, 2009. The wiki says it is now only available through trade.", "source": "wiki page 'Twisted Blade'"},
  {"claim": "Sister tints 4867-4869 (plain Twisted Blade) are priced at 225 coins in the same category, and 4872 is priced at 640 coins, so the elite tint costs more than the base.", "source": "repo:prototype/osfr-tools/data/content/stores.json:924-927"},
  {"claim": "The T633 resale note on the store row (64 coins) follows the sell_price rule Cost // 10, not a verified retail price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:34 and :927"}
 ],
 "confidence": 0.6,
 "open": [
  "The vendor for item 4872 is not named in the store data. Ned in Blackspore is the base Twisted Blade vendor per the wiki; whether Ned also sold the Elite Pink tint is not confirmed.",
  "The wiki extract truncates the coin price for the base blade, so only the store row's 640 coins is available for the elite tint.",
  "No wiki page, video, or article covers the Elite Pink tint by name. Its retirement date is inferred from the base Twisted Blade page (Dec 14, 2009), not from its own source.",
  "The 576-coin member price is derived from the 10% member discount in the store data, not from a separate source.",
  "The 'live' value is 'no' because the base blade is retired and only obtainable via trade. The jev tag says 'yes', but that tag is a guess and no source confirms it."
 ]}
