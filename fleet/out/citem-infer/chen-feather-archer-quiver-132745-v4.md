<!-- fleet job=citem-infer id=chen-feather-archer-quiver-132745-v4 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[6108, 8161, 6, 1960] model=claude-haiku-5-5 -->
# Hen Feather Archer Quiver

{"item": {"name": "Hen Feather Archer Quiver", "locale_id": 132745, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Gilbert (NPC 9500000307; sells exclusively Archer job items)", "where": "Greenwood Forest", "price": "375 coins reference price (member 337 coins, 10% discount; sell 37 coins). Reference price from stores.json, not a captured NPC quote", "currency": "coins", "source": "wiki page Gilbert (Sells: [Hen] [Feather] [Archer] [Quiver]); repo:prototype/osfr-tools/data/content/vendors.json lines 15857-15874 (stock row includes 75737); repo:prototype/osfr-tools/data/content/npcs/greenwood_forest.json line 10957 (NPC 9500000307 placed in Greenwood Forest); repo:prototype/osfr-tools/data/content/stores.json item 75737 (line 15523)"},
  {"type": "vendor", "detail": "Meridia (sells exclusively Archer job items)", "where": null, "price": null, "currency": null, "source": "wiki page Meridia (Sells: [Hen] [Feather] [Archer] [Quiver]); repo:prototype/osfr-tools/data/content/vendors.json lines 22601-22640 list 75737 but apply the shared stores.json reference price, not a per-NPC quote"},
  {"type": "vendor", "detail": "Roberge (sells exclusively Archer job items)", "where": null, "price": null, "currency": null, "source": "wiki page Roberge (Sells: [Hen] [Feather] [Archer] [Quiver]); repo vendors.json line 22128 lists 75737 (shared reference price, not a per-NPC quote)"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client name locale 132745 'Hen Feather Archer Quiver', part of the Hen Feather Archer set (locale 132740-132744), client definition 75737, slot 6 (shoulders), class 16.", "source": "locale:132745"},
  {"claim": "Coin store reference row: purchase 375 coins, member 10% discount to 337, sell 37, category 106, no_sale false.", "source": "repo:prototype/osfr-tools/data/content/stores.json item 75737"},
  {"claim": "Gilbert, Meridia and Roberge wiki pages each list Hen Feather Archer Quiver under Sells; each says it sells exclusively Archer job items.", "source": "wiki pages Gilbert, Meridia, Roberge (lookup)"},
  {"claim": "Gilbert's NPC 9500000307 is placed in Greenwood Forest.", "source": "repo:prototype/osfr-tools/data/content/npcs/greenwood_forest.json line 10957"},
  {"claim": "Sheep Watch wiki page lists [Hen] [Feather] [Archer] [Quiver] after the 'Battle Item Mystery Pack' heading, not under '[Archer] Prize Wheel'. Not counted as a prize-wheel source.", "source": "wiki page Sheep Watch (lookup snippet)"}
 ],
 "confidence": 0.6,
 "open": [
  "The 375/337/37 coin figures are a stores.json reference price, not an NPC-observed quote. vendors.json marks the Gilbert row as '(R) reference price, not captured NPC quote'. The same reference is applied to Meridia and Roberge rows, so it is not per-vendor evidence.",
  "Meridia and Roberge have no verified price or zone. Their 'where' is null. Their wiki listings are the only evidence for them.",
  "Sheep Watch lists the Quiver after 'Battle Item Mystery Pack' (8 Coins heading). It may be a Battle Item Mystery Pack reward, but the snippet is ambiguous. Not listed as a source; needs a page check.",
  "Retirement is unconfirmed. No source says it was removed. The stores.json row is a reference and does not prove current NPC stock. Retired left null."
 ]}
