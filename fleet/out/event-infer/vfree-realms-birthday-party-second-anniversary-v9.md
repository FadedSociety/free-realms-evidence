<!-- fleet job=event-infer id=vfree-realms-birthday-party-second-anniversary-v9 status=done turns=2 usd=0.0033 tokens(read,write,in,out)=[7478, 9632, 6, 4000] model=claude-haiku-5-5 -->
# Free Realms Birthday Party (second anniversary)

```json
{"event": {"name": "Free Realms Birthday Party (anniversary party, late April to May)", "aliases": ["Free Realms Birthday Bash", "Birthday Party (2010-2011 posts)", "Birthday Bash (2012 article title)", "Die Free Realms Geburtstagsfeier! (2011 German post)", "Kuchenstein / Cakenstein event (German/English names)"]},
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "Third-anniversary Birthday Bash, ran through May 24, 2012", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (article summary; full text not re-read)"},
  {"year": 2011, "when": "Second-anniversary party; anniversary April 28; ends May 18. YEAR INFERRED, not sourced: article 2099 has no post date in the pack. Capture dated 2011-04-30 supports 2011 only indirectly.", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 (German; quote 'Sie geht heute los und endet am 18. Mai.')"}
 ],
 "recurring": null,
 "zones": ["Sacred Grove (article 2580: the celebration and Cakenstein disruption took place across Sacred Grove)", "Sanctuary (article 2580 summary: cake bake-off storyline led by Queen Valerian)"],
 "npcs": ["Cakenstein (article 2580; wiki 'Cakenstein')", "Queen Valerian (article 2580 summary)", "Cakelings (wiki 'Cakeling'; locale:4732)"],
 "quests": ["Cakenstein Attacks! (locale:4917; wiki ties it to the annual Birthday Bash, year not sourced)"],
 "activities": ["Attend party events and collect party items (article 2580)", "Complete daily party-prep quests in Sanctuary (article 2580 summary, 2012)", "Defeat the cakelings before they get stronger (locale:4732)", "Defeat Cakenstein before he eats all the birthday cake (locale:4949)"],
 "items": [
  {"name": "Balloon Bow", "price": null, "currency": null, "source": "wiki 'Balloon Bow' (prize wheel reward version from the Cakenstein Attacks! encounter during the annual Birthday Bash; edition not given)"},
  {"name": "Balloon Hammer", "price": null, "currency": null, "source": "wiki 'Balloon Hammer' (same prize-wheel wording)"},
  {"name": "Balloon Axe", "price": null, "currency": null, "source": "wiki 'Balloon Axe' (same prize-wheel wording)"},
  {"name": "Balloon Sword", "price": null, "currency": null, "source": "wiki 'Balloon Sword' (same prize-wheel wording)"},
  {"name": "Balloon Saw", "price": null, "currency": null, "source": "wiki 'Balloon Saw' (same prize-wheel wording)"},
  {"name": "Balloon Wand", "price": null, "currency": null, "source": "wiki 'Balloon Wand' (same prize-wheel wording)"}
 ],
 "rewards": ["Balloon weapons from the prize wheel on the Cakenstein Attacks! encounter (wiki; edition not sourced)"],
 "evidence": [
  {"claim": "Third-anniversary Birthday Bash ran through May 24, 2012; cake bake-off storyline in Sanctuary led by Queen Valerian; daily party-prep quests; Cakenstein monster", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "Cakenstein was loose in Sacred Grove stealing cakes during the Birthday Bash", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (fact line)"},
  {"claim": "Second-anniversary party ran from the post date until May 18; anniversary April 28; Kuchenstein boss and cakelings", "source": "http://www.freerealms.com:80/article/detail.action?articleId=2099 (summary; year inferred; post date null)"},
  {"claim": "Birthday Bash is an annual event held throughout April, celebrating launch day April 29, 2009; features party items and Cakenstein", "source": "wiki page: Birthday Bash (not an article; conflicts with the April 28 anniversary and May-end windows)"},
  {"claim": "Cakenstein Attacks! is a client quest title", "source": "locale:4917"},
  {"claim": "Cakelings objective: defeat them before they get stronger", "source": "locale:4732 (confirmed this check)"},
  {"claim": "Cakenstein objective: defeat him before he eats the birthday cake", "source": "locale:4949 (confirmed this check)"},
  {"claim": "Balloon weapons come from the Cakenstein Attacks! prize wheel during the annual Birthday Bash", "source": "wiki pages: Balloon Bow, Balloon Hammer, Balloon Axe, Balloon Sword, Balloon Saw, Balloon Wand"}
 ],
 "confidence": 0.5,
 "open": [
  "Only 2012 (article 2580, end May 24) is a sourced occurrence with a year. 2011 is year-inferred from article 2099, whose post date is null in the pack. Verify from full text before wiring.",
  "2010 (first anniversary, anniversary April 29, ran to May 10; articles 1261 and 1267) is NOT in this pack and is unverified here. Dropped from occurrences.",
  "2013 (article 2924, April 29 start) was never read and has no end date. Not scheduled.",
  "Recurring is left null. The wiki calls the event 'annual', but a wiki page is not an article, and the rule needs two dated occurrences or an article saying it recurs. Two dated occurrences exist only if 2011 is accepted, so 'yearly' remains unconfirmed.",
  "Date conflicts: the wiki says the event runs 'throughout April' around launch day April 29, 2009. Articles put the anniversary on April 28-29 with the run ending in May (May 18 in 2099, May 24 in 2580). The wiki and articles disagree on the window; the articles are treated as primary.",
  "Name conflict: the wiki calls the Cakenstein boss 'the only Birthday Bash' in one place and 'annual' in another; not resolved.",
  "Zone conflict: article 2580 locates the celebration in Sacred Grove, and its summary puts the bake-off in Sanctuary. Both are kept, with their cites.",
  "Camellia (2010 birthday quests, article 1267) and article 2107 ('named in' claim, undated) are NOT verified in this pack. Camellia removed from npcs.",
  "Balloon weapons have no price, currency or edition year in any source. Attached to the event only through the wiki, not to a specific occurrence.",
  "Cakenstein Attacks! is linked to the event only by the wiki Balloon pages; no article dates it. Treat as wiki-only.",
  "Unconfirmed quest candidates not listed: Cakenstein's Last Stand (locale:428064), defeat Cakenstein outside Queensfield (locale:428092, 428094), Chef Jarvie clue (locale:428045).",
  "Not merged as this event (name-only ties): Birthday Party Balloons 4-Pack (locale:14422/14423), Glerga's Birthday Cake (locale:5170), Birthday Party! Yay! (locale:139313), Anniversary Firework (locale:14571), Orange Anniversary Silly String (locale:14575).",
  "Birthday Cake Hat and the eight-cake collection reward have no source naming them; omitted. Sacred Grove as a pre-2012 edition is not established.",
  "Pack merge risk: the 'Birthday Party' (2010-2011) and 'Birthday Bash' (2012) names may be separate editions or one event; the alias link is not sourced beyond the wiki.",
  "wireable: false. Schedule only the 2012 edition (through May 24, article 2580) until 2011 is verified."
 ]}
```
