<!-- fleet job=citem-infer id=ccelebrity-10394-v1 status=nothing_found turns=2 usd=0.0016 tokens(read,write,in,out)=[3957, 6377, 6, 1524] model=claude-haiku-5-5 -->
# Celebrity

{"item": {"name": "Celebrity", "locale_id": 10394, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "'Celebrity' (locale 10394) is the name of VIP rank 4 title, not a purchasable item. The wiki VIP page lists 'Rank 4 VIP / Title: [Celebrity]'.", "source": "wiki page: VIP (ns0), 'Costumes' section"},
  {"claim": "The sibling strings 10391-10395 (V. I. P., Trendsetter, Kind of a Big Deal, Celebrity, Superstar) are the five VIP rank titles, ranks 1-5, so 10394 belongs to that set.", "source": "locale:10391, locale:10392, locale:10393, locale:10394, locale:10395; wiki page: Titles ('VIP titles')"},
  {"claim": "locale:31735 is 'Title: Celebrity', consistent with a title label rather than an item name.", "source": "locale:31735"},
  {"claim": "The wiki shows '[Celebrity]' as a name prefix on player characters in screenshots (e.g. [Celebrity] Grayson Stonyhammer, [Celebrity] Cori Goldensea), so the title is a player-name tag earned by VIP rank.", "source": "image:world_screenshot 'Cori Goldenseas life story.png'; image:world_screenshot '281183 414202191986202 1061733191 o.jpg'"},
  {"claim": "The other 'Celebrity' hits are unrelated: the Kart Driver 'Celebrity Giveaway' quest/minigame (locale:3830, 395809, 395332) and Sanctuary NPC 'celebrity' card-deck characters Nirvi and Poe Tatters (article 168). None names an item called Celebrity.", "source": "locale:3830; locale:395809; locale:395332; http://www.freerealms.com:80/article/detail.action?articleId=168"},
  {"claim": "The client definition has no models, no coin store price, slot 0 and class 0, which fits a non-wearable title entry.", "source": "client definition 77742 (as supplied in the pack)"}
 ],
 "confidence": 0.8,
 "open": [
  "Not an item: this is a VIP rank title. It should probably be excluded from the item sources table and handled as a title/rank entry in the rebuild.",
  "Whether the VIP title system is live in the rebuild is unknown; no source in the pack gives its status.",
  "The first-pass tag (kind 'other', source 'unknown') is consistent with this finding. The Kart Driver 'Celebrity Giveaway' is a separate minigame and does not award an item named Celebrity; no source was found for that."
 ]}
