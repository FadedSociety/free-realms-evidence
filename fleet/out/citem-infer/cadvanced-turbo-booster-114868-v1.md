<!-- fleet job=citem-infer id=cadvanced-turbo-booster-114868-v1 status=done turns=7 usd=0.0045 tokens(read,write,in,out)=[59174, 17388, 16, 3373] model=claude-haiku-5-5 -->
# Advanced Turbo Booster

{"item": {"name": "Advanced Turbo Booster", "locale_id": 114868, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Client item 'Advanced Turbo Booster' (locale 114868, definition 59620, slot 2, class 75) with description 'An upgraded racing turbo booster that has more boost capacity than the basic turbo booster.' It has no model files and no coin store price.", "source": "locale:114868; client definition in pack"},
  {"claim": "It is one of a five-step kart turbo chain (Stock Turbo Booster 114866, Basic 114867, Advanced 114868, Pro 114869, Elite 114870), next to Stock/Basic Turbo Tank (114872/114873). A sibling racing-booster line says 'more boost capacity than the advanced turbo booster' (locale 114683), so Advanced sits below Pro and Elite.", "source": "locale:114866-114873; locale:114683"},
  {"claim": "It appears in the kart racing parts window (Boost tab, Power Rating 10, 'You Own: 1') next to Tight Turning and Basic Turbo Booster, in a race-lobby 'Click Here to Switch Karts' frame. The window is a parts display, not an acquisition source.", "source": "video:P2SusMJ2_tQ/00002.jpg"},
  {"claim": "Kart parts in the Kart Racing parts window are marked Cannot Sell and Cannot Trade in the tooltip.", "source": "notes/Build Guides/Gameplay/Kart Racing.md:24"},
  {"claim": "Clack is listed as the 'Kart Driver Equipment vendor' at Briarwood/Tangletrack, but no stock list was recovered for him. The repo marks his stock unresolved, with no item IDs.", "source": "prototype/osfr-tools/data/content/npcs/briarwood.json:11421-11440; prototype/osfr-tools/data/content/vendors_unresolved.json:265-269"},
  {"claim": "The parallel Derby generic-part chain (Derby Basic/Advanced/Pro/Elite Engine, Turbo Tank) has the same tier wording, but its sources are also unknown.", "source": "notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:203-208"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source is evidenced. The first-pass 'vendor' guess is not supported: Clack's stock is unresolved in the repo, and no stock list, price, or coin store entry (stores.json) names item 59620 or locale 114868.",
  "Whether Clack (Kart Driver Equipment vendor, Briarwood/Tangletrack) sells the Advanced Turbo Booster, and at what price and currency, needs a native vendor capture or a wiki/forum price.",
  "Whether it is a Station Cash Marketplace, Coin Shop, quest reward, or Kart Driver level-gated reward is unknown. The Kart Racing note says Kart Driver levels unlock items, but the unlock levels are not recovered.",
  "Retired status is unknown. No wiki page or article covers this part.",
  "Video frame is a parts-window view of an owned item only; it does not show where it was bought.",
  "Only one video frame covers this item. Wider review of kart-racing frames might show a vendor or price."
 ]}
