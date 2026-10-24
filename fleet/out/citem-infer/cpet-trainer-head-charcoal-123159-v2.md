<!-- fleet job=citem-infer id=cpet-trainer-head-charcoal-123159-v2 status=nothing_found turns=2 usd=0.0026 tokens(read,write,in,out)=[5373, 13681, 6, 1760] model=claude-haiku-5-5 -->
# Pet Trainer head charcoal

{"item": {"name": "Pet Trainer head charcoal", "locale_id": 123159, "kind": "clothing"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client defines 'Pet Trainer head charcoal' (locale:123159), definition 43160, slot 1, class 1, with no coin store price. Its neighbours in the colour family are locale:123158 (Pet Trainer chest charcoal) and locale:123160 (Pet Trainer legs charcoal).", "source": "locale:123159; locale:123158; locale:123160; client definition in pack"},
  {"claim": "Pet Trainer is a freestyle job that the wiki says has been removed from the game ('The [Pet] [Trainer] job has been removed from the game, and it was no longer..'). The removal date is not given on that page.", "source": "wiki page:ns0 'Pet Trainer'"},
  {"claim": "Pet Trainer job clothing is gated by the Freestyle Jobs requirement. The wiki's Cow Spot Apron page says it is a Chest-slot item acquired by entering redemption code MILKRULES, and it is Cannot Trade. Nothing on that page names the charcoal head piece.", "source": "wiki page 'Pet Trainer Cow Spot Apron'; wiki Category:Freestyle Jobs"},
  {"claim": "Pet Trainer job-level and trophy text exists in the client (e.g. locale:34110 'Pet Trainer: Level 4'). It is job progression text and names no charcoal clothing.", "source": "locale:34110; locale:34114"},
  {"claim": "The wiki's Pet Trainer job-item tooltips (Boots, Pants, Apron) show Freestyle Jobs as the requirement and Cannot Trade. No charcoal head item appears among them.", "source": "wiki image:item_tooltip Petboots.png, Petpants.png, Petshirt.png"},
  {"claim": "The pack's claim of a 'new member pack of pet trainer items' (locale:3755074429) is unsupported: that id does not exist in the client locale table, so it is dropped.", "source": "id_check in pack; critique evidence[4]"},
  {"claim": "The pack's repo-note citations (notes/Build Guides/Content/Jobs/Pet Trainer.md:231/232/234) were not found in repo search. Pet Trainer material lives in notes/Build Guides/Gameplay/Pets.md and Character and Customization.md instead, so those citations are dropped.", "source": "repo search 'Pet Trainer|charcoal'"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found. No wiki page, article, video frame, coin-store row, vendor stock, quest reward, drop or event names the charcoal head piece. Sources are left empty, not guessed.",
  "Possible channels to check: the Pet Trainer job outfit (job-gated; the job itself is removed per wiki), redemption or promotion codes like MILKRULES, and any Pet Trainer colour-set promotion. None is confirmed to include this colour.",
  "Retired status is unknown. The job was removed (wiki, undated), but the item's own removal date is not stated anywhere in the pack.",
  "Needs a wiki item-list page or a search of the Freestyle Jobs category for colour-by-colour sourcing before any source can be added."
 ]}
