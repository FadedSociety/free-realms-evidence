<!-- fleet job=citem-infer id=c60-slot-bank-upgrade-8-19886-v2 status=done turns=4 usd=0.0025 tokens(read,write,in,out)=[25582, 9856, 10, 2059] model=claude-haiku-5-5 -->
# 60-Slot Bank Upgrade 8

{"item": {"name": "60-Slot Bank Upgrade 8", "locale_id": 19886, "kind": "other"},
 "sources": [{"type": "coin_shop", "detail": "Bank capacity upgrade: 60-Slot Bank Upgrade 8 (+60 bank slots, requires Upgrade 7 first). Channel not confirmed for this tier: the wiki Banking page says slots are sold through the Station Cash Marketplace or the Coin Shop, and that Coin Shop upgrades must be bought in order.", "where": "Coin Shop or SC Marketplace (unconfirmed which)", "price": null, "currency": null, "source": "wiki page 'Banking' (tier table row '[60]-Slot Bank Upgrade 8'; sales-channel sentence); locale:19887"}],
 "retired": null, "live": "yes",
 "evidence": [
  {"claim": "Item name and description: '60-Slot Bank Upgrade 8' with description 'This upgrade will increase your bank capacity by 60 slots. You must buy Upgrade 7 before Upgrade 8.'", "source": "locale:19886; locale:19887; client definition 35860 (one definition, slot 0, no models, no coin store price in client data)"},
  {"claim": "The wiki Banking page lists '60-Slot Bank Upgrade 8' in its upgrade table, after the 40-Slot Upgrade 7 row.", "source": "wiki page: Banking (lookup 'Bank Upgrade 8 60 slots')"},
  {"claim": "Bank slots are sold through the Station Cash Marketplace or the Coin Shop; Coin Shop upgrades must be bought in chronological order.", "source": "wiki page: Banking"},
  {"claim": "Repo notes give bank tiers as coin purchases (2 slots for 1,000 coins up to 100 slots for 50,000) and a 50-slot upgrade for 100 SC, but the notes say the tier text is unclear. Not used as a price for this item.", "source": "notes/Build Guides/Gameplay/Coin Store and Purchases.md:193"},
  {"claim": "The client also has other 'Upgrade 8' bank names (10-slot at locale:14133/14134, 50-slot at locale:19910/19911). Those are separate items, not this 60-slot one.", "source": "locale:14133, 14134, 19910, 19911 (as cited in the prior critique; not re-read here)"}
 ],
 "confidence": 0.4,
 "open": [
  "Price and currency unverified. The wiki Banking row for the 60-slot tier was cut off in the lookup snippet, and the full page was not retrievable (refs wiki/Banking is not a file). Pull that row to get the coin or SC price.",
  "Channel unconfirmed: the wiki says the Coin Shop or the SC Marketplace sells bank slots, but the snippet does not name the channel for this tier. The coin_shop type above is a best guess; a marketplace-only sale is possible.",
  "Retirement status not sourced either way.",
  "No vendor stock, quest reward, drop or event source found. Banker NPCs provide storage, not this upgrade. The first-pass 'vendor' guess has no stock row.",
  "locale:19917 is a placeholder (negative slot count) and is excluded from evidence.",
  "Critique fix applied: the prior 'consistent chain' claim is dropped; the Upgrade 8 name conflicts (10/50/60 slots) are noted above."
 ]}
