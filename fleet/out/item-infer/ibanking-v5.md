<!-- fleet job=item-infer id=ibanking-v5 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[7202, 8178, 6, 2480] model=claude-haiku-5-5 -->
# Banking

{"item": {"name": "Banking (bank storage slots and Bank Upgrades): a feature, not a single item", "locale_id": null, "kind": "other"},
 "sources": [
  {"type": "marketplace", "detail": "50-Slot Bank Upgrade (no purchase limit per the wiki)", "where": "Station Cash Marketplace", "price": null, "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Banking (rev 30292, Storage section); locale:19870 '50-Slot Bank Upgrade'. Price unknown: the wiki's station_cash array holds one unlabelled value (100) that is not tied to this item in the page text."},
  {"type": "coin_shop", "detail": "Bank Upgrade 1 (2-Slot) through Bank Upgrade 10 (100-Slot), bought in chronological order. One row per tier; per-tier price unmapped.", "where": "Coin Shop", "price": null, "currency": "coins", "source": "https://freerealms.fandom.com/wiki/Banking (Storage section: tier slot counts 2, 4, 6, 8, 10, 20, 40, 60, 80, 100); locale:19872 '2-Slot Bank Upgrade 1' through locale:19890 '100-Slot Bank Upgrade 10'. The wiki's unlabelled coins array (1000 to 50000, ten values) is not mapped to tiers and is not used as a price."},
  {"type": "membership", "detail": "June 2013 Monthly Membership Pack: 200 free storage slots, plus a free Storage Vault, for members who logged on in June 2013", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Banking (June 2013 Monthly Membership Pack paragraph). Ended event: retired."}
 ],
 "retired": "partial",
 "live": "unsure",
 "evidence": [
  {"claim": "Bank storage was introduced December 4th, 2012, with 25 starting slots.", "source": "https://freerealms.fandom.com/wiki/Banking"},
  {"claim": "Additional slots can be bought through the Station Cash Marketplace (the 50-Slot upgrade has no purchase limit) or the Coin Shop (upgrades in chronological order).", "source": "https://freerealms.fandom.com/wiki/Banking (Storage section)"},
  {"claim": "Client names exist for the 50-Slot Bank Upgrade and for Bank Upgrades 1 to 10 with slot counts 2 to 100.", "source": "locale:19870; locale:19872 to locale:19890"},
  {"claim": "June 2013 Monthly Membership Pack gave 200 free slots and a free Storage Vault to members who logged on in June 2013; this is an ended event.", "source": "https://freerealms.fandom.com/wiki/Banking"},
  {"claim": "Robgoblin Bankers Burglz (Seaside), Bezzle (Sanctuary) and Yoink (Snowhill) give bank access. They are access points, not item sources.", "source": "https://freerealms.fandom.com/wiki/Banking"},
  {"claim": "The wiki gives no price or vendor for the Storage Vault, a Housing item placed in a Lot. This is a gap in the evidence, not a confirmed negative.", "source": "https://freerealms.fandom.com/wiki/Banking"}
 ],
 "confidence": 0.3,
 "open": [
  "Split into separate records: the 50-Slot SC upgrade, each Coin Shop Bank Upgrade tier, the June 2013 membership pack (retired), and the Storage Vault housing item.",
  "50-Slot SC upgrade price is unknown. The wiki's station_cash value 100 is unlabelled in the quoted page text; read the rendered price cell on rev 30292 before stating a price.",
  "Coin Shop per-tier prices are unknown. The wiki's ten-value coins array (1000 to 50000) is unlabelled and unmapped to tiers 1 to 10.",
  "Storage Vault has no price, vendor or locale id in this pack. Its purchasability is unknown, not confirmed absent.",
  "No current availability is stated for the SC upgrade or the Coin Shop tiers, so live is unsure.",
  "locale:1741 (placeholder test text, negative slot count) is excluded from all evidence.",
  "wireable: false. The SC and Coin Shop rows have no evidenced price, and the membership row has no where and has ended."
 ],
 "critiques_addressed": [
  "Evidence: SC 100 price removed; shown as unknown.",
  "Evidence: Coin Shop range relabelled as unlabelled, unmapped; tier slot counts and locale 19872 to 19890 cited.",
  "Evidence: locale:1741 removed everywhere.",
  "Evidence: Storage Vault stated as unpriced, not as not purchasable.",
  "Retired: June 2013 pack marked retired; record-level retired set to partial.",
  "World: wireable set to false with reason; Coin Shop split into per-tier rows with price null; SC price shown as unknown."
 ]}
