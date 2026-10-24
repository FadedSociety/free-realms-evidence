<!-- fleet job=citem-infer id=cmystery-key-436409-v3 status=done turns=2 usd=0.0027 tokens(read,write,in,out)=[7798, 10517, 6, 2561] model=claude-haiku-5-5 -->
# Mystery Key

{"item": {"name": "Mystery Key", "locale_id": 436409, "kind": "consumable"},
 "sources": [
  {"type": "marketplace", "detail": "Single Mystery Key, bought on the Station Cash Marketplace; consumed to open one Mystery Chest", "where": "Marketplace", "price": null, "currency": "station_cash", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2604 ; locale:436408 ; locale:436410 ; locale:436470 ; locale:690"},
  {"type": "promotion", "detail": "'Mystery Key Special!' limited-time bundle sale: save 40% on a Mystery Key (Priority 25, Bundle Sale). Base price not stated.", "where": "Marketplace", "price": "40% off; base price unknown", "currency": "station_cash", "source": "locale:28240 ; locale:28241"},
  {"type": "promotion", "detail": "Mystery Keys marked down sale notice (amount and dates not stated)", "where": "Marketplace", "price": "discounted; amount not stated", "currency": "station_cash", "source": "locale:33689"},
  {"type": "promotion", "detail": "New Years Mystery Key Sale: bulk bundles of 3, 5 and 10 Mystery Keys. 3-key bundle saves 100 SC; 5-key bundle saves 333 SC; 10-key bundle saves 1000 SC; 'save up to 50% on SC' in bulk, applying to these bundles only (not single keys). Base bundle prices not in the pack.", "where": "Marketplace", "price": "savings of 100 SC (3 keys), 333 SC (5 keys), 1000 SC (10 keys); base bundle price unknown", "currency": "station_cash", "source": "locale:436762-436767 ; locale:436768 ; locale:436769"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Mystery Key is bought on the Marketplace and is needed to open a Mystery Chest; it is used up on opening", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2604 ; locale:436408 ; locale:436410 ; locale:436470 ; locale:436472 (Mystery Keys can only be used once)"},
  {"claim": "May 2012 article (articleId 2609) says it is a great time to stock up on Mystery Keys and that they are bought from the Marketplace. The article does not state a discount.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2609 ; http://www.freerealms.com/article/detail.action?articleId=2611"},
  {"claim": "Single-key 40% bundle sale line exists (no base price)", "source": "locale:28241"},
  {"claim": "Bulk bundles of 3, 5 and 10 keys with SC savings of 100, 333 and 1000 SC; bulk discount up to 50% applies to these bundles only", "source": "locale:436762-436767 ; locale:436768 ; locale:436769"},
  {"claim": "Mystery Keys marked down notice", "source": "locale:33689"},
  {"claim": "Client definition 78137 has no coin store price, so no coin vendor sale for the key", "source": "client definition, definition_id 78137 (coin_store_prices empty)"},
  {"claim": "Server code treats definition 78137 as the consumed key for Mystery Chest opening", "source": "repo:prototype/osfr-tools/src/mystery_chest_loot.rs:17"}
 ],
 "confidence": 0.45,
 "open": [
  "Single-key Station Cash base price unknown; the 40% sale, markdown and 50% bulk discount give no base price in the pack.",
  "Membership source removed. The Monthly Member Pack Items page shows only Oct 2013 to Feb 2014 entries in retrieved text (Pinkeye, Toeny, SBS-1000, Lost Treasures Backpack, Lawless Gloam, Sunset Party Boat); no Mystery Key row or Dec 2011 to Apr 2012 section was seen.",
  "Promotions are dated 2012-era sale notices; no start or end dates in the pack. Not a confirmed current purchase route with a price.",
  "Current availability unknown: client text (locale 436470, 436408) still says to buy keys on the Marketplace, but client text is undated and no retirement source was found, so live is 'unsure'.",
  "Wiki News Archive snippet listing '1 Mystery Key' beside '10,000 Coins' in an unnamed January 2012 update is unresolved and not counted.",
  "No vendor stock, quest reward or enemy drop for the key found; no video frames."
 ],
 "wireable": false}
