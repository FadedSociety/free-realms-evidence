<!-- fleet job=citem-infer id=cbe-mine-basket-9988-v3 status=done turns=3 usd=0.0028 tokens(read,write,in,out)=[16030, 10855, 8, 2483] model=claude-haiku-5-5 -->
# Be-Mine Basket

{"item": {"name": "Be-Mine Basket", "locale_id": 9988, "kind": "other"},
 "sources": [
  {"type": "other", "detail": "Colour variant (Amethyst, Bubblegum, Rubyburst, Stonesurf) listed on the Gifting Basket page alongside the Be-Mine Balloon and Floral Arrangements. The page does not say whether this item was sold on its own or only obtained from the Gifting Basket; the parent Gifting Basket was sold through the SC Marketplace in the 2011 Festival of Hearts. Acquisition method unconfirmed.", "where": "SC Marketplace (Gifting Basket set, 2011 Festival of Hearts)", "price": null, "currency": null, "source": "wiki: Gifting Basket (https://freerealms.fandom.com/wiki/Gifting_Basket)"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client name 'Be-Mine Basket' is locale:9988 (item, description 'Great for giving to that special someone.' is locale:9996, the 'Be-Mine items' group line).", "source": "locale:9988; locale:9996"},
  {"claim": "The Gifting Basket is a housing item previously sold through the Station Cash Marketplace during the 2011 Festival of Hearts and can no longer be acquired.", "source": "wiki: Gifting Basket"},
  {"claim": "The Gifting Basket page lists '[Be-Mine] Basket, available in Amethyst, Bubblegum, Rubyburst, Stonesurf', with the Balloon and Large/Small Floral Arrangements in the same colours.", "source": "wiki: Gifting Basket (search excerpt)"},
  {"claim": "Pets Cupid, Heart Critter and Lovasus are obtainable from the Gifting Basket and the Gifting Basket was 2011-only.", "source": "wiki: Cupid; wiki: Heart Critter; wiki: Lovasus"},
  {"claim": "Festival of Hearts page lists the Be-Mine Bouquet, Gifting Basket and Lovely T-Shirt as 2011-only. It does not name the Be-Mine Basket.", "source": "wiki: Festival of Hearts"},
  {"claim": "Coin store listing for item 76822, category 54: purchase 2000 coins, member 1800, sell 200, no no_sale flag. The row carries no vendor, price provenance or sale note.", "source": "repo:prototype/osfr-tools/data/content/stores.json line 16334"}
 ],
 "confidence": 0.4,
 "open": [
  "Coin price conflict: stores.json item 76822 lists 2000 coins (member 1800, sell 200), but no coin vendor or sale is named anywhere, and the wiki places the Be-Mine Basket only in the Gifting Basket colour set (SC). Not counted as a source; treat as an unverified listing.",
  "Acquisition method unresolved: the Gifting Basket page's colour list could mean SC Marketplace sale of the Basket or random prizes from the Gifting Basket (pets are listed as prizes on the same page). Full Gifting Basket page not read in this pass.",
  "Price: no Station Cash price for the Be-Mine Basket is given anywhere in the sources.",
  "Kind: 'other' kept. Wiki calls the parent Gifting Basket a housing item and the model is hsg_bemine_basket_01 (decor-like), so 'furniture' is likely; not confirmed.",
  "Dropped from prior answer: 'daily gifts for 30 days' promotion wording (unsupported), 'event' source (Festival of Hearts page does not name this item), and the separate promotion source (duplicate of the Gifting Basket line).",
  "Live status: wiki says the Gifting Basket can no longer be acquired; the Be-Mine Basket inherits that, so retired=true, live=no."
 ]}
