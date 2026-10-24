<!-- fleet job=citem-infer id=cn-snowhill-explorer-s-gloves-pl-snowhill-explorer-s-gloves-30064-v3 status=done turns=2 usd=0.0022 tokens(read,write,in,out)=[6057, 9710, 6, 1850] model=claude-haiku-5-5 -->
# {n}Snowhill Explorer's Gloves{pl="Snowhill Explorer's Gloves"}

{"item": {"name": "Snowhill Explorer's Gloves", "locale_id": 30064, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Unidentified coin vendor. Coin store rows for definitions 16256 (female gloves) and 17630 (male fingerless gloves), both category 102, identical price and tags. Vendor not named in the repo; the rule that a coin store price counts as a coin vendor sale is applied here, but the store-to-vendor mapping was not found.", "where": null, "price": "270 coins (member price 243, sell price 27)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:4645 (item 16256) and :4363 (item 17630)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 30064, '{n}Snowhill Explorer's Gloves{pl=...}', item class 1, slot 2 (hands), two definitions 16256 and 17630.", "source": "locale:30064; client definition from pack"},
  {"claim": "Re-read confirmed both store rows: item 16256 at stores.json line 4645 and item 17630 at line 4363, each category_id 102, purchase 270 coins, member 243, sell 27, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4645, :4363"},
  {"claim": "Category 102 is shared by unrelated items at other prices (e.g. 16241, 16261-16263, 16269 at 270; other rows at 188, 225, 9453), so category alone does not name a vendor.", "source": "repo:prototype/osfr-tools/data/content/stores.json:4644-4649"},
  {"claim": "Wiki 'List of Collections' and 'Adventurer' pages list a '[Snowhill] Rare Exploration' collection and a [Snowhill] entry, with no item list naming these gloves. Not used as a source.", "source": "wiki List of Collections; wiki Adventurer"},
  {"claim": "Repo search for ids 16256 and 17630 finds only the two stores.json rows; no vendor stock, quest, drop or event reference.", "source": "repo search '16256|17630'"}
 ],
 "confidence": 0.35,
 "open": [
  "Vendor identity unknown: the single 270-coin offer is supported by the store rows, but no store-to-vendor mapping names the vendor. Type 'vendor' is kept only because the coin-store-row rule applies; relabel as unlocated coin store row if that rule is not accepted.",
  "The two definitions (16256 female gloves, 17630 male fingerless gloves) share one price and tag set; they are recorded as one offer, not verified as separately sold.",
  "Live status unsure: store rows exist in the repo, but no article, wiki page or video frame confirms current sale or retirement. The first-pass 'live: yes' is not evidence.",
  "No wiki article, video frame or quest/drop/event source names these gloves. Snowhill chest and Rare Exploration collection are unconfirmed reward sources and are excluded.",
  "Wiki search for the exact apostrophe name was not completed (FTS5 syntax); 'Snowhill Explorer' returned only set-level pages."
 ]}
