<!-- fleet job=citem-infer id=cspooky-speedster-chassis-416540-v1 status=done turns=4 usd=0.0045 tokens(read,write,in,out)=[33468, 22185, 10, 2792] model=claude-haiku-5-5 -->
# Spooky Speedster Chassis

{"item": {"name": "Spooky Speedster Chassis", "locale_id": 416540, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name 'Spooky Speedster Chassis' is locale 416540, description locale 416541 'The chassis for the Spooky Speedster.' (one definition, id 69826, class 141, slot 0, no coin store price).", "source": "locale:416540; locale:416541; pack client_definition"},
  {"claim": "The kart it belongs to, 'Spooky Speedster' (locale 416538), is a Halloween kart listed among the Halloween karts in the Spooktacular article.", "source": "articles/facts.json line 55302 (article-2304, 'Spooktacular Returns', http://www.freerealms.com:80/article/detail.action?articleId=2304)"},
  {"claim": "Wiki page 'Spooky Speedster' exists (pageid 2377, last revised 2013-09-14). It says 'The Spooky Speedster is a Halloween Kart' and is in Category:Karts, Category:Seasonal, Category:Race Kart and Category:Super Spooktacular. It names no price, no acquisition route and no retirement date. The pack's wiki_page: null is wrong.", "source": "wiki page Spooky Speedster (refs freerealms-wiki/raw/482ce4dbfa2306c6dff348f00b5cd966e625ed29217f66068dbc0583bf5fa29a.json)"},
  {"claim": "The sibling parts (Engine 416542, Turbo 416544, Tires 416548, Steering Column 416546) are in the same client cluster, but no source gives how any kart part was obtained.", "source": "locale:416542-416548 (client cluster)"},
  {"claim": "The kart-driver job notes say the only confirmed kart reward is 1 Blast Speedster (Sandstorm's Grand Opening). Kart parts are the job's progression items. No Spooky part source is recorded.", "source": "notes/Build Guides/Content/Jobs/Kart Driver.md:25"}
 ],
 "confidence": 0.3,
 "open": [
  "No source gives how the Spooky Speedster Chassis (or the Spooky Speedster engine, turbo, tires, steering column) was obtained. Not a coin vendor (no coin store price, no vendor stock), not a wiki price, not in the repo quest or drop data, not in video frames.",
  "Likely source is the Super Spooktacular (Halloween) event, given the kart's wiki categories, but the chassis-level route (event prize, prize wheel, SC pack, or kart bundle) is unverified. Do not mark as an event source until someone confirms.",
  "The 'live' status is unknown. The wiki gives a Seasonal and Super Spooktacular category but no retirement or unobtainable tag. The first-pass 'live: yes' is a hint only and is not confirmed.",
  "The client_definition shows 0 model files and no coin store price. Both are consistent with a non-vendor item but do not confirm the source.",
  "Next step: look for Spooktacular event quest or prize data in the repo and the Super Spooktacular category members on the wiki, and for video frames of Halloween karts being won or bought."
 ]}
