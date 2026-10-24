<!-- fleet job=guide-refresh id=Gameplay-Matchmaking-and-Lobby status=nothing_found turns=28 usd=0.0355 tokens(read,write,in,out)=[1250147, 93583, 58, 22553] model=claude-haiku-5-5 -->
# notes/Build Guides/Gameplay/Matchmaking and Lobby.md

**Verdict:** current. I found no sentence in `Matchmaking and Lobby.md` that is false at the tip. The note has no repo path:line citations, and its server-side material is a prescriptive list ("What the Rust server must do") that does not claim anything is built. Its client addresses and labels that I spot-checked still match the client table, and the table's citations (lines 293 to 301) still point at the right rows.

**Corrections:** none.

**Checked and holding:**
- Client addresses and names: `00923210` HandleLobbyPacket, `009471a0` dispatcher, `00bb1cd0` SendCreateGame, `00bb1890`/`1920`/`19b0`/`1a40` join/leave/start/leave-lobby senders, `00baff30` Lobby_OnJoinedGame, `00c08cf0` AddMatchRequest sender, `00a7fb90` ListQueuesRequest, `00aa2980` ParseMatchmakingPacket, `009c3590` 175 family entry, `00c4e490`, `00a27820`, `00c08ae0`, `00c08e30`, `00a83b80`, `00a83ed0`, `00a9a580`, `00a9f1d0`, `00aa1140`, `00a7fd30`, `00a223d0`, `00a224a0`, `00a27190`, `00a27250`, `00a29500`, `00c91670`, `0102a4d0`, `00919b60`, `008e5450`. All resolve to the named functions in `client_sql`.
- Server-side status, as read from the tip (not claimed by the note, recorded for the next editor):
  - 102/1 is answered with the 102/2 body when `data/content/kart_lobby.json` exists (`prototype/osfr-tools/src/gameplay.rs:2713-2716`). The file has six game rows (`data/content/kart_lobby.json:2-45`).
  - 141/1, 141/13 and 41/129 are routed (`prototype/osfr-tools/src/gateway.rs:490-491`; `prototype/osfr-tools/src/gameplay/matchmaking_route.rs:12-33`).
  - 141/3 is always refused with a chat line and creates no request (`prototype/osfr-tools/src/matchmaking.rs:1303-1311`; `notes/Autopilot/T007.md:89-91`).
  - 101/9 is acknowledged with no state and no reply (`prototype/osfr-tools/src/matchmaking.rs:1266-1274`; `notes/Autopilot/T007.md:93`).
  - 175 is not routed from inbound traffic (no `(Some(175` arm in `gateway.rs`). Its encoders exist in `matchmaking.rs:1320-1460` but nothing outside that module calls them.
  - 147 has no emitter in `src` (only `restoration/piece_020.rs:55`). 167 Play and refresh are routed (`gateway.rs:532-533`).
  - Not sent anywhere: 141/4, 141/5, 141/6, 141/9, 141/10, 141/12, 141/15, 141/18, 101/4 to 101/8, 101/11. Queue membership is not implemented (`notes/Autopilot/T007.md:151-152`).
  
  The must-do list (steps 1, 4, 7, 8, 9) describes the target, so these gaps do not make it false. A builder should still read this section against `notes/Autopilot/T007.md` and `T026.md` before relying on it.

**Unsure:**
- **Method line, "OSFR-held packet captures are not used" (line 14).** Our code cites a "preserved capture" for the 141/1 and 141/2 layouts: `prototype/osfr-tools/src/matchmaking.rs:812` and `notes/Autopilot/T007.md:57-58` (`notes/Research/Matchmaking Service.md`). I did not open that research note, so I cannot tell whether those captures are OSFR-held. Needs a human read.
- **Method line, "Community emulator code and tables are not used either" (line 14).** `prototype/osfr-tools/src/kart_racing.rs:56` and `kart_lobby_native.rs:28` refer to a community `LobbyGameDefinition` subset. I did not check whether it is used as a source.
- **Label wording, `00a24a60`.** Line 368 calls it the "column-name getter". The client label names it `LobbyDataSourceManager::GameListDataSource::GetColumnValue` (a cell-value getter), and line 79 uses it for column names. Possibly a naming slip; not verified against the decompile body.
- **Other notes that are stale (not this note's claims).** `notes/Design/Build Ledger.md:46` says "Guilds and matchmaking … Not routed." That is no longer true for matchmaking, since 141/1, 141/3, 141/13, 41/129 and 101/9 are routed (T007). `notes/Research/Unrouted Client Requests.md` rows R086, R087, R089 and R090 list 141/1, 141/3, 141/10 and 141/13 as unrouted, which is out of date for 141/1, 141/3 and 141/13.
