<!-- fleet job=citem-infer id=cgreat-velocity-helmet-123203-v3 status=no_submit turns=2 usd=0.0029 tokens(read,write,in,out)=[6035, 12333, 6, 2690] model=claude-haiku-5-5 -->
# Great Velocity Helmet

```json
{"item": {"name": "Great Velocity Helmet", "locale_id": 123203, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Coin store listing for definition 43205 (tint group 1); vendor/NPC not named in any source", "where": null, "price": "1266 coins (member price 1139, sell price 126)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12838 (item 43205, category 101)"},
  {"type": "coin_shop", "detail": "Coin store listing for definition 43213 (tint group 2); vendor/NPC not named in any source", "where": null, "price": "9453 coins (member price 8507, sell price 945)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12839 (item 43213, category 101)"},
  {"type": "coin_shop", "detail": "Coin store listing for definition 43220 (tint group 3); vendor/NPC not named in any source", "where": null, "price": "9453 coins (member price 8507, sell price 945)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:12840 (item 43220, category 101)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 123203 is 'Great Velocity Helmet'; set siblings are Jersey 123200, Shoes 123201, Gloves 123202, Pants 123206.", "source": "locale:123203"},
  {"claim": "Client definition lists 16 definitions (43205, 43213, 43220, 43227, 43232, 43241, 43248, 43253, 43262, 43269, 43275, 43282), slot 1, item class 24, model freestyle_<race>_<gender>_head_helmetwglasses.adr. These come from the client definition in the evidence pack; the earlier repo citation (piece_041.rs:66-67, :131-135) does not contain them and has been dropped.", "source": "client definition (locale 123203); not verifiable in repo"},
  {"claim": "Store row item 43205 (category 101, tint 1): purchase 1266 coins, member 1139, sell 126. The client definition's coin_store_prices include 1266, which ties this row to the helmet.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12838"},
  {"claim": "Store rows 43213 (tint 2) and 43220 (tint 3), category 101: purchase 9453 coins, member 8507, sell 945. Both ids are helmet definitions per the client definition, and the client's coin_store_prices include 9453.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12839-12840"},
  {"claim": "Store rows carry source_tags L1, L2, L4, R2, T633, R1; no sale-end or retirement marker is present. These tags are not decoded here.", "source": "repo:prototype/osfr-tools/data/content/stores.json:12838-12840"},
  {"claim": "No wiki page, image, article fact, or video frame names the Great Velocity Helmet. Client text lookup returns only the locale lines for the set.", "source": "lookup (client, wiki, articles, video)"},
  {"claim": "A wiki note on the Soccer Star job mentions 'Great Velocity' jersey and helmet kart pairs, but gives no source or price for the helmet.", "source": "notes/Build Guides/Content/Jobs/Soccer Star.md:245"},
  {"claim": "Kart Driver rank gate: the rank-3 row in piece_041.rs is the Great Velocity Jersey (43222, locale 123200), not the helmet. The helmet's rank gate is not sourced.", "source": "repo:prototype/osfr-tools/src/restoration/piece_041.rs:135"}
 ],
 "confidence": 0.45,
 "open": [
  "The NPC or vendor that sells category 101 is not identified. Vendor stock files and wiki text do not name it, so the coin listings have no vendor name.",
  "Only 3 of 16 definitions have price rows (43205, 43213, 43220). The other 13 (43227, 43232, 43241, 43248, 43253, 43262, 43269, 43275, 43282 and the rest of the list) have no store row, so their source is unknown.",
  "Retired and live status are unresolved. The rows have no no_sale flag set (false), but nothing dates them, and no wiki or article says whether the gear is still sold.",
  "The source_tags (L1, L2, L4, R2, T633, R1) are not decoded, so it is unclear which storefront or era they cover.",
  "The helmet's rank or quest gate is unknown. The Kart Driver rank table names only the Jersey, not the helmet.",
  "The first-pass tag (live yes, vendor) is a hint only. The vendor part is not confirmed by any named source."
 ]}
```
