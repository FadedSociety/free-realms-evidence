<!-- fleet job=citem-infer id=croyal-bixie-trinket-77470-v2 status=nothing_found turns=3 usd=0.0028 tokens(read,write,in,out)=[16801, 13158, 8, 1889] model=claude-haiku-5-5 -->
# Royal Bixie Trinket

{"item": {"name": "Royal Bixie Trinket", "locale_id": 77470, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Name 'Royal Bixie Trinket' is locale 77470; description 77471 says it turns the user into an Elite Bixie Guard.", "source": "locale:77470; locale:77471"},
  {"claim": "Client lookup for the name returns only the three client rows 77470-77472. No wiki page, article, or video frame names the item.", "source": "lookup (client, wiki, articles, video) 'Royal Bixie Trinket'"},
  {"claim": "The 'Warpstone Woes' quest (title 77433) is marked NOT LIVE, with dialog 77432, objective 77434 and reward 77435 also flagged. Its text (77435 'Now I can speed up my mail delivery') matches the trinket-adjacent lines 77472-77473, but no row binds definition 24090 to that quest or to Mili as reward giver.", "source": "locale:77433; locale:77435; locale:77473; repo search for 24090/77470 found no quest or reward row"},
  {"claim": "stores.json has an item_id 77470 row, but it is a Balloon Animal price record (basis cites wiki Balloon Animal, 349 SC) with no coin price and no_sale true. It is a locale-id collision, not a sale of the trinket, and the client definition 24090 lists no coin store price.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 16692"},
  {"claim": "The stores.json row for item_id 77433 (purchase 270 coins) is likewise an id collision with the quest title locale 77433 and does not concern this trinket.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 16671"}
 ],
 "confidence": 0.2,
 "open": [
  "No evidenced source. The only candidate is a quest reward from the NOT LIVE 'Warpstone Woes' chain (Mili as turn-in NPC, Cobblestone Village), which is an inference from adjacent locale ids and shared text. It is not confirmed, so it is not listed as a source. Confirm by finding a quest reward table row that grants definition 24090.",
  "Live status is unknown. A NOT LIVE quest chain does not prove the item is not live, and Jev's first-pass 'live: yes' has no source. Retired is null for the same reason.",
  "Critique fix applied: Mili as trinket reward giver is no longer stated as fact.",
  "Repo's data/content has no record for definition 24090 (only the id-collision rows above)."
 ]}
