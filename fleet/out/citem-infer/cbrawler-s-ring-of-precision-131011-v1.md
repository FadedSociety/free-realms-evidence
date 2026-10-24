<!-- fleet job=citem-infer id=cbrawler-s-ring-of-precision-131011-v1 status=done turns=9 usd=0.0083 tokens(read,write,in,out)=[154193, 34443, 20, 4903] model=claude-haiku-5-5 -->
# Brawler's Ring of Precision

{"item": {"name": "Brawler's Ring of Precision", "locale_id": 131011, "kind": "other"},
 "sources": [{"type": "prize_wheel", "detail": "Snowy Canyon prize wheel, Brawler slot (one of the six job-specific wheel items, alongside the Battle Item Mystery Pack, Brawler's Atlas Hammer of Rumbling, Brawler's Necklace of Vitality V, Brawler's Power Shard of Regeneration V and Power Punch Brawler Helmet). The wheel is won by completing the Snowy Canyon battle; a prize is one slot per win, not a purchase.", "where": "Snowy Canyon (Snowhill, difficulty 5, 'Levels 13 or higher'; entrance: barrier/gate in Snowhill)", "price": null, "currency": null, "source": "wiki: Snowy Canyon page (Brawler [Prize] Wheel section, lists Brawler's Ring of Precision); repo:notes/Build Guides/Content/Dungeons/Snowy Canyon.md:93 (Prize wheel by job, Brawler row, wiki + client names); repo:prototype/osfr-tools/data/content/dungeons/snowy_canyon.json:3071 and :1381"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: name 'Brawler's Ring of Precision', locale 131011, definition id 75267, slot 8, class 25 (Brawler job gear). No description, no models, no coin store price.", "source": "client definition in the evidence pack; locale:131011"},
  {"claim": "The name is exact in the client locale and is one of six job variants (Archer, Brawler, Medic, Ninja, Warrior, Wizard) that appear on the Snowy Canyon prize wheel.", "source": "locale:130946, 131011, 131076, 131141, 131206, 131271 (client lookup); wiki Snowy Canyon page"},
  {"claim": "Snowy Canyon's Brawler wheel contains Brawler's Ring of Precision.", "source": "repo:notes/Build Guides/Content/Dungeons/Snowy Canyon.md:93; repo:prototype/osfr-tools/data/content/dungeons/snowy_canyon.json:3071"},
  {"claim": "The wiki's Snowy Canyon wheel list for the other jobs also carries the same Ring of Precision names, and the Briarheart Caverns wheel uses a Ring of Energy V in that slot instead.", "source": "wiki Snowy Canyon page; repo:notes/Build Guides/Content/Dungeons/Snowy Canyon.md:99"},
  {"claim": "No coin vendor, Station Cash, Coin Shop, crafting, collection, or membership source was found for this item. No wiki article for the item itself exists.", "source": "client definition has no coin store price; lookup of wiki for 'Ring of Precision' returns only Snowy Canyon wheel entries"}
 ],
 "confidence": 0.6,
 "open": [
  "The name has no Roman numeral tier, unlike the Necklace of Vitality V and Power Shard of Regeneration V on the same wheel. The Snowy Canyon notes say wheel gear carries 'V' (matching difficulty 5), so this ring does not fit the stated tier pattern. Confirm whether this ring is a tierless variant or a different tier before trusting the tier rule.",
  "The Snowy Canyon wiki section is a truncated snippet. The Brawler wheel list was only seen through the Snowy Canyon page list and the repo's transcription of it; no direct view of a full wiki wheel table was available.",
  "No drop rate, prize-wheel weight, or win count for this slot was found. The wheel's coin slot (117 Coins) and members bonus (304 Coins) are per-run prizes and do not affect this item.",
  "Other dungeon wheels (other than Snowy Canyon) were not checked for this ring. The Briarheart note says it uses a Ring of Energy V in the same position, so Brawler's Ring of Precision is not in that wheel per the notes.",
  "Retired status and the date it stopped being available are unknown. No wiki or article source says it was removed; 'live' is marked unsure because the only source is a wiki dungeon listing.",
  "Kind: the client definition is a ring (slot 8, class 25), so 'clothing' from the first pass is not confirmed. 'other' was chosen as jewelry/accessory; change to 'clothing' if the rebuild treats accessories as clothing.",
  "The first-pass tag said source 'unknown', which this pass resolves to the Snowy Canyon wheel only. No quest reward, enemy drop, event, or promotion source was found."
 ]}
