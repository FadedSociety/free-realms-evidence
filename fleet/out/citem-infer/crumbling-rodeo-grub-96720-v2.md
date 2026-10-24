<!-- fleet job=citem-infer id=crumbling-rodeo-grub-96720-v2 status=nothing_found turns=2 usd=0.0023 tokens(read,write,in,out)=[5103, 11089, 6, 1664] model=claude-haiku-5-5 -->
# Rumbling Rodeo Grub

{"item": {"name": "Rumbling Rodeo Grub", "locale_id": 96720, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition: item id 31314, class 9, slot 0, no coin store price in our store data (coin_store_prices empty).", "source": "refs:FreeRealms-Legacy/src/Resources/ClientItemDefinitions.json:639244-639266; repo search for 31314 and Rodeo finds no vendor, quest, drop, recipe or store entry"},
  {"claim": "Name text is locale 96720 'Rumbling Rodeo Grub', in a cluster with 96719 'Eight Layered Bittercake' and 96721 'Thumped Bear Meat'. The cluster is client text only; it establishes no source.", "source": "locale:96719, locale:96720, locale:96721"},
  {"claim": "The lookup tool returns only the client text line for 'Rumbling Rodeo Grub'. No wiki page, article or video frame names it.", "source": "lookup (client, wiki, articles, video) for 'Rumbling Rodeo Grub'"},
  {"claim": "Number collision check: locale 31314 is 'New Years Eve in Snowhill', and refs:Lxzxrus-Free-Realms-Server ClientActivityDefinitions.json line 3490 has NameId 31314. This is a shared number in a different id space, not a source for this item.", "source": "locale:31314; refs:Lxzxrus-Free-Realms-Server/src/Resources/ClientActivityDefinitions.json:3490"},
  {"claim": "The description text (locale 97436) was flagged as a dev note with stray punctuation, so the talent-buff wording is not used as evidence here.", "source": "id_check flag on locale:97436"}
 ],
 "confidence": 0.15,
 "open": [
  "No acquisition source found. The first-pass 'event' guess has no evidence behind it. Do not assign a source until one is found.",
  "Client definition fields (id 31314, class 9, Cost 300, NoTrade/NoSale, ActivatableAbilityId 484) are from the Legacy server's client dump and are unverified for this build. Ability 484 was not checked.",
  "Live status is unverified. NoSale and NoTrade mean no store sale in the client data. The Bittercake sibling's store bundle (marketing id 31313, Price 1, CurrencyType 1) is a different id and was not used to infer this item's price or currency.",
  "ClientActivityDefinitions NameId 31314 (Lxzxrus-Free-Realms-Server line 3490) and locale 31314 (New Years Eve in Snowhill) share the number with this item. The link is unverified and may be a different id space.",
  "Next step: check the Legacy server's event, promotion and reward tables for item 31314 or ability 484, and check whether the sibling items 31313 and 31315 have any source that would also apply here."
 ]}
