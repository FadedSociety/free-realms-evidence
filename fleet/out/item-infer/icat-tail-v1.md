<!-- fleet job=item-infer id=icat-tail-v1 status=done turns=2 usd=0.0014 tokens(read,write,in,out)=[3206, 4177, 6, 1660] model=claude-haiku-5-5 -->
# Cat Tail

{"item": {"name": "Cat Tail", "locale_id": 8840, "kind": "clothing"},
 "sources": [
  {"type": "marketplace", "detail": "Station Cash Marketplace, open to everyone (Clothing accessory, SC Marketplace Clothing)", "where": "Station Cash Marketplace", "price": "49 Station Cash (wiki station_cash value; the wiki price text is blank in the scrape)", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Cat_Tail"},
  {"type": "marketplace", "detail": "Member price on the Station Cash Marketplace, about 10% off", "where": "Station Cash Marketplace", "price": "44 Station Cash (sale price for Members, per wiki text saying '%10 discount')", "currency": "station_cash", "source": "https://freerealms.fandom.com/wiki/Cat_Tail"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Cat Tail is a Clothing accessory sold to everyone in the Station Cash Marketplace; Members get a roughly 10% discount.", "source": "https://freerealms.fandom.com/wiki/Cat_Tail"},
  {"claim": "Wiki categories: Clothing, Marketplace Items, Misc, Mysterious Merchant, SC Marketplace, SC Marketplace Clothing.", "source": "https://freerealms.fandom.com/wiki/Cat_Tail"},
  {"claim": "Client text name 'Cat Tail' (item id 8840) with description 'Purr-fectly feline.' (locale 8841).", "source": "locale:8840"},
  {"claim": "Cat Tail was among the new Halloween outfit items added in a Halloween outfit update article.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2306"},
  {"claim": "Same Halloween outfit item list (Cat Ears, Cat Tail, Dog Ears, Dog Tail, etc.) in a second Halloween article.", "source": "http://www.freerealms.com/article/detail.action?articleId=2309"}
 ],
 "confidence": 0.6,
 "open": [
  "The wiki price text is blank; the 49 and 44 values come from the wiki's station_cash field. Confirm 49 SC is the base price and 44 SC is the Member price.",
  "The Halloween articles list Cat Tail as a new Halloween outfit item. Unclear whether it was a Halloween-only release or a permanent SC Marketplace item later. The wiki lists it as a current SC Marketplace item, but it may have been sold only during the event.",
  "No retirement or unobtainable note found, so retired is null.",
  "No vendor, quest, drop, or prize wheel source found. Coin vendor stock and Mysterious Merchant rotation were not confirmed for this item.",
  "No repo or server data check was done for the marketplace listing."
 ]}
