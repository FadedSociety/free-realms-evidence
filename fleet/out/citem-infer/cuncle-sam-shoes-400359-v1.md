<!-- fleet job=citem-infer id=cuncle-sam-shoes-400359-v1 status=done turns=2 usd=0.0019 tokens(read,write,in,out)=[3858, 6108, 6, 2207] model=claude-haiku-5-5 -->
# Uncle Sam Shoes

{"item": {"name": "Uncle Sam Shoes", "locale_id": 400359, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, sold as a single piece of the Uncle Sam Outfit (jacket, top hat, pants, shoes)", "where": "SC Marketplace", "price": "not stated for the shoes alone; the Memorial Day Pack containing them was 400 Station Cash (described as a 1300 SC value)", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2160; wiki page Uncle Sam Outfit (Category:SC Marketplace); article 2146"},
  {"type": "promotion", "detail": "Memorial Day Pack (Station Cash sale, May 2011): Uncle Sam Top Hat, Jacket, Pants, Shoes, 5 USA Flags, 1 USA T-Shirt", "where": "SC Marketplace", "price": "400 Station Cash (article calls it a 1300 SC value)", "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146; locale:435553; locale:435555 (Memorial Day Pack)"},
  {"type": "marketplace", "detail": "Uncle Sam Outfit re-offered on the Marketplace for a limited time (later return of the set)", "where": "SC Marketplace", "price": null, "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2160"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Item name and description exist in client text", "source": "locale:400359; locale:400394"},
  {"claim": "Shoes are one piece of the Uncle Sam Outfit sold on the Marketplace; wiki page is Clothing/Feet with no price", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2160; wiki page Uncle Sam Shoes"},
  {"claim": "Summer Marketplace item removed after 10 August 2011", "source": "http://www.freerealms.com/article/detail.action?articleId=2171"},
  {"claim": "Memorial Day Pack sold for 400 SC and contained the Uncle Sam Shoes", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2146; locale:435553"},
  {"claim": "Uncle Sam Outfit later returned to the Marketplace for a limited time, including shoes", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2160"},
  {"claim": "Pack's claim of a 270 coin-store price could not be verified: no repo record of definition 15925 or 60078-60088 in data/content/stores.json; the item is a Station Cash item per articles", "source": "repo search (no match)"}
 ],
 "confidence": 0.7,
 "open": [
  "The 270 coin-store price in the evidence pack is not confirmed: the repo has no stores.json entry for these definition ids, and the articles say Station Cash Marketplace. Treat as unverified; do not list as a coin vendor sale unless a stores.json row is found.",
  "The other answer's source 'event: Memorial Day and Spring Chicken Pack' with currency 'reward' is wrong: the Memorial Day Pack was a Station Cash purchase (400 SC), not a reward. Corrected above as promotion/marketplace.",
  "Shoes-alone Station Cash price is not stated in any source; only the 400 SC pack price is known.",
  "Exact dates of the Marketplace sale and the limited return are not given beyond 'removed after 10 August 2011'.",
  "No vendor, quest, or drop source found. Client has 33 definitions (tints/races) under this name; only the 12 listed ids were checked."
 ]}
