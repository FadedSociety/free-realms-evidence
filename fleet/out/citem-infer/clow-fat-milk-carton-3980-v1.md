<!-- fleet job=citem-infer id=clow-fat-milk-carton-3980-v1 status=nothing_found turns=6 usd=0.0063 tokens(read,write,in,out)=[77039, 30793, 14, 3408] model=claude-haiku-5-5 -->
# Low Fat Milk Carton

{"item": {"name": "Low Fat Milk Carton", "locale_id": 3980, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Low Fat Milk Carton' (locale 3980, description locale 3981: consumable that temporarily boosts timing as a Blacksmith, Chef, Miner and Postman). One definition (id 1147), class 9, no slots, no models, no coin store price.", "source": "client definition in task pack; locale:3980, locale:3981; opening-*/locale/en_us_data.dat (ucdt 3050917584, ugdt 3259399348)"},
  {"claim": "Sibling items 'Whole Milk Carton' (3978/3979) and 'Non Fat Milk Carton' (3982/3983) form a milk-carton consumable family with the same name pattern and job-talent text.", "source": "locale:3978, locale:3979, locale:3982, locale:3983"},
  {"claim": "Whole Milk Carton wiki page says it is a level 1 consumable that 'is no longer able to be acquired'; the catalog tags it Unobtainable. This is the only sibling with a wiki acquisition statement.", "source": "wiki page 'Whole Milk Carton'; refs freerealms-wiki/harvest/lists/catalog.json line 16944-16960"},
  {"claim": "The wiki 'Milk Carton' page (Freestyle Jobs hands clothing) says it was originally acquired through the now-unavailable 'Milk Rocks' quest and is trade-only; the 'Milk Rocks' Sanctuary rock-collection contest (locale 403232, 403234, 408601) names a milk carton signed by The Dares as its prize. That is a different item (Milk Carton, locale 154090), not the Low Fat carton.", "source": "wiki page 'Milk Carton'; locale:403232; locale:408601; quest-lines/schedule-packs.json (critique: Milk Carton removed from event rewards)"},
  {"claim": "No wiki page, article fact, video frame, coin vendor stock, store price, quest reward, or drop names the Low Fat Milk Carton. The repo has no quest or vendor row for locale 3980 or definition 1147 (the only '1147' hits are unrelated IDs).", "source": "lookup client/wiki/articles/video (only locale:3980 and 3981 returned); search repo/refs for 'Low Fat Milk' and '1147'"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. Likely a retired milk-carton consumable like Whole Milk Carton, but no source states how players got it. Needs a wiki page or a live-era source.",
  "Jev's first pass said live=yes; not supported by any evidence in the pack. Live status is unsure.",
  "Milk Rocks may be a candidate source (its sibling Milk Carton came from it), but no source ties Low Fat or Non Fat cartons to that quest. Do not list it without a source.",
  "Non Fat Milk Carton (locale 3982) is the likely sibling and should be checked the same way.",
  "No price: the client definition has no coin store entry and the wiki gives no price."
 ]}
