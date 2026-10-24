<!-- fleet job=citem-infer id=cjeweled-blade-139925-v3 status=done turns=3 usd=0.0026 tokens(read,write,in,out)=[17074, 11560, 8, 2024] model=claude-haiku-5-5 -->
# Jeweled Blade

{"item": {"name": "Jeweled Blade", "locale_id": 139925, "kind": "weapon"},
 "sources": [
  {"type": "other", "detail": "Player-to-player trade only, class-level: Blue Text weapons are 'currently only acquired through trade'. Not confirmed for the Jeweled Blade specifically.", "where": null, "price": null, "currency": null, "source": "wiki: Blue Text weapon; wiki: Category:Blue Text Weapons"},
  {"type": "drop", "detail": "Historical, unnamed dungeon drop: the Blue Text weapon page's older wording says these weapons were 'acquired in dungeons where they were dropped'. No dungeon or enemy is named for the Blade. Not a current source.", "where": "unnamed dungeon (historical)", "price": null, "currency": null, "source": "wiki: Blue Text weapon (intro)"}
 ],
 "retired": true, "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Jeweled Blade' is locale 139925, item definition 48175, slot 7, class 6, model sword_ar_ag_weapon_twistedblade.adr, one variant", "source": "locale:139925; client definition"},
  {"claim": "Blue Text weapons are members-only weapons whose names used to show in blue font, and they have been retired", "source": "wiki: Blue Text weapon (intro)"},
  {"claim": "Blue Text weapons are 'currently only acquired through trade'", "source": "wiki: Blue Text weapon; wiki: Category:Blue Text Weapons"},
  {"claim": "Store row for item 48175 exists (category 207, 811 coins, member 729, sell 81) but binds no NPC or shop; it is a reference artifact, not a sourced vendor sale", "source": "repo:prototype/osfr-tools/data/content/stores.json:13225"},
  {"claim": "Flavour text 'This jeweled blade glitters and drips with stars...' exists as locale 382731 but is not tied to item 48175 by any client field; attribution unverified", "source": "locale:382731"}
 ],
 "confidence": 0.3,
 "open": [
  "The 811-coin store row (stores.json:13225) has no NPC, shop or vendor bound and no wiki, article or video shows it sold. It is not listed as a vendor source. Treat the price as an unconfirmed reference price only.",
  "The Blade's own row in the wiki 'Table of Blue Text weapons' was not seen in the lookup output; the previous claim that it is listed there is unverified.",
  "Trade availability for this specific blade is not confirmed; the trade route is class-level only.",
  "No dedicated wiki page, retirement date or class requirement exists for the Blade itself. The only date is the Blue Text class retirement (Dec 14, 2009), which the previous answer cited and I did not re-verify.",
  "The flavour text 'Any ninja...' ties to a ninja theme, but no source confirms the Blade's class requirement.",
  "The prior answer's 'dungeon drop' route is kept only as a historical, unnamed-dungeon note, not a current source."
 ]}
