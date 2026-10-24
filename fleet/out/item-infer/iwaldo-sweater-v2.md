<!-- fleet job=item-infer id=iwaldo-sweater-v2 status=done turns=5 usd=0.0044 tokens(read,write,in,out)=[46914, 20204, 12, 2839] model=claude-haiku-5-5 -->
# Waldo Sweater

{"item": {"name": "Waldo Sweater", "locale_id": 9146, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, available to everyone at the regular price (All Jobs, chest slot clothing)", "where": "Station Cash Marketplace (SC Marketplace Clothing)", "price": "175 Station Cash", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Waldo_Sweater (rev 37241, wikitext: 'regular price of {{SC|175}}'; categories SC Marketplace, SC Marketplace Clothing, Marketplace Items); repo:Sanctuary/src/Resources/StoreBundles.json:26245-26271 (Id 5405, NameId 9146, Price tier 1)"},
  {"type": "membership", "detail": "Members' 10% discount price on the same Station Cash Marketplace listing (sale price, not a separate item source)", "where": "Station Cash Marketplace", "price": "157 Station Cash", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Waldo_Sweater (rev 37241, wikitext: 'to Members at the 10% discount price of {{SC|157}}')"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Waldo Sweater is an All Jobs, chest slot clothing item sold on the Station Cash Marketplace; regular price 175 SC; Members 10% discount price 157 SC", "source": "https://freerealms.fandom.com/wiki/Waldo_Sweater (rev 37241 wikitext, both prices printed explicitly)"},
  {"claim": "Store bundle entry: Comment 'Waldo Sweater', LaunchTime 2012-11-01T07:00:00Z, ExpireTime 2040-12-31T08:00:00Z (far-future sentinel, not a dated retirement), Status 1, CurrencyType 1, MemberDiscount 1, GameItemId 5410, MarketingItemId 17925, NameId 9146, DescriptionId 9147", "source": "repo:Sanctuary/src/Resources/StoreBundles.json:26245-26271"},
  {"claim": "Item name is client text id 9146 'Waldo Sweater'", "source": "locale:9146"},
  {"claim": "Item is inspired by Waldo's shirt from the Where's Wally books; the 'Where's Waldo?' trademark credit is in the IGD line", "source": "https://freerealms.fandom.com/wiki/Waldo_Sweater (IGD and body text)"},
  {"claim": "Wiki page carries a {{Sunset Sale}} banner; the same banner appears on many SC Marketplace pages, so it is not by itself a retirement date", "source": "https://freerealms.fandom.com/wiki/Waldo_Sweater (rev 37241 wikitext, final line)"}
 ],
 "confidence": 0.8,
 "open": [
  "No coin vendor, quest reward, enemy drop, event, prize wheel, crafting, or collection source found in the pack or repo; none claimed.",
  "Retirement is not dated anywhere in the pack. The bundle ExpireTime 2040-12-31 is a sentinel. The Sunset Sale banner on the wiki page is ambiguous (it appears on many pages) and may hint at a later sunset; confirm against a marketplace snapshot or the wiki's Sunset Sale template text.",
  "Live status is unsure: the bundle was launched 2012-11-01 and never expired in data, but whether it was still sold at the end of the live game is not confirmed.",
  "The 157 member price is printed in the wiki wikitext itself (rev 37241), so it is not arithmetic; the earlier pack's critique that it was unverified is resolved by that source. The 157 figure is the wiki's own rounding of 10% off 175."
 ]}
