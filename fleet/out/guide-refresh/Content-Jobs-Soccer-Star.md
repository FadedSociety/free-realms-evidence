<!-- fleet job=guide-refresh id=Content-Jobs-Soccer-Star status=done turns=23 usd=0.0321 tokens(read,write,in,out)=[1058031, 81618, 48, 22665] model=claude-haiku-5-5 -->
# notes/Build Guides/Content/Jobs/Soccer Star.md

**Verdict:** minor-to-moderate drift. The client function addresses, names and confidence labels in "Client code" all match the label table. The job catalogue, level milestones and the seven "Achieve Level N" titles also match the repo and locale. Three statements are stale or false: the "no Striker string" claim, the "server messages not mapped" claim, and one dangling link.

**Corrections:**

1. `old:` the client has the objective "Complete the Soccer Star Questline" (882214261, 2212314839) and no "Striker" string.
   `new:` the client has the objective "Complete the Soccer Star Questline" (locale 441586 and 441588) and the title string "Title: Striker" (locale 31731). Bare "Striker" also sits at 117715, 441585 and 441587, beside the questline rows.
   `why:` locale 31731 = "Title: Striker"; 441585 and 441587 = "Striker"; 441586 and 441588 = "Complete the Soccer Star Questline". The note's own "Striker" conflict is therefore not a conflict.

2. `old:` (882214261, 2212314839; no title string found) and, per the wiki, the title "Striker".
   `new:` (882214261, 2212314839; locale 441586, 441588) and the title "Striker" (client "Title: Striker", locale 31731; bare "Striker" 441585, 441587; the wiki agrees).
   `why:` locale lookups as in item 1. The 882214261 and 2212314839 ids return "no such id" in the locale, so they are probably hash ids, not locale ids.

3. `old:` "Striker" for finishing the questline (wiki only).
   `new:` "Striker" for finishing the questline (client "Title: Striker" 31731 and bare "Striker" 441585, 441587; wiki).
   `why:` the same locale rows as item 1. The title is no longer wiki-only.

4. `old:` The server messages for a match are therefore **not yet mapped**.
   `new:` The server messages are only partly mapped. The sub-13, sub-14 and sub-16 readers are in [[Soccer]] (Network table: 00b794b0, 00b793c0, 00b79580). The Gateway note maps the family-76 constructors for sub 5 (`SoccerPacketUpdateGameState::Ctor` 00b752a0), sub 10 (`SoccerPacketAcquirePickUp::Ctor` 00b74ee0) and sub 14 (`SoccerPacketUpdatePlayerState::Ctor` 00b746b0). The builders 00b839e0 and 00b83ae0 are still unknown-confidence. The server-side codec is `soccer_service.rs`.
   `why:` repo:notes/Build Guides/Gameplay/Soccer.md:36, 44-48; repo:notes/Build Guides/Network/Gateway and Transport.md:7255, 7361, 7390 (marked 🌐); repo:prototype/osfr-tools/src/soccer_service.rs:1-7 (client-reader-derived wire codec).

5. `old:` The match packets are not mapped in [[Soccer]] (0 network-linked functions; two packet builders in unknown-confidence functions).
   `new:` [[Soccer]] maps the sub-13, 14 and 16 readers and the Gateway note maps the sub 5, 10 and 14 constructors. The generated list still counts 0 network-linked (`wire`) functions. Only the two packet builders 00b839e0 and 00b83ae0 (unknown confidence) remain unmapped.
   `why:` repo:notes/Build Guides/Gameplay/Soccer.md:36, 44-48, 98 (`Network-linked (wire): 0`), 339-340; repo:notes/Build Guides/Network/Gateway and Transport.md:7255, 7361, 7390.

6. `old:` [[NPCs - Blackspore]] (Mud Hoppers)
   `new:` [[NPCs - Blackspore Swamp]] (Mud Hoppers)
   `why:` repo:notes/Build Guides/Content/NPCs/ has "NPCs - Blackspore Swamp.md" and no "NPCs - Blackspore.md". repo:notes/Build Guides/Content/NPCs/NPCs - Merry Vale.md:171 uses [[NPCs - Blackspore Swamp]]. The link [[NPCs - Northern Wilds]] is valid, as an alias in NPCs - Wilds.md:4.

7. `old:` Not network-linked (the page records 0 `wire` functions).
   `new:` Not network-linked in the generated list (the page records 0 `wire` functions). Its Network table does map the sub-13, 14 and 16 readers (00b794b0, 00b793c0, 00b79580).
   `why:` repo:notes/Build Guides/Gameplay/Soccer.md:98 and 44-48.

**Checked and holding:** the client function names and addresses in "Client code" (00afb4a0, 00b73b20, 00b73d40, 00b75660, 00b759e0, 00b7be70, 00b7c070, 00b7c520, 00b7c6b0, 00b7de60, 00cd7840, 00cd7900, 00cd9df0, 00cda080, 00cddf60, 01071b10, 01072020, 01074b50). Their confidence labels match (for example 00cd7840 and 01074b50 are unknown; 00b73b20 and 00cd7900 are likely). The "Football Star" claim holds, since the locale has no such string. The seven "Soccer Star: Achieve Level N" titles (2, 5, 8, 10, 13, 15, 19) match the locale. Level achievements 4, 8, 12, 16 and 20 (34120-34124) match repo:prototype/osfr-tools/src/restoration/piece_042.rs:317-321 and 409-415. Job 52 "Soccer Star" is a freestyle row with members_only false and trial true (repo:prototype/osfr-tools/src/restoration/piece_031.rs:279-287), which fits the note's "free to start" treatment.

**Unsure:**
- The "20 live Soccer Star: story titles" count. The first 30 locale hits show about 18 non-level story titles plus the NOT LIVE one, but the list was truncated. repo:piece_042.rs:462-476 lists only 12 quest names (locale 407407-407418) and no quest ids, so I could not confirm the 20.
- The questline achievement ids 882214261 and 2212314839 are not locale ids (see item 2). Their role is unclear.
- Gaps line 311 still says the title "Striker" is "(wiki)". It is now client-backed (item 3), but I did not change that line.
- The half-length, team-size and Quick Play claims are unverified in the repo. Soccer.md:54 says the 180-second default is an R (reconstructed) convenience value, which does not contradict the note's "about 3:00 †" inference.
