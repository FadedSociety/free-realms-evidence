<!-- fleet job=citem-infer id=cflower-face-paint-card-119231-v3 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[6062, 9625, 6, 2067] model=claude-haiku-5-5 -->
# Flower Face Paint Card

{"item": {"name": "Flower Face Paint Card", "locale_id": 119231, "kind": "card"},
 "sources": [
  {"type": "other", "detail": "Unconfirmed coin store price record only: no seller, vendor, or stock row names this item. Record is no_sale true with sell_price_coins null, so no live sale is shown.", "where": null, "price": "180 coins (member price 162 coins, 10% member discount), as the store file states; not confirmed as current", "currency": "coins", "source": "repo:prototype/osfr-tools/data/content/stores.json line 14892 (item 69551, category 145 Face Paints)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name is locale 119231 'Flower Face Paint Card', description \"Don't get your petals in a bunch!\", class 1, slot 6, definition 69551.", "source": "locale:119231; client definition 69551"},
  {"claim": "Store row for item 69551 is in category 145 with purchase_price_coins 180, member_price_coins 162, sell_price_coins null, no_sale true.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 14892"},
  {"claim": "source_tags [L1, L2, L4, R2, L3, L3] are shared by every no_sale row in category 145 (lines 14890-14900, 14893-14895 etc.). Rows 69553, 69556, 69557 carry [L1, L2, L4, R2, T633, R1] with sell_price 18 and no_sale false. The tags look like a category-level pattern; their meaning is unknown and they are not used to infer any vendor or event.", "source": "repo:prototype/osfr-tools/data/content/stores.json lines 14890-14900"},
  {"claim": "Locale 156821 is a separate client string 'Flower face paint' with description 'This face paint tops the charts in flower fashion!'. It is a different string from 119231, so the name is not unique in the client. The client definition maps item 69551 to 119231, so 119231 is the working identity, but this is unverified beyond the definition.", "source": "locale:156821; locale:119231; client definition 69551"},
  {"claim": "The card sits in a Halloween-themed client block (locales 119226-119236). This is a grouping hint only and confirms no event source.", "source": "client cluster locale:119226 to locale:119236"},
  {"claim": "No wiki page, article, or video names the Flower Face Paint Card; client lookup returns only locale:119231 and locale:156821.", "source": "lookup of client, wiki, articles for 'Flower face paint' and 'Flower Face Paint Card'"}
 ],
 "confidence": 0.2,
 "open": [
  "No vendor, store, quest, drop, or event is named for item 69551 anywhere in the pack. The 180-coin figure is a store price record with no seller, so it is not a vendor source. Sources are left as an unsourced price record until a stock row or live check names a seller.",
  "no_sale true means the record is not a live sale. Whether the card is sold now, or was ever sold, is unknown and needs a live check or a wiki/forum price.",
  "Locale 156821 'Flower face paint' is a separate client string, confirmed by direct lookup. Confirm that definition 69551 uses locale 119231 and not 156821 before wiring.",
  "The source_tags [L1, L2, L4, R2, L3, L3] are unexplained category-wide metadata, not an acquisition record. Their meaning needs a key.",
  "The earlier Super Spooktacular event link is unproven for this card; no source names it.",
  "Retirement status is unknown; no source states it."
 ]}
