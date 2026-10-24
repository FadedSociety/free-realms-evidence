<!-- fleet job=citem-infer id=cshaggy-hair-style-card-114541-v5 status=nothing_found turns=2 usd=0.0024 tokens(read,write,in,out)=[6405, 11640, 6, 1817] model=claude-haiku-5-5 -->
# Shaggy Hair Style Card

{"item": {"name": "Shaggy Hair Style Card", "locale_id": 114541, "kind": "card"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Shaggy Hair Style Card' is locale 114541, in a Hair Style Card cluster 114536-114546 (Bald, Dreads, Fauxhawk, Forward, Long, Wavy, Flame, Frosty, Spacey, Jubei).", "source": "locale:114541"},
  {"claim": "Lookup of 'Shaggy Hair Style Card' across client, wiki, articles and video returns only the client locale line. No wiki page, article, or video frame names it.", "source": "lookup, this run"},
  {"claim": "stores.json item 6832 is category 141 with purchase 540, member 486, sell 54, no_sale false, and source_tags L1,L2,L4,R2,T633,R1. The row has no name, style or locale field, so nothing links it to locale 114541.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 1847"},
  {"claim": "Lines 1841-1867 are a block of rows 6826-6853 (6841 absent) that all carry identical 540/486/54 values and tags. This is a category-141 default template, not a Shaggy-specific listing.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 1841-1867"},
  {"claim": "Definition 35928 is a no_sale=true row (purchase 540 listed, L3 tags) inside a no-sale category-141 block of rows 35922-35934. It is not a sale listing.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 11684 (re-read this run)"}
 ],
 "confidence": 0.1,
 "open": [
  "No sourced acquisition found. The prior coin_shop entry relied only on the id-linked category-141 default row (stores.json line 1847), which names no item and no style, so it is dropped from sources.",
  "Unverified price figures: 540 coins list / 486 coins member (10% off) appear in the category-141 default block, not tied to Shaggy. Do not use as the card's price until a store row or frame names it.",
  "Definition 35928 is no_sale=true (stores.json line 11684). Its relation to 6832 and to the Shaggy card is unknown.",
  "The sibling frames cited earlier (video:1xtVveaQ3XI/00124.jpg, 00148, 00150) show 486 coins for other style cards. They do not name Shaggy, so they do not support a Shaggy price.",
  "Retirement and live status unknown. The Jev first-pass 'yes' is a hint only and no sighting supports it.",
  "No quest, drop, event, prize wheel, crafting, collection, membership or promotion source found.",
  "Needs a dated Coin Shop frame, store row, or wiki entry that names the Shaggy Hair Style Card before it can be wired."
 ]}
