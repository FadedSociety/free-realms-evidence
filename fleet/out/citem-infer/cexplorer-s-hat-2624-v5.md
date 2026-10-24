<!-- fleet job=citem-infer id=cexplorer-s-hat-2624-v5 status=nothing_found turns=3 usd=0.0022 tokens(read,write,in,out)=[15438, 9191, 8, 1800] model=claude-haiku-5-5 -->
# Explorer's Hat

{"item": {"name": "Explorer's Hat", "locale_id": 2624, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Explorer's Hat', locale 2624, head slot, item class 1, 12 definition ids (36 definitions), two head models (medium brim hat for female, jungle hat for male)", "source": "locale:2624; client definition pack"},
  {"claim": "The hat appears in the Head slot list in three undated gameplay frames, which shows presence in game, not current availability.", "source": "video:S66oho43_CI/00048.jpg; video:p5sDafXSQtQ/00108.jpg; video:4pioItLqlU8/00160.jpg"},
  {"claim": "Region-named variants exist as separate client items: Snowhill Explorer's Hat (locale 30273), Blackspore Explorer's Hat (30281), Briarwood Explorer's Hat (30284), Memorial Caverns Explorer's Hat (30259).", "source": "locale:30273, locale:30281, locale:30284, locale:30259"},
  {"claim": "A wiki search for 'Explorer Hat' returned only Collections-related pages (Blackspore, Briarwood, Merry Vale, etc.) and no page naming the base Explorer's Hat or its vendor, quest, drop or prize source. Articles search returned nothing for the name.", "source": "lookup wiki/articles 'Explorer Hat'"},
  {"claim": "The previous coin_shop candidate is rejected. repo:prototype/osfr-tools/data/content/stores.json:160 is item_id 256 with category 101, tint group 1, 270 coins, member 243, sell 27, and carries no item name. The same values appear on many rows (248, 251, 254, 260, 262, 264, 268, and others), so the row cannot be tied to locale 2624.", "source": "repo:prototype/osfr-tools/data/content/stores.json:157-165"},
  {"claim": "locale 18142 is 'Cobblestone Village', so the collection_catalogue.json id-256 record does not identify this hat.", "source": "locale:18142; repo:prototype/osfr-tools/data/content/collection_catalogue.json:19403"}
 ],
 "confidence": 0.15,
 "open": [
  "No evidenced source for the base Explorer's Hat (locale 2624). The coin_shop candidate (stores.json item 256) is dropped because the row is unnamed and its 270-coin price is shared by many rows; it needs a store-side name or a second key before it can be credited.",
  "Vendor stock is empty in the pack, and the cheap-model 'vendor' guess is unsupported.",
  "Region variants (Snowhill 30273, Blackspore 30281, Briarwood 30284, Memorial Caverns 30259) are probably collection or Explorer Chest rewards, but no wiki page checked names them. Check the Collections and Explorer Chests pages for each named hat before crediting any source.",
  "Retirement is unknown; no source says the hat was retired or made unobtainable.",
  "Live status rests on undated video frames only, so it is marked unsure."
 ]}
