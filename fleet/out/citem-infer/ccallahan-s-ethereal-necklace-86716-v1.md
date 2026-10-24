<!-- fleet job=citem-infer id=ccallahan-s-ethereal-necklace-86716-v1 status=nothing_found turns=11 usd=0.0111 tokens(read,write,in,out)=[264193, 41531, 24, 6569] model=claude-haiku-5-5 -->
# Callahan's Ethereal Necklace

{"item": {"name": "Callahan's Ethereal Necklace", "locale_id": 86716, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: Id 22725, NameId 86716, Slot 9 (Accessory2, Necklace), Class 43, CategoryId 108, NoTrade, NoSale, Rarity 3, PowerRating 5, Cost 563, MemberDiscount 10, no coin store price in the pack.", "source": "refs:Lxzxrus-Free-Realms-Server/src/Resources/ClientItemDefinitions.json (entries Callahan's Fateful/Infernal Necklace ids 22718-22719 use the same field pattern; the Ethereal entry is the 22725 block)"},
  {"claim": "The name is locale:86716 \"Callahan's Ethereal Necklace\"; it sits in a cluster 86711-86721 of Callahan/Kai necklaces (Spectral, Mystical, Phantasmal, Eternal, Celestial, Unearthly, Cosmic, Fiendish, Corporeal, Kai's Fateful).", "source": "locale:86716 and neighbours 86711-86721"},
  {"claim": "A matching Callahan's Ethereal Ring exists (client id 22490, NameId 86481) with the same Cost 563, NoTrade and NoSale flags, so the Callahan family is a ring/necklace pair across tiers.", "source": "FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json line 465933"},
  {"claim": "Callahan's Ethereal Necklace is not named in any wiki page, wiki image, article fact, or video frame. The only Callahan item the wiki covers is Callahan's Cutter, a Medic weapon from the quest Medic: Paying Your Student Debts, which is not this item.", "source": "lookup wiki 'Callahan' (page:ns0 Callahan's Cutter); repo search for 22725/86716 found no match"},
  {"claim": "The Callahan's Tempered Circle Shard (locale 3404) is a separate item family that the wiki ties to the Daily Wheel Shards wedge; it is not a source for the necklace.", "source": "locale:3404; wiki 'Amplifier Tempered Circle Shard' (acquired from the Daily Wheel, Shards wedge)"},
  {"claim": "The 'Polished ... Necklace' family (Polished Ethereal Necklace locale:89329, Polished Fateful Necklace 89322) is a different set, dropped by Consumed by the Past and the Wraiths of Wrath minigame per video frames. It is not the Callahan line.", "source": "locale:89329, locale:89322; video:8F4ZomE2kxI/00026, 00028, 00362"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found. The client defines the item and the pack has no vendor, quest, drop, event, prize-wheel, crafting, or coin-shop evidence for it. Nothing was added to sources.",
  "No coin store price: the pack's coin_store_prices is empty and repo stores.json has no entry for 22725.",
  "Retired status is unknown. The item is NoSale and NoTrade, which fits a tiered reward item, but no source states when or whether it was removed.",
  "Jev's first-pass 'live: yes, source_guess: drop' is a hint only and is not confirmed by any source here.",
  "Still to check: whether the Callahan family (Ring 22490, Necklaces 22718-22727) is a named reward tier from a specific event or the Wraiths/Consumed by the Past line. Check the Legacy repo for loot or reward tables that reference the 2271x-2272x ids, and check the wiki Prize Wheel and Daily Wheel pages for the family names."
 ]}
