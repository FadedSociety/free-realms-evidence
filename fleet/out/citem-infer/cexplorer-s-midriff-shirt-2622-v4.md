<!-- fleet job=citem-infer id=cexplorer-s-midriff-shirt-2622-v4 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[14028, 8867, 8, 2438] model=claude-haiku-5-5 -->
# Explorer's Midriff Shirt

{"item": {"name": "Memorial Caverns Explorer's Midriff Shirt", "locale_id": 29388, "kind": "clothing"},
 "sources": [
  {"type": "collection", "detail": "Completing The Keys collection (single undated user blog; the blog does not describe a chest or key mechanic)", "where": "Memorial Caverns", "price": null, "currency": null, "source": "wiki page User blog:Amber Kindpaws :)/Memorial Caverns Explorer's Midriff Shirt (ns500); locale:29388"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Generic client name is locale 2622 \"Explorer's Midriff Shirt\"; the Memorial Caverns variant is locale 29388. Other variants: 29201 Blackspore, 29204 Briarwood, 29402 Snowhill. Seeker's Midriff Shirt (2628) and Pathfinder's Midriff Shirt (9128) are separate names.", "source": "locale:2622, locale:29388, locale:29201, locale:29204, locale:29402, locale:2628, locale:9128"},
  {"claim": "Wiki blog says the Memorial Caverns shirt requires completing The Keys collection, is girls only, tradeable, and needs Level 1 Freestyle (Adventurer).", "source": "wiki page User blog:Amber Kindpaws :)/Memorial Caverns Explorer's Midriff Shirt (ns500)"},
  {"claim": "Tooltip for the Memorial Caverns variant: Resell Value 27, Level 1 Freestyle Jobs, Girls only.", "source": "image:item_tooltip, Bandicam 2013-04-01 15-18-16-432.jpg (wiki file)"},
  {"claim": "Wiki Explorer Chests page says each chest holds a different outfit and that keys are obtained through collections; it does not name this shirt, so the chest link stays unconfirmed.", "source": "wiki page Explorer Chests (ns0)"},
  {"claim": "stores.json rows for item 254 (tint 1), 1441 (tint 2) and 1443 (tint 3) show purchase 270 coins, member price 243, sell 27, category 103, source_tags L1,L2,L4,R2,T633,R1. The rows name no vendor and the same shape recurs on unrelated items, so they are not a sourced vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 159, 5782, 5784"},
  {"claim": "The Blackspore video frame shows Blackspore set items at Adventurer 20, not this variant.", "source": "video:SdVAc6iTuK4/00000.jpg"}
 ],
 "confidence": 0.3,
 "open": [
  "Item keyed to the Memorial Caverns variant (29388) because the only source applies to it. The generic name (locale 2622) and its definition ids (254, 1441, 1443, 15373-15389) are not confirmed as the same source; treat the generic record as unresolved.",
  "Keys collection source rests on one undated user blog. No reward table, chest, or event links the shirt to The Keys collection. Needs a second source before wiring.",
  "Client coin_store_prices 270 (definition 254; member 243; sell 27) is an unverified candidate price with no vendor named. It is not recorded as a sourced vendor sale. Store rows for 254/1441/1443 use tags that may map to a vendor, but no vendor was found.",
  "No vendor, drop, quest, or prize-wheel source found for any variant in the pack or repo searches.",
  "Retirement and current availability are unknown. No source dates the Keys collection or the store row.",
  "Sibling Memorial Caverns-style collection shirts (Blackspore 29201, Briarwood 29204, Snowhill 29402) are unresolved in the same way."
 ]}
