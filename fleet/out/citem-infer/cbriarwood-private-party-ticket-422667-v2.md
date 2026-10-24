<!-- fleet job=citem-infer id=cbriarwood-private-party-ticket-422667-v2 status=nothing_found turns=4 usd=0.0031 tokens(read,write,in,out)=[28242, 13009, 10, 2380] model=claude-haiku-5-5 -->
# Briarwood Private Party Ticket

{"item": {"name": "Briarwood Private Party Ticket", "locale_id": 422667, "kind": "other"},
 "sources": [],
 "retired": null,
 "live": "unsure",
 "evidence": [
  {"claim": "Client item definition 70455 is named by locale:422667 with description locale:422668 ('This ticket grants the user admission to the exclusive Briarwood Tower!'). Its client lines are tagged to the Briarwood group.", "source": "locale:422667; locale:422668"},
  {"claim": "Client npc_dialog locale:422694 reads: \"Sorry, I can't redeem your ticket right now. There is a private party being held in the Briarwood Tower. Come back later!\" The line quotes only a refusal while a private party is running. It names no NPC, store, or redemption source.", "source": "locale:422694"},
  {"claim": "The client has a Briarwood community event, 'Tanglewood Tower party' ('It's a party in the towers high above Briarwood'). Locale 434536 adds 'SERVER 1'. Locale 18233 says to talk to Mandy Vice if you fall out. No text links this event to item 70455 or gives dates.", "source": "locale:18232; locale:18233; locale:434535; locale:434536"},
  {"claim": "Sister tickets exist: Lakeshore Private Party Ticket (locale:422705) and Pixiewood Private Party Ticket (locale:422707). Their sources were not researched in the repo pack either.", "source": "locale:422705; quest-lines/items.json (Pixiewood note)"},
  {"claim": "Luau Party Tickets are sold by Tiger in the Merchant Store per the repo vendor notes. The only price seen is 18000 coins shown with a 2000-coin sale discount; the regular price is unreadable. This is not a verified regular price. It is a Luau ticket fact, not a Briarwood one.", "source": "prototype/osfr-tools/data/content/vendors_unresolved.json:78-108"},
  {"claim": "No store price for item 70455 exists in the client definition (coin_store_prices is empty), and no wiki page, vendor stock, quest reward, drop, or article names this ticket.", "source": "client definition for definition 70455; repo search for 70455 / Briarwood Private Party Ticket (no hits in data/content)"}
 ],
 "confidence": 0.15,
 "open": [
  "No source found for how players obtained the Briarwood Private Party Ticket. The first-pass 'quest_reward' guess is unsupported. Leave sources empty until evidence appears.",
  "The redemption NPC is not identified. Locale 422694 does not name one, so linking it to a party NPC is an inference, not evidence.",
  "Whether the ticket came from the Tanglewood Tower party community event is unconfirmed. Locales 434535/434536/18232 name the event; no text ties it to the ticket. Needs event dates and a wiki or forum source.",
  "Retired status is unknown. The event looks past, but no source states it.",
  "Critique fixes applied: the Luau 18000 figure is a sale-discounted 'Your Price' with the regular price unreadable (vendors_unresolved.json:108), not a regular price. The redemption link is labelled as inference. The event evidence is split: 434535/18232 for the event name, 6675/434536 for the server and Mandy Vice.",
  "Next step: research the Lakeshore and Pixiewood party tickets for their real sources, since a sister-item source may show the same pattern."
 ]}
