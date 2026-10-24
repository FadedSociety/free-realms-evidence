<!-- fleet job=citem-infer id=cgreen-summer-sparkler-394983-v4 status=done turns=2 usd=0.0031 tokens(read,write,in,out)=[6129, 13980, 6, 2569] model=claude-haiku-5-5 -->
# Green Summer Sparkler

{"item": {"name": "Green Summer Sparkler", "locale_id": 394983, "kind": "weapon"},
 "sources": [
  {"type": "membership", "detail": "Members-only Summer Sparkler Bundle (a set of blue and green sparklers), claimable by members at login until the deadline; part of the Seaside Summer Splash event news", "where": null, "price": null, "currency": null, "source": "http://www.freerealms.com:80/article/detail.action?articleId=136"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Client name for locale 394983 is 'Green Summer Sparkler', description 'This sparkler emits vibrant green sparks', class 1, slot 7 (weapon); definitions 15918 and 57017 share the name.", "source": "locale:394983; client definition pack"},
  {"claim": "Article 136 says members could receive the exclusive Summer Sparkler Bundle, a set of blue and green sparklers, if they claimed it by the deadline, which was 11:59 PM PDT on 7/12/2009. This is the only source that names Green as a sparkler given out.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=136"},
  {"claim": "The bundle deadline 7/12/2009 is also the expiry date given for the Summer Sparkler codes on the Free Item Codes page (Red and Purple, expired July 12, 2009), which places the bundle in the same window.", "source": "wiki Free Item Codes"},
  {"claim": "Wiki pages for Blue, Golden and Red Summer Sparkler each say the item was a Weapon sold in the SC Marketplace during Summer, with a member 10% discount; Golden is also in the 2011 Summer Pass bundle (article 2153).", "source": "wiki Blue Summer Sparkler, Golden Summer Sparkler, Red Summer Sparkler; http://www.freerealms.com:80/article/detail.action?articleId=2153"},
  {"claim": "Article 2160 names Yellow, Blue and Red Summer Sparklers returned to the Marketplace; it does not name Green. Article 2171 names Golden, Blue and Red as Marketplace items removed after 10 August 2011; Green is not named.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2160; http://www.freerealms.com/article/detail.action?articleId=2171"},
  {"claim": "The lookup found no wiki page titled Green Summer Sparkler (absence in the lookup pack, not a verified wiki search).", "source": "wiki lookup, 'Summer Sparkler' query"}
 ],
 "confidence": 0.5,
 "open": [
  "Coin store row repo:prototype/osfr-tools/data/content/stores.json item 15918 (line 4053): purchase 5000 coins, member 4500, sell 500, category 12, tint group 2. It names no vendor, NPC or shop, and category 12 is the sparkler category whose siblings (e.g. 15920 Red) are sourced to the SC Marketplace via the wiki. It is not treated as a sourced vendor sale here; if it is a real coin-vendor sale, the vendor and location are still unknown.",
  "Definition 57017 (second definition, no_sale) is unexplained; it may be a tint or variant rather than a separate sale.",
  "No SC Marketplace price or wiki entry was found for Green; articles 2160 and 2171 do not name it.",
  "The Free Item Codes page excerpt shows Red and Purple sparkler codes but its visible text does not show a Green code; the full code table was not checked.",
  "Exact go-live date of the bundle is not confirmed beyond the 7/12/2009 claim deadline.",
  "First-pass tag said consumable; client slot 7 and class 1 with the wiki Weapon category point to weapon."
 ],
 "id_check": []}
