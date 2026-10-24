<!-- fleet job=citem-infer id=cpet-dog-large-shortears-solid-gold-75134-v3 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[17875, 12058, 8, 2153] model=claude-haiku-5-5 -->
# Pet: Dog: Large Shortears: solid-gold

{"item": {"name": "Pet: Dog: Large Shortears: solid-gold", "locale_id": 75134, "kind": "pet"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store sale of the pet; the selling NPC is not identified in our data (the store row has no vendor id)", "where": "Coin Shop (coin store row)", "price": "540 coins (member price 486 coins, 10% member discount)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:6861 (item_id 23984, purchase_price_coins 540, member_price_coins 486, no_sale false); client definition coin_store_prices [540]"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client definition 23984 is named 'Pet: Dog: Large Shortears: solid-gold' (locale:75134), model dog_large_shortears.adr, one definition, one slot", "source": "locale:75134; client definition"},
  {"claim": "Store data lists item 23984 at purchase_price_coins 540 with member price 486, not flagged no_sale. The client coin_store_prices field carries the same 540, so the price rests on one legacy Cost value copied to two places, not an independent check", "source": "repo:prototype/osfr-tools/data/content/stores.json:6861"},
  {"claim": "Row 23984 carries source tags L1,L2,L4,R2,T633,R1 and no price_provenance block. It has no T638 check, unlike 23978, 23982 and 23990, so its coin price is unverified", "source": "repo:prototype/osfr-tools/data/content/stores.json:6861 (compared with lines 6855, 6859, 6867)"},
  {"claim": "Sibling rows 23979-23981, 23983, 23985, 23987-23989 (and 23991-23993) carry the same 540/486 values. Rows 23978 and 23982 are no_sale Station Cash marketplace items (225 and 175 SC, per T638 wiki checks on Bruno and Nox), with the legacy 540 cleared, so they are not coin-priced siblings", "source": "repo:prototype/osfr-tools/data/content/stores.json:6855, 6859"},
  {"claim": "Same-family pets share the prefix 'Pet: Dog: Large Shortears' (locale:75135-75146 and further siblings)", "source": "locale:75135-75146 (client lookup)"},
  {"claim": "No wiki page, article, video, image, quest, drop, prize-wheel, crafting, collection or promotion source names this pet. Searches for 'solid-gold' and 'Shortears' returned only client text lines", "source": "lookup (client, wiki, articles, video)"}
 ],
 "confidence": 0.4,
 "open": [
  "Vendor NPC unknown: the store row names no vendor, and no wiki page or article places the pet at a named NPC. The 'Coin Shop' location rests only on the store row.",
  "The 540 coin price is a single legacy Cost value (also in the client coin_store_prices field). No wiki or article price exists to cross-check it.",
  "The 54 sell-back is server policy (T633), not a sourced price, so it is left out of the sources.",
  "Retirement and current availability are unknown. The row's R1 tag marks a defaulted value, so the live state is a reconstruction. The first-pass 'live: yes' is a hint only and is not used as evidence.",
  "No promotion, drop, prize-wheel, crafting, collection or membership source found."
 ]}
