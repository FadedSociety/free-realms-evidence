<!-- fleet job=citem-infer id=ctrauma-support-shockrod-102196-v1 status=done turns=2 usd=0.0023 tokens(read,write,in,out)=[4149, 10046, 6, 1972] model=claude-haiku-5-5 -->
# Trauma Support Shockrod

{"item": {"name": "Trauma Support Shockrod", "locale_id": 102196, "kind": "weapon"},
 "sources": [
  {"type": "crafting", "detail": "Blacksmith recipe 'Trauma Support Shockrod' (recipe item 'Trauma Support Shockrod Recipe', locale 1583; teaches creation per locale 1605)", "where": "Blacksmith (Medic-era crafting job)", "price": null, "currency": null, "source": "https://wiki (page: Trauma Support Shockrod); wiki page: Blacksmith; locale:1583; locale:1605"},
  {"type": "other", "detail": "Ayani's Pride Hospital crafting quest 'Forging: Trauma Support Shockrod': the hospital asks for batches of Trauma Support Shockrods to be crafted and given to Steelbloom for a reward. Shows the weapon is also a quest-crafting input; the reward amount is not in the pack.", "where": "Ayani's Pride Hospital", "price": null, "currency": null, "source": "locale:386103 (quest title); locale:387905 (quest dialog 'full batch... appropriate payment'); repo search of client en_us_data.dat strings 804728937 and 710678765"}
 ],
 "retired": null,
 "live": "yes",
 "evidence": [
  {"claim": "Trauma Support Shockrod is a level 16 Medic weapon (Power 5, Green Text weapon), obtainable from the Blacksmith recipe.", "source": "wiki page: Trauma Support Shockrod"},
  {"claim": "Blacksmith wiki page lists Trauma Support Shockrod among its recipe weapons.", "source": "wiki page: Blacksmith"},
  {"claim": "Client has a recipe item and its description: 'This recipe teaches you how to create a Trauma Support Shockrod.'", "source": "locale:1583; locale:1605"},
  {"claim": "Client quest 'Forging: Trauma Support Shockrod' and dialog about a full batch of Trauma Support Shockrods for payment, tied to Ayani's Pride Hospital.", "source": "locale:386103; locale:387905; en_us_data.dat strings 804728937, 814503095"},
  {"claim": "Wiki item tooltip image shows Resell Value 191 (a resell value, not a sale price; not used as a price).", "source": "image:item_tooltip, Trauma Support Shockrod item.png"},
  {"claim": "Client definition: 10 variants (definition_ids 30510-30519), slot 7, class 20, model club_ar_ag_weapon_shockrod.adr; no coin store price in stores data.", "source": "client definition; repo:data/content/stores.json has no entry"}
 ],
 "confidence": 0.7,
 "open": [
  "Blacksmith page carries a 'Members Only' category; whether the recipe requires membership is not confirmed by a source here.",
  "Reward amount and item for the Ayani's Pride Hospital batch quest (Steelbloom) not found in the pack; add as quest_reward once the reward data is read from quest files.",
  "Wiki gives no price for the recipe or the weapon; no coin vendor or Station Cash listing found, so no price is stated.",
  "Retired status not stated by any source; the wiki page presents it as currently acquirable, but no date was checked.",
  "Blacksmith recipe cost (materials) not gathered from recipe data in the repo; not in the pack."
 ]}
