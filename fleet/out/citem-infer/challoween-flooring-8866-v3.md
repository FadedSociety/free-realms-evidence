<!-- fleet job=citem-infer id=challoween-flooring-8866-v3 status=done turns=4 usd=0.0036 tokens(read,write,in,out)=[36394, 15127, 10, 2657] model=claude-haiku-5-5 -->
# Halloween Flooring

{"item": {"name": "Halloween Flooring", "locale_id": 8866, "kind": "furniture"},
 "sources": [
  {"type": "membership", "detail": "Super Spooktacular 2009 Member Pack (bundle for members in good standing active between Oct 1 and Oct 21, 2009). The pack's contents, per the articles, were 10,000 coins, 'a Halloween flooring item' and 'a Halloween wallpaper item'. The name 'Halloween Flooring' is matched only by the housing list in article 2309, not by the pack line itself.", "where": null, "price": null, "currency": null, "source": "wiki: Super Spooktacular (2009 Member Pack section); http://www.freerealms.com/article/detail.action?articleId=2309; http://www.freerealms.com:80/article/detail.action?articleId=2306"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Halloween Flooring' is locale:8866; description locale:8867 'Cats, bats, and ghosts. Oh my! Great flooring for your Halloween themed house.'", "source": "locale:8866; locale:8867"},
  {"claim": "Article 2309 and 2306 both say the October Member Pack included 10,000 coins, a Halloween flooring item and a Halloween wallpaper item. The line is generic and does not name the item.", "source": "http://www.freerealms.com/article/detail.action?articleId=2309; http://www.freerealms.com:80/article/detail.action?articleId=2306 (fact:membership)"},
  {"claim": "Article 2309 lists Halloween Flooring and Wallpaper among the Halloween housing items added, alongside Pumpkin Patch Flooring and the Spooky furniture set. Article 2306 lists Halloween flooring and wallpaper in the same housing update.", "source": "http://www.freerealms.com/article/detail.action?articleId=2309 (fact:housing); http://www.freerealms.com:80/article/detail.action?articleId=2306 (fact:housing)"},
  {"claim": "Wiki Super Spooktacular 2009 Member Pack: members active between October 1 and October 21, 2009 were rewarded the Halloween-themed bundle. This is the dated context for the pack source. The wiki text retrieved is truncated and does not list the bundle contents.", "source": "wiki: Super Spooktacular"},
  {"claim": "Wiki page 'Halloween Flooring' is only categorized Furniture, Seasonal, Super Spooktacular. The categories give theme, not an acquisition path, so they are not used as a source.", "source": "wiki: Halloween Flooring"},
  {"claim": "No coin store price for definition 22946 in the client data. No vendor stock row found. repo stores.json has a row with item_id 8866 (purchase 270 coins, category 6), but the pack says it is a different record and it is not linked to this definition, so it is not used.", "source": "client definition pack; repo:prototype/osfr-tools/data/content/stores.json:2509 (not linked)"}
 ],
 "confidence": 0.5,
 "open": [
  "The membership link rests on the 2309/2306 housing list matching the pack's unnamed 'Halloween flooring item'. The pack line does not name this item. A second source naming Halloween Flooring in the pack contents is needed to confirm.",
  "Exact year of articles 2306 and 2309 is not verified from the pack. Context is the 2009 Super Spooktacular Member Pack (Oct 1-21, 2009) and later October 2010 and 2013 editions, which the pack says are different. Which edition included this flooring is unconfirmed.",
  "Event was removed as an acquisition source. The Super Spooktacular category is theme only. No article says this flooring was sold or awarded during the event.",
  "Possible Halloween Coin Shop return: articles 2306/2309 summaries mention 'the return of past Halloween Coin Shop items'. No stock row or price for definition 22946 was found, so no coin_shop source is listed.",
  "Repo stores.json item_id 8866 is not confirmed to be a different record for this definition, so its 270-coin price is not attributed. Verify the key mapping before using it.",
  "Retired status is unknown. No source gives a sale end date for the October pack or the housing item. live is unsure."
 ]}
