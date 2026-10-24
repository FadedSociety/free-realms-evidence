<!-- fleet job=item-infer id=ituxedo-pants-v3 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[5759, 7847, 6, 2679] model=claude-haiku-5-5 -->
# Tuxedo Pants

{"item": {"name": "Tuxedo Pants", "locale_id": 151349, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, available to everyone at the regular price", "where": "SC Marketplace", "price": "99 Station Cash (regular; wiki station_cash field only, prose price stripped)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Tuxedo_Pants (rev 37221; categories SC Marketplace, SC Marketplace Clothing, Marketplace Items)"},
  {"type": "membership", "detail": "Members buy at a 10% discount (sale price) in the SC Marketplace", "where": "SC Marketplace", "price": "89 Station Cash for Members (10% off; wiki station_cash field only)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Tuxedo_Pants (page text: 'to Members at the 10% discount price'; station_cash field value 89)"},
  {"type": "vendor", "detail": "Cragara, the Mysterious Merchant: page is category-tagged Mysterious Merchant, but the page text names only the SC Marketplace; current stock unverified. Cragara's listed items are Station Cash items, so any Cragara sale would be Station Cash, not coins", "where": "Cragara (Mysterious Merchant)", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Category:Mysterious_Merchant ('Items that are sold by the Mysterious Merchant, Cragara'; also Category:Station Cash); https://freerealms.fandom.com/wiki/Tuxedo_Pants (Category:Mysterious Merchant tag)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Tuxedo Pants is an All Jobs, legs-slot clothing item sold in the SC Marketplace at the regular price, with a 10% discount price for Members.", "source": "https://freerealms.fandom.com/wiki/Tuxedo_Pants"},
  {"claim": "Station Cash prices 99 (regular) and 89 (Members) come from the page's station_cash field; the prose price text is stripped, so the figures are field-only.", "source": "https://freerealms.fandom.com/wiki/Tuxedo_Pants (station_cash field, rev 37221)"},
  {"claim": "Category:Mysterious Merchant defines its members as items sold by the Mysterious Merchant, Cragara, and is tagged Station Cash.", "source": "https://freerealms.fandom.com/wiki/Category:Mysterious_Merchant"},
  {"claim": "Sibling Cragara items (Soccer Ball, Chibi, Scout, Marlin, Genie Lamp, Frog Face, Bowling Pin Outfit) are described as sold by Cragara for Station Cash-style regular/member pricing, with 'occasionally available' wording on several.", "source": "wiki pages: Soccer Ball, Chibi, Scout, Marlin, Genie Lamp, Frog Face, Bowling Pin Outfit, Polka Dot Umbrella, Cardboard Robot Head"},
  {"claim": "Client name locale:151349 reads 'Tuxedo Pants'. locale:143530 is a plural-form name entry '{n}Tuxedo Pants' with pl 'Tuxedo Pants', the same name in another form.", "source": "locale:151349; locale:143530"},
  {"claim": "locale:151350 is listed under the same name hint but its text ('A ninja needs many faces... add one to your shoulder!') describes a shoulder item, so it is not this item's description.", "source": "locale:151350"}
 ],
 "confidence": 0.5,
 "open": [
  "Station Cash prices 99 and 89 are from the stripped station_cash field, not readable prose. Confirm with a Marketplace screenshot or archive.",
  "The Cragara vendor link rests only on the Mysterious Merchant category tag. The Tuxedo Pants page text does not name Cragara, and no coin price is given. Stock and any Cragara price are unverified.",
  "Retirement status and end date are not in the pack. Live status is unsure.",
  "The page text retrieved for the Tuxedo Pants wiki page was truncated; the Mysterious Merchant tag was confirmed only through the pack's category list, not in the readable excerpt.",
  "locale:143530 is a plural-form name entry; it is not independent proof of the item's identity beyond the shared name."
 ]}
