<!-- fleet job=citem-infer id=cracing-basic-nitro-upgrade-114888-v1 status=done turns=6 usd=0.0054 tokens(read,write,in,out)=[75099, 22565, 14, 3634] model=claude-haiku-5-5 -->
# Racing Basic Nitro Upgrade

{"item": {"name": "Racing Basic Nitro Upgrade", "locale_id": 114888, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name locale 114888 'Racing Basic Nitro Upgrade', description 'Improves racing vehicles' turbo boost.' (client definitions 59640 and 59655, slots 5 and 6, class 75; no model files; no coin store price).", "source": "locale:114888; client definition pack"},
  {"claim": "It is a Kart Racing parts item (Boost tab, Slot A, Power Rating, Cannot Sell / Cannot Trade), not a clothing or pet item. Video frames show it in the kart parts window with 'You Own: 1'.", "source": "video:P2SusMJ2_tQ/00004.jpg; video:FkCPRbskFVU/00004.jpg; notes/Build Guides/Gameplay/Kart Racing.md:24"},
  {"claim": "The wiki Items page lists a '[Racing] [Basic] [Nitro] [Upgrade]' entry among race kart nitro upgrades (alongside Pro Nitro Upgrade, Advanced Anti-Missile Armor, Advanced Anti-Mine Armor).", "source": "wiki page Items (ns0), lookup result"},
  {"claim": "Related client items in the same family: Racing Advanced Nitro Upgrade (locale 114889), Pro Nitro Upgrade (locale 114893), and the per-kart custom nitro upgrades (e.g. Slicing Racer, Fiery Speedster). Client text for the family describes Advanced as 'more than the basic nitro upgrade' (locale 114721).", "source": "locale:114889; locale:114893; locale:114721; locale:117507; locale:117557"},
  {"claim": "The only kart-parts vendor found is Clack, Kart Driver Equipment vendor at the Tangletrack kart gate (Briarwood). Its stock is recorded as unresolved: no item-level stock evidence was found, so no sale of this item is attested.", "source": "repo:prototype/osfr-tools/data/content/npcs/briarwood.json:11421-11447; repo:prototype/osfr-tools/data/content/vendors_unresolved.json:263-269"},
  {"claim": "No coin store price, Station Cash listing, quest reward, drop, or event for this item was found in repo stores, vendors, quests or refs.", "source": "search of repo and refs for 'nitro' and ids 59640/59655/114888; no hits in stores or vendors"}
 ],
 "confidence": 0.3,
 "open": [
  "No acquisition source is confirmed. Clack (Kart Driver Equipment, Tangletrack gate) is the likely vendor by role, but his stock is unresolved; do not attribute this item to him without a stock capture.",
  "The Kart Racing note says the kart parts window shows the item, but it does not say how it is obtained (vendor, Kart Driver level, quest, prize wheel, or race drop). Need a wiki page, a vendor capture, or a video of a purchase.",
  "Price unknown: no coin store price in client definitions or stores.json; no wiki price found.",
  "Retired status unknown. The Items wiki page lists it, which suggests it existed in the wiki era, but no retirement note was found.",
  "Two definitions (59640 and 59655) share the same name. Not checked whether they differ by tint or by kart variant; the pack gives no per-definition detail.",
  "The first-pass tag said source_guess 'vendor'. That is a hint only and is not supported by evidence here.",
  "Kart Racing note says Cannot Sell and Cannot Trade, so no player-to-player or marketplace resale is expected."
 ]}
