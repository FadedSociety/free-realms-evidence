<!-- fleet job=item-infer id=iholigoblin-mask-v2 status=done turns=2 usd=0.0016 tokens(read,write,in,out)=[5186, 6138, 6, 1530] model=claude-haiku-5-5 -->
# Holigoblin Mask

{"item": {"name": "Holigoblin Mask", "locale_id": 5102960, "kind": "consumable"},
 "sources": [
  {"type": "event", "detail": "12 Days of Presents 2013 (annual Snow Days quest event). The wiki says the mask was acquired as part of this event; the specific granting quest/day is unconfirmed.", "where": "Snow Days / 12 Days of Presents", "price": null, "currency": null, "source": "https://freerealms.fandom.com/wiki/Holigoblin_Mask (rev 48696); https://freerealms.fandom.com/wiki/12_Days_of_Presents (2013 reward list includes Holigoblin Mask)"}
 ],
 "retired": true, "live": "no",
 "evidence": [
  {"claim": "Holigoblin Mask is an unobtainable, unlimited-use consumable acquired as part of the 12 Days of Presents 2013, an annual Snow Days quest event; it transforms the user into a Holigoblin for one hour.", "source": "https://freerealms.fandom.com/wiki/Holigoblin_Mask (rev 48696)"},
  {"claim": "Wiki categories include 12 Days of Presents, Snow Days, Consumable, Unlimited Consumable, and Unobtainable. No coin, Station Cash, or vendor entries exist, so price is null.", "source": "https://freerealms.fandom.com/wiki/Holigoblin_Mask (rev 48696)"},
  {"claim": "The 12 Days of Presents 2013 reward list on the wiki includes 'Holigoblin Mask' among its items.", "source": "https://freerealms.fandom.com/wiki/12_Days_of_Presents"},
  {"claim": "Client text: name 'Holigoblin Mask', description 'Turns you into a Holigoblin. Use it as many times as you want!', effect 'Illusion: Holigoblin - 1 hour'.", "source": "locale:5102960, locale:5102961, locale:5102962"},
  {"claim": "Related client text 'Holigoblin Illusion' exists.", "source": "locale:421013"}
 ],
 "confidence": 0.6,
 "open": [
  "Granting quest and day are unknown. The earlier draft's 'daily quest rewards' wording was removed because no evidence in the pack supports it.",
  "No price: the wiki lists no coins or Station Cash price and no vendor stocks it.",
  "Obtainability after 2013 rests on the Unobtainable category; no article or forum confirmation was found.",
  "Repo reward wiring was not checked, so the source rests on the wiki and client text."
 ],
 "critique_fixes": "Evidence critique: removed the unsupported 'daily quest rewards' claim. World critique: kept the source at event level and marked quest-level wiring as unknown. Both critiques accepted the null price and retired status."
 ,"wireable": "event-level only"
}
