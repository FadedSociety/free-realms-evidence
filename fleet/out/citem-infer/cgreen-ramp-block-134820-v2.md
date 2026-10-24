<!-- fleet job=citem-infer id=cgreen-ramp-block-134820-v2 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[6057, 13114, 6, 2069] model=claude-haiku-5-5 -->
# Green Ramp Block

{"item": {"name": "Green Ramp Block", "locale_id": 134820, "kind": "furniture"},
 "sources": [
  {"type": "vendor", "detail": "Coin store, category 147, unnamed vendor (repo data does not name the vendor). Price row for definition 77227 only; the link from 77227 to this name is inferred from the client definition record, not cross-checked. 77227 sits in a uniform run of 50-coin no-sale rows (77217-77234).", "where": "unknown (category 147 coin store, vendor and zone not named in repo data)", "price": "50 coins (member price 45 coins); no sell-back", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:16558 item 77227"},
  {"type": "vendor", "detail": "Coin store, category 147, unnamed vendor. Price row for definition 77276; same link caveat. Uniform run of 400-coin rows with sell-back in the 77267-77276 range.", "where": "unknown (category 147 coin store, vendor and zone not named in repo data)", "price": "400 coins (member price 360 coins); sell-back 40 coins", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json:16607 item 77276"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Green Ramp Block' as locale 134820, description 'Great for stackability.', definition IDs 77227 and 77276, model hsg_block_ramp_01.adr", "source": "locale:134820"},
  {"claim": "stores.json item 77227 is category 147, 50 coins, member 45, no_sale true", "source": "repo:prototype/osfr-tools/data/content/stores.json:16558"},
  {"claim": "stores.json item 77276 is category 147, 400 coins, member 360, sell-back 40", "source": "repo:prototype/osfr-tools/data/content/stores.json:16607"},
  {"claim": "Client has a sibling family of ramp blocks (134815-134825, plus Green Ramp Tiger Block locale 134861 and Green Ramp Polka Dot Block locale 31870), suggesting tint/pattern variants of one block line", "source": "locale:134815-134825; locale:134861; locale:31870"},
  {"claim": "No wiki page, article, or video names Green Ramp Block; the wiki Items page does not list it", "source": "lookup of 'Green Ramp Block' across client, wiki, articles, video"},
  {"claim": "No repo string links 134820 or 77227/77276 to a name; the ID-to-name link is only the client definition record", "source": "search repo for 77227|77276|134820"}
 ],
 "confidence": 0.3,
 "open": [
  "Vendor name and zone for coin store category 147 are not in repo data; the 'vendor' type is a price-table fact, not a named NPC sale.",
  "Two definitions with different prices (50 no-sale vs 400 with sell-back) are not reconciled. They may be different SKUs, tint variants, or one of them may belong to a neighbouring item in its batch. The 77227 row is part of a 50-coin batch (77217-77234) and may not be this item.",
  "No wiki, article, or video evidence for availability, release date, retirement, or later sale (SC Marketplace, Coin Shop, events). Live status is unverified; the first-pass 'live: yes' is a hint only.",
  "No quest reward, drop, prize wheel, crafting, collection, or membership source found.",
  "Kind 'furniture' is inferred from the description 'Great for stackability.' and the housing block model; no source names the kind.",
  "Critique fix applied: vendor and where left as unknown rather than a named vendor; the name-to-ID link is marked as inferred. Wireable status: partial (price evidence for both IDs, name link and vendor unverified)."
 ],
 "wireable": "partial"}
