<!-- fleet job=item-infer id=istupendous-spandex-chestpiece-v2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[4979, 6262, 6, 1638] model=claude-haiku-5-5 -->
# Stupendous Spandex Chestpiece

{"item": {"name": "Stupendous Spandex Chestpiece", "locale_id": 5103045, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin Shop purchase during HeroRealms Month (Hero vs. Villain month-long event, introduced in-game January 14, 2014); listed in the HeroRealms Month 'Coin Shop HeroRealms gear sets' as the [Stupendous] set's chest piece. Members get a 10% discount price (merged membership tier, not a separate source).", "where": "Coin Shop", "price": null, "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Stupendous_Spandex_Chestpiece (categories: Coin Shop, Coin Shop Clothing, HeroRealms Month); https://freerealms.fandom.com/wiki/HeroRealms_Month"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Any Job, chest slot, clothing item, available during HeroRealms Month to everyone via the Coin Shop; Members get a 10% discount price", "source": "https://freerealms.fandom.com/wiki/Stupendous_Spandex_Chestpiece"},
  {"claim": "Introduced in-game January 14, 2014 as part of HeroRealms Month", "source": "https://freerealms.fandom.com/wiki/Stupendous_Spandex_Chestpiece"},
  {"claim": "Grants Gleam Strength buff (+10% Health) during HeroRealms Month", "source": "https://freerealms.fandom.com/wiki/Stupendous_Spandex_Chestpiece (igd and Passive Effects)"},
  {"claim": "Name string for the item", "source": "locale:5103045"},
  {"claim": "HeroRealms Month lists the Spandex Chestpiece in the Coin Shop HeroRealms gear sets", "source": "https://freerealms.fandom.com/wiki/HeroRealms_Month"},
  {"claim": "Stupendous Silver Spandex Chestpiece (locale:5103092) is a different item: a Trading Card Game Series 5 loot-card reward, not this Coin Shop item", "source": "https://freerealms.fandom.com/wiki/Stupendous_Silver_Spandex_Chestpiece; locale:5103092"}
 ],
 "confidence": 0.5,
 "open": [
  "Price not confirmed. The wiki price sentence is stripped ('at the regular price of , ... 10% discount price of .'). The page's coin list gives [10, 9], but which is regular and which is member is not stated in any readable text, so price is left null. Needs a readable source before setting 10 coins regular / 9 coins member.",
  "Retirement not confirmed. The item is tied to HeroRealms Month (January 2014) and is likely no longer sold, but no source in the pack states when it left the Coin Shop. Live status is unsure.",
  "No quest, drop, prize wheel, crafting, or other non-Coin-Shop source found in the pack or repo (repo search for 'Spandex' only hits unrelated Astonishing entries in vendors_unresolved.json).",
  "Critique fix applied: the membership entry was merged into the single Coin Shop source rather than listed separately."
 ]}
