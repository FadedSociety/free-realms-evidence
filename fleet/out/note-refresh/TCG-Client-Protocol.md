<!-- fleet job=note-refresh id=TCG-Client-Protocol status=done turns=18 usd=0.0274 tokens(read,write,in,out)=[798465, 80030, 38, 18823] model=claude-haiku-5-5 -->
# notes/Research/TCG Client Protocol.md

**Verdict:** minor drift. One citation has moved; the rest of the checkable claims I could reach hold at the tip. Most of the note's claims are about the shipped `FreeRealmsTCG.dll` and sit in the `lab/` evidence, which is outside the repo root, so I could not re-check them directly.

**Corrections:**

1. `old:` The input copy is `lab/runs/client-baseline-20261008T015138Z/client/tcg/FreeRealmsTCG.dll`
   `new:` The input copy is `lab/working/OSFR.Client/OSFR Client/tcg/FreeRealmsTCG.dll` (the W61 path `lab/runs/client-baseline-20261008T015138Z/client/` now contains only logs)
   `why:` `repo:notes/Research/Card Game.md:55-61` says the older audit path "now contains only logs" and cites the working copy, with the same DLL hash (`22f0e8f9…cd8b`). The client tree has the DLL at `tcg/FreeRealmsTCG.dll` (`client:tcg/`, listed; 8,990,720 bytes per `repo:notes/Research/Card Game.md:63`).

**Checked and holding:**

- Build Guide links resolve: `repo:notes/Build Guides/Gameplay/Trading Card Game.md` and `repo:notes/Research/TCG Card Data.md` both exist.
- Launch boundary: `010d1ab0` (DLL load) and `00ad47f0` (startup and argument builder) match `repo:notes/Build Guides/Gameplay/Trading Card Game.md:80-81`.
- Launch argument list matches `repo:notes/Build Guides/Gameplay/Trading Card Game.md:81`.
- Import count: the 30 WS2_32 names listed in the note are 30.
- Command IDs in the EXE-map paragraphs match the client `command` table: 97, 446, 59, 160, 165, 471, 342, 449, 440, 441, 410, 411, 78, 79, 80, 81, 206, 193, 214, and 414 (`GatewayCommand_GetConnectionServer`, handler `013ee970`). Hex-to-decimal conversions for 0x19e, 0x19b, 0x19a, and 0x4e–0x51 are correct.
- Counts agree with the sibling notes and T031/F123 reports: 499 registrations; 117 unnamed classes and 5 unnamed creators (so 382 named classes and 494 named creators); 60 curated rows, with 22/22/16 class-name comparison; 1,391 index rows; 195,063 collection integers; 201 candidate IDs; 201/201 occurring at least once. Also, 546 and 575 are absent from the DLL map (`repo:notes/Autopilot/F123.md:39-41`), which the note does not contradict.
- The `78 C>S, 79 S>C, 80 C>S` direction and the `1017a080` → `101790a0` / `10068af0` chain match `repo:notes/Research/Card Game.md:239-244` and `repo:notes/Autopilot/F123.md:20-23`.
- Nothing in the repo implements a TCG gateway, login, or match server, so no "our code" status claim in the note is contradicted. The "Rust service outline" is marked as proposal.

**Unsure:**

- **Gateway framing.** This note (line 32) states that every outbound DLL frame is `[len+12][3 routing words][body]`, and line 103 says the DLL `FUN_101935d0` sends `GetConnectionServer` on the gateway path. `repo:notes/Research/Card Game.md:271-274` says the TCG DLL game connection sends `GetConnectionServer` **without** the routing triple. That claim rests on the in-EXE `012f1e00` path (`repo:notes/Build Guides/Gameplay/Trading Card Game.md:174-175`), not on the DLL. I could not settle which is right for the DLL without the lab binary. The note should state explicitly whether the gateway request carries the triple.
- **Host and port values** (lines 22, 24): the DLL strings for `frtcg_livetest`, `sdtccg-dev2`, `10.132.64.6`, and `fr.patch.station` could not be searched; the `client` search does not index the binary and the DLL is not in the decompiled `fn` table. The sibling Build Guide uses `sdtccg-dev1` and 21xxx ports for the in-EXE card link (`repo:notes/Build Guides/Gameplay/Trading Card Game.md:173`), which is a different link, so I did not treat it as a conflict.
- **Lab artifacts** (`lab/content/tcg/analysis/*`, `run-w61b.ps1`, `merge_dll_registration.py`, `w61b-*.json`, SHA-256 values, and the 224-second analysis time): not reachable from the repo root. `scripts/native_map/test_tcg_research.py` reads `ROOT.parent/lab/content/tcg/analysis`, and F123 reports it passing, so the directory presumably exists.
- **Note line 104** says `LoginCommand_SendSessionID` "serializes a list, multiple strings, a boolean, and further strings" (DLL serializer). The EXE reader in the Build Guide lists different fields (`repo:notes/Build Guides/Gameplay/Trading Card Game.md:150`). These are different binaries, so I did not call it false.
