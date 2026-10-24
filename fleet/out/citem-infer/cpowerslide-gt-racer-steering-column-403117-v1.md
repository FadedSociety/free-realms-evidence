<!-- fleet job=citem-infer id=cpowerslide-gt-racer-steering-column-403117-v1 status=nothing_found turns=8 usd=0.0060 tokens(read,write,in,out)=[105809, 24985, 18, 3595] model=claude-haiku-5-5 -->
# Powerslide GT Racer Steering Column

{"item": {"name": "Powerslide GT Racer Steering Column", "locale_id": 403117, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name for locale 403117 is 'Powerslide GT Racer Steering Column' (item class 80, slot 3, definition 60817, no coin store price).", "source": "locale:403117; client definition as supplied in the pack"},
  {"claim": "Sibling client lines define the same Powerslide GT Racer kit: Engine (403115), Turbo (403116), Tires (403118), Jump Springs (403119), and a 'Powerslide GT Racer Chassis' (114818). The chassis is the vehicle base (locale:114632 'The chassis for the Powerslide GT Racer.'), and the 'Made for powersliding action' line (locale:141864) sits next to the Powerslide GT Racer name (locale:141863).", "source": "locale:403115, locale:403116, locale:403118, locale:403119, locale:114818, locale:114632, locale:141863, locale:141864"},
  {"claim": "The description 'The customized steering column for the Powerslide GT Racer.' is stored under locale 403172 (name text 'Powerslide GT Racer'), not under 403117 as the pack's client_definition states. Engine and turbo descriptions are likewise at 403170 and 403171. The pack's description field should be checked against the definition table.", "source": "locale:403172, locale:403170, locale:403171; opening-journal-text-v2/locale/en_us_data.dat"},
  {"claim": "Demo-derby kart part family: the wiki 'Items' page has a '[Derby] Kart Parts' section (Derby Elite Engine, Elite Turbo Tank, Pro Jumping Springs, ...), and the Demo Derby Driver job note says derby karts are sold in the Station Cash Marketplace. Neither source lists the Powerslide steering column in the captured text, and the page is truncated.", "source": "wiki page 'Items' (lookup result); notes/Build Guides/Content/Jobs/Demolition Derby Driver.md:197"},
  {"claim": "No vendor stock, quest reward, drop, event, wiki page, image, article fact or video frame names this steering column. Searches of repo, refs, and articles for 'Powerslide' and 'steering column' found only locale lines and the Demo Derby context.", "source": "search of repo/refs/articles/client; lookup of wiki/articles/video"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. The item needs a manual check of the Wiki 'Derby Kart Parts' / Items page (full, untruncated) and of the Station Cash Marketplace or Coin Shop listings for Powerslide GT Racer parts.",
  "The jev first-pass tag ('live: yes', 'source guess: unknown', 'demo derby vehicle part') is a hint only. The 'live' value is not confirmed by any source here, so it is left as 'unsure'.",
  "Retirement status is unknown. No source in the pack says it was retired or made unobtainable.",
  "The definition 60817 has no models in the pack and no coin store price in repo:data/content/stores.json, so no vendor price can be cited.",
  "The kit's sibling parts (Engine, Turbo, Tires, Jump Springs, Chassis) also lack sources in this pack. Resolving them together would likely settle this item's sources too."
 ]}
