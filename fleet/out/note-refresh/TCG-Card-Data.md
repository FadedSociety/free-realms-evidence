<!-- fleet job=note-refresh id=TCG-Card-Data status=done turns=10 usd=0.0149 tokens(read,write,in,out)=[265301, 54472, 22, 10831] model=claude-haiku-5-5 -->
# notes/Research/TCG Card Data.md

**Verdict:** minor-to-moderate drift. The lab-side inventory numbers and the in-repo references (README `catalog`/`extract` commands, Build Guide `Trading Card Game.md` with its 5,092-row locale count, Pieces 010 link, native-map addresses `012b8530`, `012b8ff0`, `012b87e0`, `0131cee0`, `0131e290`, `0137cd70`, `013c23f0`, `013c24d0`, `010d1ab0` all resolve) hold. The "unknown" framing about the DLL's network side is stale: the later Research note `TCG Client Protocol.md` (W61/W61b, same DLL hash) recovered its transport, gateway and registration table.

**Corrections:**

1. `old:` Before a Rust TCG service can serve gameplay data, the DLL's own connection and login flow must be identified from `FreeRealmsTCG.dll`; the native map currently only establishes its launch boundary.
   `new:` Before a Rust TCG service can serve gameplay data, the DLL's login and match flow must be finished from `FreeRealmsTCG.dll`. Its connection path (`FUN_10193430`), framing (`FUN_101921e0` / `FUN_10192500`) and login challenge IDs 78–81 are recorded in [[Research/TCG Client Protocol]]; the response-to-lobby sequence is not.
   `why:` repo:notes/Research/TCG Client Protocol.md:26, :28, :33 (the W61b addendum at :3 and :106 covers the challenge path).

2. `old:` The rules engine and the DLL's own network protocol/server are outside this extraction pass and remain unknown. Do not infer that the mapped Treasure War/game-connection protocol is the DLL protocol.
   `new:` The rules engine and the DLL's match protocol remain unknown. The DLL's own transport is recovered in [[Research/TCG Client Protocol]]: a custom TCP `NetworkService` (`FUN_10191dc0`), the gateway request `GatewayCommand_GetConnectionServer` (ID 414), and about 499 numeric factory registrations (`dll-registration.tsv`). Do not infer that the mapped Treasure War/game-connection protocol is the DLL protocol.
   `why:` repo:notes/Research/TCG Client Protocol.md:17, :26, :71; repo:notes/Research/Card Game.md:334 (499 unique numeric IDs); repo:notes/Autopilot/F123.md:40.

3. `old:** Full Ghidra auto-analysis timed out at 120 and 300 seconds; the no-analysis script output is in `lab/content/tcg/decomp/tcg-data-functions.txt` with run logs beside it.`
   `new:` An earlier Ghidra auto-analysis timed out at 120 and 300 seconds; the no-analysis script output is in `lab/content/tcg/decomp/tcg-data-functions.txt` with run logs beside it. A later full headless analysis of the same DLL (SHA-256 `22F0E8F9…`) completed in 224 seconds; see [[Research/TCG Client Protocol]].
   `why:` repo:notes/Research/TCG Client Protocol.md:11 (completed in 224 s, same hash) and :93 (W61b reused the saved Ghidra project).

**Unsure:**
- The `lab/` artifacts (63-file tree, 357 KB collection hash, 201 candidate IDs, 195,063 integers, 1,391 index rows) are outside this repo. The 1,391-row count matches the Client Protocol note (repo:notes/Research/TCG Client Protocol.md:47), but I could not open the inventory files to check the rest.
- The `../../../lab/native-map/run/shards/S0603/findings.md` link (lines 94–107) points outside the repo, so I could not confirm it.
- Line 3 says the client guide "leaves the DLL's own network link unresolved." That is still true of `Build Guides/Gameplay/Trading Card Game.md` (repo:notes/Build Guides/Gameplay/Trading Card Game.md:14, :84, :225), so I left it. That guide is itself behind the Client Protocol note and may need its own check.
- The "Java static-string/xref scan" wording (line 54) and the `10070b50` constructor address could not be checked against any repo tool. `FUN_10070b50` is the function the Client Protocol note names for `data\collections` (repo:notes/Research/TCG Client Protocol.md:49).
