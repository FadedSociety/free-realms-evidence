<!-- fleet job=citem-infer id=cpolkadot-flooring-26387-v1 status=nothing_found turns=3 usd=0.0023 tokens(read,write,in,out)=[11215, 10337, 8, 1858] model=claude-haiku-5-5 -->
# Polkadot Flooring

{"item": {"name": "Polkadot Flooring", "locale_id": 26387, "kind": "furniture"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is 'Polkadot Flooring' (locale:26387), description 'A polkadot print for your floor.' (locale:26388), definition id 27961, slot 0, class 1, no model files and no coin store price.", "source": "locale:26387; locale:26388; client definition in evidence pack"},
  {"claim": "No wiki page, image, article fact, or video frame names Polkadot Flooring. Wiki lookup returned only client text rows for 26387, 26388, 26389 and 26390.", "source": "lookup wiki/articles/video query 'Polkadot Flooring' and 'flooring polkadot OR houndstooth OR leopard OR rainbow'"},
  {"claim": "No coin vendor stock (stores.json has no entry for definition 27961), no quest, drop, or event answer mentions it.", "source": "repo:prototype/osfr-tools/data/content/stores.json (search for Polkadot/27961 returned no flooring entry); evidence pack vendor_stock and mentioned_by_other_answers empty"},
  {"claim": "Its client cluster is a set of room floor/wallpaper prints (Houndstooth Flooring locale:26383-26384, Leopard Flooring locale:26385-26386, Small Polkadot Flooring locale:26389, Rainbow Flooring locale:26391-26392, Seaside Sand Flooring locale:26382). The cluster is a housing decor set with no source text attached.", "source": "client_cluster in evidence pack; locale table"},
  {"claim": "Rainbow Flooring, the set's sibling, appears in articles only as a housing theme, not a sale or source fact (articles 1532 and 1521 mention cloud blocks in rainbow colors, not flooring).", "source": "http://www.freerealms.com:80/article/detail.action?articleId=1532; http://www.freerealms.com:80/article/detail.action?articleId=1521"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found. Acquisition path (coin vendor, Station Cash, housing reward, promotion, or other) is unknown; the first-pass 'unknown' guess is unsupported.",
  "Live status is unverified. The client defines it, but no evidence shows it was sold or granted in the 2009-2014 live game, and no retirement record was found.",
  "Price unknown: no coin store price in stores.json and no wiki price.",
  "Client text issue: locale:26390 'Small Polkadot Flooring' reuses the description 'A polkadot print for your floor.' from 26388 (flagged duplicate). The description for Small Polkadot Flooring is probably wrong, but the name of 26389 is clear. Do not copy 26390's text onto Polkadot Flooring.",
  "Suggested next step: check the Sanctuary or Legacy server data for definition 27961 and any housing decor vendor (furniture/flooring vendor) lists, and ask for a wiki page on Housing decor flooring or the Rainbow Flooring set."
 ]}
