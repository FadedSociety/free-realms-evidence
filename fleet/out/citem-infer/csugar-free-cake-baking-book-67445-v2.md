<!-- fleet job=citem-infer id=csugar-free-cake-baking-book-67445-v2 status=done turns=3 usd=0.0022 tokens(read,write,in,out)=[14193, 8382, 8, 2010] model=claude-haiku-5-5 -->
# Sugar Free Cake Baking Book

{"item": {"name": "Sugar Free Cake Baking Book", "locale_id": 67445, "kind": "collection"},
 "sources": [
  {"type": "collection", "detail": "Entry (1 of 8) in the Chef's Cake Baking Books cascading collection; completing the set rewards the Party Sized Platter (locale 67448). Membership only: no acquisition method for the individual book is sourced.", "where": "Chef job collections (Job Specific (Collections))", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Job_Specific_(Collections) (rev 27853, 2013-07-13); repo:prototype/osfr-tools/data/content/collections.json:3163-3243 (key wiki:2:45, entry at line 3200)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Item name is locale:67445 'Sugar Free Cake Baking Book', in the Chef cake book/platter cluster (locale 67440-67450).", "source": "locale:67445"},
  {"claim": "Client definition (definition 23832) has no model, no coin store price, and one variant; description says it can be added to the Chef's Cake Baking Books Collection.", "source": "client definition"},
  {"claim": "Wiki Job Specific (Collections) lists Sugar Free Cake Baking Book among the 8 Chef cake book entries.", "source": "https://freerealms.fandom.com/wiki/Job_Specific_(Collections)"},
  {"claim": "Repo collection record wiki:2:45 lists the same 8 entries, reward Party Sized Platter, quality Common, spawn_type 'Job Material' (a collection-level tag, not this book's acquisition).", "source": "repo:prototype/osfr-tools/data/content/collections.json:3163-3243"},
  {"claim": "Video frame shows the book inside the Chef's Cake Baking Books collection window.", "source": "video:0IaICGnTWWQ/00098"}
 ],
 "confidence": 0.3,
 "open": [
  "Wireable: false. No price, vendor, quest, drop, event or crafting source exists for the individual book in any cited source; the only source is collection membership.",
  "Live status: the earlier pack cited repo quest-lines/flags.tsv:7353 ('placeholder: novelty diet book, verify live'). That flag could not be found in the repo (search for 67445 and 'novelty diet' returned no match), so it is unverified. Live is set to 'unsure' until the flag is checked.",
  "Retirement is not stated by any source.",
  "No coin vendor stocks the book: no store price in the client definition and no vendor_stock entry.",
  "The Chef.md:333 citation in the earlier pack was not verified and is dropped. The '20 coins per reward' note concerns the collection tiles, not this book, and is dropped.",
  "How a player obtains the individual book (the 'Job Material' spawn type suggests Chef job gathering or drops) is unsourced."
 ]
}
