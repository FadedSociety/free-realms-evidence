<!-- fleet job=citem-infer id=cstudent-miner-hat-35369-v2 status=nothing_found turns=2 usd=0.0015 tokens(read,write,in,out)=[5172, 5767, 6, 1527] model=claude-haiku-5-5 -->
# Student Miner Hat

{"item": {"name": "Student Miner Hat", "locale_id": 35369, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client definition 21665 is named Student Miner Hat (locale 35369), slot 1, class 12, no description, no coin store price on the definition.", "source": "locale:35369"},
  {"claim": "Definition 21665 appears in a starter item fixture list, which is a repo test/seed list and not a retail source.", "source": "repo:scripts/fixtures/starter_items.json:62"},
  {"claim": "Definition 21665 appears in a test save-schema fixture; this shows a test profile owns it, not how players get it.", "source": "repo:prototype/osfr-tools/tests/fixtures/save_schema/current-v2.json:198"},
  {"claim": "Reconstructed Miner starter list from pinned Legacy data includes 21665 (PARTLY PROVEN, reconstruction, not a retail source). Gear Up review shows only that a test profile's Gear Up added it.", "source": "repo:notes/Research/Job Starter Outfits.md:10,73,130; repo:notes/Reviews/Native Gear Up and Smelting 173814.md:3"},
  {"claim": "Miner.md:307 says the grant method for Student Miner Shovel starter gear (99257210) is unknown; it does not mention this hat, so it cannot support a grant path for 21665.", "source": "repo:notes/Build Guides/Content/Jobs/Miner.md:307"},
  {"claim": "The stores.json row with item_id 35369 (270 coins, member 243, sell 27) is keyed on the locale id, not definition 21665, and sits in a bulk block of similar rows; it is not attached to this item.", "source": "repo:prototype/osfr-tools/data/content/stores.json:11484"},
  {"claim": "No wiki page, article, video frame, or vendor stock names this item; lookup over client, wiki, articles, video returned only locale:35369.", "source": "lookup"}
 ],
 "confidence": 0.2,
 "open": [
  "No evidenced acquisition source: no vendor, coin shop, marketplace, quest reward, drop, event, prize wheel, crafting, collection, membership, or promotion source found. The earlier 'granted when Miner job is learned / starter outfit equipped' claim is unsupported and has been removed.",
  "Coin price 270 (stores.json item 35369) is keyed on locale id and belongs to a bulk block; not attached. Needs a check of whether store item_id uses locale or definition ids.",
  "Retired status unknown; live status unsure (client definition exists, no retail source evidence).",
  "Cluster neighbour locale 35370 (Elite Black Ash Branded Apron) is a different item and shares no source."
 ]}
