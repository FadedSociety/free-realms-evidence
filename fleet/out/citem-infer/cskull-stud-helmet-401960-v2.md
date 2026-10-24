<!-- fleet job=citem-infer id=cskull-stud-helmet-401960-v2 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[5064, 11207, 6, 2229] model=claude-haiku-5-5 -->
# Skull Stud Helmet

{"item": {"name": "Skull Stud Helmet", "locale_id": 401960, "kind": "clothing"},
 "sources": [
  {"type": "coin_shop", "detail": "Reconstructed Coin Shop catalogue price for head-helmet tint definitions 60493 (tint group 1), 60494 (tint group 2), 60495 (tint group 3). Price 270 coins from the Legacy ClientItemDefinitions Cost field, not confirmed against a live transaction (notes/Research/Coin Shop.md line 33). Member price 243 coins is R2 arithmetic (10% floor), not observed. Not confirmed by any wiki page, article or video.", "where": "Coin Shop", "price": "270 coins (member 243 coins, computed)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 14446-14448 (item_id 60493, 60494, 60495); refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json NameId 401960 entries; repo:notes/Research/Coin Shop.md:33-34"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Skull Stud Helmet' is locale 401960, the only client line tagged to it.", "source": "locale:401960"},
  {"claim": "Legacy ClientItemDefinitions has many entries with NameId 401960 (the grep returned about 20 Legacy hits and more in Lxzxrus and Sanctuary); the count of 34 definitions was not re-verified here.", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:1121246"},
  {"claim": "stores.json has Coin Shop rows at 270 coins with 10% member discount for item_id 60493, 60494, 60495 (tint groups 1-3), category 101, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json:14446-14448"},
  {"claim": "The stores.json rows for this range are 60493-60495 and then 60528-60530; the 60493-60504 range in the prior answer is not supported by stores.json.", "source": "repo:prototype/osfr-tools/data/content/stores.json:14446-14449"},
  {"claim": "Coin Shop catalogue prices are reconstructed from Legacy Cost fields; the mapping is not checked against a real client transaction.", "source": "repo:notes/Research/Coin Shop.md:33"},
  {"claim": "Lookup of 'Skull Stud Helmet' across client, wiki, articles and video returns only locale:401960. No wiki page, article, video frame, or vendor stock names it.", "source": "lookup (client, wiki, articles, video)"}
 ],
 "confidence": 0.4,
 "open": [
  "The only coin source is a reconstructed catalogue row. No live vendor, wiki or article confirms the Coin Shop sale. Treat the 270-coin price as unverified.",
  "Jev's 'vendor' guess is not supported: no named NPC vendor stocks it in the vendor data. The prior answer's 'Coin Shop purchase' is downgraded to reconstructed.",
  "The 34-definition / 60493-60504 mapping is not supported. Only 60493-60495 were checked in stores.json; the other definitions' shop rows were not read, so whether they are all on sale is open.",
  "Sell-back 27 coins (T633) is server policy, not a live source.",
  "Whether the Coin Shop sold it late in the original service is unknown; retired is null.",
  "The near-identical 'Skull Studded Helmet' (locales 585565400 and 4199549381) is a different name and was not checked."
 ]}</result>
