<!-- fleet job=citem-infer id=cpet-dog-small-pointy-darkmark-chocolate-75094-v2 status=nothing_found turns=2 usd=0.0023 tokens(read,write,in,out)=[5551, 9096, 6, 2116] model=claude-haiku-5-5 -->
# Pet: Dog: Small Pointy: darkmark-chocolate

{"item": {"name": "Pet: Dog: Small Pointy: darkmark-chocolate", "locale_id": 75094, "kind": "pet"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 23944 is a dog pet (model dog_small_pointy.adr), one of the 11 Small Pointy tint names locale:75089 to locale:75099. The name is the client's own text.", "source": "locale:75094; client definition 23944 as supplied in the pack"},
  {"claim": "stores.json item 23944 carries a legacy purchase_price_coins of 540 (member 486, sell 54) with no price_provenance block and no category or tint group. Source tags are L1, L2, L4, R2, T633, R1; no note explains them.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6821"},
  {"claim": "The 540 coin value is a shared legacy block, not a checked price. Rows 23935 to 23951 all carry 540, and the same tag set. Items 23941 and 23943 (neighbours in the block) were corrected to SC Marketplace at 400 Station Cash with provenance, and their 540 coin cost was cleared because no coin vendor stocks them.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6812-6828 (items 23935 to 23951); lines 6818 and 6820 for the corrections"},
  {"claim": "No vendor in vendors.json stocks item 23944. The only repo hit for 23944 is its stores.json row.", "source": "repo search for '23944' (vendors.json has only an unrelated sha256 hash match at line 32540)"},
  {"claim": "The client has no wiki page, article, image or video for this tint or the Small Pointy dog. Lookup returns only the client's own locale lines for this darkmark-chocolate tint family (Small Fluffy locale:75076, Small Floppy locale:75058).", "source": "lookup client/wiki/articles/video for 'darkmark chocolate dog pet'"},
  {"claim": "Cragara the Mysterious Merchant sells some dog pets per the wiki, but no page ties her to the Small Pointy model or this tint, and the wiki price is blank.", "source": "prior pack lookup of wiki pages Scout, Marlin, Peccadillo, Bort, Stretch, Jinx (not re-verified here)"}
 ],
 "confidence": 0.15,
 "open": [
  "No verified acquisition source. The 540 coin figure in stores.json:6821 is a legacy default shared with rows 23935 to 23951 and has no provenance. It is not evidence of a coin vendor sale, so the earlier 'vendor' source is withdrawn. Treat the 540/486/54 values as unverified until a source or a clearing decision is recorded, as was done for 23941 and 23943.",
  "The Mysterious Merchant (Cragara) link is unconfirmed. The wiki gives no price and no model or tint mapping.",
  "Live status is unsure. The client defines the item and the store row exists, but no wiki, article, or video shows it in play, and the first-pass 'live: yes' is only a hint.",
  "Pet display name and any SC Marketplace listing are unknown. Check whether the Small Fluffy and Small Floppy darkmark-chocolate tints (locale:75076, locale:75058) have a documented source, since sibling tints may share one.",
  "Retirement status is unknown; no retirement evidence was found.",
  "Critique fixes applied: removed the 'vendor' type and the 'where' value, cited the stores.json line for the legacy price, and stated that the 540 is inherited from the shared block. Confidence lowered to 0.15."
 ]}
