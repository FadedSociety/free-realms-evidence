<!-- fleet job=citem-infer id=ceasy-bake-cauldron-16637-v2 status=done turns=2 usd=0.0017 tokens(read,write,in,out)=[5377, 6957, 6, 1590] model=claude-haiku-5-5 -->
# Easy Bake Cauldron

{"item": {"name": "Easy Bake Cauldron", "locale_id": 16637, "kind": "furniture"},
 "sources": [{"type": "event", "detail": "Halloween event: listed as a Halloween activate-able housing item in the official article. The article does not state how it was acquired (sale, prize, or reward), so the acquisition route is unknown.", "where": null, "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"}],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "The official Halloween article (articleId 2304) lists Easy Bake Cauldron among the Halloween activate-able housing items, with Jack-O-Lantern and Haunted Headstone. It does not say how the item was obtained.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2304"},
  {"claim": "Client item name is 'Easy Bake Cauldron' (locale 16637). Its description (locale 16650) says to place the cauldron on the ground and click it to receive a spooky treat.", "source": "locale:16637"},
  {"claim": "Client definition 69842 has no coin store price, and no repo stores or vendor data mentions it, so there is no coin vendor sale evidence.", "source": "repo search (data/content, no hits for 69842 or Easy Bake outside unrelated files)"},
  {"claim": "The wiki has no page for this item, and lookup shows no wiki, forum, or article fact beyond the Halloween housing listing.", "source": "lookup wiki/articles/client"},
  {"claim": "Video frames kDK28IIUpoc/00004.jpg and C3fysVLxrMg/00454.jpg show the item name on screen (a placed object with a 'Press X or' prompt; near the Bud Grimyfoot cooking table and Active Quest text). They show use and placement only, not an acquisition route.", "source": "video:kDK28IIUpoc/00004.jpg; video:C3fysVLxrMg/00454.jpg"}
 ],
 "confidence": 0.3,
 "open": [
  "Acquisition route is unknown. The article lists the item only as a Halloween activate-able housing item. No source says whether it was sold (coin vendor, Station Cash, Coin Shop), given as a Halloween reward, or dropped. The earlier 'sold or given' wording was a guess and has been removed.",
  "No price in client definition, repo stores, or wiki.",
  "Retirement and current availability are not stated by any source. Live status is unsure; the first-pass 'live: yes' is not confirmed.",
  "Wireable: false. The only source has no price, named event, or reward, so it cannot be wired until a Halloween vendor, prize, or reward is evidenced.",
  "The Bud Grimyfoot frame shows the name near a cooking table and Active Quest text. It is not evidence of a quest reward or placement source."
 ]}
