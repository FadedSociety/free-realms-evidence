<!-- fleet job=citem-infer id=clarge-spineless-stickleback-407638-v5 status=done turns=2 usd=0.0026 tokens(read,write,in,out)=[6877, 10497, 6, 2486] model=claude-haiku-5-5 -->
# Large Spineless Stickleback

{"item": {"name": "Large Spineless Stickleback", "locale_id": 407638, "kind": "collection"},
 "sources": [
  {"type": "other", "detail": "Fisherman quest 'To the Rescue!' (repo quest 39, Fisherman.md line 139): Helena asks the player to reel in a large Spineless Stickleback and bring it to her as live bait to lure the creature that swallowed Ernest. This is a catch requirement, not a reward or purchase. Whether the fish is consumed is not stated in the cited text.", "where": "Wintery Basin", "price": null, "currency": null, "source": "locale:412251 ('a large Spineless Stickleback'); locale:410080 ('Reel in a large Spineless Stickleback'); locale:412258 ('Take the Spineless Stickleback to Helena.'); repo:notes/Build Guides/Content/Jobs/Fisherman.md line 139"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item 'Large Spineless Stickleback' is locale 407638; sibling size names are Small 407636 and Medium 407637; base fish is 'Spineless Stickleback' locale 99947.", "source": "locale:407638; locale:407636; locale:407637; locale:99947"},
  {"claim": "Quest text asks the player to reel in a large Spineless Stickleback and take it to Helena as bait for the creature that swallowed Ernest.", "source": "locale:412251; locale:410080; locale:412258; repo:notes/Build Guides/Content/Jobs/Fisherman.md line 139"},
  {"claim": "The only fish documented as catchable at level 10 is the base Spineless Stickleback, in Wintery Basin and Frostbitten Banks. No source names a level-10 Large catch.", "source": "wiki Wintery Basin ('[Spineless] [Stickleback] - Catchable at level 10'); wiki Frostbitten Banks; locale:410081; repo:notes/Build Guides/Gameplay/Fishing.md lines 132-133"},
  {"claim": "Wiki 'Extra [Large] Catch of the Day' and '[Large] Catch of the Day' are catch-bonus headings, not a separate Large Spineless Stickleback item; they do not establish this item as a catch.", "source": "wiki Wintery Basin; wiki Frostbitten Banks"},
  {"claim": "Tiny Rib lure gives a 10% better chance of catching Spineless Stickleback, Calico Catfish and Purplenosed Shark.", "source": "locale:412943; locale:409564; wiki Fisherman (Tiny Rib entry)"},
  {"claim": "No coin store price: client coin_store_prices is empty and no stores.json entry matches id 68040 or 407638. No vendor, Station Cash, Coin Shop, prize wheel or enemy drop source found.", "source": "client definition; repo:data/content/stores.json"}
 ],
 "confidence": 0.3,
 "open": [
  "Large-size catch is unconfirmed. Only the base fish (locale 99947) is documented as catchable at level 10. The quest asks for a large one, but no source says the client's Large item drops or can be caught in the open world. Whether the quest source is the only way to get it is unknown.",
  "Quest-consumed status unverified: the cited text does not say the fish is taken or consumed.",
  "Quest name conflict: repo Fisherman.md line 139 names quest 39 'Fisherman: To the Rescue!', while the earlier pack tagged locale 412258 as 'Fisherman: Live Bait!'. The tag was not re-checked here. The quest-39 reward (Ernest's thanks, treasure-map half) is unverified and is not attributed to this fish.",
  "Retirement unknown; no end-of-life text found either way.",
  "Live is 'unsure': fishing data and spot tables do not prove the Large item is live today.",
  "No price or sale source: fish are caught, not bought; no coin vendor, Station Cash, or Coin Shop listing found.",
  "Removed the nonexistent id locale:978952005 from the earlier open note; no replacement id is cited for it."
 ]
}
