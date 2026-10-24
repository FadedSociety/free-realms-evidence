<!-- fleet job=item-infer id=iseaside-school-of-medicine-v2 status=nothing_found turns=2 usd=0.0015 tokens(read,write,in,out)=[4539, 5128, 6, 1653] model=claude-haiku-5-5 -->
# Seaside School of Medicine

{"item": {"name": "Seaside School of Medicine", "locale_id": null, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "no",
 "evidence": [
  {"claim": "The wiki page is a location article (infobox type 'Medic school', ownership Doctor Callahan, location Seaside). It is not an item and has no coin, Station Cash or IGD price data.", "source": "https://freerealms.fandom.com/wiki/Seaside_School_of_Medicine (rev 50150)"},
  {"claim": "The client has no item named 'Seaside School of Medicine'. The closest client string is 'Seaside School of Combat Medicine Diploma'.", "source": "locale:93620; locale:93621"},
  {"claim": "The diploma is tagged quest_reward in the client text table, and its item text says it requires the quest 'Medic: Paying Your Student Debts'.", "source": "locale:93620 (quest_reward tag); locale:93621"},
  {"claim": "Wiki 'Doctor Gordon' says Dr. Gordon writes a recommendation letter to Doctor Callahan at the Seaside School of Medicine once enough of the player's medic quests are done, so the player can receive the diploma from the school. This supports the diploma as a quest-chain reward, not a vendor item.", "source": "wiki: Doctor Gordon"},
  {"claim": "Doctor Callahan runs the school and gives the Medic level-20 quest. This is NPC and quest context, not an item source.", "source": "wiki page: Doctor Callahan; repo:notes/Build Guides/Content/NPCs/NPCs - Seaside.md row 51"}
 ],
 "confidence": 0.5,
 "open": [
  "The named target is a location, so it has no item sources, prices or vendors. Sources are left empty on purpose.",
  "If the intended item is the 'Seaside School of Combat Medicine Diploma' (locale:93620/93621), its likely source is a quest reward from the medic quest chain ending in 'Medic: Paying Your Student Debts', per the Doctor Gordon wiki text. No price, vendor or Station Cash listing is in the pack, and no reward row for the quest has been checked in the repo. A quest_reward entry needs that repo check before it is wired.",
  "The wiki page has no revision history, so retirement status cannot be read from it. The diploma's retirement status is also unknown."
 ],
 "confidence_note": "Confidence 0.5 reflects that the target is a location and the diploma link is a quest-chain inference.",
 "critiques_addressed": "The evidence and world critiques are fixed: locale:93620 (quest_reward tag) and the Doctor Gordon wiki text are now cited for the diploma. The diploma is kept as an open candidate, not a confirmed source, since no quest reward row was verified."
}
