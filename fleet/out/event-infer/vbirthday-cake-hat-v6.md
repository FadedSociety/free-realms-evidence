<!-- fleet job=event-infer id=vbirthday-cake-hat-v6 status=done turns=2 usd=0.0029 tokens(read,write,in,out)=[7696, 9765, 6, 3250] model=claude-haiku-5-5 -->
# Birthday Cake hat

{
 "event": {
  "name": "Birthday Bash 2012 (Free Realms 3rd anniversary party)",
  "aliases": ["Birthday Bash"]
 },
 "kind": "holiday",
 "live": "yes",
 "occurrences": [
  {"year": 2012, "when": "Announced 2012-04-26; ran through May 24, 2012 (start date not stated in sources)", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"}
 ],
 "recurring": null,
 "zones": ["Sanctuary", "Sacred Grove"],
 "npcs": ["Queen Valerian", "Camellia", "Cakenstein"],
 "quests": ["Free Realms Turns Three!"],
 "activities": [
  "Cake bake-off storyline in Sanctuary; Camellia starts the competition near the great tree in Sanctuary (locale:707, article 2580)",
  "Log in during the Bash to claim the free Birthday Cake hat (article 2580)",
  "Stop Cakenstein and the cakelings disrupting the cake competition in Sacred Grove (locale:707)",
  "Buy Birthday Bash furniture and party items in the Marketplace (wiki Template:News/Archive, Update of April 24, 2012)"
 ],
 "items": [
  {"name": "Birthday Cake hat", "price": null, "currency": "reward", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (free login reward during the Bash); wiki image 'Birthday cake hat.jpg' (tooltip text matches locale:695, hat link from wiki image only)"},
  {"name": "Birthday Bash Furniture Bundle", "price": "1350 Station Cash", "currency": "station_cash", "source": "Name: locale:691. Price: locale:692 (description, inferred to belong to the bundle). Marketplace listing: wiki Template:News/Archive, Update of April 24, 2012"},
  {"name": "Birthday Bash Wall Sconce", "price": null, "currency": null, "source": "locale:666 (name); wiki Template:News/Archive, Update of April 24, 2012 (Marketplace)"},
  {"name": "Birthday Bash Chair, Floor Lamp, Dining Table, Bed, Sofa", "price": null, "currency": null, "source": "Names: locale:436980-436983 and 437014; Marketplace listing: wiki Template:News/Archive, Update of April 24, 2012"},
  {"name": "Four pinata pets (names unknown)", "price": null, "currency": null, "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (says four new pinata pets in the Marketplace; no names, prices or currency stated)"}
 ],
 "rewards": ["Birthday Cake hat (free login reward during the Bash)"],
 "evidence": [
  {"claim": "The 2012 Birthday Bash (3rd anniversary) was announced 2012-04-26 and ran through May 24, 2012. Start date not stated.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "Logging in during the Bash granted a free Birthday Cake hat, available until the Bash ended.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580 (quote: 'Log in today to get your free Birthday Cake hat before the Bash is over!')"},
  {"claim": "Queen Valerian led a cake bake-off storyline in Sanctuary with daily party-prep quests; Cakenstein disrupted the party in Sacred Grove.", "source": "http://www.freerealms.com/article/detail.action?articleId=2580"},
  {"claim": "The client names the 2012 party: 'Birthday Bash 2012 marks the 3rd Anniversary of Free Realms.'", "source": "locale:695"},
  {"claim": "Quest 'Free Realms Turns Three!' is the cake competition start with Camellia near the great tree in Sanctuary; Cakenstein and cakelings are stopped in Sacred Grove.", "source": "locale:706 (title), locale:707 (dialog)"},
  {"claim": "Birthday Bash furniture (Wall Sconce, Chair, Floor Lamp, Dining Table, Bed, Sofa, Furniture Bundle) appeared in the Marketplace in the April 24, 2012 update.", "source": "wiki 'Template:News/Archive' (Update of April 24, 2012, Marketplace section)"},
  {"claim": "Birthday Bash Furniture Bundle costs 1350 Station Cash (250 saved).", "source": "locale:692 (price, inferred to belong to bundle named in locale:691)"},
  {"claim": "Wiki Events page describes the Birthday Bash as an annual April event tied to Free Realms' April 29 launch day; only 2012 is dated here.", "source": "wiki 'Events' (general statement, not a dated occurrence)"},
  {"claim": "Sal Monella, Glerga, Quills and Bordon Cloo in the client text mention the Birthday Bash (cake bake-off and balloon quests).", "source": "locale:428708, 428710, 428711, 428726, 428550, 428078, 428071 (no year stated; not attached to 2012 occurrence)"}
 ],
 "confidence": 0.6,
 "open": [
  "Start date of the 2012 Bash is not sourced; only announcement (2012-04-26) and end (2012-05-24) are. Not schedulable as a start-end range; wireable is false.",
  "Recurrence: wiki Events says annual in April, but no second dated year is verified. 2013 article (articleId=2924, April 29, 2013) not re-verified, so not listed as an occurrence. Recurring is null until verified.",
  "'Cakenstein Attacks!' and its Balloon weapons are not dated to 2012 (Cakenstein also appears in other zones, locale 6707-6713). Excluded from quests.",
  "'Birthday Bash!' was removed from quests: the only client string is locale:29341 ('Birthday Bash!'), with no confirmed quest link or year.",
  "Party-prep NPC quests (Sal Monella, Quills, Glerga, Bordon Cloo; locale 428071-428726, 432476) name the Birthday Bash but are not dated to 2012 and are not confirmed as part of this 2012 event. Left out of quests pending a dated source; the quest titles themselves are not in the pack.",
  "Four pinata pet names, prices and currency are unknown and unsourced.",
  "Birthday Cake hat locale 694 not checked.",
  "Other birthday parties (articleIds 1197, 1261, 1282, 2106, 2107) are earlier years and may be merged by the pack; not attached to 2012. Birthday T-shirts in Category:Birthday Bash have no year; not attached.",
  "Alias 'Free Realms Turns Three!' removed (it is a quest title, locale:706); alias '3rd Anniversary Birthday Bash' removed (unsourced).",
  "Article 2578 (4/28/2012 login and tripled Station Cash) is not in the pack or lookup; the TentonHammer April 30 date is unverified and not used.",
  "live 'yes' means the 2012 run was live per article 2580; it does not mean the event is running now."
 ]
}
