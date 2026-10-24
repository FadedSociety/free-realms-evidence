<!-- fleet job=citem-infer id=cteal-half-cylinder-block-134785-v3 status=done turns=3 usd=0.0029 tokens(read,write,in,out)=[18909, 13698, 8, 1911] model=claude-haiku-5-5 -->
# Teal Half Cylinder Block

{"item": {"name": "Teal Half Cylinder Block", "locale_id": 134785, "kind": "furniture"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store row for item definition 77249 (purchase 300 coins, member price 270, sell-back 30, sellable). Store and vendor name not identified. The row sits in stores.json category 147 with undecoded source_tags [L1, L2, L4, R2, T633, R1]. Definition 77249 is not evidenced as the Teal tint; it is one of a run of identical 300-coin rows (77245-77252) in the same category.", "where": "store unidentified (stores.json category 147)", "price": "300 coins (member 270; sell-back 30)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 77249 (line 16580)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 134785 'Teal Half Cylinder Block', description 'Great for stackability.', one model hsg_block_cylinderhalf_01.adr, slot 0, class 0", "source": "locale:134785"},
  {"claim": "Two item definitions (77192 and 77249) share the name. Store data lists 77249 at 300 coins (sellable, sell-back 30) and 77192 at 50 coins (no_sale true, member 45, no sell-back). Verified on re-read.", "source": "repo:prototype/osfr-tools/data/content/stores.json items 77249 (line 16580) and 77192 (line 16523)"},
  {"claim": "Row 77192 belongs to a block of 50-coin no_sale rows (77184-77235 range) in category 147, separate from the 300-coin block. Which definition is the Teal product is not established.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 16515-16566, 16523"},
  {"claim": "Neighbouring colour variants share the client id block: Green, Orange, Pink, Purple, Red, White, Yellow Half Cylinder Block, and Black/Blue/Green Half Cylinder Down Block.", "source": "locale:134780 through locale:134790"},
  {"claim": "No wiki page, article fact or video frame names this Teal block. Lookup returns only the other Half Cylinder Block entries (locale 29975, 29977, 8666, 8677, 8688, 8699, 134778-134781).", "source": "lookup: wiki, client, articles, query 'Half Cylinder Block'"}
 ],
 "confidence": 0.3,
 "open": [
  "Store identity unknown. Only the stores.json category id (147) links the row; the source_tags are undecoded, so the vendor, NPC, zone and shop are not confirmed. The 'coin_shop' type is a store-data label, not a confirmed shop.",
  "Definition-to-tint mapping is not evidenced. 77249 (300 coins, sellable) and 77192 (50 coins, no_sale) both carry the Teal name. Which one is the Teal product, or whether both are Teal variants, is unresolved. Do not treat 300 coins as the sole Teal price.",
  "Retired status and current availability unknown. stores.json has no availability window for category 147, so the 300-coin price is historical data only.",
  "The earlier claim of 350-coin and 200-coin entries in category 147 was wrong and is dropped. The rows checked show only 50-coin and 300-coin prices.",
  "No wiki or community source confirms any sale of this block. Every source is store data alone."
 ]}
