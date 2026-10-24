<!-- fleet job=citem-infer id=cstorm-charmed-skirt-124821-v1 status=done turns=7 usd=0.0036 tokens(read,write,in,out)=[58910, 13576, 16, 2696] model=claude-haiku-5-5 -->
# Storm Charmed Skirt

{"item": {"name": "Storm Charmed Skirt", "locale_id": 124821, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name text is 'Storm Charmed Skirt' (locale 124821); it sits in a set with Storm Charmed Medium Cloak (124817), Shoes (124818), Fez (124820) and Slacks (124822).", "source": "locale:124821; locale:124817; locale:124818; locale:124820; locale:124822"},
  {"claim": "Sibling item Storm Charmed Wand has a wiki page: a level 8 Wizard weapon, Green Text, 'can only be acquired through trade'. This is a sibling, not proof for the skirt.", "source": "wiki page 'Storm Charmed Wand'; wiki page 'Green Text weapon' lists [Storm] [Charmed] Wand"},
  {"claim": "The pack says the coin store price is 618. stores.json has several rows at 618 coins (member price 556, sell 61), but the rows are item_ids 10600-10602 and 10680-10682 (category 106). None of them is in the skirt's definition ids (44822-44888), so the row cannot be tied to this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json:3093-3107"},
  {"claim": "Client definition: slot 4, item class 8, model caster_<race>_f_legs_skirt.adr, 16 definitions in 12 listed ids.", "source": "client definition in the evidence pack"}
 ],
 "confidence": 0.2,
 "open": [
  "No vendor source is confirmed. The 618-coin price in the pack does not match any store row for this item's definition ids (44822-44888). The store rows at 618 belong to item_ids 10600-10602 and 10680-10682, which are unrelated, so the vendor claim is unproven. Someone needs to check how client definition ids map to stores.json item_id before the vendor source can be kept.",
  "No wiki page, article, image, or video names the Storm Charmed Skirt. No vendor stock or quest/drop/event answer mentions it.",
  "The sibling Storm Charmed Wand is documented as trade-only (Green Text). The skirt may be a Green Text trade item too, which would make the vendor guess wrong. This is unverified.",
  "Retired and live status cannot be settled from the evidence. The first-pass 'live: yes' is only a hint.",
  "Sources list is empty because no source has evidence that meets the rules. Do not add a coin_shop or vendor source without a store row for definition id 44822-44888."
 ]}
