<!-- fleet job=citem-infer id=cillusion-food-fungal-vinegolem-wolf-1227-v1 status=nothing_found turns=6 usd=0.0043 tokens(read,write,in,out)=[66153, 17531, 14, 2976] model=claude-haiku-5-5 -->
# Illusion Food - Fungal Vinegolem Wolf

{"item": {"name": "Illusion Food - Fungal Vinegolem Wolf", "locale_id": 1227, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item name is 'Illusion Food - Fungal Vinegolem Wolf' (definition 4068, class 9, slot 0). Description: 'Eating this food will temporarily change the player into a Fungal Vinegolem Wolf.'", "source": "locale:1227; client definition in pack"},
  {"claim": "Client has no coin store price for this definition (coin_store_prices empty), so no coin vendor sale is evidenced.", "source": "pack client_definition; repo:data/content/stores.json has no entry for 4068 (no search hit for 4068/Vinegolem in repo data)"},
  {"claim": "Sibling 'Illusion Food' names exist in the client (Vinegolem Bear 1228, Evil Wolf 1229, Fungal Vinegolem Wolf 1227) and in the wider Illusion Food family, but none of the lookups returned a wiki page, article, or video naming this item.", "source": "lookup client/wiki/articles/video for 'Illusion Food Vinegolem' and 'Vinegolem' (no wiki or article hits); locale:1228"},
  {"claim": "The only wiki Illusion Food tooltip found is Bark Chocolate (Illusion: Dog Large Floppy, 30 minutes, Cannot Sell, Cannot Trade, Required: Any Job, Resell Value 18). It shows the family's behaviour but says nothing about this item's source.", "source": "wiki image:item_tooltip 'Bark chocolate.jpg'"},
  {"claim": "Repo and reference refs (community server copies, asset manifest 'Bear Vinegolem.gfx', locale dat files) contain the item name in the locale dumps but no vendor, quest, drop or recipe reference to it.", "source": "search repo and refs for Vinegolem / Illusion Food; refs locale dat files list 'Illusion Food - Fungal Vinegolem Wolf' (ucdt 884649093)"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found: no coin vendor price, no wiki article, no quest, drop, event, prize wheel, crafting or promotion evidence names this item.",
  "Live status unknown. The client defines it, but nothing confirms it was sold or awarded in the live game; the first-pass 'unsure' is not contradicted.",
  "Retired status unknown; no retirement source found.",
  "Check the Illusion Food family as a group (Bark Chocolate and the 'Illusion Food - ...' animal and monster foods) for a shared source such as a vendor, event or prize wheel, then test whether 1227 sits in it.",
  "Client-side fact: the Vinegolem Bear (1228) and Vinegolem Fungus Bear illusion item exist in the client, so the Vinegolem theme may be tied to a Briarwood/Nettleseed or Blackspore event. Not verified."
 ]}
