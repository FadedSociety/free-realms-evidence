<!-- fleet job=citem-infer id=ctiki-mask-42278-v3 status=done turns=2 usd=0.0025 tokens(read,write,in,out)=[6547, 10203, 6, 2328] model=claude-haiku-5-5 -->
# Tiki Mask

{"item": {"name": "Tiki Mask", "locale_id": 42278, "kind": "clothing"},
 "sources": [{"type": "coin_shop", "detail": "Unplaced coin-store row. No vendor, NPC or zone is named in the row, and no vendor-stock row lists this item. Store category 104 is not mapped to a shop in the pack.", "where": null, "price": "433 coins (member 389, sell-back 43); candidate only, not confirmed for this item", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12711 (item_id 42278, category_id 104, tint_group 1, no_sale false; re-read and confirmed). Matched to this item by locale id 42278 only."}],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Tiki  Mask' with description 'Creep out friends and acquaintances!', clothing head model freestyle_<race>_<gender>_head_tikimask.adr, 4 definitions (10902, 10943, 15726, 76727).", "source": "locale:42278; client definition in pack"},
  {"claim": "Store row item_id 42278 is 433 coins, member 389, sell-back 43, not no_sale. Rows 42275, 42276, 42280, 42281, 42283, 42285, 42286 and 42288 share the same 433 price, so this looks like a price group rather than a per-item price.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12709-12717 (re-read)"},
  {"claim": "Definition-keyed rows 10902, 10943 and 15726 list 270 coins but are no_sale:true, so they are not player sales. This is the source of the client's coin_store_prices [270].", "source": "repo:prototype/osfr-tools/data/content/stores.json:14106, :14108, :14111 (re-read)"},
  {"claim": "Video frame OCR reads 'Innertube Suit', then 'Tiki Mask?' (with a question mark), then 'Hula Outfit' Boys/Girls, at Adventurer 20 on a sandy beach with tiki torches. It is weak, unconfirmed OCR and not a sale listing.", "source": "video:yBwnL7jnweI/00058.jpg (re-checked via lookup)"},
  {"claim": "Locale 420210 is a second name locale for 'Tiki Mask'. Locale 150529 is a placeholder ('This is a ... item.') and is excluded.", "source": "locale:420210; locale:150529 (placeholder flag)"},
  {"claim": "No wiki page, article, quest, drop, prize-wheel, crafting or marketplace source names the Tiki Mask.", "source": "lookup 'Tiki Mask' over wiki, articles, video, client (no hits beyond the video frame and locale rows)"}
 ],
 "confidence": 0.25,
 "open": [
  "Vendor not identified. The 433-coin row has no NPC or zone, and vendor_stock is empty, so no vendor source is evidenced. Do not wire a vendor source until a stock row names one.",
  "Price conflict: 433 coins (stores.json:12711, keyed by locale 42278) vs 270 coins (client coin_store_prices; definition rows 10902/10943/15726 are no_sale). Unresolved. Confirm whether store item_id keys are locale or definition ids. The shared 433 price across eight neighbouring rows suggests a group price.",
  "Event origin unconfirmed. The Summer Splash article (articleId=137) names Hula Outfit but not Tiki Mask, so it is not a source.",
  "Retired status and availability window unknown; no wiki page exists.",
  "No quest, drop, prize-wheel, crafting, collection or marketplace source found.",
  "wireable: false. stores.json:12711 is a candidate only."
 ]}
