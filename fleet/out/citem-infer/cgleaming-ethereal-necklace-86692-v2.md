<!-- fleet job=citem-infer id=cgleaming-ethereal-necklace-86692-v2 status=nothing_found turns=2 usd=0.0017 tokens(read,write,in,out)=[5318, 7342, 6, 1359] model=claude-haiku-5-5 -->
# Gleaming Ethereal Necklace

{"item": {"name": "Gleaming Ethereal Necklace", "locale_id": 86692, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 22701: equip slot 8, item class 50, one variant, no model files, no coin store price. Description text: 'A necklace made of many different green stones that increase Defense for any Combat Job.' (taken from the client definition's description field, not from a locale line; locale:86692 is the name only).", "source": "client pack definition 22701"},
  {"claim": "Name text is locale:86692 'Gleaming Ethereal Necklace'. locale:150434 is a FLAGGED placeholder stub ('This is a Gleaming Ethereal Necklace item.') and is not used as evidence for the description or for liveness.", "source": "locale:86692; locale:150434 (placeholder)"},
  {"claim": "The item belongs to a family of Gleaming necklaces (locale:86684-86696) and rings (locale:86449-86461), plus 'Gleaming Light' (locale:40929). Other Gleaming rings exist for Ocean, Jungle and Grape (locale:96096-96098). None of these family members is named by any wiki page, article, video frame, vendor, quest, drop or recipe found.", "source": "locale:86449-86461; locale:86684-86696; locale:40929; locale:96096-96098"},
  {"claim": "Repo search for 'Gleaming|22701|86692' returned no store, vendor, quest, recipe or drop entry for this item (only unrelated hits such as coordinates and NPC notes). Wiki, article and video lookups for 'Gleaming Necklace' returned only client text entries for the family, no source page.", "source": "repo search; lookup (wiki/articles/video) 'Gleaming Necklace'"}
 ],
 "confidence": 0.1,
 "open": [
  "No source found: no coin vendor, Station Cash listing, Coin Shop entry, quest reward, drop, event, prize wheel, crafting or collection record names this necklace. The first-pass 'drop' guess is unsupported and not used.",
  "Live status unverified. The first-pass 'live: yes' is a model hint only; live is 'unsure' and retired is null.",
  "The Gleaming family (rings and necklaces) may share one source, but that is unverified. Check enemy drop tables, event data and the Gleaming Light ability for a link.",
  "Defense stat claim comes from the client description only; no in-game value was checked.",
  "A direct wiki category check (SC Marketplace, Coin Shop, Prize Wheel, Retired, holiday) was not possible from the tools available; search returned none."
 ]}
