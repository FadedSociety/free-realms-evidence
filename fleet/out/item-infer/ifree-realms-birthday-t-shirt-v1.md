<!-- fleet job=item-infer id=ifree-realms-birthday-t-shirt-v1 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[12418, 11190, 8, 1925] model=claude-haiku-5-5 -->
# Free Realms Birthday T-Shirt

{"item": {"name": "Free Realms Birthday T-Shirt", "locale_id": 5721, "kind": "clothing"},
 "sources": [
  {"type": "event", "detail": "Birthday Bash (annual game anniversary celebration); the shirt is a Freestyle Jobs clothing item acquired during the event. Exact mechanism (which chest, which NPC or minigame) not stated", "where": null, "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Free_Realms_Birthday_T-Shirt (rev 45348); wiki category Birthday Bash"},
  {"type": "event", "detail": "Anniversary gift reward: party t-shirts, one per party zone; this is the base/Free Realms version", "where": null, "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=2107"}
 ],
 "retired": null, "live": "unsure",
 "evidence": [
  {"claim": "Item is a Freestyle Jobs clothing item acquired during the Birthday Bash event", "source": "https://freerealms.fandom.com/wiki/Free_Realms_Birthday_T-Shirt"},
  {"claim": "Wiki categories: Clothing, Chest, Birthday Bash, Seasonal (no coin, Station Cash, or Coin Shop price listed)", "source": "https://freerealms.fandom.com/wiki/Free_Realms_Birthday_T-Shirt"},
  {"claim": "Client name string for the base shirt is locale 5721; zone variants are 5723 (Wugachug), 19956-19962 (other zones)", "source": "locale:5721"},
  {"claim": "Party t-shirts are anniversary gift rewards, one per party zone", "source": "http://www.freerealms.com/article/detail.action?articleId=2107"},
  {"claim": "Birthday Bash listed as the rewards source for minigame clothing, including this shirt", "source": "another answer in pack: event 'Free Realms Birthday Bash (game anniversary celebration)' (open), citing wiki: Birthday Bash (Rewards: minigame clothing)"},
  {"claim": "Zone-specific Birthday T-Shirts share the same wiki wording and categories", "source": "wiki pages Wugachug, Sanctuary, Snowhill, Blackspore Swamp, Merry Vale, Shrouded Glade, Briarwood, Seaside Birthday T-Shirt"}
 ],
 "confidence": 0.4,
 "open": ["No price or currency in any source: no coin vendor stock, no Station Cash or Coin Shop listing found.",
  "Acquisition mechanism is unclear: the 'Chest' category suggests a chest reward, but no chest name, drop table, or quest reward was found in the pack or repo.",
  "No vendor_stock, drop, or quest_reward evidence in the pack; the event source is supported only by the wiki wording and the anniversary article.",
  "Retired status and whether the shirt can still be obtained after the Birthday Bash ends are not stated; live status is unsure.",
  "The wiki page is a stub with no description text beyond the event line."]}
