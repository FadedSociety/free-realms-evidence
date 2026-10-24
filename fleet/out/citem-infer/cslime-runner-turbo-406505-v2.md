<!-- fleet job=citem-infer id=cslime-runner-turbo-406505-v2 status=done turns=3 usd=0.0025 tokens(read,write,in,out)=[15166, 10443, 8, 2178] model=claude-haiku-5-5 -->
# Slime Runner Turbo

{"item": {"name": "Slime Runner Turbo", "locale_id": 406505, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Slime Runner Turbo' is locale 406505; its description is locale 406565 'The turbo for the Slime Runner.' It is a race-kart part for the Slime Runner vehicle, not a pet. The first-pass 'pet' tag is wrong.", "source": "locale:406505; locale:406565"},
  {"claim": "The wiki Items page lists the race-kart vehicle 'Slime [Runner]' under Race Karts; it does not list a Slime Runner Turbo entry or any turbo sale.", "source": "wiki page Items (lookup result)"},
  {"claim": "The wiki SC Marketplace wikitext lists 'Slime Runner - {{SC|495}}' and 'Arrow Runner - {{SC|630}}'. These are vehicle prices only. The 'Elite Turbo Tank' and 'Elite Turbo Booster' (derby parts, SC 270) are the only turbo entries in that list; no Slime Runner Turbo price appears.", "source": "freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki lines 470, 472, 477, 495"},
  {"claim": "No repo row, vendor stock, quest, recipe or client store price links to definition 61035 or locale 406505.", "source": "repo search for 61035 and 406505 (no hits); client definition coin_store_prices []"},
  {"claim": "Correction to prior answer: the SC 399 figure for Arrow Runner was not found in any source and is dropped. The only verified Arrow Runner price is SC 630 (wikitext line 470).", "source": "freerealms-wiki/wikitext/2242-43382-0a935accf24e.wiki line 470"}
 ],
 "confidence": 0.2,
 "open": [
  "No source for how the Slime Runner Turbo is obtained: no store, vendor, quest, drop, event, crafting or collection evidence was found. Sources stay empty rather than guessed.",
  "The Slime Runner vehicle is SC 495 on the wiki SC list, but the turbo is not in that list; it may be bundled with the vehicle or sold separately. Needs a wiki page or live check.",
  "Item class conflict: the client pack says class_ids [125]; the research note 041 maps Racing Kart parts to ItemClasses row 75 (Type 9). Unverified. The 'Turbo category 130' figure from that note is not confirmed elsewhere.",
  "The FreeRealms-Legacy StoreBundles row (NameId 7163, GameItemId 1910, MarketingItemId 61003) was not re-checked and describes the vehicle, not the turbo; it is not cited as evidence.",
  "Live status and retirement are unknown; no source states whether the part was ever released or retired.",
  "Sibling race-kart turbos (Arrow, Speedy, Elliptical, Basphomie Runner Turbo) have no verified sources in this pack either; they may share a common acquisition path that could be confirmed from a wiki page for the Race Karts category."
 ]}
