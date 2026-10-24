<!-- fleet job=citem-infer id=cmedium-spineless-stickleback-407637-v4 status=done turns=2 usd=0.0024 tokens(read,write,in,out)=[6931, 9008, 6, 2378] model=claude-haiku-5-5 -->
# Medium Spineless Stickleback

{"item": {"name": "Medium Spineless Stickleback", "locale_id": 407637, "kind": "other"},
 "sources": [
  {"type": "other", "detail": "Fishing catch of the species Spineless Stickleback (base name locale:99947), reeled in with a rod. Only the species is evidenced as catchable. The Medium size grade as a catch outcome is NOT evidenced by any source; it is an unverified inference from the client's size-grade names.", "where": "Snowhill: Wintery Basin and Frostbitten Banks (fishing areas)", "price": null, "currency": null, "source": "wiki page 'Wintery Basin' (Types of Fish: '[Spineless] [Stickleback] - Catchable at level 10'); wiki page 'Frostbitten Banks' (same entry, Catchable at level 10); locale:410081 ('Spineless Stickleback can be caught in the Wintery Basin.'); locale:410546 and locale:410545 (area lists naming spineless stickleback)"}
 ],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item locale:407637 is 'Medium Spineless Stickleback'; siblings are Small (locale:407636) and Large (locale:407638); base species name is locale:99947 'Spineless Stickleback'.", "source": "locale:407637; locale:407636; locale:407638; locale:99947"},
  {"claim": "Spineless Stickleback is listed as catchable at level 10 in Wintery Basin and in Frostbitten Banks, with no retirement note.", "source": "wiki page 'Wintery Basin'; wiki page 'Frostbitten Banks'"},
  {"claim": "Client area text confirms the species is catchable in Wintery Basin.", "source": "locale:410081"},
  {"claim": "The Tiny Rib lure gives a 10% better chance of catching Spineless Stickleback. This is species-wide, not grade-specific, so it applies to any grade including Medium.", "source": "wiki page 'Fisherman' (Tiny Rib text); locale:412943; locale:409564; locale:29780"},
  {"claim": "Quest objective locale:410080 'Reel in a large Spineless Stickleback' (Wintery Basin) points at the Large grade (locale:407638), not Medium. Quest objective locale:412258 'Take the Spineless Stickleback to Helena.' does not name a grade.", "source": "locale:410080; locale:412258; locale:407638"},
  {"claim": "No coin store price exists for this item.", "source": "client definition: coin_store_prices empty"}
 ],
 "confidence": 0.35,
 "open": [
  "The Medium grade as a catch outcome is unevidenced. No source names the Medium grade. The fishing.json size_weights (27/35/27/11) mapping to grades is unverified and the Medium weight range is unknown. Not wireable as a Medium-specific source.",
  "repo fishing.json record (key spineless_stickleback, minimum_level 10, size_weights) has name_id 3504078607, which does not match client locale 99947. The level-10 figure therefore rests on the wiki area lists, not on the repo record.",
  "Extra Large grade is not claimed; locale:407642 belongs to Flutterfish.",
  "No vendor, Station Cash, Coin Shop, prize wheel, quest reward or event source for the Medium grade was found; no price is known.",
  "Live status: the species is shown as catchable on wiki area lists with no retirement note and no date. The Medium grade itself is unconfirmed, hence 'unsure'.",
  "Client description is empty; no use beyond being a catch is recorded.",
  "Corrections applied: the invalid citation locale:69065426 is removed everywhere. locale:412262 was not found in lookup output and is also dropped; the quest citations used are locale:412258 and locale:410080 only. The Tiny Rib lure text is cited as locale:412943 (Tiny Rib - Lure) and wiki 'Fisherman', stated as species-wide."
 ],
 "critiques_addressed": "world 1-4 and evidence 1-4 handled: Medium grade catch claim removed/flagged as unverified; wireable set to false; Tiny Rib bonus stated as species-wide; name_id mismatch disclosed; id-check error removed; Large-grade quest objective noted."
}
