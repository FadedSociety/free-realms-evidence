<!-- fleet job=citem-infer id=cgreen-speed-racer-nitro-upgrade-403109-v1 status=nothing_found turns=4 usd=0.0031 tokens(read,write,in,out)=[24246, 14248, 10, 2164] model=claude-haiku-5-5 -->
# Green Speed Racer Nitro Upgrade

{"item": {"name": "Green Speed Racer Nitro Upgrade", "locale_id": 403109, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines the item: name locale:403109, description 'The customized mod for the Green Speed Racer.', one definition (id 60809), slot 5, item class 78, no coin store price.", "source": "client definition in evidence pack"},
  {"claim": "It is one part of a kart-part set: Green Speed Racer Engine (locale:403105, 'The customized engine for the Green Speed Racer.'), Turbo (403106), Steering Column (403107), Tires (403108), Nitro Upgrade (403109), with a parallel Turbo Racer set (403110-403114) and a Volt Racer set (403100-403104).", "source": "locale:403105-403109; locale:403100-403114"},
  {"claim": "The 'Green Speed Racer' base vehicle and its chassis are separate client items (locale:141858 'Green Speed Racer', locale:114816 'Green Speed Racer Chassis', locale:114630 'The chassis for the Green Speed Racer.').", "source": "locale:141858, locale:114816, locale:114630"},
  {"claim": "The wiki Items page lists race kart parts such as Racing Elite Engine, Elite Turbo Booster and Pro [Nitro] [Upgrade], but does not list any Green Speed Racer or Turbo Racer part.", "source": "wiki page Items (ns0)"},
  {"claim": "No vendor stock, coin store price, quest reward, drop, event, or other answer names this item. Repo searches for 'Green Speed', 'Racer' parts and 'Nitro Upgrade' in data files found no store or vendor entry.", "source": "repo search; refs search"}
 ],
 "confidence": 0.2,
 "open": [
  "No acquisition source found. Probable context is the Kart Driver / Kart Racing system (kart parts), but no page, vendor, quest, or prize link ties this part to a source. Do not assign a source without evidence.",
  "Kind is 'other' (kart vehicle part, slot 5, class 78). Confirm the class meaning against the client item-class table.",
  "Live status is unknown: the cheap first pass said 'live: yes', but no source evidence supports that. Retired status is also unknown.",
  "Check the Kart Racing build guide and any Green Speed Racer or Turbo Racer vehicle/unlock records for the vehicle's sale or reward route, then check whether the nitro part is sold with the vehicle or as a separate reward.",
  "Variant count is 1 (definition 60809). No tints or races are shared under this name."
 ]}
