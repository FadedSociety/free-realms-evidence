<!-- fleet job=citem-infer id=cfaded-jungle-ring-89463-v2 status=nothing_found turns=3 usd=0.0024 tokens(read,write,in,out)=[13263, 9211, 8, 2236] model=claude-haiku-5-5 -->
# Faded Jungle Ring

{"item": {"name": "Faded Jungle Ring", "locale_id": 89463, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition id 10454, NameId 89463, Type 1, Slot 8, Class 67, CategoryId 108, MinProfileRank 4, MemberDiscount 10, PowerRating 2, TintAlias dyetint, DescriptionId 1114 (no text resolves for 1114 in the locale lookup).", "source": "refs:Sanctuary-PS3-20261009/src/Resources/ClientItemDefinitions.json:220712-220730"},
  {"claim": "The block for Id 10454 carries its own 'Cost': 640 at line 220721. The previous answer's claim that this Cost belongs to Id 582 was wrong: Id 582 is only the Icon of the Faded Ocean Ring (Id 10453), whose own block also has Cost 640 at line 220702.", "source": "refs:Sanctuary-PS3-20261009/src/Resources/ClientItemDefinitions.json:220693-220730"},
  {"claim": "The Cost 640 is a client-definition field, not a store row. Nothing in the repo links definition 10454 to a stores.json entry, and the pack lists no coin_store_prices, so it is not treated as a coin vendor sale.", "source": "refs:Sanctuary-PS3-20261009/src/Resources/ClientItemDefinitions.json:220721; repo search for '10454' found no store row"},
  {"claim": "Faded ring family is real in the client text table: Faded Air Ring 89382, Faded Wind Ring 89383, Faded Void Ring 89384, plus Faded Air/Wind/Void Necklace 89412-89414. Faded Ocean Ring 89462 and Faded Jungle Ring 89463 are adjacent ids in the same block.", "source": "locale:89382, locale:89383, locale:89384, locale:89412-89414, locale:89462, locale:89463"},
  {"claim": "No wiki page, image, article fact, video frame, coin vendor, quest reward, drop or event names this ring. The first-pass 'live yes, drop' tag is a cheap-model hint and is not used.", "source": "lookup client/wiki/articles/video 'Faded Ring' (no ring match); jev_first_pass in evidence pack"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. The 'drop' guess remains unsupported.",
  "Client Cost 640 on definition 10454 is an unverified price lead. It may be a vendor or store price, but no store row, wiki price or article confirms it. Do not record it as a coin price until a source does.",
  "Live status and retirement date are unknown. The item exists in the client and the Sanctuary build, but no source shows it was obtainable in the 2009-2014 game.",
  "The family's sibling source (refs:quest-lines/citem-packs.json:109383-109384) was not checked. If it names a shared set reward or event, it could apply to this ring.",
  "Description id 1114 resolves to no text, so it gives no source or flavour hint.",
  "Kind 'clothing' is inferred from slot 8 and class 67, not from a confirmed in-game description."
 ]}
