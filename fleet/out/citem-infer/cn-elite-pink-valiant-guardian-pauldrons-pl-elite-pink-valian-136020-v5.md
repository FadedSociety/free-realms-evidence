<!-- fleet job=citem-infer id=cn-elite-pink-valiant-guardian-pauldrons-pl-elite-pink-valian-136020-v5 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[5881, 10483, 6, 2344] model=claude-haiku-5-5 -->
# {n}Elite Pink Valiant Guardian Pauldrons{pl="Elite Pink Valiant Guardian Pauldrons"}

{"item": {"name": "Elite Pink Valiant Guardian Pauldrons", "locale_id": 136020, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store row for item_id 47020 (category 106, tint_group null). Only candidate source; the link to locale 136020 is by definition id 47020 (client definition name_locale_id 136020), and the client icon for 47020 conflicts with the name (see open).", "where": "Coin store (category 106)", "price": "9453 coins purchase; 10% member price 8507 coins; sell price 945 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:13086 (item_id 47020); client definition 47020 coin_store_prices [9453]"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Elite Pink Valiant Guardian Pauldrons' is locale 136020; client definition 47020 names it via name_locale_id 136020, slot 6, class 15, model warrior_<race>_<gender>_shoulders_thincollarpauldron.adr.", "source": "locale:136020; client definition 47020"},
  {"claim": "Store row item_id 47020 exists in category 106 with purchase 9453 coins, member price 8507, sell price 945, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json:13086"},
  {"claim": "The same 9453-coin price also appears on item_ids 47021 (and 46950, 46951 per prior pass), so the price alone does not identify the item.", "source": "repo:prototype/osfr-tools/data/content/stores.json:13087"},
  {"claim": "Icon table maps definition 47020 to 'icon_item_superhero_race_gender_chest_spandexshoulders', which conflicts with the Valiant Guardian name.", "source": "Resources/Images/Images.txt:39348"},
  {"claim": "The Valiant Guardian warrior family exists in client text: Pauldrons 136015, Hightops 135210, Gauntlets 135385, Breeches 135700, Tunic 135105, Helm 135630, Elite Pink Hightops 135215. Wiki covers the Valiant Guardian Cudgel as a Blacksmith recipe (Members Only, green-text weapon) but has no page or row for the pauldrons.", "source": "lookup: 'Valiant Guardian' (client, wiki)"},
  {"claim": "No wiki page, article, video frame, vendor stock row, quest, drop or event names locale 136020 or the pauldrons.", "source": "lookup: 'Valiant Guardian' (wiki, articles, video); repo search for 47020"}
 ],
 "confidence": 0.3,
 "open": [
  "Name-to-definition conflict: definition 47020 has name_locale_id 136020 but its icon is a superhero spandex shoulder piece. Confirm from the client item table that 47020 is the Elite Pink Valiant Guardian Pauldrons before treating the coin row as this item's source.",
  "The 9453-coin price is shared by 47021 and other rows, so the price does not confirm the item; the coin_shop source rests only on the id match.",
  "No sale window, shop-day or retirement date is in evidence. Retired is null and live is unsure.",
  "No vendor, quest, drop, crafting, event or collection source is evidenced for the pauldrons. The 'vendor' first-pass guess has no stock row behind it.",
  "Unknown whether the Pink and Black elite tints were sold separately or as a set; no stock row shows tint_group for 47020 (tint_group_id null)."
 ]}
