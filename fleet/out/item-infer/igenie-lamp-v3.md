<!-- fleet job=item-infer id=igenie-lamp-v3 status=done turns=2 usd=0.0021 tokens(read,write,in,out)=[5107, 10520, 6, 1481] model=claude-haiku-5-5 -->
# Genie Lamp

{"item": {"name": "Genie Lamp", "locale_id": 385810, "kind": "weapon"},
 "sources": [
  {"type": "vendor", "detail": "Cragara, the Mysterious Merchant: sold to everyone at the regular price; members get a 10% discount price", "where": "Mysterious Merchant (Cragara; roaming, town not verified in the pack)", "price": "225 (regular); 202 (member discount price)", "currency": "station_cash", "source": "wiki Genie_Lamp rev 37276 wikitext: freerealms-wiki/wikitext/12316-37276-3e9bd967740c.wiki line 2, '{{SC|225}}' and '{{SC|202}}'; sale also listed in quest-lines/npcs.json (Cragara 'vendor_sells' citing wiki Genie Lamp)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Genie Lamp is a Freestyle Jobs weapon-slot item sold through Cragara, the mysterious merchant, to everyone, with a members discount.", "source": "wiki Genie_Lamp (rev 37276), wikitext line 2"},
  {"claim": "Regular price is 225 Station Cash; member price is 202 Station Cash (the wiki's rendered page text is blank for these figures, but the raw wikitext of the same revision carries them via the SC template).", "source": "freerealms-wiki/wikitext/12316-37276-3e9bd967740c.wiki line 2"},
  {"claim": "Cragara's list of sold items includes Genie Lamp.", "source": "quest-lines/npcs.json line 32831 (citing wiki Genie Lamp); line 80810 and 105658 (Cragara vendor_sells, rotating limited stock)"},
  {"claim": "Item name 'Genie Lamp' is client text id 385810.", "source": "locale:385810"},
  {"claim": "Cragara's goods are a rotating, limited-stock selection, so current availability is not confirmed.", "source": "quest-lines/npcs.json line 80810 (citing wiki Cragara)"}
 ],
 "confidence": 0.8,
 "open": [
  "Current availability is unverified: Cragara's stock rotates and the pack has no dated evidence that the lamp is still on sale. Retirement status is unknown (retired: null).",
  "Price 225/202 Station Cash comes from the wikitext of revision 37276; it is not confirmed against a store table (Lxzxrus-Free-Realms-Server StoreBundles.json line 36578 has a 'Genie Lamp' entry that was not checked for price).",
  "The Cragara town/location is not evidenced in the pack; 'where' is left as the Mysterious Merchant.",
  "No quest, drop, event, crafting, collection, or promotion source was found."
 ]}
