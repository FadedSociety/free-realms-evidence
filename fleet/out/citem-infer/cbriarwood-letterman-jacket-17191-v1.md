<!-- fleet job=citem-infer id=cbriarwood-letterman-jacket-17191-v1 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[12554, 12209, 8, 2261] model=claude-haiku-5-5 -->
# Briarwood Letterman Jacket

{"item": {"name": "Briarwood Letterman Jacket", "locale_id": 17191, "kind": "clothing"},
 "sources": [{"type": "promotion", "detail": "Free giveaway for the 20-million-player celebration: every player who logged in and claimed it during the window. The client name (Briarwood Letterman Jacket, 17191) is a different label than the wiki's 'Free Realms Letterman Jacket', so the client name and the promotion are matched by the jacket type and the 8172 store row, not by name. Treat the match as likely, not certain.", "where": null, "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2305 ; http://www.freerealms.com/article/detail.action?articleId=2308 ; wiki page 'Free Realms Letterman Jacket'"}],
 "retired": true, "live": "no",
 "evidence": [{"claim": "Client definition 8172 / locale 17191 is a Freestyle chest jacket (slot 3, class 1, model freestyle_<race>_<gender>_chest_puffyjacket.adr), one variant.", "source": "locale:17191; client definition 8172"},
  {"claim": "The store data has a row for item 8172 with a legacy coin price of 270 (member 243, 10% discount), but no_sale is true, no category is set, and no coin vendor stocks it in the repo vendor data. The 270 is a legacy price field, not a confirmed vendor sale.", "source": "repo:prototype/osfr-tools/data/content/stores.json:6270 (item 8172); search of repo vendors for 8172 returned no vendor entry"},
  {"claim": "Free Realms Letterman Jacket was a Freestyle Jobs clothing item given out to everyone who logged in and claimed it from Oct 21 to Oct 31, 2011 (11:59 p.m. PDT), to celebrate 20 million registered players.", "source": "http://www.freerealms.com/article/detail.action?articleId=2308 ; http://www.freerealms.com:80/article/detail.action?articleId=2305 ; wiki 'Free Realms Letterman Jacket'"},
  {"claim": "The video frame shows the Free Realms Letterman Jacket in the inventory as a Chest item, Level 1, Freestyle Jobs, boys only.", "source": "video:6mmERh2D8yc/00308"},
  {"claim": "Other items in the client cluster (Disco Fever set, Card Duelist Bandolier, Leopard Pants) are separate items; the cluster does not link this jacket to a quest or vendor.", "source": "locale:17188-17195"}],
 "confidence": 0.6,
 "open": ["The 270-coin store row (8172) is a legacy price with no_sale true and no vendor stocking it. Do not list a coin vendor sale unless a vendor is found.",
  "The client name 'Briarwood Letterman Jacket' differs from the wiki/article name 'Free Realms Letterman Jacket'. Confirm the 8172 item is the 2011 giveaway jacket and not a separate Briarwood-themed item.",
  "The claim window closed Oct 31, 2011, so the jacket is retired. Later re-release or redemption is not documented in the sources checked.",
  "The video shows the wiki-style name as 'Boys only'; the client slot data does not show gender restrictions, so verify before rebuilding."]}
