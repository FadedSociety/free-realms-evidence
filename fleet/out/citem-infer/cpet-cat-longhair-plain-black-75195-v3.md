<!-- fleet job=citem-infer id=cpet-cat-longhair-plain-black-75195-v3 status=nothing_found turns=2 usd=0.0022 tokens(read,write,in,out)=[6553, 10719, 6, 1503] model=claude-haiku-5-5 -->
# Pet: Cat: Longhair: plain_black

{"item": {"name": "Pet: Cat: Longhair: plain_black", "locale_id": 75195, "kind": "pet"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text defines the name 'Pet: Cat: Longhair: plain_black' as locale 75195, in a cat pet cluster (75190-75200) with the same naming pattern.", "source": "locale:75195; lookup client confirms the same line"},
  {"claim": "stores.json row for item 24045 has purchase 540, member 486 (10%), sell 54, and Legacy-style source tags L1, L2, L4, R1, R2, T633. The row has no price_provenance block, unlike rows 24041, 24044 and 24056, which carry wiki-backed provenance.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6922"},
  {"claim": "Rows 24041, 24044 and 24056 state that no coin vendor stocks the item, so the Legacy coin cost of 540 is cleared. The 540 value appears to be a bulk template across rows 24035-24057, so it does not show a sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6918, 6921, 6933"},
  {"claim": "The client ships no pet species, price, or trick table. The 'client coin price 540' claim is not supported and must not be cited as client evidence.", "source": "repo:notes/Build Guides/Gameplay/Pets.md:100"},
  {"claim": "No wiki page, image, article fact, video frame, vendor stock list, or other answer names this pet as sold, dropped, rewarded, or won.", "source": "lookup of client, wiki, articles, video for 'Longhair plain_black cat pet' returned only locale:75195"}
 ],
 "confidence": 0.1,
 "open": [
  "No acquisition source is evidenced. The Coin Shop claim rested only on a generic 540 template row in stores.json (item 24045, no provenance block), so it is removed as a source.",
  "Pets.md:20 says pets are not ordinary inventory items, which argues against a plain coin-store SKU. Unresolved.",
  "The earlier answer cited repo:notes/Research/Coin Shop.md, which does not exist. Its provenance claim is not used.",
  "Live status is unknown. A check is needed against a Coin Shop or merchant listing for item 24045, a player report, or a legacy pet-vendor source for the cat cluster 75190-75200.",
  "Retired status is unknown with no source."
 ]}
