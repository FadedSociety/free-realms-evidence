<!-- fleet job=citem-infer id=cdisciple-wizard-skirt-133448-v1 status=done turns=4 usd=0.0044 tokens(read,write,in,out)=[24755, 19280, 10, 3575] model=claude-haiku-5-5 -->
# Disciple Wizard Skirt

{"item": {"name": "Disciple Wizard Skirt", "locale_id": 133448, "kind": "clothing"},
 "sources": [
  {"type": "drop", "detail": "Dungeon reward/loot list on the Mugwort's Hollow wiki page (listed under a '97 Coins' entry alongside [Wizard] Prize Wheel and Battle Item Mystery Pack). Exact mechanism (chest, completion reward, or drop) not stated on the page.", "where": "Mugwort's Hollow (Wilds dungeon, Combat Mini-game, Difficulty 4)", "price": "97 Coins (as printed on the page; meaning of the figure unclear)", "currency": "coins", "source": "wiki: Mugwort's Hollow; wiki: Dark Spore Depths and Melninster/Merhione-type vendor pages list the adjacent Wizard skirt tiers but not Disciple"},
  {"type": "other", "detail": "Coin store price of 902 in the client definition. The only stores.json entries with purchase_price_coins 902 are item_ids 75768, 75769-75773, 75827-75830, 75889, 75941, 76002, 76056, 76114, 76180, 76244, 76296, 76354, 76434. None is 76440 (the definition id), so the link from this item to the 902 price is not verified.", "where": "unverified", "price": "902", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json (price match only; item 76434 is the nearest id, category 103, not confirmed as this skirt)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 133448 reads 'Disciple Wizard Skirt', one of a set (Shoes 133443, Gloves 133445, Fez 133446, Slacks 133447, Talisman 133449, Long Cloak 133442) defined as a Disciple-tier wizard outfit.", "source": "locale:133448; locale:133442-133449"},
  {"claim": "Wiki Mugwort's Hollow lists '[Disciple Wizard Slacks] / [Disciple] [Wizard Skirt]' in its reward/loot block with a '97 Coins' figure.", "source": "wiki: Mugwort's Hollow"},
  {"claim": "Wiki Chugawump!, Shady Smugglers!, Mushroom Mania! and Moldy Shamblers! list [Disciple] [Wizard] items (Long Cloak, Talisman, Gloves) in the same kind of block, so the Disciple set appears as dungeon-page loot in several places.", "source": "wiki: Chugawump!; wiki: Shady Smugglers!; wiki: Mushroom Mania!; wiki: Moldy Shamblers!"},
  {"claim": "Client definition: 1 definition (id 76440), slot 4 (legs), class 8, model caster_<race>_f_legs_skirt.adr.", "source": "client definition pack; repo:prototype/osfr-tools/data/content/quests/wizard.json:1811 (76440 appears there only as a quest description string id, not as an item id)"},
  {"claim": "Wiki vendor pages (Melninster, Merhione, Fladnag, Falemicent, Glenda, Linraist, Redsden, Alusru) sell the other wizard skirt tiers (Novice, Hedge, Scholar, Adept, Practitioner, Archmage, Journeyman, Adherent, Amateur-line) but none lists the Disciple skirt.", "source": "wiki: Melninster; Merhione; Fladnag; Falemicent; Glenda; Linraist; Redsden; Alusru"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin shop claim is not verified. The 902 price in the pack matches many stores.json rows, and none is keyed to definition 76440. Needs a check of which item_id the Disciple skirt uses in the store, or a wiki/Coin Shop page.",
  "The wiki's '97 Coins' figure on Mugwort's Hollow is ambiguous. It may be a dungeon entry or reward amount, not a store price. Do not record it as a purchase price until confirmed.",
  "No wiki page, article, or video names the Disciple Wizard Skirt directly. Its source list rests on the dungeon loot blocks and the unverified price match.",
  "Vendor stock for this item was empty in the pack, and no vendor page lists the Disciple tier.",
  "Retirement status is unknown. The item is live in the client, but no source states when it was sold or removed."
 ]}
