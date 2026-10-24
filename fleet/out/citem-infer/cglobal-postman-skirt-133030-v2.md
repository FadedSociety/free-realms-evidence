<!-- fleet job=citem-infer id=cglobal-postman-skirt-133030-v2 status=done turns=3 usd=0.0020 tokens(read,write,in,out)=[13686, 7654, 8, 1750] model=claude-haiku-5-5 -->
# Global Postman Skirt

{"item": {"name": "Global Postman Skirt", "locale_id": 133030, "kind": "clothing"},
 "sources": [
  {"type": "vendor", "detail": "Clavin (NPC id 9500000660), gear merchant; wiki Clavin 'Sells' section lists 'Global Postman Skirt' (2013 snapshot)", "where": "Shrouded Glade", "price": null, "currency": null, "source": "wiki page Clavin, https://freerealms.fandom.com/wiki/Clavin (revision 2013-10-09T00:59:21Z, section Sells); repo:prototype/osfr-tools/data/content/vendors.json:29218-29226"},
  {"type": "other", "detail": "Catalogue coin-store reference price for item 76022 (store row with no named vendor or store; price_basis is a reference, not a captured NPC quote)", "where": null, "price": "1276 coins (member 1148 coins at 10% discount; sell-back 127 coins)", "currency": "coins", "source": "repo:data/content/stores.json item 76022 (line 15754); repo:prototype/osfr-tools/data/content/vendors.json:29207-29211"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Global Postman Skirt', locale 133030, one definition 76022, slot 4, class 3, model courier_<race>_f_legs_skirt.adr", "source": "locale:133030"},
  {"claim": "Wiki Clavin Sells lists 'Global Postman Skirt' (2013-10-09 revision); the wiki entry gives no price", "source": "repo:prototype/osfr-tools/data/content/vendors.json:29218-29226"},
  {"claim": "stores.json has a row for item 76022 (category 104) with purchase 1276, member 1148, sell 127 coins; the row does not name a vendor", "source": "repo:data/content/stores.json:15754"},
  {"claim": "Set-mates Global Postman Shoes/Gloves/Hat/Pants and First-Class Postman items share the client locale block 133025-133035", "source": "locale:133025 through locale:133035"},
  {"claim": "Wiki text '[Global] [Postman] [Skirt]' appears in lookup results; no category is asserted", "source": "lookup wiki: '[Global] [Postman] [Skirt]'"}
 ],
 "confidence": 0.5,
 "open": [
  "Clavin's price is not evidenced: the 1276/1148/127 coin figures are a stores.json catalogue reference price, not a quote seen on Clavin or the wiki. Do not treat them as Clavin's price until a captured NPC quote is found.",
  "The stores.json coin row does not name a store or NPC, so it is not confirmed to be the same sale as Clavin's listing.",
  "Only source for the Clavin link is a 2013 wiki snapshot; no removal date found, so live status is unsure and retirement is unknown.",
  "No drop, quest, event, prize-wheel, crafting or collection source found in the pack or repo.",
  "Pack's earlier 'Ids on Postman (hat 2750038008...)' note uses a different id scheme and was not used."
 ]}
