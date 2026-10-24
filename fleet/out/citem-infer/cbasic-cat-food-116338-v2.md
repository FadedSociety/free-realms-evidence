<!-- fleet job=citem-infer id=cbasic-cat-food-116338-v2 status=nothing_found turns=2 usd=0.0017 tokens(read,write,in,out)=[4980, 7237, 6, 1417] model=claude-haiku-5-5 -->
# Basic Cat Food

{"item": {"name": "Basic Cat Food", "locale_id": 116338, "kind": "consumable"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client name 'Basic Cat Food' is locale 116338 (item). Client definition 37075, slot 205, class 61, no coin store price.", "source": "locale:116338; pack client_definition"},
  {"claim": "Repo search for 'cat food', 37075 and 116338 finds no vendor stock row, quest reward, drop or recipe naming this item. The only repo hits are the Pet Trainer food family (Basic, plain and Super Cat Food, ids 3471528303, 1954306991, 3020054161) and a Gooplemoop kitten-chain note that mentions cat food with no reward named.", "source": "notes/Build Guides/Content/Jobs/Pet Trainer.md:247; notes/Build Guides/Content/NPCs/NPCs - Wugachug.md:200"},
  {"claim": "Client text 'A normal quality cat food.' is locale 78506, which is the likely description of this item. The id locale:4265490437 cited earlier does not exist and is withdrawn. The text 'A normal quality pet food.' is locale 20259, a different string.", "source": "locale:78506; locale:20259"},
  {"claim": "Client locale 78505 'Cat food' ('This is basic cat food.') is a separate item name. It is not confirmed to be the same item as 116338, so the earlier 'older and newer copy' claim is dropped.", "source": "locale:78505"},
  {"claim": "The first-pass 'vendor' guess has no supporting source and is rejected.", "source": "jev_first_pass; critique evidence lens"}
 ],
 "confidence": 0.15,
 "open": [
  "No source names Basic Cat Food as sold, rewarded, dropped, crafted or promoted. Sources stay empty.",
  "No coin store price in the client definition, and no wiki or article page covers the item. Price unknown.",
  "Cobblestone 'Pet Supplies' vendor stock is not in the repo data. Check it for cat food before crediting a vendor.",
  "Check the Gooplemoop kitten chain (Wugachug) for a cat food reward or purchase.",
  "Confirm whether locale 78505 'Cat food' and the Pet Trainer ids (3471528303 etc.) are the same item as 116338 / definition 37075.",
  "Live status unproven: the item is in the Pet Trainer food family, but that does not show it is sold today."
 ]}
