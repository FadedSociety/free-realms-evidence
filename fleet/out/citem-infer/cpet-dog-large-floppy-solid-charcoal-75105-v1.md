<!-- fleet job=citem-infer id=cpet-dog-large-floppy-solid-charcoal-75105-v1 status=done turns=4 usd=0.0026 tokens(read,write,in,out)=[19148, 12079, 10, 1881] model=claude-haiku-5-5 -->
# Pet: Dog: Large Floppy: solid-charcoal

{"item": {"name": "Pet: Dog: Large Floppy: solid-charcoal", "locale_id": 75105, "kind": "pet"},
 "sources": [{"type": "vendor", "detail": "Coin store sale, unnamed coin vendor (vendor not identified in the pack; the store row carries no NPC name)", "where": null, "price": "540 coins (member price 486 coins, 10% member discount)", "currency": "coins", "source": "repo:data/content/stores.json item 23955 (purchase_price_coins 540, member_price_coins 486, sell_price_coins 54, no_sale false)"}],
 "retired": null, "live": "yes",
 "evidence": [{"claim": "Client name and definition: 'Pet: Dog: Large Floppy: solid-charcoal', definition 23955, locale 75105, model dog_large_floppy.adr, one variant", "source": "locale:75105"},
  {"claim": "Coin store row exists for item 23955 at 540 coins, not marked no_sale, with a 10% member price of 486 coins", "source": "repo:data/content/stores.json item 23955"},
  {"claim": "Sibling dog pets 75100-75110 are in the same Large/Small Floppy/Pointy set; the store data prices the neighbouring rows 23936-23954 at the same 540 coins, so this is a standard coin-store pet line", "source": "repo:data/content/stores.json items 23936-23954"},
  {"claim": "Wiki and article searches return no page, image or forum fact naming this pet; the client has related tint variants 75113 'darkmark-charcoal' and 75117 'spots-charcoal'", "source": "lookup client/wiki/articles: no match for this name"},
  {"claim": "The T633 and L1-L4 tags in stores.json describe the sell-back rule and legacy data fields, not a vendor or source, so they were not used as source evidence", "source": "notes/Research/Coin Shop.md:33-34; notes/Autopilot/T633.md"}],
 "confidence": 0.5,
 "open": ["Which coin vendor (NPC and zone) sells item 23955 is not named in any source in the pack; the price row alone does not give the vendor. Needs a vendor lookup in the store data or a wiki/video check.",
  "No wiki page, image, video frame or forum fact confirms this pet; the 'live' status rests on the store row and the first-pass tag only.",
  "Whether the 540 coin price was ever changed or the pet was retired is not documented in the pack.",
  "Not checked: whether this pet is a Coin Shop item or a Legacy-only vendor item; the sell-back value of 54 coins is server policy, not a source."]}
