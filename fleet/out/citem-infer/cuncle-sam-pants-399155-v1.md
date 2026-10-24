<!-- fleet job=citem-infer id=cuncle-sam-pants-399155-v1 status=done turns=6 usd=0.0027 tokens(read,write,in,out)=[27044, 7595, 14, 2869] model=claude-haiku-5-5 -->
# Uncle Sam Pants

{"item": {"name": "Uncle Sam Pants", "locale_id": 399155, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Sold individually as a piece of the Uncle Sam Outfit (jacket, top hat, pants, shoes) on the Station Cash Marketplace; no per-piece SC price found in sources", "where": "Station Cash Marketplace", "price": null, "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2160; wiki page 'Uncle Sam Outfit' (Category:SC Marketplace, Category:Marketplace Items, Category:Seasonal)"},
  {"type": "promotion", "detail": "Memorial Day Pack (bundle: Uncle Sam Top Hat, Jacket, Pants, Shoes, 5 USA Flags, 1 USA T-Shirt), a May 2011 Memorial Day sale", "where": "Station Cash Marketplace", "price": "400 Station Cash (described as 1300 SC value)", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146; locale:435553; locale:435555"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Uncle Sam Pants is the client item name, locale 399155, with description 'No flags were harmed in the making of these pants.' (locale 399295)", "source": "locale:399155; locale:399295"},
  {"claim": "Uncle Sam Pants is one of the four pieces of the Uncle Sam Outfit sold on the Marketplace", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2160"},
  {"claim": "The Uncle Sam Outfit was later available again on the Marketplace for a limited time", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2160"},
  {"claim": "Summer Marketplace Uncle-Sam Hose (pants) were removed after 10 August 2011", "source": "http://www.freerealms.com/article/detail.action?articleId=2171"},
  {"claim": "Memorial Day Pack sold for 400 Station Cash and contained Uncle Sam Top Hat, Jacket, Pants, Shoes, 5 USA Flags, 1 USA T-Shirt", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146; locale:435553"},
  {"claim": "Wiki 'Uncle Sam Outfit' page lists the Uncle Sam Pants in Category:SC Marketplace Clothing", "source": "wiki page 'Uncle Sam Outfit'"}
 ],
 "confidence": 0.6,
 "open": [
  "The client definition's coin store price of 50 coins could not be verified: a search of prototype/osfr-tools/data/content (stores.json and all others) finds no entry for definition 15924 or the variant ids 58496-58506. Treat the 50-coin vendor source as unconfirmed and do not add a coin vendor until a store entry is found. Also the pack's 'vendor_stock' is empty.",
  "The per-piece Marketplace price in Station Cash is not stated in any source; only the 400 SC Memorial Day Pack price is documented.",
  "Retirement is conflicting: article 2171 says the summer Marketplace Uncle-Sam pants were removed after 10 Aug 2011, but article 2160 says the outfit returned to the Marketplace for a limited time. The dates of the return and the final removal are not sourced.",
  "The 'currency: reward' claim for the Memorial Day event in the other answer is not supported by article 2146, which says Station Cash sale; that answer's event row was not used as a source.",
  "The 36 definitions (15924 plus 58496-58506 variants) were not individually checked for which races/genders were sold; the item count was not verified against sources.",
  "Items in the Memorial Day Pack in locale 435555 is a second copy of the pack text; the sale dates (May 2011) come from the pack's name and the other answer, not from article 2146 itself."
 ]}
