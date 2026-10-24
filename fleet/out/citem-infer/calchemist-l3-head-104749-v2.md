<!-- fleet job=citem-infer id=calchemist-l3-head-104749-v2 status=nothing_found turns=2 usd=0.0015 tokens(read,write,in,out)=[5167, 6216, 6, 1336] model=claude-haiku-5-5 -->
# Alchemist L3 Head

{"item": {"name": "Alchemist L3 Head", "locale_id": 104749, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client text defines 'Alchemist L3 Head' as an item at locale:104749 (lookup returns only the client row, no wiki, article or video hit).", "source": "locale:104749"},
  {"claim": "Same-named tier series exists in client text: Alchemist L1 Head = locale:104994, L2 Head = locale:105029, L4 Head = locale:104784, L1 Chest = locale:104644, L2 Chest = locale:104609, L3 Chest = locale:104539, L4 Chest = locale:104469, L5 Chest = locale:104399; 'Alchemist Gear' = locale:8, 'Alchemist Tools' = locale:9. These are context only; none names a source.", "source": "locale:8; locale:9; locale:104399; locale:104469; locale:104539; locale:104609; locale:104644; locale:104784; locale:104994; locale:105029"},
  {"claim": "Alchemist storyline dialog (Potion of Truth for the Dwarven Captive, Alchemist Bubbles, Alchemist's Cauldron) exists but no line names the L3 Head as a reward or craft output.", "source": "locale:90932; locale:90934; locale:437496; locale:437498; locale:437504; locale:437516; locale:437542"},
  {"claim": "Repo search for '104749' and 'Alchemist' returned no matches, and the client definition has no coin store price (stores.json has no match). No vendor stocks it.", "source": "search repo (no matches); client definition pack"}
 ],
 "confidence": 0.1,
 "open": [
  "No verified source. The first-pass quest_reward guess is unsupported; no quest, vendor, drop, recipe, or event text names this item.",
  "The prior answer's locale IDs for the tier series (1418728780, 881210510, 740954401, 21563090, 338229407, 2872962251, and the dialog IDs 943088891, 2533722873, 2940738019) do not exist and were removed. Corrected IDs are cited above.",
  "Next step: find which quest or recipe grants the L1-L5 Alchemist tier pieces, checking the Alchemist storyline quest tables and the Alchemist Gear/Tools set.",
  "The 51 definitions (tints/races across 12 definition ids) were not checked individually; they may have different sources.",
  "Price and retirement status are unknown: no coin store price and no wiki entry."
 ]}
