<!-- fleet job=citem-infer id=cpet-dog-large-pointy-solid-gold-75119-v2 status=done turns=3 usd=0.0043 tokens(read,write,in,out)=[21207, 22530, 8, 2613] model=claude-haiku-5-5 -->
# Pet: Dog: Large Pointy: solid-gold

{"item": {"name": "Pet: Dog: Large Pointy: solid-gold", "locale_id": 75119, "kind": "pet"},
 "sources": [
  {"type": "vendor", "detail": "Unnamed coin vendor. No NPC, shop or stock row names this pet; vendors.json has no entry for item 23969. The only coin evidence is the store row's 540-coin price, which is the legacy Cost default and is not tied to a vendor. Unresolved.", "where": null, "price": "540 coins (legacy Cost default; member price 486, 10% member discount; sell-back 54 coins per the T633 rule)", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json item 23969 (line 6846, source_tags L1,L2,L4,R2,T633,R1; no T638 tag and no price_provenance block, so not cleared as the T638 rows were)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item as 'Pet: Dog: Large Pointy: solid-gold', locale 75119, definition 23969, model dog_large_pointy.adr, one definition, coin_store_prices [540]", "source": "locale:75119"},
  {"claim": "stores.json row for item 23969 carries purchase_price_coins 540, member_price_coins 486, sell_price_coins 54 and no price_provenance block", "source": "repo:prototype/osfr-tools/data/content/stores.json line 6846"},
  {"claim": "Sibling dog pets 23941, 23943, 23957, 23961 and 23966 have their 540 Legacy Cost cleared under T638 because no coin vendor stocks them and they are repriced in Station Cash (225 or 400 SC). Item 23969 has no such clearing, so its 540 is still unverified rather than shown to be sold.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 6818, 6820, 6834, 6838, 6843"},
  {"claim": "The T638 note says the Legacy coin Cost is a starting default, not a verified transaction price; the T633 note covers only the sell-back rule", "source": "repo:prototype/osfr-tools/data/content/stores.json line 42; repo:notes/Autopilot/T638.md; repo:notes/Autopilot/T633.md lines 5-13"},
  {"claim": "No wiki page, image, article fact, video frame, quest answer or vendor stock row names this pet. Lookups on 'Pointy dog pet solid-gold' failed on a query error, so the wiki and article search for it is not confirmed", "source": "lookup wiki/client/articles (query error); repo search for '23969' returns only stores.json line 6846 and an unrelated quest exclusion"},
  {"claim": "Name cluster locale 75114-75124 is the Dog pet set (Floppy and Pointy variants), with no source giving the set's sale channel", "source": "locale:75114 through locale:75124"}
 ],
 "confidence": 0.3,
 "open": [
  "The vendor NPC and zone are unidentified. vendors.json has no row for item 23969, so the 'vendor' type rests only on the coin store price. Source it to a vendor stock row before treating it as a vendor sale.",
  "The 540-coin price is the legacy Cost default copied into CoinStoreItems, not a checked transaction price. The sibling rows that were cleared (T638) show that the default can be wrong for pets. Confirm with a wiki or player price before trusting 540.",
  "Retirement status is unknown. No wiki page exists, so there is no 'Retired' or 'Coin Shop' category to cite.",
  "The lookup for this name failed with a query error (the FTS query was parsed wrongly), so the wiki, client-text and article checks are not confirmed. Rerun them with the name quoted as an exact phrase.",
  "T633 is a sell-back rule tag only. It says nothing about where the item is sold.",
  "The critique's point that the vendor is unnamed and that 540 is a catalogue default is correct; this answer drops the confirmed-sale wording and keeps the source as unverified."
 ]}
